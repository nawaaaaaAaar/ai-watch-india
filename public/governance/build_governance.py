"""Offline deterministic governance-layer packager; never modifies the system registry."""
from pathlib import Path
import collections
import csv
import hashlib
import io
import json
import shutil
import sqlite3
import zipfile

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "research/governance"
OUT = ROOT / "public/governance"
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name):
    return json.loads((INPUT / name).read_text())
def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".md":
        value = value.rstrip() + "\n"
    path.write_text(value, encoding="utf-8")
def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"
def cell(value):
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, bool):
        return int(value)
    return value

baseline = read("baseline-registry.json")
for item in baseline["files"]:
    assert sha(ROOT / "public/registry" / item["path"]) == item["sha256"], f"Registry changed: {item['path']}"
registry = json.loads((ROOT / "public/registry/data.json").read_text())
assert len(registry["systems"]) == baseline["systems"] == 144
tables = read("curation.json")
tables["system_keys"] = [{**{k: s[k] for k in ("system_id", "name", "sector", "jurisdiction", "owner_institution_id")}, "registry_version": "1.3.0"} for s in registry["systems"]]
ids = {t: {r[next(iter(r))] for r in rows} for t, rows in tables.items()}
for t, rows in tables.items():
    assert rows and len(ids[t]) == len(rows), f"Duplicate or empty {t}"
FK = {
    "instrument_domains": {"instrument_id": ("instruments", "instrument_id")},
    "provisions": {"instrument_id": ("instruments", "instrument_id"), "source_id": ("sources", "source_id"), "evidence_id": ("evidence", "evidence_id")},
    "instruments": {"primary_source_id": ("sources", "source_id")},
    "instrument_sources": {"instrument_id": ("instruments", "instrument_id"), "source_id": ("sources", "source_id")},
    "evidence": {"instrument_id": ("instruments", "instrument_id"), "source_id": ("sources", "source_id"), "provision_id": ("provisions", "provision_id")},
    "system_links": {"instrument_id": ("instruments", "instrument_id"), "system_id": ("system_keys", "system_id")},
    "instrument_relationships": {"instrument_id": ("instruments", "instrument_id"), "related_instrument_id": ("instruments", "instrument_id")}
}
for t, refs in FK.items():
    for row in tables[t]:
        for column, (target, _) in refs.items():
            assert row[column] is None or row[column] in ids[target], (t, column, row[column])
assert len(tables["instruments"]) == 52 and len(tables["jurisdiction_coverage"]) == 37
for i in tables["instruments"]:
    dims = [p["dimension"] for p in tables["provisions"] if p["instrument_id"] == i["instrument_id"]]
    assert sorted(dims) == sorted(["Oversight", "Evaluation", "Procurement", "Redress", "Accountability and data"])
    assert i["primary_source_url"] == next(s["url"] for s in tables["sources"] if s["source_id"] == i["primary_source_id"])
assert all(not p["implementation_verified"] for p in tables["provisions"])
assert all(r["selected_passages_match"] and r["selected_words"] <= 250 for r in read("quote-audit.json"))
assert sum(r["hits"] for r in read("search-log.json")) == 948
for l in tables["system_links"]:
    assert l["instrument_evidence_ids"] and l["system_assertion_ids"] and l["system_source_ids"]
    assert set(l["instrument_evidence_ids"]) <= ids["evidence"]
    assert all(next(e for e in tables["evidence"] if e["evidence_id"] == eid)["instrument_id"] == l["instrument_id"] for eid in l["instrument_evidence_ids"])
    assert set(l["system_assertion_ids"]) <= {a["assertion_id"] for a in registry["assertions"]}
    assert all(next(a for a in registry["assertions"] if a["assertion_id"] == aid)["system_id"] == l["system_id"] for aid in l["system_assertion_ids"])
    assert set(l["system_source_ids"]) <= {s["source_id"] for s in registry["sources"]}
    assert set(l["system_source_urls"]) == {s["url"] for s in registry["sources"] if s["source_id"] in l["system_source_ids"]}

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
for source in tables["sources"]:
    source["snapshot"] = f"sources/{source['source_id']}.md"
    text = f"# {source['title']}\n\nPrimary official record: [original document]({source['url']}). This snapshot contains selected excerpts, not the full document.\n\n"
    text += f"Retrieval: {source['retrieval_basis']}; cached: {source['is_cached']}. Retrieved-text SHA-256: `{source['reviewed_text_sha256']}`. This is not original-binary authentication.\n\n"
    for e in tables["evidence"]:
        if e["source_id"] == source["source_id"]:
            text += f"## {e['evidence_id']}\n\n> {e['quote']}\n\n{e['locator']}; supports {e['supports']}. [Read the original]({source['url']}).\n\n"
    write(OUT / source["snapshot"], text)

