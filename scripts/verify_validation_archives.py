"""Run both extracted archive workflows; all completed ratings here are SYNTHETIC."""
from pathlib import Path
import tempfile,zipfile,subprocess,json,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
def readcsv(p):
 with p.open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def writecsv(p,rows):
 with p.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)
def hashfile(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(name,value):
 assert value,name;checks.append({"check":name,"passed":True})
with tempfile.TemporaryDirectory() as temporary:
 t=Path(temporary);review=t/"reviewer";manager=t/"manager"
 for archive,folder in [(ROOT/"public/validation/reviewer-pack.zip",review),(ROOT/"private-validation/manager-kit.zip",manager)]:
  with zipfile.ZipFile(archive) as z:z.extractall(folder)
 reference=manager/"baseline.csv";ratings=review/"ratings.csv";schema=review/"variables.json";units=review/"units.csv"
 def run(rating,out,adjudication=None):
  cmd=["python",str(manager/"compare_coding.py"),"--reference",str(reference),"--review",str(rating),"--schema",str(schema),"--units",str(units),"--out",str(out)]
  if adjudication:cmd+=["--adjudication",str(adjudication)]
  result=subprocess.run(cmd,cwd=manager,capture_output=True,text=True);assert result.returncode==0,result.stderr
  return json.loads((out/"agreement.json").read_text())
 empty=run(ratings,t/"empty")
 check("Extracted blank reviewer pack waits with zero paired ratings",empty["state"]=="waiting_for_second_review" and empty["paired_ratings"]==0 and empty["assigned_ratings"]==992)
 check("Empty forms do not create agreement scores",all(m["observed_agreement"] is None and m["kappa"] is None for m in empty["metrics"].values()))
 tests=subprocess.run(["python",str(manager/"tests/test_review_agreement.py")],cwd=manager,capture_output=True,text=True)
 check("Extracted manager kit runs its standalone synthetic tests",tests.returncode==0 and "Ran 24 tests" in tests.stderr)
 rows=readcsv(reference)
 for r in rows:r["reviewer_id"]="SYNTHETIC_VERIFICATION_NOT_A_RESEARCHER";r["rationale"]="Synthetic fixture only, not a second coding pass"
 synthetic=t/"synthetic-review.csv";writecsv(synthetic,rows)
 perfect=run(synthetic,t/"synthetic-perfect")
 check("Full synthetic pass joins every assignment exactly once",perfect["paired_ratings"]==992 and perfect["disagreement_rows"]==0)
 check("Non-equivalent coverage comparison is diagnostic only",perfect["comparable_paired_ratings"]==892 and perfect["diagnostic_paired_ratings"]==100 and perfect["metrics"]["coverage_presence"]["kappa"] is None)
 row=next(r for r in rows if r["variable"]=="dimension")
 spec=json.loads(schema.read_text())["variables"]["dimension"]
 row["value"]=next(v for v in spec["allowed"] if v!=row["value"]);writecsv(synthetic,rows)
 changed=run(synthetic,t/"synthetic-changed")
 check("Synthetic changed label produces one disagreement",changed["disagreement_rows"]==1)
 ledger=readcsv(t/"synthetic-changed/adjudication-template.csv")
 ledger[0].update(decision="resolved",resolved_value=ledger[0]["review_value"],cause="synthetic_fixture",rationale="Fixture resolution, not research",evidence_anchor="synthetic anchor",adjudicator="SYNTHETIC_ADJUDICATOR",reference_ack="acknowledged",review_ack="acknowledged",decision_date="2026-10-06")
 completed=t/"synthetic-adjudication.csv";writecsv(completed,ledger)
 before=(hashfile(reference),hashfile(synthetic),hashfile(completed))
 adjudicated=run(synthetic,t/"synthetic-adjudicated",completed)
 check("Consensus export leaves pre-adjudication metrics unchanged",adjudicated["disagreement_rows"]==1 and (t/"synthetic-adjudicated/consensus.csv").exists())
 check("Reference review and completed decision files remain byte-identical",before==(hashfile(reference),hashfile(synthetic),hashfile(completed)))
 with zipfile.ZipFile(ROOT/"public/validation/reviewer-pack.zip") as z:
  check("Reviewer ZIP contains no original baseline or linkage key",not any("baseline" in name or name=="key.json" for name in z.namelist()))
 check("No owner-only manager key or ZIP lives under public",not (ROOT/"public/validation/manager").exists() and not (ROOT/"public/validation/manager-kit.zip").exists())
receipt={"state":"archive_workflow_verified_using_synthetic_fixtures_only","independent_review_completed":False,"checks":checks,"empty_review_paired_ratings":0,"reviewer_zip_sha256":hashfile(ROOT/"public/validation/reviewer-pack.zip"),"manager_zip_sha256":hashfile(ROOT/"private-validation/manager-kit.zip")}
out=ROOT/"verification/validation/archive-workflow.json";out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
