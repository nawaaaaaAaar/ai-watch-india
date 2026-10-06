"""Two-pass descriptive agreement and separate adjudication; no third-party packages."""
import argparse,collections,csv,hashlib,json,math
from pathlib import Path
STATUS={"coded","unresolved","unreadable","not_applicable","pending"}
FIELDS=["schema_version","unit_id","variable","reviewer_id","value","coding_status","rationale","evidence_anchor","source_access"]
ADJ=["unit_id","variable","reference_value","review_value","decision","resolved_value","cause","rationale","evidence_anchor","adjudicator","reference_ack","review_ack","decision_date"]
def fingerprint(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write_csv(p,rows,fields):
 with Path(p).open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n");w.writeheader();w.writerows(rows)
def read_csv(p):
 with Path(p).open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def canon(value,spec):
 if spec["kind"]=="set":
  try:tags=json.loads(value)
  except Exception as e:raise ValueError("Set value must be a JSON array") from e
  if not isinstance(tags,list) or not tags or any(not isinstance(v,str) for v in tags):raise ValueError("Set must contain labels")
  if len(tags)!=len(set(tags)) or not set(tags)<=set(spec["allowed"]):raise ValueError("Invalid/duplicate set label")
  if "Not established" in tags and len(tags)>1:raise ValueError("Not established must be a singleton")
  return json.dumps(sorted(tags),ensure_ascii=False,separators=(",",":"))
 value=" ".join(value.split())
 if not value:raise ValueError("Coded value is empty")
 if spec["kind"]=="nominal" and value not in spec["allowed"]:raise ValueError("Unknown category: "+value)
 return value
def load_ratings(path,schema,expected,allow_partial=False):
 rows=read_csv(path);out={}
 for row in rows:
  if set(row)!=set(FIELDS):raise ValueError("Rating CSV columns differ from schema")
  key=(row["unit_id"],row["variable"])
  if key not in expected or key in out:raise ValueError("Unknown or duplicate assignment: "+str(key))
  if row["schema_version"]!=schema["version"]:raise ValueError("Schema version mismatch")
  status=row["coding_status"]
  if status not in STATUS:raise ValueError("Invalid coding_status")
  if status=="coded":
   if not all(row[k].strip() for k in ["reviewer_id","rationale","evidence_anchor","source_access"]):raise ValueError("Coded rating needs identity, rationale, anchor and access basis")
   row["value"]=canon(row["value"],schema["variables"][row["variable"]])
  elif row["value"].strip():raise ValueError("Uncoded response must have a blank value")
  out[key]=row
 if set(out)!=expected and not allow_partial:raise ValueError("Missing assignment rows; use --allow-partial for deliberate partial submission")
 if len({r["reviewer_id"] for r in out.values() if r["coding_status"]=="coded"})>1:raise ValueError("One submission must represent one coder, not mixed identities")
 return out
def agreement(pairs,kind):
 n=len(pairs)
 if not n:return {"paired":0,"agreements":0,"observed_agreement":None,"kappa":None,"kappa_reason":"No complete paired ratings","mean_jaccard":None,"marginals_reference":{},"marginals_review":{},"confusion":[]}
 a=collections.Counter(x for x,y in pairs);b=collections.Counter(y for x,y in pairs);cells=collections.Counter(pairs)
 equal=sum(x==y for x,y in pairs);po=equal/n
 pe=sum(a[k]*b[k] for k in set(a)|set(b))/(n*n)
 kappa=(po-pe)/(1-pe) if kind=="nominal" and not math.isclose(pe,1,abs_tol=1e-12) else None
 reason="Constant-category marginals: chance agreement is one" if kind=="nominal" and kappa is None else "Not computed for exact text or set variables" if kind!="nominal" else ""
 jaccard=None
 if kind=="set":
  sets=[(set(json.loads(x)),set(json.loads(y))) for x,y in pairs]
  jaccard=sum(len(x&y)/len(x|y) for x,y in sets)/n
 return {"paired":n,"agreements":equal,"observed_agreement":po,"kappa":kappa,"kappa_reason":reason,"mean_jaccard":jaccard,"marginals_reference":dict(sorted(a.items())),"marginals_review":dict(sorted(b.items())),"confusion":[{"reference":x,"review":y,"count":count} for (x,y),count in sorted(cells.items())]}
def compare(reference,review,schema,units,out,adjudication=None):
 a_ids={r["reviewer_id"] for r in reference.values() if r["coding_status"]=="coded"}
 b_ids={r["reviewer_id"] for r in review.values() if r["coding_status"]=="coded"}
 if a_ids & b_ids:raise ValueError("Reference and review must identify distinct coding passes")
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 index={u["unit_id"]:u for u in units};expected={(uid,v) for uid,u in index.items() for v in json.loads(u["variables"])}
 if set(reference)!=expected:raise ValueError("Reference does not contain all assignments")
 metrics={};disagree=[];unpaired=[];profiles=collections.Counter()
 for variable,spec in schema["variables"].items():
  keys=sorted(k for k in expected if k[1]==variable);pairs=[]
  ar=collections.Counter();br=collections.Counter()
  for key in keys:
   ra=reference[key];rb=review.get(key)
   ar[ra["coding_status"]]+=1;br[rb["coding_status"] if rb else "missing"]+=1
   if ra["coding_status"]=="coded" and rb and rb["coding_status"]=="coded":
    pairs.append((ra["value"],rb["value"]))
    if ra["value"]!=rb["value"]:
     row={"unit_id":key[0],"variable":variable,"reference_value":ra["value"],"review_value":rb["value"],"reference_rationale":ra["rationale"],"review_rationale":rb["rationale"],"source_ids":index[key[0]]["source_ids"]}
     disagree.append(row)
     for source in json.loads(index[key[0]]["source_ids"]):profiles[(source,variable)]+=1
   else:unpaired.append({"unit_id":key[0],"variable":variable,"reference_status":ra["coding_status"],"review_status":rb["coding_status"] if rb else "missing"})
  m=agreement(pairs,spec["kind"])
  comparable=spec.get("comparable_reference",True)
  if not comparable:m["kappa"]=None;m["kappa_reason"]="Non-equivalent reference/review constructs; diagnostic comparison only"
  metrics[variable]={"kind":spec["kind"],"metric_purpose":"intercoder comparison" if comparable else "construct diagnostic, not intercoder reliability","assigned":len(keys),"reference_statuses":dict(ar),"review_statuses":dict(br),**m}
 summary={"schema_version":schema["version"],"state":"waiting_for_second_review" if not any(m["paired"] for m in metrics.values()) else "complete_paired_review" if not unpaired else "partial_paired_review","assigned_ratings":len(expected),"paired_ratings":sum(m["paired"] for m in metrics.values()),"comparable_paired_ratings":sum(m["paired"] for m in metrics.values() if m["metric_purpose"]=="intercoder comparison"),"diagnostic_paired_ratings":sum(m["paired"] for m in metrics.values() if m["metric_purpose"]!="intercoder comparison"),"disagreement_rows":len(disagree),"unpaired_rows":len(unpaired),"metrics":metrics,"interpretation":"Descriptive pre-adjudication comparison; coverage is a non-equivalent-construct diagnostic. Not correctness, independence certification, operational validation or national prevalence."}
 (out/"agreement.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
 write_csv(out/"metrics.csv",[{k:m.get(k) for k in ["kind","metric_purpose","assigned","paired","agreements","observed_agreement","kappa","kappa_reason","mean_jaccard"]}|{"variable":v} for v,m in metrics.items()],["variable","kind","metric_purpose","assigned","paired","agreements","observed_agreement","kappa","kappa_reason","mean_jaccard"])
 write_csv(out/"confusion.csv",[{"variable":v,**cell} for v,m in metrics.items() for cell in m["confusion"]],["variable","reference","review","count"])
 write_csv(out/"disagreements.csv",disagree,["unit_id","variable","reference_value","review_value","reference_rationale","review_rationale","source_ids"])
 write_csv(out/"unpaired.csv",unpaired,["unit_id","variable","reference_status","review_status"])
 write_csv(out/"source-disagreement-profile.csv",[{"source_id":s,"variable":v,"disagreements":n} for (s,v),n in sorted(profiles.items())],["source_id","variable","disagreements"])
 adjrows=[{k:(r.get(k,"") if k in ["unit_id","variable","reference_value","review_value"] else "") for k in ADJ} for r in disagree]
 write_csv(out/"adjudication-template.csv",adjrows,ADJ)
 if adjudication:
  decisions=read_csv(adjudication);seen=set();valid={(r["unit_id"],r["variable"]):r for r in disagree};consensus=[]
  for r in decisions:
   if set(r)!=set(ADJ):raise ValueError("Adjudication columns differ from schema")
   key=(r["unit_id"],r["variable"])
   if key not in valid or key in seen:raise ValueError("Unknown/duplicate adjudication key")
   seen.add(key);initial=valid[key]
   if r["reference_value"]!=initial["reference_value"] or r["review_value"]!=initial["review_value"]:raise ValueError("Initial values were changed in adjudication")
   if r["decision"] not in ["resolved","unresolved"]:raise ValueError("Missing/invalid decision")
   if not all(r[k].strip() for k in ["cause","rationale","evidence_anchor","adjudicator","decision_date"]):raise ValueError("Adjudication needs provenance and named decision-maker")
   if r["reference_ack"]!="acknowledged" or r["review_ack"]!="acknowledged":raise ValueError("Both initial coders must acknowledge reviewing the adjudication")
   if r["decision"]=="resolved":value=canon(r["resolved_value"],schema["variables"][key[1]])
   else:
    if r["resolved_value"].strip():raise ValueError("Unresolved decision must not invent a consensus value")
    value=""
   consensus.append({**r,"resolved_value":value})
  write_csv(out/"consensus.csv",consensus,ADJ)
  (out/"adjudication-audit.json").write_text(json.dumps({"decisions":len(consensus),"unadjudicated_disagreements":len(valid)-len(seen),"pre_adjudication_metrics_unchanged":True},indent=2)+"\n")
 return summary
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("--reference",required=True);p.add_argument("--review",required=True);p.add_argument("--schema",required=True);p.add_argument("--units",required=True);p.add_argument("--out",required=True);p.add_argument("--allow-partial",action="store_true");p.add_argument("--adjudication");args=p.parse_args()
 reserved={"agreement.json","metrics.csv","confusion.csv","disagreements.csv","unpaired.csv","source-disagreement-profile.csv","adjudication-template.csv","consensus.csv","adjudication-audit.json","input-fingerprints.json"}
 for field in ["reference","review","schema","units"]+(['adjudication'] if args.adjudication else []):
  path=Path(getattr(args,field)).resolve()
  if path.parent==Path(args.out).resolve() and path.name in reserved:raise ValueError("Output would overwrite an input file")
 schema=json.loads(Path(args.schema).read_text());units=read_csv(args.units)
 if len(units)!=len({u["unit_id"] for u in units}):raise ValueError("Duplicate unit IDs")
 expected={(u["unit_id"],v) for u in units for v in json.loads(u["variables"])}
 reference=load_ratings(args.reference,schema,expected);review=load_ratings(args.review,schema,expected,args.allow_partial)
 summary=compare(reference,review,schema,units,args.out,args.adjudication)
 inputs={k:{"path":str(getattr(args,k)),"sha256":fingerprint(getattr(args,k))} for k in ["reference","review","schema","units"]+(['adjudication'] if args.adjudication else [])}
 Path(args.out,"input-fingerprints.json").write_text(json.dumps(inputs,indent=2)+"\n")
 print(json.dumps({k:summary[k] for k in ["state","assigned_ratings","paired_ratings","disagreement_rows","unpaired_rows"]},indent=2))
if __name__=="__main__":main()
