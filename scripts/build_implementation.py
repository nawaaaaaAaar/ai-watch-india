"""Reproduce ten implementation checkpoints, without treating proposals as outcomes.

Exact extracted quotes and immutable snapshots are separate from editorial status.
Negative findings describe this reviewed corpus, not the whole public record.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
CHECKED="5 October 2026"
sources=[]
texts={}
def source(id,title,url,date,status,description):
    path=ROOT/"public"/"snapshots"/f"{id}.txt"
    texts[id]=re.sub(r"\s+"," ",path.read_text()).strip()
    sources.append(dict(id=id,title=title,url=url,documentDate=date,publication=date,
        instrument=title,status=status,description=description,checked=CHECKED,
        snapshot=f"snapshots/{id}.txt",hash=hashlib.sha256(path.read_bytes()).hexdigest(),
        hashType="SHA-256 of extracted UTF-8 text, not original PDF bytes"))

source("impl-aigeg-order","AIGEG constitution memorandum",
 "https://www.meity.gov.in/static/uploads/2026/04/43a4ec455c26b0f061cc7cca98770a45.pdf",
 "13 April 2026","Constitution order","Office memorandum: composition and terms of reference; OCR anomalies are preserved.")
source("impl-tpec-order","TPEC constitution memorandum",
 "https://d12aarmt01l54a.cloudfront.net/cms/files/constitution-of-tpec/1776447206.pdf",
 "13 April 2026","Constitution order","Official PIB-linked memorandum. Local pdftotext fallback after SDK robots failure; OCR spelling is not silently repaired.")
source("impl-aigeg-release","AIGEG constitution announcement",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2252739&reg=1&lang=1",
 "16 April 2026","Official announcement","Confirms constitutional action and names the chair and vice-chair; not evidence of meeting outcomes.")
source("impl-tpec-release","TPEC constitution announcement",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2253322&reg=1&lang=1",
 "18 April 2026","Official announcement","Describes the advisory relationship; differs from the order's 13 April date.")
source("impl-partners","IndiaAI Safety Institute partner EOI",
 "https://indiaai.s3.ap-south-1.amazonaws.com/docs/sg-call-for-partnerships-indiaai-safety-institute.pdf",
 "Published 9 May 2025; deadline 9 June 2025","Partnership call","Call, staffing/funding requirements and output-publication rules; not a partner award list.")
source("impl-director","Safety Institute director recruitment",
 "https://dic.gov.in/jobs/director-indiaai-safety-institute/",
 "Application deadline 2 June 2026; posting date not certified","Recruitment notice","One contractual position advertised. Historical recruitment, not proof of an appointment or a vacancy today.")
source("impl-safety-status","Safe & Trusted AI parliamentary explanation",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2289946&reg=3&lang=1",
 "27 July 2026","Official self-report","Reports 13 approved projects and describes the Safety Institute as established; does not independently audit results.")
source("impl-mission-status","IndiaAI Mission governance progress explanation",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2291062&reg=48&lang=1",
 "29 July 2026","Official self-report","Describes institutions as initiated and the Safety Institute as being established; preserve the wording conflict.")
source("impl-projects","Second Safe & Trusted AI EOI selections",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175698",
 "7 October 2025","Project selection announcement","Five named projects and selected applicants. Text snapshot extracted from the equivalent PIB mobile release; not evaluation results.")
source("impl-commitments","AI Impact Summit deliverables",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2234343&reg=3&lang=1",
 "2 March 2026","Official self-report","Reports frontier developer commitments and other voluntary summit initiatives; not compliance evidence.")
source("impl-redress","Deepfake safeguards and grievance explanation",
 "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2291671&reg=3&lang=1",
 "30 July 2026","Official explanation","Describes intermediary grievance officers and GAC appeals; not universal redress for all AI harms.")
source("impl-cert-directions","CERT-In cyber incident directions",
 "https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf",
 "28 April 2022","Directions","Existing cyber incident duties, including listed AI/ML-related attacks; distinct from a national AI-harm repository.")

prior=json.loads((ROOT/"src"/"data"/"expansion.json").read_text())
guidelines=next(s for s in prior["sources"] if s["id"]=="aig-guidelines")
texts["aig-guidelines"]=re.sub(r"\s+"," ",(ROOT/"public"/guidelines["snapshot"]).read_text()).strip()
source_by_id={s["id"]:s for s in sources}
source_by_id["aig-guidelines"]=guidelines

def evidence(id,start,end=None,locator="Document wording"):
    text=texts[id]
    if end:
        i=text.index(start)
        q=text[i:text.index(end,i+len(start))].strip()
    else:
        assert start in text,(id,start)
        q=start
    return dict(sourceId=id,url=source_by_id[id]["url"],title=source_by_id[id]["title"],
        locator=locator,quote=q)

records=[]
def record(id,label,title,parent,status,summary,interpretation,question,caution,trail,request):
    p=next(p for p in prior["provisions"] if p["id"]==parent)
    before=p["afterExcerpt"]
    relevant_recommendations={
      "impl-aigeg":("The Committee recommends the creation of an AI Governance Group (AIGG) to develop and oversee India’s position and strategy on AI governance.","Part 2.6; printed p. 34"),
      "impl-tpec":("The TPEC’s primary goal is to provide expertise to the AI Governance Group (AIGG) and enable it to perform its functions effectively.","Part 2.6; printed p. 35"),
      "impl-aisi-status":("The recently established AI Safety Institute (AISI) should act as the main body responsible for guiding the safe and trusted development and use of AI in India.","Part 2.6; printed p. 36"),
      "impl-aisi-leadership":("The AISI should be involved in research, risk assessment, and capacity-building. It should test and evaluate AI systems for risks and provide advice to policymakers and industry actors on issues of AI safety.","Part 2.6; printed p. 36"),
      "impl-aisi-partners":("The AISI can operate on a hub-and-spoke model and should be supported by a dedicated secretariat for research, drafting, and capacity building.","Part 2.6; printed p. 36"),
      "impl-projects":("Further, the ongoing work under the IndiaAI mission to support the development of technical solutions to address issues relating to machine unlearning, bias mitigation, privacy-enhancing tools, explainable AI, etc. should also continue.","Part 2.6; printed p. 36"),
      "impl-tool-delivery":("Promote the adoption of AI safety tools in areas such bias mitigation, fairness testing, and explainability, through platforms, APIs and open access tools.","Part 2.6; printed p. 36"),
      "impl-incident-repository":("The database should be a national-level centralised system that has the ability to query and collect data from smaller, local databases in a federated manner.","Part 2.4; printed pp. 26–27"),
      "impl-redress":("The Committee recommends that organisations deploying AI systems should establish accessible and effective grievance redressal mechanisms as part of their accountability obligations.","Part 2.5; printed p. 32")
    }
    locator=p["finalLocator"]
    if id in relevant_recommendations:
        before,locator=relevant_recommendations[id]
    assert before in texts["aig-guidelines"],id
    primary=trail[0]
    records.append(dict(id=id,label=label,title=title,familyId="impl",
        comparisonKind="Recommendation to implementation evidence",
        legalStatus=status,evidenceStatus=status,implementationCheckpoint=True,
        type="Evidence checkpoint",actor="IndiaAI, MeitY and oversight bodies",
        draftLabel=locator,draftUrl=p["finalUrl"],finalUrl=primary["url"],
        draftLocator=locator,finalLocator=primary["locator"],
        beforeSourceId="aig-guidelines",afterSourceId=primary["sourceId"],
        beforeLabel="POLICY RECOMMENDATION",afterLabel="REVIEWED IMPLEMENTATION RECORD",
        draftText=before,finalText=primary["quote"],correctedText=primary["quote"],
        beforeExcerpt=before,afterExcerpt=primary["quote"],draftPage=0,finalPage=0,
        summary=summary,interpretation=interpretation,question=question,caution=caution,
        evidenceTrail=trail,requestChecklist=request,relatedId=parent,
        evidenceScope="An implementation checkpoint, not a textual redline or operational audit. Read the whole evidence trail.",
        reviewStatus="Analyst-reviewed extracted official records; no agency confirmation requested.",
        correctionIds=[],contribution=True,featured=False,checked=CHECKED))

record("impl-aigeg","AIGEG","A constitution order exists; policy delivery needs separate evidence",
 "aig-institutions","Formal constitution documented",
 "A 13 April memorandum constitutes AIGEG; the public announcement follows on 16 April.",
 "The recommendation has a formal institutional response, with a ten-seat composition and terms of reference. Constitution is not evidence that the group has met, issued decisions or delivered its labour-transition roadmap.",
 "What agendas, minutes, guidelines and deploy/pilot/defer decisions has AIGEG issued?",
 "The reviewed order and announcement do not establish meeting activity or outcomes. OCR errors are visible in the order snapshot; use the original for quoting names and exact wording.",
 [evidence("impl-aigeg-order","Subject: - Constitution","(i).",locator="Office memorandum, p. 1"),
  evidence("impl-aigeg-release","The constitution of the AIGEG gives formal effect to institutional recommendations made in India’s AI Governance Guidelines and the Economic Survey.",locator="Constitution announcement, opening paragraphs"),
  evidence("impl-aigeg-order","Terms of Reference of AIGEG","S.No.",locator="Office memorandum, terms of reference")],
 ["Constitution order and subsequent revisions","Meeting dates, agendas and releasable minutes","Issued decisions and implementation roadmap","Secretariat staffing and allocated expenditure"])
record("impl-tpec","TPEC","The expert committee has an order and an advisory remit",
 "aig-institutions","Formal constitution documented",
 "The TPEC memorandum is dated 13 April; its public announcement is dated 18 April.",
 "The six-seat composition combines the MeitY secretary, two academic seats and representatives of NASSCOM, DSCI and MAIT. An advisory remit is not a statutory licence to approve or ban every AI system.",
 "What risk assessments or recommendations has TPEC delivered, and how are expertise and conflicts managed?",
 "This verifies the order, not completion of work, attendance or the currently serving individuals. No inference about legitimacy follows solely from the composition. OCR text needs checking against the PDF.",
 [evidence("impl-tpec-order","Subject: - Constitution","(i).",locator="Office memorandum, p. 1"),
  evidence("impl-tpec-order","S.No","Terms of Reference of TPEC",locator="Office memorandum, composition table, p. 1"),
  evidence("impl-tpec-release","As an advisory body for the AIGEG, it will provide the Group with expert inputs necessary to make well-informed decisions on policy design, regulatory measures and India’s engagements in AI governance across international forums.",locator="Announcement, advisory-remit paragraph")],
 ["Current membership and substitutions","Conflict-of-interest and disclosure arrangements","Delivered assessments and recommendations","Record of AIGEG action on those recommendations"])
record("impl-aisi-status","AISI status","Official Safety Institute wording does not settle operational readiness",
 "aig-institutions","Official wording unresolved",
 "The 27 July record says the institute has been established; the 29 July record says it is being established.",
 "An institutional creation claim is documented, but these adjacent statements do not establish the institute's staffing, budget, testing capacity or live public services. Preserve both descriptions rather than choose the more convenient one.",
 "What precise milestones distinguish announcement, constitution, staffing and operational launch?",
 "The statements may describe different stages rather than a factual contradiction. This ledger does not declare the institute nonexistent or fully operational.",
 [evidence("impl-safety-status","The AI Safety Institute has been established","• The India AI Governance",locator="27 July release, Safe & Trusted AI section"),
  evidence("impl-mission-status","An **IndiaAI Safety Institute** is being established as a hub for indigenous research and development on AI safety, to support India’s technical and institutional infrastructure for AI governance.",locator="29 July release, institutional progress section")],
 ["Instrument defining legal/administrative location and remit","Operational launch milestones and dates","Staff, testing capacity and budget","Published evaluation programme and reports"])
record("impl-aisi-leadership","AISI leadership","A director advertisement is not an appointment record",
 "aig-institutions","Process documented; outcome unverified",
 "DIC advertises one contractual director position with a 2 June 2026 application deadline.",
 "Recruitment is concrete administrative action, but the historical advertisement cannot show whether a director was appointed, when they joined or whether the position is vacant now.",
 "Was the recruitment completed, and what authority and resources were delegated to the appointee?",
 "A past deadline is not an open job listing. The appointment outcome was not verified in the reviewed corpus.",
 [evidence("impl-director","India AI is currently inviting applications","**Roles and Responsibilities",locator="Recruitment notice, position and deadline table"),
  evidence("impl-director","Provide overall strategic direction, leadership and oversight for the IndiaAI Safety Institute, including finalisation of its scope of work.",locator="Recruitment notice, roles and responsibilities")],
 ["Appointment outcome and joining date","Term and delegated responsibilities","Approved organisational structure and staff positions","Institute programme of work"])
record("impl-aisi-partners","AISI partners","The partner call specifies cells and cost sharing, not awarded partners",
 "aig-institutions","Process documented; outcome unverified",
 "The partner EOI sets 9 May/9 June 2025 publication and submission dates, dedicated Safety Cells and a 50% partner cost contribution.",
 "The hub-and-spoke architecture has a concrete application process. A call and requirements are not evidence that partners were selected, agreements executed or funds spent.",
 "Which partner cells were contracted, funded and assigned work, and what outputs became public?",
 "Do not treat an expired EOI as an open application window or its funding rules as disbursement evidence. Confidential-output exceptions also limit what can legitimately be inferred from missing public reports.",
 [evidence("impl-partners","Date of EoI Publishing","8. Intellectual Property",locator="EOI section 7, timelines"),
  evidence("impl-partners","Partner institutions are to support 50% of the total project cost estimated.",locator="EOI section 6.2(a)"),
  evidence("impl-partners","Each selected partner institution will be required to enter into an agreement with IndiaAI","The IndiaAI Safety Institute will retain",locator="EOI section 6.5"),
  evidence("impl-partners","8.3 IndiaAI may classify certain Collective Outputs as confidential","undertaking any work",locator="EOI section 8.3")],
 ["Selected partners and executed agreements","Assigned scopes of work and Safety Cell staffing","Sanctions, disbursements and utilisation records","Released collective outputs and publication policy"])
record("impl-projects","Responsible AI portfolio","Thirteen approved projects are not thirteen validated tools",
 "aig-techno","Programme activity reported",
 "The July official record reports 13 approved Responsible AI projects across safety themes.",
 "There is documentary evidence of a selected programme portfolio, but approvals and ongoing development are not completion certificates, independent benchmarks or proof that every tool is available.",
 "For each approved project, what was funded, delivered, evaluated and released?",
 "The mission-wide financial outlay is not an institute-specific or project-specific expenditure figure. No portfolio-wide effectiveness score is assigned.",
 [evidence("impl-safety-status","13 Responsible AI projects have been approved","Key initiatives",locator="27 July release, Safe & Trusted AI pillar"),
  evidence("impl-mission-status","Under the **Safe & Trusted AI pillar**","**India AI Governance",locator="29 July release, responsible AI projects")],
 ["Complete awarded-project list and scopes","Project-level sanctions and spending","Milestones and acceptance reports","Evaluation datasets, benchmarks and released artefacts"])
record("impl-tool-delivery","Technical tools","Named selections identify owners, not proven detection performance",
 "aig-techno","Programme activity reported",
 "The second EOI names five selected projects: three detection projects, an agriculture bias project and Anvil.",
 "The table gives journalists identifiable project owners and themes. It does not establish accuracy, robustness, licensing, release status or operational deployment.",
 "Can a reporter reproduce a stated benchmark and inspect false-positive rates before describing a tool as effective?",
 "The October 2025 selection predates the November framework; it is relevant programme lineage, not an outcome caused by that framework. The five selections are a subset, not five additional projects beyond the reported thirteen.",
 [evidence("impl-projects","List of Projects selected under Second EOI","The five selected projects",locator="Second EOI selection table"),
  evidence("impl-safety-status","Key initiatives include","**Nature & Objectives",locator="27 July release, named initiatives")],
 ["Repository or usable release and licence","Evaluation data, baselines and reproducibility instructions","Error rates across languages and demographic groups","Completion, acceptance and deployment records"])
record("impl-incident-repository","Incident reporting","Existing cyber duties do not prove a national AI-harm repository is live",
 "aig-incidents","Implementation not established by reviewed records",
 "The framework proposes a federated AI incident database; the reviewed corpus does not establish a live national intake mechanism.",
 "CERT-In's existing directions cover specified cyber incidents, including listed attacks or suspicious activity affecting AI/ML systems. That is a different scope from the proposed broader repository of AI harms.",
 "Who operates the national repository, what schema and intake endpoint exist, and how does reporting overlap with CERT-In?",
 "No verified national repository launch or public intake endpoint was found in this bounded review. That is not proof of absence. The six-hour cyber duty is not a universal deadline for every AI harm, and current legal advice requires checking later instruments.",
 [evidence("aig-guidelines","The database should be a national-level centralised system that has the ability to query and collect data from smaller, local databases in a federated manner.",locator="Guidelines Part 2.4; printed pp. 26–27"),
  evidence("impl-cert-directions","Any service provider","(iii)When required by",locator="Directions clause (ii), PDF p. 3"),
  evidence("impl-cert-directions","Attacks or malicious/ suspicious activities affecting systems/ servers/software/ applications related to Artificial Intelligence and Machine Learning",locator="Annexure I, category xx, PDF p. 7")],
 ["Operator, launch instrument and production intake URL","Incident taxonomy and schema","Confidentiality and data-sharing rules","Relationship to existing cyber reporting and complaint routes"])
record("impl-redress","Grievance redress","Platform appeals exist; universal AI-harm redress is not established",
 "aig-accountability","Limited-scope route documented",
 "The July explanation documents intermediary grievance officers and online GAC appeals.",
 "These are concrete routes for relevant platform-content disputes, not an all-purpose appeal against healthcare, hiring, credit or government AI decisions. A general governance recommendation is not itself a new complaint portal.",
 "For a particular AI decision, which body has jurisdiction, what remedy is available and where is that procedure documented?",
 "The reviewed records do not establish universal AI-specific redress. Other sectoral, consumer, constitutional or legal remedies may exist; their eligibility and current procedures require separate verification.",
 [evidence("impl-redress","Intermediaries are required to appoint Grievance Officers","**",locator="30 July release, Grievance Redressal Mechanism"),
  evidence("aig-guidelines","The Committee recommends that organisations deploying AI systems should establish accessible","xlviii",locator="Guidelines Part 2.5; printed p. 32")],
 ["Decision-specific complaint and appeal policy","Responsible decision-maker and human-review procedure","Jurisdiction, eligibility and remedies","Outcome records and accessibility of the route"])
record("impl-voluntary","Voluntary commitments","Frontier commitments were announced; compliance needs different evidence",
 "aig-voluntary","Commitments reported; compliance unverified",
 "The March summit release reports voluntary frontier AI impact commitments, and the July explanation reiterates them.",
 "A voluntary commitment is a real governance artefact but does not prove implementation or create a universal statutory mandate. Global summit deliverables should not be conflated with every domestic voluntary framework proposed in the guidelines.",
 "Which companies committed to what, on which timetable, and what public compliance or assurance evidence followed?",
 "The ledger verifies the official reporting of commitments, not every signatory, exact commitment text, follow-through or legal enforceability. No compliance ranking is inferred from pledges.",
 [evidence("impl-commitments","The New Delhi Frontier AI Impact Commitments were announced by 13 leading global and Indian frontier model developers to promote trustworthy and inclusive AI deployment.",locator="2 March release, global declarations section"),
  evidence("impl-safety-status","As part of New Delhi Frontier AI Impact Commitments","These outcomes reflect",locator="27 July release, summit deliverables")],
 ["Exact commitment instrument and signatory list","Specified deliverables and dates","Public progress reports and released evaluations","Independent assurance or verification method"])

assert len(records)==10
family=dict(id="impl",title="AI governance implementation evidence",shortTitle="Implementation evidence",
 status="Documented action ≠ verified outcome",
 description="Ten checkpoints connecting recommendations to orders, recruitment, programme records and unresolved outcomes.",
 coverage="Ten curated checkpoints across institutions, capacity, tools, incident reporting, redress and commitments.",
 scope="A bounded record review through 5 October 2026, not proof of absence, current staffing certification or a nationwide operational audit.",
 count=10,contributionCount=10,defaultId="impl-aigeg",
 timeline=[dict(date="May–Jun 2025",title="Partner process",detail="Safety Institute EOI; call is not an award"),
  dict(date="13 Apr 2026",title="Constitution orders",detail="AIGEG and TPEC; public announcements follow"),
  dict(date="Jun–Jul 2026",title="Recruitment and status records",detail="Keep administrative action separate from verified delivery"),
  dict(date="05 Oct 2026",title="Bounded review",detail="Unresolved questions remain visible")])
out=dict(families=[family],provisions=records,sources=sources,corrections=[])
for target in [ROOT/"src"/"data"/"implementation.json",ROOT/"public"/"implementation-data.json"]:
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(ROOT/"src"/"data"/"implementation.json")
print("Built ten implementation checkpoints, ten briefs and twelve official source snapshots.")
