"""Deterministic, offline compilation of analyst-curated institution/system evidence."""
from pathlib import Path
from collections import Counter
import csv, hashlib, io, json, re, sqlite3, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"public/registry"
CHECKED="2026-10-05"
FIELDS=["Owner & purpose","Decision role & affected people","Deployment & date","Procurement & supplier","Funding & contract","Data & integration","Evaluation & error rates","Human review & overrides","Privacy & retention","Complaints & appeal","Public outputs & access","Current-status limits"]
TABLES=["systems","institutions","system_institutions","system_links","deployments","procurements","evaluations","metrics","controls","policies","system_policy_links","assertions","evidence","evidence_links","sources","issues","candidate_decisions"]
db={k:[] for k in TABLES}
curation=json.loads((ROOT/"research/registry-curation.json").read_text())
old=json.loads((ROOT/"public/combined-data.json").read_text())
old_sources={s["id"]:s for s in old["sources"]}
source_map={};evidence_map={};institutions={}

def stable(prefix,text):
    return prefix+"-"+hashlib.sha256(text.encode()).hexdigest()[:16]
def clean(t):
    return re.sub(r"\s+"," ",t.replace("**","").replace("^","")).strip()
def date(text):
    import datetime
    for fmt in ("%d %B %Y","%d %b %Y","%Y-%m-%d"):
        try:return datetime.datetime.strptime(text,fmt).date().isoformat()
        except ValueError:pass
    return None
def add_source(sid):
    if sid in source_map:return
    s=old_sources[sid]
    row=dict(source_id=sid,title=s["title"],url=s["url"],source_type=s.get("sourceType",s["status"]),published_date=date(s.get("documentDate","")),date_basis="Inherited analyst-coded document date; see original",checked_date=CHECKED)
    source_map[sid]=row
def evidence(e):
    sid=e.get("source_id",e.get("sourceId"))
    if sid not in source_map:add_source(sid)
    q=clean(e["quote"]);eid=stable("ev",sid+"\n"+q)
    if eid not in evidence_map:evidence_map[eid]=dict(evidence_id=eid,source_id=sid,quote=q,locator=e["locator"])
    return eid
def links(table,rid,es):
    for eid in sorted(set(evidence(e) for e in es)):
        db["evidence_links"].append(dict(link_id=stable("link",table+rid+eid),record_type=table,record_id=rid,evidence_id=eid))
def inst(name):
    if name not in institutions:
        institutions[name]=stable("inst",name)
        db["institutions"].append(dict(institution_id=institutions[name],name=name,legal_identity_status="Name as stated in reviewed record; not a registry-certified legal identity"))
    return institutions[name]
def role(sid,name,role,es):
    rid=stable("role",sid+name+role)
    db["system_institutions"].append(dict(role_id=rid,system_id=sid,institution_id=inst(name),role=role))
    links("system_institutions",rid,es)

for s in curation["sources"]:
    source_map[s["source_id"]]={k:v for k,v in s.items() if k!="quotes"}
    source_map[s["source_id"]]["checked_date"]=CHECKED

# The six older cases remain source-backed seed observations, not policy rows.
seed={
 "service-upsc":("sys-upsc","UPSC face authentication","Union Public Service Commission","India","Biometric application; current model architecture not verified"),
 "service-cyberguard":("sys-cyberguard","I4C CyberGuard","Indian Cyber Crime Coordination Centre","India","Explicit AI in official integration description"),
 "service-suvas":("sys-suvas","SUVAS judicial translation","Supreme Court of India","India","Explicit AI translation in official source"),
 "service-supace":("sys-supace","SUPACE research assistance","Supreme Court of India","India","Explicit AI in official experimental description"),
 "service-esanjeevani":("sys-esanjeevani","eSanjeevani clinical decision support","Ministry of Health and Family Welfare","India","Explicit AI in official integration description"),
 "service-mahacrimeos":("sys-mahacrimeos","MahaCrimeOS investigation support","Maharashtra Police","Maharashtra","AI described by vendor/reporting; independent architecture not verified"),
}
profiles=list(curation["profiles"])
for p in old["provisions"]:
    if p["id"] not in seed:continue
    sid,name,owner,jurisdiction,ai=seed[p["id"]]
    fields=p["caseFields"]
    assert [f["name"] for f in fields]==FIELDS
    dated=[date(old_sources[e["sourceId"]].get("documentDate","")) for f in fields for e in f["evidence"]]
    profiles.append(dict(system_id=sid,name=name,owner=owner,sector=p["sector"],jurisdiction=jurisdiction,stage=p["deploymentStage"],latest_record_date=max([d for d in dated if d],default=None),ai_basis=ai,fields=fields,legacy_id=p["id"]))

