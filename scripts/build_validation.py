"""Offline, separate conclusion-blinded reviewer pack and coordinator kit."""
from pathlib import Path
import json,csv,hashlib,zipfile,shutil,collections
from compare_coding import FIELDS,write_csv
ROOT=Path(__file__).resolve().parents[1];INPUT=ROOT/"research/validation";OUT=ROOT/"public/validation"
PRIVATE=ROOT/"private-validation"
def read(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def opaque(kind,key):return kind+hashlib.sha256(("review-v1|"+key).encode()).hexdigest()[:10]
def arr(x):return json.dumps(x,ensure_ascii=False,separators=(",",":"))
fixed=read(INPUT/"baseline-fixed.json")
for f in fixed["files"]:assert sha(ROOT/f["path"])==f["sha256"],f["path"]
d=read(ROOT/"public/implementation-evidence/data.json");g=read(ROOT/"public/governance/data.json")
assert len(d["system_keys"])==144 and len(d["cases"])==10
if OUT.exists() or PRIVATE.exists():
 # A reviewer may have filled local forms. Never rebuild over edited submissions.
 for folder in [OUT/"reviewer",OUT/"manager",PRIVATE/"manager"]:
  if not folder.exists():continue
  manifest=folder/"manifest.json"
  if not manifest.exists():raise ValueError("Existing partial pack has no manifest; preserve it outside the output folder before rebuilding")
  payload=read(manifest)["files"]
  known={f["path"] for f in payload}|{"manifest.json","manifest.sha256"}
  actual={str(p.relative_to(folder)) for p in folder.rglob("*") if p.is_file()}
  if actual!=known:raise ValueError("Pack contains additional/missing files; preserve submissions/results before rebuilding")
  for f in payload:
   if sha(folder/f["path"])!=f["sha256"]:raise ValueError("Edited pack/submission detected; refusing to overwrite "+str(folder/f["path"]))
 if OUT.exists():shutil.rmtree(OUT)
 if PRIVATE.exists():shutil.rmtree(PRIVATE)
REVIEW=OUT/"reviewer";MANAGER=PRIVATE/"manager";REVIEW.mkdir(parents=True);MANAGER.mkdir(parents=True)
case_map={c["system_id"]:opaque("C",c["system_id"]) for c in d["cases"]}
source_map={s["url"]:opaque("D",s["url"]) for s in d["documents"]}
instrument_map={i:opaque("P",i) for i in {l["instrument_id"] for l in d["governance_links"]}}
original_docs={s["document_id"]:s for s in d["documents"]}
sources={source_map[s["url"]]:{"source_id":source_map[s["url"]],"original_url":s["url"],"reviewed_text_sha256":s["reviewed_text_sha256"],"is_cached":s["is_cached"],"retrieval_phase":s["retrieval_basis"],"technical_note":"Frozen selected extraction; verify original page and version. Text hash is not binary authentication.","fragments":[]} for s in d["documents"]}
fragment_map={}
for e in d["evidence"]:
 fid=opaque("F",e["evidence_id"]);fragment_map[e["evidence_id"]]=fid
 sources[source_map[e["source_url"]]]["fragments"].append({"fragment_id":fid,"quote":e["quote"],"locator":e["locator"].replace("; original PDF pages 4–5 visually checked",""),"material_kind":"verbatim selected excerpt"})
for ctx in read(INPUT/"context-input.json"):
 assert ctx["passages_match"] and ctx["selected_words"]<=250
 sources[source_map[ctx["url"]]]["fragments"].append({"fragment_id":opaque("F","opening|"+ctx["url"]),"quote":ctx["quote"],"locator":ctx["locator"],"material_kind":"bounded original-text context"})
gov_fragments={}
for iid in sorted(instrument_map):
 i=next(i for i in g["instruments"] if i["instrument_id"]==iid);url=i["primary_source_url"]
 if url not in source_map:
  source_map[url]=opaque("D",url);s=next(s for s in g["sources"] if s["source_id"]==i["primary_source_id"])
  sources[source_map[url]]={"source_id":source_map[url],"original_url":url,"reviewed_text_sha256":s["reviewed_text_sha256"],"is_cached":s["is_cached"],"retrieval_phase":s["retrieval_basis"],"technical_note":"Frozen selected extraction; verify original text and version. No status/applicability classification supplied.","fragments":[]}
  selected={eid for l in d["governance_links"] if l["instrument_id"]==iid for eid in l["instrument_evidence_ids"]}
  for eid in sorted(selected):
   e=next(e for e in g["evidence"] if e["evidence_id"]==eid)
   sources[source_map[url]]["fragments"].append({"fragment_id":opaque("F",eid),"quote":e["quote"],"locator":e["locator"],"material_kind":"verbatim selected excerpt"})
 gov_fragments[iid]=[f["fragment_id"] for f in sources[source_map[url]]["fragments"]]
for s in sources.values():
 assert sum(len(f["quote"].split()) for f in s["fragments"])<=250,s["source_id"]
 if "document.kerala.gov.in/documents/cabinetdecisions" in s["original_url"]:
  s["technical_note"]+=" Malayalam extraction is damaged; numeric/English tokens are not a full clause. Original-page review and appropriate language competence are needed."
def nominal(allowed,definition):return {"kind":"nominal","allowed":allowed,"definition":definition}
variables={
 "dimension":nominal(["Procurement","Contracts and awards","Funding","Supplier","Implementation","Evaluation","Human oversight","Redress","Data safeguards","Operational status"],"Primary documentary subject, not exclusive relevance."),
 "claim_type":nominal(["Embedded supplier claim","General institutional route","Implementer account of award / agreement","Official reported activity","Official reported outcome","Procurement invitation","Requirement / specification","Other / mixed","Not established"],"Source speech act, not truth or verified deployment."),
 "evidence_strength":nominal(["First-party reported activity or outcome","Formal prescribed requirement","Implementer's historical account","Institutional contextual evidence","Procurement-stage invitation","Other / mixed","Not established"],"Categorical source/stage classification; not ordinal."),
 "event_date":{"kind":"exact","definition":"Event date or stated interval; Unknown is substantive, not missing."},
 "current_version_match":nominal(["Document-specific; no wider version or coverage inference","Not established","Current deployed version established","Different version established","Unclear"],"Version/scope distinction; explain which construct drives choice."),
 "independent_outcome_verified":nominal(["Established","Not established"],"Whether reviewed evidence establishes independent verification, not global absence."),
 "document_date":{"kind":"exact","definition":"Publication/effective date as defined in notes; Unknown when not established after adequate review."},
 "date_precision":nominal(["Day","Month","Year","Interval / other","Not established"],"Precision of coded document date."),
 "document_association_scope":nominal(["Named-system or component evidence","Institutional/platform context","Association not defensible","Unclear"],"Candidate case-source association, not assumed applicability."),
 "coverage_presence":nominal(["Relevant evidence in reviewed corpus","Not established in reviewed corpus","Unclear"],"Relevant corpus evidence, not verified implementation; may expose primary-dimension allocation mismatch."),
 "amount_text":{"kind":"exact","definition":"Independent source monetary transcription; exact match is only format agreement."},
 "finance_stage":{"kind":"set","allowed":["Estimate","Bid security","Authorised cost / sanction","Reported cost / price","Payment arrangement","Verified expenditure","Not established"],"definition":"Source financial stages; multiple allowed except singleton Not established."},
 "governance_link_type":nominal(["Common original primary document","Inherited, expressly qualified governance association","Association not defensible","Unclear"],"Independent scope judgment for a candidate instrument-system pair."),
 "compliance_verified":nominal(["Established","Not established"],"Reviewed evidence of compliance, not inference from a policy's existence.")
}
schema={"version":"1.0.0","variables":variables,"statuses":["coded","unresolved","unreadable","not_applicable","pending"],"missing_rule":"Only coded-coded pairs are scored; substantive Unknown/Not established are valid codes where defined.","rating_columns":FIELDS}
variables["coverage_presence"]["comparable_reference"]=False
variables["coverage_presence"]["comparison_limit"]="Legacy A records primary-dimension allocation; B audits relevant corpus evidence. Treat matches/disagreements as construct diagnostics, not intercoder reliability, until A is recoded under the same rubric."
units=[];baseline=[];key=[];qual=[];projections=[]
def add(kind,old_id,cases,sourceids,fragments,values,prompt,dimension="",instruments=None):
 uid=opaque("U",kind+"|"+old_id)
 u={"unit_id":uid,"unit_kind":kind,"case_ids":arr(sorted(cases)),"source_ids":arr(sorted(set(sourceids))),"fragment_ids":arr(fragments),"candidate_instrument_ids":arr(instruments or []),"task_dimension":dimension,"task":prompt,"variables":arr(list(values))}
 units.append(u);key.append({"unit_id":uid,"original_kind":kind,"original_id":old_id})
 for v,value in values.items():
  baseline.append({"schema_version":"1.0.0","unit_id":uid,"variable":v,"reviewer_id":"original_analyst_reference","value":arr(sorted(value)) if isinstance(value,list) else str(value),"coding_status":"coded","rationale":"Published first-analyst coding or explicitly documented projection; not a gold standard.","evidence_anchor":";".join(fragments or sourceids),"source_access":"original_dataset_reference"})
 return uid
obs_map={}
for o in d["observations"]:
 links=[l for l in d["case_observations"] if l["observation_id"]==o["observation_id"]]
 doc=original_docs[o["document_id"]];fid=fragment_map[o["evidence_id"]]
 vals={k:o[k] for k in ["dimension","claim_type","evidence_strength","event_date","current_version_match","independent_outcome_verified"]}
 vals["event_date"]=o["event_date"] or "Unknown";vals["independent_outcome_verified"]="Established" if o["independent_outcome_verified"] else "Not established"
 uid=add("observation",o["observation_id"],[case_map[l["system_id"]] for l in links],[source_map[doc["url"]]],[fid],vals,"Independently reconstruct and classify this documentary fragment; consult original context for dates, scope and limits.")
 obs_map[o["observation_id"]]=uid
 qual.append({"unit_id":uid,"original_statement":o["statement"],"original_limitation":o["limitation"],"original_date_basis":o["date_basis"],"party_observations":[p for p in d["party_observations"] if p["observation_id"]==o["observation_id"]]})
for doc in d["documents"]:
 add("document",doc["document_id"],[],[source_map[doc["url"]]],[],{"document_date":doc["document_date"] or "Unknown","date_precision":doc["date_precision"]},"Independently identify the document date and precision from the original; distinguish issue/effective dates from embedded events or filename dates.")
for sid in case_map:
 oids={l["observation_id"] for l in d["case_observations"] if l["system_id"]==sid}
 docs={o["document_id"] for o in d["observations"] if o["observation_id"] in oids}
 for did in sorted(docs):
  doc=original_docs[did]
  add("case_source",sid+"|"+did,[case_map[sid]],[source_map[doc["url"]]],[],{"document_association_scope":doc["association_scope"]},"Test the candidate source-to-case association; reject or qualify it if the text supports only context or another component/version.")
 for cv in [v for v in d["coverage"] if v["system_id"]==sid]:
  add("coverage",cv["coverage_id"],[case_map[sid]],[source_map[original_docs[did]["url"]] for did in docs],[],{"coverage_presence":"Relevant evidence in reviewed corpus" if cv["observation_ids"] else "Not established in reviewed corpus"},"Review the case's documents for relevant evidence in this dimension, regardless of which selected fragment received a primary code.",cv["dimension"])
STAGE={
 "money-obs-rail-iti-02":["Estimate"],
 "money-obs-vss-tender-02":["Estimate","Bid security"],
 "money-obs-vss-2025-tender-02":["Estimate"],
 "money-obs-upsc-tender-01":["Bid security"],
 "money-obs-upsc-correction-02":["Bid security"],
 "money-obs-tn-launch-02":["Authorised cost / sanction"],
 "money-obs-tn-policy-note-01":["Reported cost / price"],
 "money-obs-igms-rfp-02":["Bid security"],
 "money-obs-safe-report-02":["Reported cost / price"],
 "money-obs-safe-report-03":["Reported cost / price"],
 "money-obs-safe-order-01":["Authorised cost / sanction","Payment arrangement"],
 "money-obs-safe-order-04":["Payment arrangement"]}
for f in d["financial_observations"]:
 o=next(o for o in d["observations"] if o["observation_id"]==f["observation_id"]);doc=original_docs[o["document_id"]]
 cases=[case_map[l["system_id"]] for l in d["case_observations"] if l["observation_id"]==o["observation_id"]]
 uid=add("financial",f["financial_observation_id"],cases,[source_map[doc["url"]]],[fragment_map[o["evidence_id"]]],{"amount_text":f["amount_text"],"finance_stage":STAGE[f["financial_observation_id"]]},"Independently transcribe relevant monetary amounts and identify financial stages; preserve mixed scopes and malformed text.")
 projections.append({"unit_id":uid,"original_field":"amount_kind","original_value":f["amount_kind"],"projected_finance_stage":STAGE[f["financial_observation_id"]],"provenance":"Retrospective original-analyst operationalisation, frozen before second review; not independent recoding."})
for l in d["governance_links"]:
 i=next(i for i in g["instruments"] if i["instrument_id"]==l["instrument_id"]);sid=source_map[i["primary_source_url"]]
 add("governance",l["governance_link_id"],[case_map[l["system_id"]]],[sid],gov_fragments[l["instrument_id"]],{"governance_link_type":l["link_type"],"compliance_verified":"Established" if l["compliance_verified"] else "Not established"},"Test this candidate case-instrument association from the original text; separately assess whether compliance is established.",instruments=[instrument_map[l["instrument_id"]]])
units.sort(key=lambda u:u["unit_id"]);baseline.sort(key=lambda r:(r["unit_id"],r["variable"]))
blank=[{**r,"reviewer_id":"","value":"","coding_status":"pending","rationale":"","evidence_anchor":"","source_access":""} for r in baseline]
write_csv(REVIEW/"units.csv",units,list(units[0]));write_csv(REVIEW/"ratings.csv",blank,FIELDS)
write_csv(REVIEW/"cases.csv",sorted([{"case_id":case_map[c["system_id"]],"target_name":c["name"]} for c in d["cases"]],key=lambda c:c["case_id"]),["case_id","target_name"])
write_csv(REVIEW/"instruments.csv",[{"candidate_instrument_id":instrument_map[iid],"source_id":source_map[next(i for i in g["instruments"] if i["instrument_id"]==iid)["primary_source_url"]]} for iid in sorted(instrument_map)],["candidate_instrument_id","source_id"])
dump(REVIEW/"sources.json",sorted(sources.values(),key=lambda s:s["source_id"]));dump(REVIEW/"variables.json",schema)
notesfields=["unit_id","reviewer_id","independent_reconstruction","parties_and_roles","human_review_and_redress","secondary_dimensions","version_scope_and_limits","evidence_anchor","additional_source_ids"]
write_csv(REVIEW/"unit-notes.csv",[{k:u["unit_id"] if k=="unit_id" else "" for k in notesfields} for u in units],notesfields)
accessfields=["source_id","reviewer_id","access_date","access_result","original_reviewed","original_page_locator","version_or_drift_note","additional_text_sha256"]
write_csv(REVIEW/"source-access.csv",[{k:s["source_id"] if k=="source_id" else "" for k in accessfields} for s in sorted(sources.values(),key=lambda s:s["source_id"])],accessfields)
write_csv(REVIEW/"nominations.csv",[],["nomination_id","reviewer_id","case_id","unit_id_if_related","reason","original_url","locator","independent_statement","proposed_variable_change","notes"])
dump(REVIEW/"reviewer-declaration.json",{"schema_version":"1.0.0","reviewer_id":"","prior_project_exposure":"","discussions_of_expected_results":"","conflicts":"","relevant_language_competence":"","additional_support_or_ai_tools_used":"","start_date":"","completion_date":"","frozen_submission_sha256s":{}})
for p in (INPUT/"reviewer").iterdir():shutil.copyfile(p,REVIEW/p.name)
write_csv(MANAGER/"baseline.csv",baseline,FIELDS)
dump(MANAGER/"key.json",{"cases":case_map,"sources":source_map,"instruments":instrument_map,"units":key,"observation_units":obs_map,"blinding":"Keep separate until review is locked; deterministic masking, not access control."})
dump(MANAGER/"qualitative-reference.json",qual);dump(MANAGER/"baseline-projections.json",projections)
dump(MANAGER/"baseline-fixed.json",fixed);dump(MANAGER/"context-audit.json",read(INPUT/"context-input.json"))
for p in (INPUT/"manager").iterdir():shutil.copyfile(p,MANAGER/p.name)
shutil.copyfile(INPUT/"methodological-weaknesses.pplx.md",MANAGER/"methodological-weaknesses.pplx.md")
shutil.copyfile(INPUT/"vulnerable-variables.csv",MANAGER/"vulnerable-variables.csv")
shutil.copyfile(ROOT/"scripts/compare_coding.py",MANAGER/"compare_coding.py")
shutil.copyfile(Path(__file__),MANAGER/"build_validation.py")
(MANAGER/"tests").mkdir()
shutil.copyfile(ROOT/"tests/test_review_agreement.py",MANAGER/"tests/test_review_agreement.py")
(MANAGER/"REPRODUCE.md").write_text("# Reproducing and testing the review workflow\n\nIn a clean repository checkout run `npm ci && npm run package:validation && npm test`. Packaging reads the frozen original layers and research/validation inputs and makes no network calls. The manager ZIP is intentionally Git-ignored and rebuilt locally; do not publish the key or send it to the reviewer. This copied build_validation.py belongs at scripts/build_validation.py in the repository, not as a standalone builder.\n\nThe comparison tool is standalone, uses Python's standard library and can run from this extracted kit with the separately extracted reviewer forms/schema. Run `python tests/test_review_agreement.py` for labelled synthetic fixtures; these are not a completed independent review. Keep outputs outside the input folders and never replace initial A/B responses with adjudicated values.\n")
sample=[]
for did in sorted(original_docs):
 candidates=[obs_map[o["observation_id"]] for o in d["observations"] if o["document_id"]==did]
 sample.append({"unit_id":min(candidates),"source_id":source_map[original_docs[did]["url"]],"selection":"Deterministic minimum masked observation ID; one per original document, fixed before B","audit_status":"pending","source_checked":"","auditor":"","rationale":""})
write_csv(MANAGER/"control-check-sample.csv",sample,list(sample[0]))
def archive(folder,name,destination=OUT):
 files=[{"path":str(p.relative_to(folder)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(folder.rglob("*")) if p.is_file()]
 dump(folder/"manifest.json",{"version":"1.0.0","files":files})
 (folder/"manifest.sha256").write_text(sha(folder/"manifest.json")+"  manifest.json\n")
 with zipfile.ZipFile(destination/name,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(folder.rglob("*")):
   if p.is_file():
    info=zipfile.ZipInfo(str(p.relative_to(folder)),(2026,10,6,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,p.read_bytes(),compresslevel=9)
archive(REVIEW,"reviewer-pack.zip");archive(MANAGER,"manager-kit.zip",PRIVATE)
inventory={"version":"1.0.0","system_count":144,"cases":10,"sources":len(sources),"instruments":len(instrument_map),"units":len(units),"assigned_ratings":len(baseline),"variables":len(variables),"comparable_variables":13,"diagnostic_only_variables":["coverage_presence"],"unit_types":dict(sorted(collections.Counter(u["unit_kind"] for u in units).items())),"source_fragments":sum(len(s["fragments"]) for s in sources.values()),"fixed_files_unchanged":len(fixed["files"]),"independent_review_completed":False,"reviewer_zip_sha256":sha(OUT/"reviewer-pack.zip"),"manager_zip_sha256":sha(PRIVATE/"manager-kit.zip"),"blinding_limit":"Conclusion-blinded, not identity/sample blind; public prior analyses and analyst-selected passages remain exposure risks."}
dump(OUT/"inventory.json",inventory)
print(json.dumps(inventory,indent=2))
