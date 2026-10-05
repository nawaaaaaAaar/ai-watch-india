"""Build six bounded public-service cases and all twelve accountability dimensions.

Snapshots are short selected excerpts, not full copyrighted page archives. They
reproduce the passages used here; full documents remain at their original URLs.
Unknowns describe this corpus, never absence of a policy or a remedy.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
CHECKED="5 October 2026"
sources=[]
texts={}
def norm(t):return re.sub(r"\s+"," ",t).strip()
def source(id,title,url,date,kind,quotes):
    path=ROOT/"public"/"snapshots"/f"{id}.txt"
    raw=norm(path.read_text())
    for q in quotes:assert q in raw,(id,q)
    assert sum(len(q.split()) for q in quotes)<=250,id
    selected=f"Selected excerpt snapshot, not a full document archive.\n{title}\nURL: {url}\nSource date: {date}; checked {CHECKED}.\n\n"+"\n\n".join(quotes)+"\n"
    path.write_text(selected)
    texts[id]=norm(selected)
    sources.append(dict(id=id,title=title,url=url,documentDate=date,publication=date,
        status=kind,instrument=title,sourceType=kind,snapshotKind="Selected excerpts",
        description="Selected source excerpts used by the case; open the original for the complete record. Not an independent audit.",
        checked=CHECKED,snapshot=f"snapshots/{id}.txt",hash=hashlib.sha256(path.read_bytes()).hexdigest(),
        hashType="SHA-256 of selected extracted UTF-8 excerpts, not original PDF bytes"))
    return quotes

UT="https://upsc.gov.in/sites/default/files/Tender-AadhaarQRFaceRecgAI-Corrgn_Eng-180724.pdf"
UL="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1"
UO="https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1"
CW="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2132817&reg=3&lang=1"
J="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2226283&reg=48&lang=2"
V="https://www.allahabadhighcourt.in/event/event_16290_18-09-2023.pdf"
D="https://cdnbbsr.s3waas.gov.in/s3ec0490f1f4972d133619a60c30f3559e/uploads/2026/06/2026060342.pdf"
HP="https://cdac.in/index.aspx?id=product_details&productId=eSanjeevaniNationalTelemedicineService"
HA="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps"
HV="https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf"
HE="https://nihrjodhpur.icmr.org.in/uploads/policybriefs/1782386587_1.PolicyBrief_Telemedicine.pdf"
HR="https://www.nhsrcindia.org/sites/default/files/2025-09/Telemedicine%20Final%20Report%202025.pdf"
PV="https://news.microsoft.com/source/asia/features/a-race-against-time-maharashtra-police-get-an-ai-copilot-to-fight-cybercrime/"
PS="https://www.microsoft.com/en-in/aifirstmovers/FY26CrimeOS"
PN="https://indianexpress.com/article/explained/mahacrimeos-ai-maharashtra-10418600/"

q={}
q["ut"]=source("service-upsc-tender","UPSC biometric/AI tender specification",UT,"18 July 2024 corrigendum filename; inspect instrument","Official tender",[
 "Tender responses are invited from PSUs for Aadhaar based Fingerprint Authentication/Digital Fingerprint Capturing & Facial Recognition of Candidates, QR Code Scanning of e-Admit Cards and Live AI-based CCTV Surveillance",
 "6.1.11 The Service Provider has to perform physical verification of candidates’ photos with Application Database (provided by UPSC) at the time of security gate entry.",
 "6.1.12 After the completion of the entire process as per the scope of work, the Service Provider will hold the data on its Secured Cloud Server with 256-bit encryption for a minimum period of one (01) year from the date of the examination or 30 days after the declaration of final result of the examination, whichever is later."])
q["ul"]=source("service-upsc-live","UPSC face authentication implementation",UL,"4 June 2026","Official self-report",[
 "UPSC conducted real-time face-authentication exercise across all 2,072 examination venues nationwide during this year’s Civil Services (Preliminary) examinations 2026.",
 "The face authentication application has been developed and implemented by UPSC with technical support from the National e-Governance Division (NeGD) of Ministry of Electronics and IT.",
 "It works on any Android smartphone, and invigilators used their own mobile phones for the purpose, thereby reducing hardware costs and easing the logistical burden.",
 "The time required for a typical face authentication of a candidate is only about 6–8 seconds, which ensured smooth entry and prevented queuing at examination centres."])
q["uo"]=source("service-upsc-october","UPSC centenary current-status explanation",UO,"4 October 2026","Official self-report",[
 "A significant technological initiative has been the introduction of AI-based facial authentication.",
 "Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates."])
q["cw"]=source("service-cyber-winners","CyberGuard hackathon results",CW,"30 May 2025 event; source date checked against release","Official announcement",[
 "The Hackathon resulted in the development of AI-based solutions to enhance the classification of cybercrime complaints and support the identification of emerging crime patterns, trends, and modus operandi on the National Cyber Crime Reporting Portal (NCRP).",
 "These models can interpret complex inputs such as handwritten FIRs, screenshots, and audio calls with improved speed and accuracy.",
 "Winners of IndiaAI I4C CyberGuard AI Hackathon Team Lead Names of the Team members Affiliated Organization Nisarg Gandhi Patel Darshankumar Shankarbhai and Bhensdadiya Kevin Vasantbhai S4AI Technologies LLP Lasya Ippagunta Shubham Luharuka and Puneet Hegde CloudSEK Information Security Limited Meet Bisht Rohit Ganaka and Yukta Chauhan Voldebug Innovations Pvt. Ltd."])
q["j"]=source("service-judiciary","Official judicial AI backgrounder",J,"11 February 2026","Official explanation",[
 "The **Supreme Court Portal for Assistance in Court Efficiency (SUPACE)** is an AI-based system **designed to help identify relevant precedents and understand the factual matrix of cases**. SUPACE remains in an experimental stage and is not yet deployed for regular judicial use.",
 "For this, **SUVAS** **(Supreme Court Vidhik Anuvaad Software)**, an AI-driven translation tool of the Supreme Court, converts English judgments and orders into vernacular languages, enhancing accessibility and regional language use in courts. These translated judgments are hosted on the **e-SCR portal**, significantly expanding public access.",
 "**Supreme Court and High Court AI Translation Committees** oversee quality and constitutional accuracy. AI use remains assistive, with translations reviewed within judicial frameworks to support access to justice."])
q["v"]=source("service-translation-vetting","Allahabad translation-vetting notice",V,"September 2023; deadline 22 September 2023","Court administrative notice",[
 "High Court of Judicature at Allahabad invites application from desirous Advocates practising at this High Court to create a panel of Vetters for vetting of software generated translation of its Reportable Judgments from English into Hindi.",
 "After due vetting & corrections, the said Vetters shall return the same, certifying the correctness of the translation.",
 "The remuneration for vetting & correction of the software generated translation of the judgments of this Court will be paid at the rate of Re. 1/- per word of the English version.",
 "A disclaimer shall be included in the footer of each page of the vetted judgment."])
q["d"]=source("service-court-draft","Court AI consultation draft",D,"3 June 2026","Consultation draft",[
 "Sub.: Seeking views/suggestions of all stakeholders and the general public on draft ‘Regulations for Use of Artificial Intelligence (AI) in Courts, 2026’.",
 "(2) Every AI System shall function solely in an assistive capacity and shall not supplant or compromise the independent exercise of judicial authority by a duly appointed judicial officer.",
 "(3) The ultimate authority to determine matters of law, fact and justice shall vest exclusively in the judicial officers of the competent jurisdiction."])
q["hp"]=source("service-health-platform","C-DAC eSanjeevani product description",HP,"Undated page; statistics labelled 16 August 2026","Official developer description",[
 "eSanjeevani is an indigenous, cloud-native telemedicine platform developed by C-DAC Mohali to address critical healthcare accessibility challenges, including the shortage and uneven distribution of healthcare professionals, limited access to specialist care in rural and remote areas, and gaps in continuity of care.",
 "AI-enabled Clinical Decision Support System (CDSS) to support clinical decision-making."])
q["ha"]=source("service-health-parliament","Lok Sabha telemedicine/CDSS response",HA,"7 August 2026","Parliamentary response",[
 "Further, the AI based Clinical Decision Support System (CDSS) available on this platform also enables a systematic capture of the diseases symptoms through a detailed patient assistance form, and identification of possible diseases.",
 "It also makes recommendation of a specialist doctor through a ‘rule engine’ and offers a differential diagnosis of possible diseases to the doctor at the hub end, thus facilitating connect of the patients with specialists as well as aiding consultations.",
 "Since its integration in April, 2023 till July, 2026, nearly 30.4 crore eSanjeevani consultations across all States/UTs have been benefited from standardized data capture and nearly 2.13 crore AI based differential diagnosis, ensuring consistency across health and wellness centres."])
q["hv"]=source("service-health-privacy","eSanjeevani privacy policy",HV,"Undated PDF; checked 5 October 2026","Published privacy policy",[
 "When the Community Health Officer registers patient on eSanjeevani, the following information besides the users' information is collected from the patient and stored on a server operated and managed by C-DAC Mohali – name, gender, age, address, mobile number, Email ID, health records, etc.",
 "All personal information collected from you under Clause 1(a) at the time of registration and later will be retained for as long as your account remains in existence and in sync with telemedicine practice guidelines issued by Niti Aayog/Board of Governors MCI and if any academic or medical or public health and administrative interventions have been commenced under Clause 2, for such period thereafter as is required.",
 "Nothing set out herein shall apply to medical reports, diagnoses or other medical information generated by medical professionals in the course of treatment.",
 "If you have any suggestions, concerns or queries in relation to this Privacy Policy, you may address them at esanjeevaniopd@cdac.in"])
q["he"]=source("service-health-local-study","ICMR local telemedicine research brief",HE,"2026 publication location; exact publication day not certified","Government research brief",[
 "An AI-driven Clinical Decision Support System (CDSS) achieved 90% validation accuracy, strengthening evidence-based prescribing in resource-constrained settings.",
 "the AI-driven Clinical Decision Support System (AI-CDSS), which has achieved 90% validation accuracy using 4,401 locally sourced patient records, should be integrated into the eSanjeevani platform"])
# This utilisation report is not treated as a CDSS accuracy study.
q["hr"]=source("service-health-report","NHSRC telemedicine utilisation study",HR,"2025 report","Government programme study",[
 "TELEMEDICINE / e-SANJEEVANI in the Public Health Facilities of India 2025",
 "Efforts should be made to address privacy concerns by implementing robust safeguards, ensuring inclusivity through initiatives by the Government to improve access to technology, and expanding the scope of telemedicine services to cater to a broader range of healthcare needs."])
q["pv"]=source("service-police-vendor","Microsoft MahaCrimeOS feature",PV,"12 December 2025","Vendor account",[
 "Since April, police there have been using MahaCrimeOS AI, a customized crime investigation platform powered by Microsoft Foundry that helps them process complaints faster and navigate complex data and procedures — all crucial functions for handling cybercrime.",
 "On Dec. 12, 2025, the government of Maharashtra and Microsoft announced that MahaCrimeOS AI will be extended from Nagpur’s 23 police stations to all 1,100 police stations across the state."])
q["ps"]=source("service-police-summary","Microsoft CrimeOS customer story",PS,"Undated page; checked 5 October 2026","Vendor account",[
 "MARVEL worked to adapt CrimeOS AI, developed by CyberEye - Microsoft AI Partner, to finetune it for compliance with state investigation protocols and further configure it in Marathi for easy adoption across the force.",
 "MahaCrimeOS AI ingests complaints in any format such as PDFs, audio, handwritten notes, or images, and then uses multimodal intelligence to extract critical information in any language.",
 "This was successfully deployed as a pilot across 25 police stations in Nagpur Rural, including the Cyber Crime Police Station (CCPS)."])
q["pn"]=source("service-police-reporting","Indian Express MahaCrimeOS reporting",PN,"14 December 2025","News reporting",[
 "On December 12, 2025, the Maharashtra government and Microsoft announced that the tool would be expanded from Nagpur’s 25 police stations to all 1,100 police stations across the state.",
 "This was successfully deployed as a pilot across 23 police stations in Nagpur Rural, including the cybercrime police stations (CCPS)."])

previous=json.loads((ROOT/"src"/"data"/"implementation.json").read_text())
old_sources={s["id"]:s for s in previous["sources"]}
for sid in ["impl-mission-status"]:
    texts[sid]=norm((ROOT/"public"/old_sources[sid]["snapshot"]).read_text())
sources_by_id={s["id"]:s for s in sources}|old_sources
def ev(sid,quote,locator):
    assert quote in texts[sid],(sid,quote)
    s=sources_by_id[sid]
    return dict(sourceId=sid,title=s["title"],url=s["url"],quote=quote,locator=locator)
def E(sid,key,i,locator):return ev(sid,q[key][i],locator)
DIMENSIONS=["Owner & purpose","Decision role & affected people","Deployment & date","Procurement & supplier",
 "Funding & contract","Data & integration","Evaluation & error rates","Human review & overrides",
 "Privacy & retention","Complaints & appeal","Public outputs & access","Current-status limits"]
def field(name,status,statement,*evidence):
    return dict(name=name,status=status,statement=statement,evidence=list(evidence))
def missing(name,explanation="n.a. Not verified in the reviewed corpus; request the relevant record."):
    return field(name,"Not verified",explanation)
cases=[]
def case(id,name,sector,stage,summary,interpretation,caution,fields,requests):
    assert [f["name"] for f in fields]==DIMENSIONS,id
    trail=[]
    for f in fields:
        for e in f["evidence"]:
            if not any(x["sourceId"]==e["sourceId"] and x["quote"]==e["quote"] for x in trail):trail.append(e)
    assert len(trail)>=2,id
    before,after=trail[0],trail[1]
    cases.append(dict(id=id,label=name,title=name+": decision-accountability case",familyId="service",
        type="Public-service case",actor=sector,sector=sector,deploymentStage=stage,
        comparisonKind="System claim to accountability evidence",legalStatus=stage,
        publicServiceCase=True,caseFields=fields,checked=CHECKED,
        summary=summary,interpretation=interpretation,caution=caution,
        question="Which decision can this system influence, what evidence supports its use, and how can a person obtain human review?",
        draftLabel=before["locator"],draftLocator=before["locator"],finalLocator=after["locator"],
        draftUrl=before["url"],finalUrl=after["url"],beforeSourceId=before["sourceId"],afterSourceId=after["sourceId"],
        beforeLabel="SYSTEM RECORD",afterLabel="SUPPORTING RECORD",
        draftText=before["quote"],finalText=after["quote"],correctedText=after["quote"],
        beforeExcerpt=before["quote"],afterExcerpt=after["quote"],draftPage=0,finalPage=0,
        evidenceTrail=trail,requestChecklist=requests,correctionIds=[],contribution=True,featured=False,
        evidenceScope="Twelve accountability dimensions, all retained even when unverified. A case file, not a word-aligned legal redline.",
        reviewStatus="Analyst-reviewed source corpus; not a system audit, patient advice or current legal-procedure certification."))

u1=E("service-upsc-live","ul",1,"4 June release, implementation and developer")
u2=E("service-upsc-october","uo",1,"4 October release, examination reform")
u3=E("service-upsc-tender","ut",0,"2024 tender, cover/scope")
u4=E("service-upsc-live","ul",2,"4 June release, mobile workflow")
u5=E("service-upsc-live","ul",3,"4 June release, reported timing")
u6=E("service-upsc-tender","ut",1,"2024 tender clause 6.1.11")
u7=E("service-upsc-tender","ut",2,"2024 tender clause 6.1.12")
case("service-upsc","UPSC face authentication","Public examinations","Official deployment reported",
 "UPSC reports nationwide mobile face authentication in May 2026; the current application is described as developed with NeGD support.",
 "Identity verification can affect entry to an examination. Throughput, coverage and an older tender are not a measured false-rejection rate or proof that a rejected candidate has a documented fallback route.",
 "Do not equate the 2024 biometric/CCTV procurement package with the 2026 in-house mobile application. Tender requirements are not current deployed behaviour. No candidate case or device inspection was undertaken.",
 [field(DIMENSIONS[0],"Documented","UPSC with technical support from NeGD; exam identity authentication.",u1),
  field(DIMENSIONS[1],"Partial","Mobile identity matching concerns examination candidates; detailed adverse-decision rules are not verified.",u2,u4),
  field(DIMENSIONS[2],"Documented","A September 2025 pilot and scaled use on 24 May 2026 are officially reported, with about 5.50 lakh candidates.",u2),
  field(DIMENSIONS[3],"Partial","A 2024 PSU tender covered biometrics, facial recognition, QR scans and AI CCTV; the June record describes in-house development. The contract link between them is unverified.",u3,u1),
  missing(DIMENSIONS[4],"n.a. Awarded supplier, current application budget and contract value were not verified; the tender alone is not an award."),
  field(DIMENSIONS[5],"Partial","Invigilators' Android phones were used. The current data-flow diagram and device/data lifecycle were not verified.",u4),
  field(DIMENSIONS[6],"Partial","UPSC reports six-to-eight-second typical authentication; no independent false-accept/reject or subgroup evaluation was verified.",u5),
  field(DIMENSIONS[7],"Partial","The older tender requires physical photo verification. The current mismatch/technical-failure SOP was not verified.",u6),
  field(DIMENSIONS[8],"Partial","The older tender specifies encrypted cloud holding for at least one year or 30 days after final results, whichever is later. Applying it to the current mobile system is not established.",u7),
  missing(DIMENSIONS[9],"n.a. A system-specific candidate mismatch appeal, deadline and non-biometric fallback were not verified."),
  field(DIMENSIONS[10],"Partial","UPSC publishes implementation descriptions; the actual current failure-handling SOP, audit and test report were not obtained.",u1,u2),
  field(DIMENSIONS[11],"Partial","The October source confirms reported scaled use, not independently audited accuracy or every current operational detail.",u2)],
 ["Current face-authentication SOP, including mismatch and offline fallback","Contract/award lineage distinguishing biometric CCTV tender from mobile app",
  "False-rejection/acceptance and subgroup test results","Data-flow, device deletion and retention policy","Candidate review route and anonymised error-resolution records"])

c1=E("service-cyber-winners","cw",0,"Hackathon explanation")
c2=ev("impl-mission-status","The shortlisted solution has been integrated with I4C systems.","29 July release, CyberGuard paragraph")
c3=E("service-cyber-winners","cw",2,"Annexure I, winner table")
c4=E("service-cyber-winners","cw",1,"Hackathon explanation, supported inputs")
case("service-cyberguard","I4C CyberGuard","Cybercrime administration","Official integration reported",
 "Government reporting says the shortlisted classifier was integrated with I4C systems; the hackathon results identify teams but do not identify an executed production contract.",
 "Complaint classification may influence routing and prioritisation, but the records do not establish that a model decides FIR registration or rejects a complaint. Research metrics from a different hackathon entry cannot be transferred to the production system.",
 "Winner selection is not proof of the deployed supplier or a service contract. Integration does not establish measured operational accuracy, complaint outcomes, or automatic adverse decisions.",
 [field(DIMENSIONS[0],"Documented","IndiaAI and I4C developed a challenge around NCRP complaint classification and crime-pattern identification.",c1),
  field(DIMENSIONS[1],"Partial","The task is complaint classification/pattern support; effects on registration, prioritisation and investigations are not specified in the reviewed record.",c1),
  field(DIMENSIONS[2],"Documented","The 29 July official record reports integration with I4C systems.",c2),
  field(DIMENSIONS[3],"Partial","The results list winning organisations. Which finalist supplied the integrated production system and on what contract is not verified.",c3),
  missing(DIMENSIONS[4],"n.a. Production award, fees, ongoing support terms and project-specific expenditure were not verified."),
  field(DIMENSIONS[5],"Partial","The challenge description mentions handwritten FIRs, screenshots and audio calls. The production ingestion schema and access controls were not verified.",c4),
  field(DIMENSIONS[6],"Not verified","n.a. 'Improved speed and accuracy' is an official qualitative claim, not a production benchmark with error distributions.",c4),
  missing(DIMENSIONS[7],"n.a. Human correction, routing overrides and audit-log procedures were not verified."),
  missing(DIMENSIONS[8],"n.a. System-specific retention, training reuse, processors and minimisation rules were not verified."),
  missing(DIMENSIONS[9],"n.a. A classifier-specific correction/appeal route was not verified; ordinary cybercrime reporting is not proof of an AI-error appeal."),
  field(DIMENSIONS[10],"Partial","The winner table and integration statement are public; no production model card or evaluation report was verified.",c3,c2),
  field(DIMENSIONS[11],"Partial","Official integration is documented as a source claim; live access, coverage and decision impact were not independently tested.",c2)],
 ["Production supplier and acceptance/award documents","Classification taxonomy and human routing/override SOP",
  "Production evaluation across Indian languages and error severity","Retention, access and training-use rules","Mechanism to correct a misclassified complaint"])

j1=E("service-judiciary","j",1,"Judgment translation section")
j2=E("service-judiciary","j",2,"Translation committee oversight")
v1=E("service-translation-vetting","v",0,"Allahabad notice, opening")
v2=E("service-translation-vetting","v",1,"Allahabad notice, condition 2")
v3=E("service-translation-vetting","v",2,"Allahabad notice, remuneration")
v4=E("service-translation-vetting","v",3,"Allahabad notice, condition 4")
case("service-suvas","SUVAS judicial translation","Judicial access","Official use reported",
 "The official backgrounder describes translations hosted on e-SCR and judicial translation committees; a separate Allahabad notice documents a local vetting workflow.",
 "A translation aids access to a judgment but is not an automated judicial determination. The local vetting record shows concrete human review, without establishing one nationwide SOP or a current universal correction route.",
 "The 2023 Allahabad process is jurisdiction-specific and historical. Do not infer that its remuneration, panel or disclaimer governs every court or every current SUVAS output.",
 [field(DIMENSIONS[0],"Documented","Supreme Court SUVAS translates judgments and orders to vernacular languages.",j1),
  field(DIMENSIONS[1],"Documented","Translation supports people reading court records; it is not itself a decision on the merits of a case.",j1,j2),
  field(DIMENSIONS[2],"Documented","The February official explanation reports use and hosting on e-SCR; current court-by-court coverage is not certified.",j1),
  missing(DIMENSIONS[3],"n.a. Software/model contract, procurement award and current supplier chain were not verified."),
  field(DIMENSIONS[4],"Partial","The historical Allahabad notice quotes Re. 1 per English-source word for vetting; this is not a national software budget.",v3),
  field(DIMENSIONS[5],"Partial","English judgments/orders are translated; model training, confidential-case exclusions and processor access were not verified.",j1),
  missing(DIMENSIONS[6],"n.a. Independent legal-semantic error rates by language, case type and model version were not verified."),
  field(DIMENSIONS[7],"Documented","Translation committees are described, and the Allahabad notice requires vetting/correction and certification. Coverage of that process is local, not universal.",j2,v2),
  missing(DIMENSIONS[8],"n.a. Tool-specific retention, confidential-document handling and training-data reuse rules were not verified."),
  field(DIMENSIONS[9],"Partial","The notice requires a disclaimer but does not establish a national translation-error appeal route.",v4),
  field(DIMENSIONS[10],"Documented","The official explanation reports translated judgments on e-SCR; the local notice exposes a review mechanism.",j1,v1),
  field(DIMENSIONS[11],"Partial","The reviewed records support assistive translation use, not perfect equivalence or current uniform governance across courts.",j2)],
 ["Current court-specific translation SOP and disclaimer","Error correction route and turnaround",
  "Language-specific validation and approved-version logs","Vendor/model/procurement and data-processing records",
  "Handling of sealed, sensitive or personal data"])

s1=E("service-judiciary","j",0,"SUPACE research-assistance section")
d1=E("service-court-draft","d",0,"3 June consultation notice")
d2=E("service-court-draft","d",1,"Draft human-primacy provision")
case("service-supace","SUPACE research assistance","Judicial administration","Experimental in reviewed official record",
 "The February official explanation explicitly calls SUPACE experimental and not yet used regularly; later general commentary is not a deployment certificate.",
 "This is a deliberately included counterexample to a deployed-only directory. It helps a journalist distinguish a designed capability from a routinely operating decision system.",
 "The June court-AI instrument is a consultation draft in this corpus, not verified enacted regulation. The February deployment description does not establish October status; no court-registry confirmation was requested.",
 [field(DIMENSIONS[0],"Documented","Supreme Court research-assistance system for identifying precedents and case facts.",s1),
  field(DIMENSIONS[1],"Partial","The stated role is assistance with relevant material, not autonomous adjudication; operational influence on actual cases is unverified.",s1),
  field(DIMENSIONS[2],"Documented","The February official source describes experimental status and no regular judicial use, rather than completed deployment.",s1),
  missing(DIMENSIONS[3],"n.a. Current supplier, procurement award, GPU/infrastructure contract and production acceptance were not verified."),
  missing(DIMENSIONS[4],"n.a. SUPACE-specific budget and expenditure were not verified; an eCourts-wide allocation is not a system budget."),
  field(DIMENSIONS[5],"Partial","The source describes precedent and factual-matrix assistance; actual ingestion, training and access-control configuration are unverified.",s1),
  missing(DIMENSIONS[6],"n.a. Current independent citation, omission and hallucination tests or courtroom outcome evaluations were not verified."),
  field(DIMENSIONS[7],"Partial","The June draft proposes assistive operation and human primacy; this proposal is not proof of an enacted or implemented operational SOP.",d2),
  missing(DIMENSIONS[8],"n.a. System-specific confidential-case handling, data retention and model-provider terms were not verified."),
  missing(DIMENSIONS[9],"n.a. A system-output correction/objection route was not verified; ordinary judicial remedies are not analysed here."),
  field(DIMENSIONS[10],"Partial","Official descriptions and a draft governance instrument are public; no current public operational/test record was verified.",s1,d1),
  field(DIMENSIONS[11],"Not verified","n.a. A later final regulation or routine SUPACE deployment was not verified after recency searches. This is not proof that neither exists.",d1,s1)],
 ["Current deployment confirmation and pilot-to-production decision","System-specific model/citation evaluation",
  "Current applicable final instrument, if adopted","Confidentiality, provider terms and logs",
  "Human verification and party objection procedure"])

h1=E("service-health-platform","hp",0,"Product brief")
h2=E("service-health-parliament","ha",0,"Parliamentary CDSS explanation")
h3=E("service-health-parliament","ha",1,"Rule engine and hub-doctor workflow")
h4=E("service-health-parliament","ha",2,"April 2023 integration and July 2026 usage")
h5=E("service-health-privacy","hv",0,"Privacy policy clause 1(a)")
h6=E("service-health-privacy","hv",1,"Privacy policy clause 3(a)")
h7=E("service-health-privacy","hv",2,"Privacy policy clause 3(b)")
h8=E("service-health-privacy","hv",3,"Privacy policy clause 10")
h9=E("service-health-local-study","he",1,"Local study recommendation, integration proposal")
h10=E("service-health-report","hr",1,"Programme utilisation study, concluding recommendations")
case("service-esanjeevani","eSanjeevani clinical support","Public healthcare","Official integration reported",
 "Government reporting describes an AI-labelled CDSS integrated in April 2023, with specialist recommendations through a rule engine and differential diagnoses supplied to a doctor.",
 "This is clinician support, not evidence of an autonomous diagnosis. Consultation counts are not safety or diagnostic-accuracy results, and a local CDSS study proposing later integration cannot validate the existing national component.",
 "Not clinical advice. The records do not establish every CDSS component is machine learning. The privacy policy is undated, and its medical-output carve-out must not be omitted when quoting retention.",
 [field(DIMENSIONS[0],"Documented","C-DAC Mohali developed the national platform; the parliamentary record describes CDSS functionality.",h1,h2),
  field(DIMENSIONS[1],"Documented","Possible diseases and specialist referral support are presented to a doctor at the hub end, affecting patient consultations.",h2,h3),
  field(DIMENSIONS[2],"Documented","The response dates integration to April 2023 and reports usage through July 2026.",h4),
  field(DIMENSIONS[3],"Partial","The platform developer is identified, but CDSS component suppliers, model provenance and procurement awards were not verified.",h1),
  missing(DIMENSIONS[4],"n.a. CDSS-specific contract, budget, licensing and maintenance expenditure were not verified."),
  field(DIMENSIONS[5],"Documented","Patient assistance forms collect symptoms; the privacy policy lists identifying and health records stored on a C-DAC-managed server.",h2,h5),
  field(DIMENSIONS[6],"Not verified","n.a. National deployed-CDSS accuracy was not verified. A separate local 4,401-record study recommends integration into eSanjeevani; its 90% figure is not the existing national system's score.",h9),
  field(DIMENSIONS[7],"Partial","Differential diagnosis is supplied to the hub doctor. Mandatory override, escalation and safety-monitoring procedures were not verified.",h3),
  field(DIMENSIONS[8],"Partial","The policy ties some data retention to account existence and further interventions, but excludes medical reports/diagnoses generated in treatment from that clause; no single universal retention period follows.",h6,h7),
  field(DIMENSIONS[9],"Partial","The privacy policy provides a contact for privacy concerns; a CDSS clinical-error review/remedy procedure was not verified.",h8),
  field(DIMENSIONS[10],"Partial","Developer, parliamentary and privacy records are public; no national CDSS model card or clinical validation dossier was verified.",h1,h4,h8),
  field(DIMENSIONS[11],"Partial","The dated response supports reported integrated use, not independent safety certification or all October operational details. The programme utilisation study raises privacy and access recommendations, but is not a deployed-CDSS accuracy study.",h4,h10)],
 ["Deployed CDSS version, component suppliers and intended use","Clinical validation, exclusions and subgroup safety evaluation",
  "Doctor override/escalation and adverse-event SOP","Applicable retention rules including treatment-generated records",
  "Patient complaint, clinical review and remedy procedures"])

m1=E("service-police-vendor","pv",0,"Vendor account, reported pilot use")
m2=E("service-police-vendor","pv",1,"Vendor account, expansion announcement")
m3=E("service-police-summary","ps",0,"Customer story, supplier and adaptation")
m4=E("service-police-summary","ps",1,"Customer story, inputs")
m5=E("service-police-summary","ps",2,"Customer story, pilot count")
m6=E("service-police-reporting","pn",1,"News report, pilot count")
case("service-mahacrimeos","MahaCrimeOS investigation support","State policing","Vendor/reporting-supported pilot; scale unverified",
 "Vendor accounts and reporting describe a Nagpur pilot and announced statewide expansion, with inconsistent 23/25-station counts in the reviewed material.",
 "Investigation support can shape what an officer sees and pursues, but claims of speed or statewide scale need operational records. A company story and a repeating news report are not independent performance audits.",
 "The reviewed corpus did not establish a government procurement award, station-wise completed rollout, performance audit or tool-specific redress procedure. Count differences may reflect dates/denominators; do not choose a convenient number.",
 [field(DIMENSIONS[0],"Partial","Vendor material describes MARVEL adapting CyberEye's CrimeOS with Microsoft technology; the government-authorisation instrument was not verified.",m3),
  field(DIMENSIONS[1],"Partial","The reported purpose is complaint processing and investigation assistance; legal consequences and decision boundaries were not verified.",m1),
  field(DIMENSIONS[2],"Conflicting sources","Sources describe 23 and 25 pilot stations and an announcement to extend to 1,100; a completed station-wise rollout was not verified.",m2,m5,m6),
  field(DIMENSIONS[3],"Partial","CyberEye/Microsoft/MARVEL are named in vendor material. A named supplier is not a procurement award or proof of the current contract.",m3),
  missing(DIMENSIONS[4],"n.a. Government contract, licence cost, funding, renewal and procurement evaluation were not verified."),
  field(DIMENSIONS[5],"Partial","Vendor description lists PDFs, audio, handwritten notes and images as inputs, with Marathi adaptation; actual production data flows are not independently verified.",m3,m4),
  missing(DIMENSIONS[6],"n.a. Independent error, bias, accuracy and workload evaluations were not verified; vendor anecdotes are not benchmarks."),
  missing(DIMENSIONS[7],"n.a. An enforceable officer verification/override SOP and audit trail were not verified."),
  missing(DIMENSIONS[8],"n.a. Tool-specific processor, hosting, model-training use, access, retention and deletion terms were not verified."),
  missing(DIMENSIONS[9],"n.a. Tool-specific correction, access or complaint mechanisms were not verified; ordinary policing remedies are outside this case's verified scope."),
  field(DIMENSIONS[10],"Partial","Public vendor descriptions and reporting exist. Authoritative station-wise deployment, procurement and audit artefacts were not verified.",m1,m3,m6),
  field(DIMENSIONS[11],"Not verified","n.a. A current government-confirmed rollout inventory and operational audit were not obtained. This is not proof of non-use.",m2,m5)],
 ["Government authorisation, procurement and executed contract","Station-wise rollout with dates and active use",
  "Officer verification, override and audit-log SOP","Independent error/bias/workload evaluations",
  "Data-processing, hosting, retention and model-training terms","Subject/victim correction and grievance procedure"])

assert len(cases)==6 and len(sources)==15
family=dict(id="service",title="Public-service AI decision accountability",shortTitle="Public-service cases",
 status="Deployment evidence varies",
 description="Six case files and twelve accountability dimensions per case: procurement, evaluation, human review, privacy and redress.",
 coverage="Six complete bounded case files with all 72 dimension slots retained, including explicit unverified fields.",
 scope="Not a census of Indian AI systems. Official self-reports, experimental descriptions, vendor accounts and unknowns are distinguished.",
 count=6,contributionCount=6,defaultId="service-upsc",
 timeline=[dict(date="2023–2025",title="Programme and procurement lineage",detail="Historical terms are not automatically current implementation"),
  dict(date="2026",title="Dated deployment and policy records",detail="Experimental and live-use claims remain distinct"),
  dict(date="05 Oct 2026",title="Six-case review",detail="Every dimension answered or explicitly marked unverified")])
out=dict(families=[family],provisions=cases,sources=sources,corrections=[],dimensions=DIMENSIONS)
for target in [ROOT/"src"/"data"/"public-services.json",ROOT/"public"/"public-services-data.json"]:
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(ROOT/"src"/"data"/"public-services.json")
print("Built six cases, 72 accountability dimension slots, six briefs and fifteen selected source snapshots.")
