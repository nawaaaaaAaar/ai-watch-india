"""Deterministic complete curated-data bundle and per-file integrity manifest."""
from pathlib import Path
import hashlib
import json
import zipfile
ROOT=Path(__file__).resolve().parents[1]
PUB=ROOT/"public"
ROOM=PUB/"data-room"
files=[]
for folder in ["briefs","snapshots","research","data-room"]:
    files.extend(p for p in (PUB/folder).rglob("*") if p.is_file() and p.name not in ["manifest.json","complete-data.zip","archive-sha256.txt","manifest-sha256.txt"])
files.extend(PUB/n for n in ["combined-data.json","policy-data.json","expansion-data.json","implementation-data.json","public-services-data.json","context-data.json"])
files.append(ROOT/"shared/schema.ts")
rows=[]
for path in sorted(set(files)):
    name=path.relative_to(PUB).as_posix() if path.is_relative_to(PUB) else "schema/schema.ts"
    rows.append(dict(path=name,size=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
summary=json.loads((ROOM/"dataset-summary.json").read_text())
manifest=dict(title="AI Watch India: Complete Curated Data Manifest",edition="05",checked="5 October 2026",
 counts=summary["counts"],files=rows,recordIds=[p["id"] for p in summary["records"]],
 sourceIds=[s["id"] for s in summary["sources"]],
 archiveScope="All listed curated records, dossiers, briefs, snapshots, research, registers and schema. Not all Indian AI systems; not full original PDF binaries or full copyrighted articles; no private notebook notes.",
 integrityScope="Hashes verify included file bytes, not source truth or live deployment.",
 omittedKinds=["Original PDF binaries","Full copyrighted articles","Unretrieved records","Private user notes","Application dependencies/build binaries"])
raw=json.dumps(manifest,ensure_ascii=False,indent=2)+"\n"
(ROOM/"manifest.json").write_text(raw)
(ROOM/"manifest-sha256.txt").write_text(hashlib.sha256(raw.encode()).hexdigest()+"  manifest.json\n")
archive=ROOM/"complete-data.zip"
with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for row,path in sorted(zip(rows,sorted(set(files))),key=lambda x:x[0]["path"]):
        info=zipfile.ZipInfo(row["path"],date_time=(2026,10,5,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
        z.writestr(info,path.read_bytes())
    for name,content in [("data-room/manifest.json",raw),("data-room/manifest-sha256.txt",(ROOM/"manifest-sha256.txt").read_text())]:
        info=zipfile.ZipInfo(name,date_time=(2026,10,5,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,content)
(ROOM/"archive-sha256.txt").write_text(hashlib.sha256(archive.read_bytes()).hexdigest()+"  complete-data.zip\n")
print(archive)
print(f"Archived {len(rows)} manifested payload files plus manifest and checksum; {archive.stat().st_size} bytes.")