for p in sorted(profiles,key=lambda p:p["system_id"]):
    sid=p["system_id"];owner=inst(p["owner"]);fields=p["fields"]
    row={k:p.get(k) for k in ["system_id","name","sector","jurisdiction","stage","latest_record_date","ai_basis","legacy_id"]}
    qualified={"sys-digiyatra","sys-upsc","sys-insight","sys-fest"}
    row.update(owner_institution_id=owner,checked_date=CHECKED,unit="Named service/system; not each installation or model",selection="Purposive exploratory seed",ai_class="Qualified algorithmic / biometric context" if sid in qualified else "Explicit source attribution",ai_class_basis="AI attribution includes vendor/editorial sources, not independent or government validation. Qualified subset lacks verified system-specific AI identification in the reviewed records.")
    db["systems"].append(row)
    role(sid,p["owner"],"Responsible institution/operator as described; not necessarily legal owner",fields[0]["evidence"])
    for n,(fname,f) in enumerate(zip(FIELDS,fields),1):
        aid=sid+f"-field-{n:02}"
        db["assertions"].append(dict(assertion_id=aid,system_id=sid,field=fname,value=f["statement"],evidence_status=f["status"],checked_date=CHECKED,coding_basis="Single-analyst source coding; not operational audit"))
        links("assertions",aid,f["evidence"])
    for fld,idx,table in [("Deployment & date",2,"deployments"),("Evaluation & error rates",6,"issues"),("Current-status limits",11,"issues")]:
        if not p.get("legacy_id"):continue
        f=fields[idx];rid=stable(table,sid+fld)
        if table=="deployments":
            db[table].append(dict(deployment_id=rid,system_id=sid,event_date=None,date_precision="Mixed dates in source-backed narrative; not assigned one go-live date",stage=p["stage"],place=p["jurisdiction"],description=f["statement"]))
        else:db[table].append(dict(issue_id=rid,system_id=sid,issue_type=fld,description=f["statement"]))
        links(table,rid,f["evidence"])
    if p.get("legacy_id"):
        f=fields[6]
        if f["evidence"]:
            rid=stable("evaluation",sid+"seed")
            db["evaluations"].append(dict(evaluation_id=rid,system_id=sid,evaluation_type="Evaluation-related documentary evidence; not verified current performance",sample_n=None,sample_unit=None,setting="See assertion and linked source context",current_version_match="Not established",result_summary=f["statement"],evidence_status=f["status"]))
            links("evaluations",rid,f["evidence"])
        for idx in (7,8,9):
            f=fields[idx]
            if not f["evidence"]:continue
            rid=stable("control",sid+FIELDS[idx])
            db["controls"].append(dict(control_id=rid,system_id=sid,control_type=FIELDS[idx],implementation_basis="Published description/requirements; not verified live enforcement",description=f["statement"],evidence_status=f["status"]))
            links("controls",rid,f["evidence"])
    db["candidate_decisions"].append(dict(candidate_id=sid,name=p["name"],decision="Included",reason="Named India public-service AI attribution or qualified algorithmic/biometric context; purposive selection",system_id=sid))