schema = {}
sql = ["PRAGMA foreign_keys=ON;", "BEGIN;"]
for t, rows in tables.items():
    columns = list(rows[0])
    assert all(list(r) == columns for r in rows), t
    types = {c: "INTEGER" if any(isinstance(r[c], bool) for r in rows) else "TEXT" for c in columns}
    schema[t] = {"primary_key": columns[0], "columns": types, "foreign_keys": FK.get(t, {}), "array_columns": [c for c in columns if any(isinstance(r[c], list) for r in rows)]}
    defs = [f'"{c}" {types[c]}' + (" PRIMARY KEY" if c == columns[0] else "") for c in columns]
    for col, (target, targetcol) in FK.get(t, {}).items():
        defs.append(f'FOREIGN KEY("{col}") REFERENCES "{target}"("{targetcol}") DEFERRABLE INITIALLY DEFERRED')
    sql.append(f'CREATE TABLE "{t}" ({", ".join(defs)});')
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(columns)
    for row in rows:
        values = []
        for c in columns:
            v = cell(row[c])
            if isinstance(v, str) and v.lstrip().startswith(("=", "+", "-", "@")):
                v = "'" + v
            values.append(v)
        writer.writerow(values)
    write(OUT / f"{t}.csv", stream.getvalue())
sql.append("COMMIT;")
write(OUT / "schema.sql", "\n".join(sql) + "\n")
conn = sqlite3.connect(OUT / "dataset.sqlite")
conn.executescript("\n".join(sql))
conn.execute("PRAGMA foreign_keys=ON")
conn.execute("BEGIN")
conn.execute("PRAGMA defer_foreign_keys=ON")
for t, rows in tables.items():
    columns = list(rows[0])
    conn.executemany(f'INSERT INTO "{t}" VALUES ({",".join("?" for _ in columns)})', [tuple(cell(r[c]) for c in columns) for r in rows])
