"""Reproduce the curated SGI amendment and AI-guidelines lineage collections.

The inputs are immutable extracted public-source snapshots. Classification and
interpretation below are editorial observations, never legal determinations.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
CHECKED="5 October 2026"
sources=[]
def source(id,title,url,date,status,description,instrument):
    path=ROOT/"public"/"snapshots"/f"{id}.txt"
    raw=path.read_text()
    sources.append(dict(id=id,title=title,url=url,documentDate=date,publication=date,
        status=status,description=description,instrument=instrument,checked=CHECKED,
        snapshot=f"snapshots/{id}.txt",hash=hashlib.sha256(path.read_bytes()).hexdigest(),
        hashType="SHA-256 of extracted UTF-8 text, not original PDF bytes"))
    return re.sub(r"\s+"," ",raw).strip()

DURL="https://www.meity.gov.in/static/uploads/2025/10/9de47fb06522b9e40a61e4731bc7de51.pdf"
FURL="https://www.meity.gov.in/static/uploads/2026/02/f55fe52418b03f58b0669f6a8bc03b6d.pdf"
CURL="https://www.meity.gov.in/static/uploads/2026/03/20c30107195f68865104dd4e16176f4d.pdf"
BURL="https://www.meity.gov.in/static/uploads/2025/10/708f6a344c74249c2e1bbb6890342f80.pdf"
ADURL="https://indiaai.s3.ap-south-1.amazonaws.com/docs/subcommittee-report-dec26.pdf"
AFURL="https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf"
d=source("sgi-draft","Synthetic-media consultation draft",DURL,"22 October 2025","Consultation draft","Five proposed amending rules; not enacted law.","Draft SGI amendments")
f=source("sgi-final","Notified synthetic-media amendments",FURL,"10 February 2026","Notified amendment","G.S.R. 120(E); five amending rules. Express commencement: 20 February 2026.","G.S.R. 120(E)")
c=source("sgi-corrigendum","Synthetic-media English-text corrigenda",CURL,"26 February 2026","Correction","Two English substitutions on Gazette page 10. Hindi corrections are not conflated with the English register.","G.S.R. 148(E)")
b=source("sgi-baseline","Prior consolidated IT Rules",BURL,"Updated 22 October 2025","Prior consolidated text","Context for final changes absent from the consultation draft. This snapshot includes the October amendment's separate operative date.","Consolidated IT Rules")
source("sgi-consolidated","IT Rules incorporating the SGI corrigenda","https://www.meity.gov.in/static/uploads/2026/03/0b576f2071694b52e4cd6bb1b6dfab1e.pdf","26 February 2026 corrigenda","Corrected consolidation","Supporting cross-check; the final Gazette's original print remains the comparison source.","Consolidated IT Rules")
source("sgi-faq","MeitY synthetic-media FAQ","https://www.meity.gov.in/static/uploads/2025/10/065b6deb585441b5ccdf8be42502a49c.pdf","10 February 2026","Official explanation","Explanation, not the amending instrument; the upload-directory date is not treated as the document date.","MeitY FAQ")
ad=source("aig-consultation","AI Governance Guidelines Development report",ADURL,"Public consultation: 6 January 2025","Consultation report","Six recommendations and seven proposed principles; official IndiaAI article supplies the public-consultation date.","Subcommittee report")
af=source("aig-guidelines","India AI Governance Guidelines",AFURL,"Released 5 November 2025","Policy recommendations","Four-part governance framework, not a separately enacted AI statute. Printed-page locators are not asserted as PDF-page indices.","IndiaAI framework")
source("aig-launch","Official AI guidelines launch record","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2186639&reg=3&lang=2","5 November 2025","Official launch record","Confirms release and context; does not establish every proposed institution or recommendation was implemented.","PIB release")

# Isolate the English Gazette text. No hidden typographic repair is performed.
f=f[f.index("MINISTRY OF ELECTRONICS AND INFORMATION TECHNOLOGY NOTIFICATION"):]
def between(text,start,end):
    i=text.index(start)
    j=text.index(end,i+len(start))
    return text[i:j].strip()
def quote(text,start,end):
    return between(text,start,end)
def exact(text,value):
    assert value in text,value
    return value
records=[]
def row(id,label,title,before,after,bq,aq,typ,actor,summary,interpretation,question,caution,
        bl,al,family="sgi",beforeUrl=None,beforeSource=None,kind="Draft to final",featured=False,contribution=True):
    beforeUrl=beforeUrl or (DURL if family=="sgi" else ADURL)
    beforeSource=beforeSource or ("sgi-draft" if family=="sgi" else "aig-consultation")
    assert bq in before and aq in after,id
    records.append(dict(id=id,label=label,title=title,draftLabel=bl,type=typ,actor=actor,
        summary=summary,interpretation=interpretation,question=question,caution=caution,
        draftText=before,finalText=after,correctedText=after,beforeExcerpt=bq,afterExcerpt=aq,
        draftPage=0,finalPage=0,draftUrl=beforeUrl,finalUrl=FURL if family=="sgi" else AFURL,
        draftLocator=bl,finalLocator=al,familyId=family,comparisonKind=kind,
        beforeSourceId=beforeSource,afterSourceId="sgi-final" if family=="sgi" else "aig-guidelines",
        beforeLabel="PRIOR CONSOLIDATED RULE" if kind=="Prior law to amended law" else "CONSULTATION REPORT" if family=="aig" else "CONSULTATION DRAFT",
        afterLabel="PUBLISHED GUIDELINES" if family=="aig" else "NOTIFIED AMENDMENT",
        legalStatus="Recommendations; not a new standalone legal mandate" if family=="aig" else "Notified amendment; operative-date and court-status limits apply",
        evidenceScope="Mapped evidence segment; open the source for the complete instrument.",
        reviewStatus="Analyst-reviewed extracted English text; not independent legal approval.",
        featured=featured,contribution=contribution,correctionIds=[]))

dc=between(d,"1. (1)","2. In the")
fc=between(f,"1. Short Title","2. In the")
dd=between(d,"“(wa)","(ii) after sub-rule")
fd=between(f,"“(wa)","(b) after sub-rule")
di=between(d,"“(1A)","3. In the")
fi=between(f,"“(1A)","(1B) For")
ds=between(d,"“Provided that","4. In the")
fs=between(f,"(1B) For","3. In the")
dl=between(d,"“(3) Due diligence","5. In the")
fl=between(f,"“(3) Due diligence","4. In the")
du=between(d,"“(1A) A significant","[F. No.")
fu=between(f,"“(1A) A significant","(b) in sub-rule (4)")
fn=between(f,"“(c) an intermediary","(ii) in clause (d)")
bn=between(b,"(c) an intermediary","2[(d)")
ft=between(f,"(ii) in clause (d)","(b) in sub-rule (2)")
bt=between(b,"2[(d) an intermediary","(e) the temporary")
fg=between(f,"(b) in sub-rule (2)","(c) after sub-rule (2)")
bg=between(b,"3[(i) acknowledge the complaint","1[3A. Appeal")
fp=between(f,"(b) in sub-rule (4)","5. In the said rules")
bp=between(b,"(4) A significant social media intermediary","(5) 1[")
fr=between(f,"5. In the said rules","[F. No.")
br=between(b,"7. Non-observance","PART III")

row("sgi-commencement","Amendment 1","An express commencement date",dc,fc,
    exact(dc,"(2) They shall come into force on the ___ day of________, 2025."),
    exact(fc,"(2) They shall come into force on the 20 th day of February, 2026."),
    "Timing","Intermediaries","The draft's blank date becomes 20 February 2026 in the notification.",
    "A specified operative date replaces the placeholder. It is not the same as the notification's 10 February date.",
    "What changed operationally during the ten-day notice period?",
    "This verifies the instrument's date, not an exhaustive court-order or later-amendment chain.",
    "Draft amendment 1","Final amendment 1; Gazette p. 8",contribution=False)
row("sgi-definition","Rule 2(1)(wa)","SGI narrows to realistic audio and visual media",dd,fd,
    quote(dd,"information which",";”."),
    quote(fd,"audio, visual or audio-visual information which","; Provided"),
    "Scope change","Creators and platforms","The draft covered information generally; the final adds audio/visual forms and a real-person or event resemblance test.",
    "A headline about all AI-generated text being covered by this SGI definition would be overbroad. Other laws may still apply to text.",
    "Which content formats and transformations do platform policies classify as SGI?",
    "The final also inserts Rule 2(1)(ca) defining audio/visual information. Scope is not an exemption from other applicable law.",
    "Draft amendment 2(i)","Final amendment 2(a)(i)-(ii); Gazette p. 9",featured=True)
row("sgi-exclusions","Rule 2(1)(wa) proviso","Routine editing is conditionally outside the SGI definition",dd,fd,
    quote(dd,"information which",";”."),
    quote(fd,"routine or good-faith editing","; or (b)"),
    "Qualification","Journalists and researchers","The final adds three exclusion limbs for good-faith editing, document preparation and limited accessibility/quality uses.",
    "Routine editing is treated differently from materially misleading alterations. Educational or research content is not unconditionally exempt.",
    "Does an organisation document why a transformation qualifies for an exclusion?",
    "Read all three limbs: material distortion, false records and material manipulation remain limiting conditions.",
    "Draft amendment 2(i); no exclusion limbs","Final amendment 2(a)(ii), proviso (a)-(c); Gazette p. 9")
row("sgi-unlawfulreferences","Rule 2(1A)","Unlawful-information references retain SGI coverage",di,fi,
    quote(di,"For the purposes of these rules",".”."),
    exact(fi,"For the purposes of these rules, any reference to ‘information’ in the context of information being used to commit an unlawful act, including under clauses (b) and (d) of sub-rule (1) of rule 3 and sub-rules (2) and (4) of rule 4, shall be construed to include synthetically generated information, unless the context otherwise requires."),
    "Continuity","Intermediaries","The draft's rule making unlawful-information references include SGI is carried into the final.",
    "This is continuity, not a newly invented standalone offence for every use of synthetic media.",
    "Are public explanations distinguishing underlying illegality from the mere use of AI?",
    "The qualifying context and underlying applicable law still matter.",
    "Draft amendment 2(ii)","Final amendment 2(b), Rule 2(1A); Gazette p. 9",contribution=False)
row("sgi-removal-safeharbour","Rule 2(1B)","The removal clarification moves and broadens",ds,fs,
    quote(ds,"the removal or disabling",";”."),
    quote(fs,"the removal of, or disabling",".”."),
    "Scope change","Intermediaries","The proposed Rule 3(1)(b) removal proviso becomes a broader clarification in Rule 2(1B).",
    "The final expressly addresses rule-compliant removal and awareness from technical measures in relation to section 79(2)(a)-(b). It does not grant blanket immunity.",
    "What internal safeguards accompany proactive takedowns?",
    "Do not treat this limited clarification as removing all other safe-harbour conditions or legal remedies.",
    "Draft amendment 3","Final amendment 2(b), Rule 2(1B); Gazette p. 9",contribution=False)
row("sgi-user-notices","Rule 3(1)(c), (ca), (cb)","Quarterly notices and SGI-specific consequences",bn,fn,
    quote(bn,"an intermediary shall periodically",";"),
    quote(fn,"an intermediary shall periodically","that—"),
    "Scope change","Intermediaries and users","The final replaces annual reminders with at least quarterly notices and inserts SGI consequence and response clauses.",
    "Notifications now describe penalties, account action, evidence preservation, conditional identity disclosure and mandatory-reporting situations. Those are not automatic penalties in every case.",
    "Can users understand the notices and challenge inaccurate classification or account action?",
    "This is prior-law-to-amended-law context, not an October draft proposal. The two English criminal-law citations were later corrected; identity disclosure is expressly subject to applicable law.",
    "Prior Rule 3(1)(c), updated 22 Oct 2025","Final amendment 3(a)(i); Gazette pp. 9-10",
    beforeUrl=BURL,beforeSource="sgi-baseline",kind="Prior law to amended law")
row("sgi-takedown","Rule 3(1)(d)","Three-hour ordered takedowns are not a universal complaint clock",bt,ft,
    exact(bt,"remove or disable access to such information within thirty-six hours of the receipt of such actual knowledge"),
    exact(ft,"for the words “thirty-six hours”, the words “within three hours” shall be substituted"),
    "Timing","Intermediaries and public authorities","The final shortens the actual-knowledge takedown clock and changes authorisation wording and the police rank threshold.",
    "The three-hour change belongs to Rule 3(1)(d)'s actual-knowledge pathway. Ordinary user grievances have separate clocks.",
    "How are authorised notices authenticated, logged and reviewed before accelerated removal?",
    "The October draft did not propose this change. Read the underlying court/government actual-knowledge conditions; not every complaint starts this clock.",
    "Prior Rule 3(1)(d), updated 22 Oct 2025","Final amendment 3(a)(ii); Gazette p. 11",
    beforeUrl=BURL,beforeSource="sgi-baseline",kind="Prior law to amended law",featured=True)
row("sgi-grievance","Rule 3(2)","Three grievance clocks become shorter",bg,fg,
    exact(bg,"resolve such complaint within a period of fifteen days from the date of its receipt"),
    exact(fg,"for the words “fifteen days”, the words “seven days” shall be substituted"),
    "Timing","Complainants and grievance officers","General resolution becomes seven days, the specified removal-request category becomes 36 hours, and Rule 3(2)(b) becomes two hours.",
    "The clocks refer to different triggers and classes of grievance. A single 'all deepfakes removed in two hours' statement loses these distinctions.",
    "Do complaint channels route intimate-image and impersonation requests to the correct workflow?",
    "These substitutions were absent from the October draft. The two-hour category retains the underlying complaint-content requirements; acknowledgement remains a separate matter.",
    "Prior Rule 3(2), updated 22 Oct 2025","Final amendment 3(b); Gazette p. 11",
    beforeUrl=BURL,beforeSource="sgi-baseline",kind="Prior law to amended law")
row("sgi-prevention","Rule 3(3)(a)(i)","Prevention duties extend beyond a labelling-only draft",dl,fl,
    quote(dl,"Where an intermediary offers","it shall ensure"),
    quote(fl,"it deploys reasonable and appropriate technical measures","and includes any such"),
    "Scope change","SGI-enabling intermediaries","The final extends covered activities through publication and sharing, and adds technical prevention duties for unlawful SGI.",
    "The instrument now separates unlawful SGI prevention from labelling other covered SGI. This can affect distribution services, not only generation tools.",
    "What evidence demonstrates the measures' precision, false positives and appeal safeguards?",
    "The duties are tied to the final definition and applicable-law context. This desk does not decide whether a particular tool is an intermediary or a particular item is unlawful.",
    "Draft amendment 4, Rule 3(3)","Final amendment 3(c), Rule 3(3)(a)(i); Gazette p. 11")
row("sgi-label","Rule 3(3)(a)(ii)","The fixed ten-percent label is replaced",dl,fl,
    exact(dl,"covering at least ten percent of the surface area of the visual display or, in the case of audio content, during the initial ten percent of its duration"),
    quote(fl,"every such information not covered","and such information shall be embedded"),
    "Qualification","Platforms and publishers","The final removes the draft's ten-percent visual/audio formula in favour of prominent visibility or prefixed audio disclosure.",
    "Dropping the numeric formula does not drop the labelling duty. The revised standard leaves practical design and accessibility questions.",
    "Are labels readily noticeable across cropping, mobile display and audio-only playback?",
    "This obligation applies through the defined SGI and covered-service conditions, not every edited asset.",
    "Draft amendment 4, Rule 3(3)(a)","Final amendment 3(c), Rule 3(3)(a)(ii); Gazette p. 11",featured=True)
row("sgi-provenance","Rule 3(3)(a)(ii), (b)","Visible labels and feasible provenance are distinct",dl,fl,
    exact(dl,"labelled or embedded with a permanent unique metadata or identifier"),
    quote(fl,"such information shall be embedded","(b) the intermediary"),
    "Qualification","Platforms and provenance providers","The final uses a visible/audible label plus provenance metadata or another appropriate mechanism, to the extent technically feasible.",
    "The draft's 'or' formulation changes to distinct labelling and provenance requirements. Technical feasibility qualifies provenance, not an unrestricted permission to hide the label.",
    "What provenance survives export, reposting and screenshotting, and what is the disclosed feasibility limit?",
    "The no-removal limb is retained in revised wording. Metadata does not by itself prove that a depicted event is true.",
    "Draft amendment 4, Rule 3(3)(a)-(b)","Final amendment 3(c); Gazette pp. 11-12")
row("sgi-declarations","Rule 4(1A)","Upload declarations survive with revised verification wording",du,fu,
    exact(du,"deploy reasonable and appropriate technical measures, including automated tools or other suitable mechanisms"),
    exact(fu,"deploy appropriate technical measures, including automated tools or other suitable mechanisms"),
    "Qualification","Significant social media intermediaries","Declaration, technical verification and prominent notice remain; the operative verification phrase is revised.",
    "This is not removal of the declaration workflow. The explanation still requires reasonable and proportionate verification measures.",
    "How do platforms deal with inaccurate declarations and uncertain detector results?",
    "The difference between the operative clause and retained explanation must be read together. Not every intermediary is an SSMI.",
    "Draft amendment 5, Rule 4(1A)","Final amendment 4(a); Gazette p. 12")
row("sgi-proactive","Rule 4(4)","Proactive identification changes from endeavour to deploy",bp,fp,
    exact(bp,"endeavour to deploy technology-based measures, including automated tools or other mechanisms"),
    exact(fp,"deploy appropriate technical measures, including automated tools or other suitable mechanisms"),
    "Scope change","Significant social media intermediaries","A pre-existing proactive-identification clause shifts from 'endeavour to deploy' to 'deploy'.",
    "The final strengthens the operative wording for the existing categories, rather than introducing unlimited monitoring of every content type.",
    "Are proportionality, privacy and human-oversight safeguards applied alongside the technical deployment?",
    "Read the unchanged Rule 4(4) category limits and safeguards in the consolidated rules. This was not an October SGI draft amendment.",
    "Prior Rule 4(4), updated 22 Oct 2025","Final amendment 4(b); Gazette p. 12",
    beforeUrl=BURL,beforeSource="sgi-baseline",kind="Prior law to amended law")
row("sgi-criminal","Rule 7","The criminal-code cross-reference is updated",br,fr,
    exact(br,"including the provisions of the Act and the Indian Penal Code"),
    exact(fr,"“the Bharatiya Nyaya Sanhita, 2023 (45 of 2023)”"),
    "Wording","Intermediaries","Rule 7's Indian Penal Code reference is replaced with the Bharatiya Nyaya Sanhita citation.",
    "This updates the named criminal-law reference; it is not evidence that every breach automatically creates criminal guilt.",
    "Are explanations distinguishing due-diligence consequences from the elements of an underlying offence?",
    "This final substitution was absent from the October draft. Legal liability depends on the applicable law and facts.",
    "Prior Rule 7, updated 22 Oct 2025","Final amendment 5; Gazette p. 12",
    beforeUrl=BURL,beforeSource="sgi-baseline",kind="Prior law to amended law",contribution=False)

# Recommendation lineage, not an aligned legal redline. Supporting material is
# available in the full snapshots, but annexures/glossary are not scored as changes.
def ai(id,title,bs,be,as_,ae,bqs,bqe,aqs,aqe,summary,meaning,question,caution,bl,al,
       typ="Scope change",contribution=True,featured=False):
    before=between(ad,bs,be);after=between(af,as_,ae)
    row(id,al.split(";")[0],title,before,after,quote(before,bqs,bqe),quote(after,aqs,aqe),
        typ,"AI developers, regulators and public institutions",summary,meaning,question,
        "Recommendation lineage, not a one-to-one legal deletion/insertion. "+caution,
        bl,al,family="aig",kind="Recommendation lineage",featured=featured,contribution=contribution)

ai("aig-principles","Seven principles are reframed as seven sutras",
   "A. AI Governance Principles","B. Considerations",
   "Part 1: Key Principles","Using these seven principles",
   "Transparency: AI systems","2. Accountability",
   "All other things being equal","Fairness and Equity",
   "The earlier seven-principle list is reorganised into seven sutras, including explicit innovation-over-restraint framing.",
   "The new framing is a policy priority, not permission to disregard binding privacy, equality or safety law.",
   "How do procurement and deployment decisions justify the balance between innovation and harm mitigation?",
   "A principle disappearing as a standalone heading does not establish that its substance or legal protection was abolished.",
   "Consultation report II.A; printed pp. 3-4","Part 1; printed pp. 12-13",featured=True)
ai("aig-infrastructure","Infrastructure becomes an explicit governance pillar",
   "Accordingly, the Government","The Safe & Trusted",
   "Part 2: Issues & Recommendations","India AI Governance Guidelines 17",
   "The IndiaAI mission will","The Mission will",
   "Empower the India AI mission","Increase data availability",
   "Infrastructure moves from mission background to a dedicated pillar covering data, compute and DPI.",
   "Governance is framed as enabling access and safety evaluation as well as setting restrictions.",
   "Who receives affordable compute and representative evaluation datasets, and how is access assessed?",
   "The historical infrastructure figures in the November report are not verified current inventory or scheme eligibility.",
   "Consultation report introduction; printed p. 1","Part 2.1; printed pp. 14-16",contribution=False)
ai("aig-capacity","Public procurement and enforcement training gain explicit attention",
   "6. Form a sub-group","Conclusion",
   "India AI Governance Guidelines 17","India AI Governance Guidelines 18",
   "review and strengthen the mechanisms","This should extend",
   "Conduct training programs for government officials","Develop the capacity",
   "The earlier regulatory-capacity recommendation broadens into training for officials, public procurement, police and wider public literacy.",
   "The final makes administrative capability a visible condition for responsible adoption.",
   "Can agencies show training, procurement-evaluation criteria and independent expertise rather than awareness events alone?",
   "This is a thematic successor, not a claim that the earlier adjudication proposal was enacted.",
   "Consultation recommendation 6; printed p. 19","Part 2.2; printed p. 17",contribution=False)
ai("aig-policy","A proposed Digital India Act path becomes targeted legal review",
   "6. Form a sub-group","Conclusion",
   "India AI Governance Guidelines 18","India AI Governance Guidelines 25",
   "Form a sub-group","Given the rapid development",
   "The Committee’s current assessment","For example",
   "The final broadens the legal-review approach across existing statutes, classification, liability, copyright, authentication and sectoral gaps.",
   "The guidelines do not themselves enact a standalone AI law, grant a copyright licence or settle intermediary liability.",
   "Which recommended amendments have been separately issued, and which remain proposals?",
   "The November document's DPDP discussion predates the final DPDP Rules. Copyright and other later policy developments require separate current-law checks.",
   "Consultation recommendation 6; printed p. 19","Part 2.3; printed pp. 18-24")
ai("aig-risk","Context-sensitive risk analysis becomes an explicit India framework",
   "B. The need for transparency","C. The need for",
   "India AI Governance Guidelines 25","India AI Governance Guidelines 31",
   "The risks posed by a system","For systems deployed",
   "the Committee recommends that a suitable risk assessment","Incident Reporting",
   "The final sets out risk categories, vulnerable-group concerns and a locally adapted classification framework.",
   "The recommended response is based on context and harm evidence, not merely model size or computational capacity.",
   "What local evidence, affected-group participation and validation support the eventual risk taxonomy?",
   "This is a recommended framework, not a verified operational classification system or binding risk-tier schedule.",
   "Consultation report III.B; printed pp. 11-12","Part 2.4; printed pp. 25-30")
ai("aig-incidents","An incident repository becomes a federated reporting proposal",
   "3. To build evidence","4. To enhance transparency",
   "Incident Reporting","Voluntary Frameworks",
   "the database should receive reports","Private entities",
   "The database should be a national-level","Local databases",
   "The final adds a federated national/local architecture, common schemas and wider participation to the earlier incident-database proposal.",
   "The design provides useful accountability questions: reporting access, confidentiality, interoperability and feedback into risk assessment.",
   "Has a reporting route been launched, and can victims distinguish learning-oriented incident reporting from grievance redress?",
   "Both documents discourage punitive reporting design. Recommendations and launch rhetoric do not prove the database is live; grievance channels are separately recommended.",
   "Consultation recommendation 3; printed pp. 16-17","Part 2.4; printed pp. 26-27",featured=True)
ai("aig-voluntary","Voluntary commitments get incentives and a possible mandatory trajectory",
   "4. To enhance transparency","5. The Technical",
   "Voluntary Frameworks","Techno-legal approach",
   "The voluntary commitments are expected","The role of the",
   "Their essential features","The table",
   "The final describes voluntary frameworks as non-binding and says some baseline measures may later become mandatory.",
   "A future mandatory trajectory should not be misreported as already enforceable obligations imposed by this document.",
   "Which commitments produce public, understandable evidence, and which remain self-certification?",
   "Any eventual mandatory measure needs its own legal basis and instrument. Adoption and enforcement are not established here.",
   "Consultation recommendation 4; printed pp. 17-18","Part 2.4; printed pp. 27-28")
ai("aig-techno","Techno-legal solutions acquire explicit limitations",
   "5. The Technical","6. Form a sub-group",
   "Techno-legal approach","Mitigating Loss of Control",
   "examine the viability of such technological solutions","The Secretariat should",
   "DEPA for AI Training) is an example","It supports",
   "The final expands the technology-measures proposal into compliance-by-design and DEPA examples, while acknowledging downstream and performance limitations.",
   "Technical architecture is not presented as sufficient governance on its own.",
   "What independent tests support a claimed privacy, bias or provenance safeguard, and what does it not control?",
   "No product efficacy is certified by this collection; a recommendation or architecture diagram does not prove compliance in deployment.",
   "Consultation recommendation 5; printed pp. 18-19","Part 2.4; printed pp. 28-30",contribution=False)
ai("aig-accountability","Grievance redress is kept separate from incident learning",
   "6. Form a sub-group","Conclusion",
   "India AI Governance Guidelines 31","India AI Governance Guidelines 34",
   "review and strengthen the mechanisms","This should extend",
   "These grievance redressal systems","xlviii",
   "The final adds accessible, multilingual grievance recommendations, graded liability and non-statutory accountability mechanisms.",
   "A channel for resolving an individual's harm is not interchangeable with an incident repository for learning.",
   "Can an affected person locate a human-reviewed grievance route and receive a meaningful response?",
   "The report's '9-12 months' possible schedule is not treated as a statutory deadline. Liability and mandatory redress require applicable legal authority.",
   "Consultation recommendation 6; printed p. 19","Part 2.5; printed pp. 31-33")
ai("aig-institutions","The technical secretariat proposal becomes a broader institutional architecture",
   "1. To implement a whole-of-government","3. To build evidence",
   "India AI Governance Guidelines 34","India AI Governance Guidelines 38",
   "MeitY should establish and host a technical secretariat","As the Committee",
   "It should be supported by a Technology & Policy Expert Committee","Further details",
   "The final specifies AIGG coordination, TPEC expert advice and AISI technical functions, rather than repeating the earlier secretariat structure.",
   "The useful reporting task is to trace mandates, membership, budgets and issued decisions, not infer institutional implementation from a recommendation.",
   "Which proposed bodies have appointment orders, published terms of reference and actual outputs?",
   "Do not call every institution merely proposed: the November report describes AISI as recently established. Current establishment and operational status need separate records.",
   "Consultation recommendations 1-2; printed pp. 13-16","Part 2.6; printed pp. 34-37")
ai("aig-action-plan","The final introduces a staged action plan without exact dates",
   "IV. Recommendations","Conclusion",
   "Part 3: Action Plan","India AI Governance Guidelines 42",
   "The committee recommends the following","1. To implement",
   "The Action Plan below","Establish the AI Governance",
   "The final groups action items into short-, medium- and long-term stages and illustrates institutional responsibilities.",
   "This creates a useful implementation checklist, but not a precise countdown or proof of completion.",
   "Which action items have a named owner, milestone, budget and published completion evidence?",
   "The table's qualitative timelines should not be converted into invented dates. Flattened table extraction is not automatically diff-highlighted.",
   "Consultation report IV; six recommendations","Part 3; printed pp. 38-41",typ="Addition")
ai("aig-practical","Industry and regulators receive separate practical recommendations",
   "4. To enhance transparency","5. The Technical",
   "Part 4: Practical Guidelines","India AI Governance Guidelines 44",
   "commitments to release regular transparency reports","commitments to internal",
   "Proposed AI governance frameworks should avoid","The appropriate regulator",
   "The final adds a distinct practical part for industry and regulators, including transparency, redress, proportionality and instrument choice.",
   "Recommended practices can guide reporting enquiries and procurement discussions without being mislabelled as a new statutory compliance checklist.",
   "What evidence distinguishes published transparency or redress commitments from actually implemented practice?",
   "Existing legal obligations remain binding through their own instruments. Recommendations to comply with them do not change their commencement or exemptions.",
   "Consultation recommendation 4; printed pp. 17-18","Part 4; printed pp. 42-43",contribution=False)

corrections=[]
target=next(r for r in records if r["id"]=="sgi-user-notices")
old="the Bharatiya Nagarik Suraksha Sanhita, 2023 (46 of 2023)"
new="the Bharatiya Nyaya Sanhita, 2023 (45 of 2023) read with the Bharatiya Nagarik Suraksha Sanhita, 2023 (46 of 2023)"
assert target["finalText"].count(old)==2
target["correctedText"]=target["finalText"].replace(old,new)
for n,locator in enumerate(["Gazette p. 10, lines 10-11","Gazette p. 10, lines 42-43"],1):
    id=f"SGI-CR-0{n}"
    target["correctionIds"].append(id)
    corrections.append(dict(id=id,provisionId=target["id"],locator=locator,before=old,after=new,
        note="English-text criminal-law reference correction; not a global replacement.",familyId="sgi",sourceUrl=CURL))

families=[
 dict(id="sgi",title="Synthetic media & platform duties",shortTitle="Synthetic media rules",
      status="Notified rules + corrigenda",description="October draft to February amendment, with prior-law context for additions not proposed in the draft.",
      coverage="All five final amending rules mapped across 14 comparison units; two English corrigenda tracked.",
      count=14,contributionCount=10,defaultId="sgi-definition",
      scope="This collection covers the SGI amendment, not all provisions of the IT Rules or a current court-status certification.",
      timeline=[dict(date="22 Oct 2025",title="Consultation draft",detail="Five proposed amending rules"),
                dict(date="10 Feb 2026",title="Notified amendment",detail="Express commencement: 20 Feb 2026"),
                dict(date="26 Feb 2026",title="Corrigenda",detail="Two directed English substitutions")]),
 dict(id="aig",title="India AI Governance Guidelines",shortTitle="AI governance guidelines",
      status="Policy recommendations",description="January consultation report to November governance framework; a recommendation-lineage comparison, not a legal redline.",
      coverage="12 thematic units map all four main parts and all six consultation recommendations; glossary, annexures and references are supporting material, not scored changes.",
      count=12,contributionCount=8,defaultId="aig-incidents",
      scope="No recommendation is automatically labelled a new legal mandate; current institutional implementation remains a separate verification task.",
      timeline=[dict(date="06 Jan 2025",title="Consultation report",detail="Six recommendations; seven proposed principles"),
                dict(date="05 Nov 2025",title="Published framework",detail="Four parts, six pillars, seven sutras")])
]
result=dict(title="AI Watch India expanded policy collections",checked=CHECKED,
            families=families,sources=sources,provisions=records,corrections=corrections)
assert len(records)==26 and len(corrections)==2 and len(sources)==9
assert sum(r["contribution"] for r in records)==18
for path in [ROOT/"src/data/expansion.json",ROOT/"public/expansion-data.json"]:
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(ROOT/"src/data/expansion.json")
print("Built two collections: 26 comparisons, 18 additional briefs, nine source snapshots, two English corrections.")
