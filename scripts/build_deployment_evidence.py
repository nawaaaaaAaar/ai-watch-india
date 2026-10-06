"""Offline reproducible implementation layer. Registry and governance are read-only."""
from pathlib import Path
import json,csv,io,sqlite3,hashlib,zipfile,shutil,collections
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"research/implementation-evidence"
OUT=ROOT/"public/implementation-evidence"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((INPUT/n).read_text())
def dump(x):return json.dumps(x,ensure_ascii=False,indent=2)+"\n"
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding="utf-8")
def cell(v):
 if isinstance(v,(list,dict)):return json.dumps(v,ensure_ascii=False,separators=(",",":"))
 if isinstance(v,bool):return int(v)
 return v
baseline=read("baseline-layers.json")
for f in baseline["files"]:assert sha(ROOT/f["path"])==f["sha256"],f["path"]
tables=read("curation.json")
assert len(tables["system_keys"])==144 and len(tables["governance_keys"])==52
assert len(tables["cases"])==10 and len(tables["coverage"])==100
ids={t:{r[next(iter(r))] for r in rows} for t,rows in tables.items()}
assert all(rows and len(rows)==len(ids[t]) for t,rows in tables.items())
FK={
 "cases":{"system_id":("system_keys","system_id")},
 "observations":{"document_id":("documents","document_id"),"evidence_id":("evidence","evidence_id")},
 "evidence":{"document_id":("documents","document_id"),"observation_id":("observations","observation_id")},
 "case_observations":{"system_id":("cases","system_id"),"observation_id":("observations","observation_id")},
 "party_observations":{"observation_id":("observations","observation_id")},
 "financial_observations":{"observation_id":("observations","observation_id")},
 "coverage":{"system_id":("cases","system_id")},
 "governance_links":{"system_id":("cases","system_id"),"instrument_id":("governance_keys","instrument_id")},
 "selection_decisions":{"system_id":("system_keys","system_id")}}
for t,refs in FK.items():
 for r in tables[t]:
  for col,(target,_) in refs.items():assert r[col] in ids[target],(t,col,r[col])
registry=json.loads((ROOT/"public/registry/data.json").read_text())
governance=json.loads((ROOT/"public/governance/data.json").read_text())
assert {s["system_id"] for s in registry["systems"]}==ids["system_keys"]
assert {i["instrument_id"] for i in governance["instruments"]}==ids["governance_keys"]
for link in tables["case_observations"]:
 assert set(link["registry_assertion_ids"])<={a["assertion_id"] for a in registry["assertions"] if a["system_id"]==link["system_id"]}
for r in tables["coverage"]:
 assert set(r["observation_ids"])<=ids["observations"]
 assert all(any(l["system_id"]==r["system_id"] and l["observation_id"]==oid for l in tables["case_observations"]) for oid in r["observation_ids"])
for r in tables["governance_links"]:
 old=next(l for l in governance["system_links"] if l["system_link_id"]==r["existing_governance_link_id"])
 assert old["system_id"]==r["system_id"] and old["instrument_id"]==r["instrument_id"]
 assert set(r["instrument_evidence_ids"])==set(old["instrument_evidence_ids"])
 assert set(r["implementation_observation_ids"])<=ids["observations"]
assert all(not o["independent_outcome_verified"] for o in tables["observations"])
assert all(q["selected_passages_match"] and q["selected_words"]<=250 for q in read("quote-audit.json"))
if OUT.exists():shutil.rmtree(OUT)
OUT.mkdir()
schema={};sql=["PRAGMA foreign_keys=ON;","BEGIN;"]
for t,rows in tables.items():
 cols=list(rows[0]);assert all(list(r)==cols for r in rows)
 types={c:"INTEGER" if any(isinstance(r[c],bool) for r in rows) else "TEXT" for c in cols}
 defs=[f'"{c}" {types[c]}'+(" PRIMARY KEY" if c==cols[0] else "") for c in cols]
 for c,(target,targetcol) in FK.get(t,{}).items():defs.append(f'FOREIGN KEY("{c}") REFERENCES "{target}"("{targetcol}") DEFERRABLE INITIALLY DEFERRED')
 sql.append(f'CREATE TABLE "{t}" ({", ".join(defs)});')
 schema[t]={"primary_key":cols[0],"columns":types,"foreign_keys":FK.get(t,{}),"array_columns":[c for c in cols if any(isinstance(r[c],list) for r in rows)]}
 stream=io.StringIO(newline="");w=csv.writer(stream,lineterminator="\n");w.writerow(cols)
 for r in rows:
  values=[cell(r[c]) for c in cols]
  w.writerow(["'"+v if isinstance(v,str) and v.lstrip().startswith(("=","+","-","@")) else v for v in values])
 write(OUT/f"{t}.csv",stream.getvalue())