idcols={"deployments":"deployment_id","procurements":"procurement_id","evaluations":"evaluation_id","metrics":"metric_id","controls":"control_id","issues":"issue_id","system_links":"system_link_id"}
for i,d in enumerate(curation["details"]):
    table=d["table"];sid=d["system_id"];v=d["values"];es=d["evidence"]
    if table=="system_institutions":role(sid,v["name"],v["role"],es);continue
    if table=="policies":
        pid=stable("policy",v["title"])
        if not any(r["policy_id"]==pid for r in db["policies"]):db["policies"].append(dict(policy_id=pid,title=v["title"],status=v["status"]))
        links("policies",pid,es)
        rid=stable("policy-link",sid+pid)
        db["system_policy_links"].append(dict(policy_link_id=rid,system_id=sid,policy_id=pid,relation=v["relation"]))
        links("system_policy_links",rid,es);continue
    rid=stable(table,sid+json.dumps(v,sort_keys=True))
    row={idcols[table]:rid,"system_id":sid,**v}
    if table=="metrics":
        row["value_qualifier"]="More than stated lower bound" if sid in ["sys-digiyatra","sys-bhashini","sys-kisan-emitra"] else "About" if sid=="sys-plcs" else "Maximum requirement; not observation" if v["metric_kind"]=="Specification threshold" else "Reported value"
    if table=="procurements":
        row["supplier_institution_id"]=inst(v["supplier_name"]) if v.get("supplier_name") else None
    db[table].append(row);links(table,rid,es)

for name,decision,reason in [
 ("AIKosh","Context only","Training-data repository is not coded as a public-service deployment unit."),
 ("BharatGen","Not included in this seed","Model/programme announcement alone was not converted into a named institution/service deployment."),
 ("Nigeria qXR clinical study","Excluded as Indian deployment validation","Different country and setting; cannot validate the BMC pilot."),
 ("Generic elephant-detection IoT prototype","Excluded as Railway IDS validation","Reviewed deployment identity was not established."),
 ("IndiaAI Impact Casebooks","Related resource","Sectoral India/global casebooks already exist; not proof of exclusive dataset novelty."),
 ("DCI Social Protection AI Hub Kisan e-Mitra entry","Related resource","Existing structured use-case documentation; independent primary-source coding here, not an exclusive discovery."),
 ("Digi Yatra RTI request","Context only","Questions requested are not an authority reply, supplier award or operational evidence."),
 ("NITI frontier-tech Qure.ai submission","Context only","Page explicitly disclaims endorsement/certification/validation; not an independent BMC evaluation."),
]:
    db["candidate_decisions"].append(dict(candidate_id=stable("candidate",name),name=name,decision=decision,reason=reason,system_id=None))

db["evidence"]=sorted(evidence_map.values(),key=lambda r:r["evidence_id"])
db["sources"]=sorted(source_map.values(),key=lambda r:r["source_id"])
for s in db["systems"]:
    records={(t,next(iter(r.values()))) for t,rows in db.items() for r in rows if r.get("system_id")==s["system_id"]}
    used={evidence_map[l["evidence_id"]]["source_id"] for l in db["evidence_links"] if (l["record_type"],l["record_id"]) in records}
    dates=[source_map[sid]["published_date"] for sid in used if source_map[sid]["published_date"]]
    s["latest_record_date"]=max(dates,default=None)
for sid,basis in {
 "reg-irctc-report-mirror":"Exchange filing date of historical 2020–21 report, not a current operating date",
 "reg-plcs":"Publisher/search date metadata; not visible in extracted body; historical case study",
}.items():
    source_map[sid]["date_basis"]=basis
OUT.mkdir(parents=True,exist_ok=True)
(OUT/"snapshots").mkdir(exist_ok=True)
(OUT/"dossiers").mkdir(exist_ok=True)
for s in db["sources"]:
    qs=list(dict.fromkeys(e["quote"] for e in db["evidence"] if e["source_id"]==s["source_id"]))
    # No whole documents: excerpt text only, unique passages shared across uses.
    text=f'{s["title"]}\nOriginal: {s["url"]}\nDocument date: {s["published_date"] or "Undated/uncertain"}\nSource type: {s["source_type"]}\nChecked: {CHECKED}\nSelected excerpts, not original document bytes or an independent audit.\n\n'+"\n\n".join(qs)+"\n"
    if s["source_id"].startswith("reg-"):assert sum(len(q.split()) for q in qs)<=250
    path=OUT/"snapshots"/(s["source_id"]+".txt");path.write_text(text)
    s.update(snapshot="snapshots/"+path.name,snapshot_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),hash_basis="Selected-excerpt UTF-8 snapshot; not original PDF")

