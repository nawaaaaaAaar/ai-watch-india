"""Add the previously linked parent Act to the downloadable source inventory."""
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/"public/snapshots/context-dpdp-act.txt"
text=path.read_text()
assert "Digital Personal Data Protection Act, 2023" in text
s=dict(id="context-dpdp-act",title="Digital Personal Data Protection Act, 2023",
 instrument="Parent statute",documentDate="11 August 2023; Gazette code dated 12 August",
 publication="Gazette statute, not a certification of all current commencement or court status",
 status="Parent statute; contextual source",url="https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf",
 snapshot="snapshots/context-dpdp-act.txt",hash=hashlib.sha256(path.read_bytes()).hexdigest(),
 hashType="SHA-256 of extracted UTF-8 text, not PDF bytes",sourceType="Official statute",
 snapshotKind="Extracted source text",checked="5 October 2026",
 description="The parent Act linked by the DPDP briefs is now included as extracted text. This is a contextual document, not an additional comparison or contribution.")
out={"sources":[s]}
for name in ["src/data/context.json","public/context-data.json"]:(ROOT/name).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(ROOT/"src/data/context.json")
print("Packaged one contextual parent-statute source; no new evidence-unit count.")