sql.append("COMMIT;");write(OUT/"schema.sql","\n".join(sql)+"\n")
conn=sqlite3.connect(OUT/"dataset.sqlite");conn.executescript("\n".join(sql))
conn.execute("PRAGMA foreign_keys=ON");conn.execute("BEGIN");conn.execute("PRAGMA defer_foreign_keys=ON")
for t,rows in tables.items():conn.executemany(f'INSERT INTO "{t}" VALUES ({",".join("?" for _ in rows[0])})',[tuple(cell(v) for v in r.values()) for r in rows])
assert not conn.execute("PRAGMA foreign_key_check").fetchall()
conn.commit();assert conn.execute("PRAGMA integrity_check").fetchone()[0]=="ok"
conn.execute("VACUUM");conn.close()
counts={t:len(rows) for t,rows in tables.items()}
meta={"version":"1.0.0","checked_date":"2026-10-05","counts":counts,"system_count":144,"selected_cases":10,"registry_version":"1.3.0","governance_version":"1.0.0","scope":"Purposive ten-case implementation/procurement deepening; no new system families, operational audit or national prevalence inference.","review":"LLM-assisted extraction and single-analyst review; no independent outcome verification."}
write(OUT/"data.json",dump({"metadata":meta,**tables}));write(OUT/"schema.json",dump(schema))
analysis={"counts":counts,"strength_counts":dict(sorted(collections.Counter(o["evidence_strength"] for o in tables["observations"]).items())),"search_queries":len(read("search-log.json")),"search_hits":sum(r["hits"] for r in read("search-log.json")),"retained_retrieval_receipts":len(read("retrieval-log.json")),"cached_documents":sum(d["is_cached"] for d in tables["documents"]),"unknown_coverage_rows":sum(not c["observation_ids"] for c in tables["coverage"]),"independently_verified_outcomes":0,"baseline_files_preserved":len(baseline["files"])}
write(OUT/"analysis.json",dump(analysis))
for d in tables["documents"]:
 text=f"# {d['title']}\n\n[Original primary record]({d['url']}). This is a selected-excerpt snapshot, not a full document mirror.\n\n"
 for k in ["issuing_body","document_date","date_precision","date_text","document_kind","source_role","association_scope","review_depth","retrieval_basis","is_cached","reviewed_text_sha256","extraction_limit"]:
  text+=f"- **{k.replace('_',' ')}**: {d[k] if d[k] is not None else 'Not established'}\n"
 for e in tables["evidence"]:
  if e["document_id"]==d["document_id"]:text+=f"\n## {e['evidence_id']}\n\n> {e['quote']}\n\n{e['locator']}. {e['verification_mode']}. [Original record]({d['url']}).\n"
 write(OUT/d["snapshot"],text)
for c in tables["cases"]:
 sid=c["system_id"];text=f"# {c['name']}: implementation and procurement evidence\n\nChecked {c['checked_date']}. Existing registry family `{sid}`; baseline values unchanged.\n\n## What changes\n\n{c['change_in_understanding']}\n\n{c['coverage_limit']}\n\n## Ten dimensions, including unknowns\n\n"
 links=[l for l in tables["case_observations"] if l["system_id"]==sid]
 for cv in tables["coverage"]:
  if cv["system_id"]!=sid:continue
  text+=f"### {cv['dimension']}\n\n{cv['evidence_status']}. Next record: {cv['unknown_or_next_record']}\n\n"
  for oid in cv["observation_ids"]:
   o=next(o for o in tables["observations"] if o["observation_id"]==oid);e=next(e for e in tables["evidence"] if e["evidence_id"]==o["evidence_id"]);d=next(d for d in tables["documents"] if d["document_id"]==o["document_id"])
   text+=f"{o['statement']} ([{d['title']}]({d['url']})).\n\nStrength: {o['evidence_strength']}; type: {o['claim_type']}; event date: {o['event_date'] or 'Not established'}. Independent outcome verification: no.\n\n> {e['quote']}\n\n{e['locator']}. [Original text]({d['url']}).\n\nLimit: {o['limitation']}\n\n"
 text+="## Existing governance links, not compliance findings\n\n"
 for g in tables["governance_links"]:
  if g["system_id"]==sid:
   i=next(i for i in tables["governance_keys"] if i["instrument_id"]==g["instrument_id"])
   text+=f"- **{i['title']}**: {g['link_type']}. {g['rationale']} {g['applicability_determination']} ([primary text]({i['primary_source_url']})).\n"
 write(OUT/f"dossiers/{sid}.md",text)
for n in ["METHOD.md","CODEBOOK.md","implementation-findings.pplx.md","queries.sql","curation.json","baseline-layers.json","baseline-candidates.json","quote-audit.json","search-log.json","search-leads.json","retrieval-log.json","review-decisions.json"]:shutil.copyfile(INPUT/n,OUT/n)
shutil.copyfile(Path(__file__),OUT/"build_deployment_evidence.py")
write(OUT/"REPRODUCE.md","# Reproducing implementation evidence\n\nUse a clean repository checkout and run `npm ci && npm run package:implementation && npm test && npm run build`. The builder reads frozen inputs in research/implementation-evidence and the unchanged registry/governance layers. It performs no network calls. This ZIP is the new layer, not the full 144-family registry or governance archive; join keys are included. See METHOD.md for retrieval and scope limits.\n")
files=[{"path":str(p.relative_to(OUT)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(OUT.rglob("*")) if p.is_file()]
write(OUT/"manifest.json",dump({"version":"1.0.0","counts":counts,"files":files}));write(OUT/"manifest.sha256",sha(OUT/"manifest.json")+"  manifest.json\n")
with zipfile.ZipFile(OUT/"complete-implementation-evidence.zip","w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(OUT.rglob("*")):
  if p.is_file() and p.name!="complete-implementation-evidence.zip":
   info=zipfile.ZipInfo(str(p.relative_to(OUT)),(2026,10,5,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,p.read_bytes(),compresslevel=9)
print(dump({**analysis,"zip_sha256":sha(OUT/"complete-implementation-evidence.zip"),"json_sha256":sha(OUT/"data.json"),"sqlite_sha256":sha(OUT/"dataset.sqlite")}))