# Deduplicate generic links; all concrete tables and their provenance have stable IDs.
db["evidence_links"]=list({r["link_id"]:r for r in db["evidence_links"]}.values())
for t,rows in db.items():rows.sort(key=lambda r:str(next(iter(r.values()))))
ids={t:{next(iter(r.values())) for r in rows} for t,rows in db.items()}
assert len(db["systems"])==18 and len(db["assertions"])==216
for row in db["evidence_links"]:
    assert row["record_id"] in ids[row["record_type"]]
    assert row["evidence_id"] in ids["evidence"]
for t in TABLES:
    for row in db[t]:
        if row.get("system_id"):assert row["system_id"] in ids["systems"]
        if row.get("source_id"):assert row["source_id"] in ids["sources"]
        for k in ("institution_id","owner_institution_id","supplier_institution_id"):
            if row.get(k):assert row[k] in ids["institutions"]
        if row.get("policy_id") and t!="policies":assert row["policy_id"] in ids["policies"]
        if row.get("target_system_id"):assert row["target_system_id"] in ids["systems"]

metadata=dict(title="AI Watch: India institution-and-system dataset",version="1.0.0",checked_date=CHECKED,scope="18 purposively selected named systems/services, historical and experimental cases included. Not a census, representative sample or operational/legal audit.",unit="System/service linked to institutions and observations",review="Single analyst; no independent duplicate coding or user-demand validation",counts={t:len(r) for t,r in db.items()},field_order=FIELDS)
data={"metadata":metadata,**db}
(OUT/"data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")

def csvcell(v):
    if isinstance(v,(dict,list)):v=json.dumps(v,ensure_ascii=False,sort_keys=True)
    if isinstance(v,str) and v.startswith(("=","+","-","@","\t","\r")):v="'"+v
    return v
for t,rows in db.items():
    cols=list(dict.fromkeys(k for row in rows for k in row))
    with (OUT/(t+".csv")).open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
        for row in rows:w.writerow({k:csvcell(row.get(k)) for k in cols})

sqlpath=OUT/"dataset.sqlite"
temporary=ROOT/"research/registry/.dataset-build.sqlite"
if temporary.exists():temporary.unlink()
conn=sqlite3.connect(temporary);conn.execute("PRAGMA foreign_keys=ON")
schemas={}
for t,rows in db.items():
    cols=list(dict.fromkeys(k for row in rows for k in row));schemas[t]=cols
    parts=[]
    for i,col in enumerate(cols):
        numeric=any(isinstance(r.get(col),(float,int)) for r in rows)
        ref=None
        if col=="system_id" and t!="systems":ref="systems(system_id)"
        if col=="source_id" and t!="sources":ref="sources(source_id)"
        if col=="evidence_id" and t!="evidence":ref="evidence(evidence_id)"
        if col in ("institution_id","owner_institution_id","supplier_institution_id") and t!="institutions":ref="institutions(institution_id)"
        if col=="policy_id" and t!="policies":ref="policies(policy_id)"
        if col=="target_system_id":ref="systems(system_id)"
        parts.append('"'+col+'" '+("REAL" if numeric else "TEXT")+(" PRIMARY KEY" if i==0 else "")+(" REFERENCES "+ref if ref else ""))
    conn.execute('CREATE TABLE "'+t+'" ('+",".join(parts)+")")
# Insert parent tables first, defer other foreign keys until transaction end.
conn.execute("PRAGMA defer_foreign_keys=ON")
for t,rows in db.items():
    cols=schemas[t]
    for row in rows:
        conn.execute('INSERT INTO "'+t+'" VALUES ('+",".join("?" for _ in cols)+")",[json.dumps(row.get(k)) if isinstance(row.get(k),(dict,list)) else row.get(k) for k in cols])