assert not conn.execute("PRAGMA foreign_key_check").fetchall()
conn.commit()
assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
conn.execute("VACUUM")
conn.close()
write(OUT / "schema.json", dump(schema))
counts = {t: len(rows) for t, rows in tables.items()}
metadata = {"version": "1.0.0", "checked_date": "2026-10-05", "counts": counts, "system_registry_version": "1.3.0", "system_count": 144, "scope": "Selected central and subnational official governance documents; all 37 jurisdictions screened, not a national census.", "review": "LLM-assisted extraction and single-analyst review; no independent recoding or operational assurance."}
write(OUT / "data.json", dump({"metadata": metadata, **tables}))
analysis = {"counts": counts, "status_counts": dict(sorted(collections.Counter(i["document_status"] for i in tables["instruments"]).items())), "linked_systems": len({l["system_id"] for l in tables["system_links"]}), "linked_instruments": len({l["instrument_id"] for l in tables["system_links"]}), "instrument_families": len({i["instrument_family"] for i in tables["instruments"]}), "subnational_jurisdictions": len({i["jurisdiction"] for i in tables["instruments"] if i["jurisdiction"] != "Central"}), "search_queries": len(read("search-log.json")), "search_hits": sum(r["hits"] for r in read("search-log.json")), "retrieval_receipts": len(read("retrieval-log.json")), "independently_verified_implementation": 0, "interpretation": "Selected-document counts, not national prevalence, compliance scores or verified deployment coverage"}
write(OUT / "analysis.json", dump(analysis))
for i in tables["instruments"]:
    iid = i["instrument_id"]
    text = f"# {i['title']}\n\n[Primary official text]({i['primary_source_url']}). Checked {i['checked_date']}; {i['review_depth']}.\n\n## Identity, status and scope\n\n"
    for k, v in i.items():
        if k not in ("instrument_id", "title", "primary_source_url"):
            text += f"- **{k.replace('_', ' ')}**: {v if v is not None else 'Not established'}\n"
    text += "\n## Five complete coding dimensions\n\n"
    for p in tables["provisions"]:
        if p["instrument_id"] != iid:
            continue
        text += f"### {p['dimension']}\n\n{p['presence']}: {p['summary']}\n\nForce: {p['provision_force']}. Implementation independently verified: no.\n\n"
        if p["evidence_id"]:
            e = next(e for e in tables["evidence"] if e["evidence_id"] == p["evidence_id"])
            url = next(s["url"] for s in tables["sources"] if s["source_id"] == e["source_id"])
            text += f"> {e['quote']}\n\n{e['locator']}. [Read the original]({url}).\n\n"
        if p["unknown_basis"]:
            text += f"Limit: {p['unknown_basis']}\n\n"
    text += "## System associations, not compliance determinations\n\n"
    links = [l for l in tables["system_links"] if l["instrument_id"] == iid]
    if not links:
        text += "No defensible system association included in this release. Not proof of non-applicability.\n\n"
    for l in links:
        name = next(s["name"] for s in tables["system_keys"] if s["system_id"] == l["system_id"])
        text += f"### {name} ({l['system_id']})\n\n{l['link_type']}. {l['rationale']}\n\n{l['applicability_determination']}. Registry assertions: {', '.join(l['system_assertion_ids'])}. Instrument evidence: {', '.join(l['instrument_evidence_ids'])}.\n\n"
        for u in l["system_source_urls"]:
            text += f"Registry evidence: [original record]({u}).\n\n"
    write(OUT / f"dossiers/{iid}.md", text)
for file in ("METHOD.md", "CODEBOOK.md", "ANALYSIS.pplx.md", "queries.sql", "curation.json", "baseline-registry.json", "quote-audit.json", "search-log.json", "search-leads.json", "retrieval-log.json"):
    shutil.copyfile(INPUT / file, OUT / file)
shutil.copyfile(Path(__file__), OUT / "build_governance.py")
write(OUT / "REPRODUCE.md", "# Reproducing the governance layer\n\nUse a clean repository checkout and run `npm ci && npm run package:governance && npm test && npm run build`. The included builder is the source used at scripts/build_governance.py; its frozen inputs belong in research/governance. The separate unchanged public/registry corpus is required for baseline validation and join anchors. This package alone is not the complete deployment registry. Packaging makes no network calls. See METHOD.md and CODEBOOK.md for evidence and scope limits.\n")
files = [{"path": p.relative_to(OUT).as_posix(), "bytes": p.stat().st_size, "sha256": sha(p)} for p in sorted(OUT.rglob("*")) if p.is_file()]
write(OUT / "manifest.json", dump({"version": "1.0.0", "files": files, "counts": counts}))
write(OUT / "manifest.sha256", sha(OUT / "manifest.json") + "  manifest.json\n")
with zipfile.ZipFile(OUT / "complete-governance.zip", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for p in sorted(OUT.rglob("*")):
        if p.is_file() and p.name != "complete-governance.zip":
            info = zipfile.ZipInfo(p.relative_to(OUT).as_posix(), date_time=(2026, 10, 5, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, p.read_bytes(), compresslevel=9)
print(dump({**analysis, "zip_sha256": sha(OUT / "complete-governance.zip"), "sqlite_sha256": sha(OUT / "dataset.sqlite"), "json_sha256": sha(OUT / "data.json"), "registry_baseline_files_unchanged": len(baseline["files"])}))