conn.commit()
assert not conn.execute("PRAGMA foreign_key_check").fetchall()
assert conn.execute("PRAGMA integrity_check").fetchone()[0]=="ok"
conn.close()
temporary.replace(sqlpath)
(OUT/"schema.json").write_text(json.dumps({"tables":schemas,"generic_link_rule":"evidence_links.record_type names a table; record_id matches its first-column primary key. Enforced by builder/tests; SQLite cannot express a polymorphic FK."},indent=2)+"\n")

def citations(table,rid):
    es=[e for l in db["evidence_links"] if l["record_type"]==table and l["record_id"]==rid for e in db["evidence"] if e["evidence_id"]==l["evidence_id"]]
    return "\n".join(f'> {e["quote"]}\n>\n> [{source_map[e["source_id"]]["title"]}]({source_map[e["source_id"]]["url"]}); {e["locator"]}.' for e in es)
for s in db["systems"]:
    sid=s["system_id"]
    text=f'# AI Watch: {s["name"]}\n\nIndia institution-and-system dataset v1.0.0. Checked {CHECKED}; analyst-coded documentary evidence, not an operational audit.\n\n'
    for a in db["assertions"]:
        if a["system_id"]!=sid:continue
        text+=f'## {a["field"]}\n\nEvidence status: {a["evidence_status"]}. {a["value"]}\n\n'+citations("assertions",a["assertion_id"])+"\n\n"
    for table in ["deployments","procurements","evaluations","metrics","controls","issues"]:
        rows=[r for r in db[table] if r["system_id"]==sid]
        if rows:text+=f"## {table.capitalize()}\n\n"
        for r in rows:
            rid=next(iter(r.values()))
            text+="\n".join(f"- **{k.replace('_',' ')}**: {v if v is not None else 'Unknown / not assigned'}" for k,v in r.items() if k not in ["system_id",next(iter(r))])+"\n\n"+citations(table,rid)+"\n\n"
    (OUT/"dossiers"/(sid+".md")).write_text(text)

# Derived statistics describe only this selected corpus and coding state.
analysis={"scope":metadata["scope"],"coverage_status":dict(Counter(a["evidence_status"] for a in db["assertions"])),"ai_qualification":dict(Counter(s["ai_class"] for s in db["systems"])),"metrics_by_kind":dict(Counter(m["metric_kind"] for m in db["metrics"])),"evaluation_types":[dict(system_id=e["system_id"],evaluation_type=e.get("evaluation_type"),current_version_match=e.get("current_version_match")) for e in db["evaluations"]]}
(OUT/"analysis.json").write_text(json.dumps(analysis,indent=2)+"\n")
for name in ["PROTOCOL.md","CODEBOOK.md","RESEARCH_NOTE.md","queries.sql","search-log.json","retrieval-log.json"]:
    src=ROOT/"research/registry"/name
    if src.exists():(OUT/name).write_bytes(src.read_bytes())

payloads=sorted(p for p in OUT.rglob("*") if p.is_file() and p.name not in ["complete-registry.zip","manifest.json","manifest.sha256"])
manifest={"title":metadata["title"],"version":metadata["version"],"counts":metadata["counts"],"files":[{"path":p.relative_to(OUT).as_posix(),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in payloads]}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
(OUT/"manifest.sha256").write_text(hashlib.sha256((OUT/"manifest.json").read_bytes()).hexdigest()+"  manifest.json\n")
with zipfile.ZipFile(OUT/"complete-registry.zip","w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(payloads+[OUT/"manifest.json",OUT/"manifest.sha256"]):
        zi=zipfile.ZipInfo(p.relative_to(OUT).as_posix(),date_time=(2026,10,5,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16
        z.writestr(zi,p.read_bytes())
print(json.dumps({"counts":metadata["counts"],"archive_sha256":hashlib.sha256((OUT/"complete-registry.zip").read_bytes()).hexdigest(),"analysis":analysis},indent=2))
