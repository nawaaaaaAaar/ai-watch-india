"""Rebuild curated records from supplied public research artifacts.

This is data processing, not an autonomous legal interpretation engine.
The source snapshots are extracted text, never claimed to be PDF binary copies.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INPUT = HERE / "research"
OUT = HERE / "src" / "data"
OUT.mkdir(parents=True, exist_ok=True)
raw = [json.loads(x) for x in (INPUT / "provision-comparison.jsonl").read_text().splitlines()]
coverage = list(csv.DictReader((INPUT / "provision-coverage.csv").open()))

def clean(text):
    text = re.sub(r"(?m)^.*(?:THE GAZETTE OF INDIA|SEC\. 3\(i\)|भाग II|भारत का रािपत्र).*$", "", text)
    text = re.sub(r"(?m)^\s*\d{1,2}\s*$", "", text)
    text = text.split("[F. No.", 1)[0]
    return re.sub(r"\s+", " ", text).strip()

# Titles and judgements are curated, not inferred from machine diff counts.
titles = [
    "Phased commencement", "Definitions and relocated terms", "Consent notices",
    "Consent Manager registration", "State provision of benefits and services",
    "Reasonable security safeguards", "Personal data breach notices",
    "Retention and erasure", "Processing contact information", "Children's verifiable consent",
    "Disability and lawful-guardian consent", "Children's-data exemptions",
    "Significant Data Fiduciary duties", "Rights and grievance mechanisms",
    "Cross-border transfers", "Research, archiving and statistics",
    "Board appointment committees", "Board member service terms",
    "Board meetings and inquiries", "The Board as a digital office",
    "Board officers and employees", "Appeals to the Tribunal", "Information-calling powers",
    "Consent Manager conditions and duties", "State and research processing standards",
    "Purpose-expiry periods and thresholds", "Conditional children's-data exemptions",
    "Board member salary and service terms", "Board employee service terms",
    "Information purposes and authorised persons",
]
types = ["Timing","Wording","Wording","Continuity","Wording","Qualification","Scope change","Addition",
         "Continuity","Wording","Qualification","Continuity","Scope change","Addition","Wording","Continuity",
         "Scope change","Continuity","Continuity","Continuity","Wording","Wording","Wording",
         "Continuity","Scope change","Wording","Addition","Continuity","Continuity","Scope change"]
actors = ["All regulated entities","All regulated entities","Data Fiduciaries","Consent Managers",
          "State bodies","Data Fiduciaries","Data Fiduciaries","Data Fiduciaries","Data Fiduciaries",
          "Children and parents","Persons with disabilities","Children and parents",
          "Significant Data Fiduciaries","Data Principals","Data Fiduciaries","Researchers",
          "Data Protection Board","Data Protection Board","Data Protection Board","Data Protection Board",
          "Data Protection Board","Appellants","State bodies","Consent Managers","State bodies",
          "Large online platforms","Children and parents","Data Protection Board","Data Protection Board","State bodies"]
details = {
    "rule-1": ("A notified provision is not necessarily already operative. Preserve the official formula and the unresolved publication-date basis.",
               "Confirm which publication date is the base for calculated commencement dates.",
               "13 versus 14 November appears in official metadata and explanations. Do not treat a computed compliance date as settled."),
    "rule-3": ("The personal-data description remains itemised; only the goods/services/uses description changes to specific.",
               "How will organizations implement specific notices without bundling unrelated purposes?",
               "Wording change alone does not establish unlimited bundled consent."),
    "rule-5": ("The enabling sentence is removed from the rule, not the parent statute. Read section 7(b) and the Second Schedule together.",
               "Which legal basis and processing standards apply to a named public service?",
               "Do not infer unrestricted state processing from a shortened rule."),
    "rule-6": ("The access-control and processor-contract clauses acquire applicability qualifiers; the general security duty remains.",
               "What facts make these safeguards applicable to an organization's architecture?",
               "This is not a blanket exemption for small organizations."),
    "rule-7": ("Location is removed from individual notice requirements, but remains in the Board notice. The recipient matters.",
               "Why do individual and Board disclosure channels differ?",
               "The 72-hour detailed Board report is not a 72-hour grace period for every notification."),
    "rule-8": ("A general minimum one-year retention provision is added alongside existing security-purpose retention. Erasure, purpose and lawful exceptions must be read together.",
               "How will deletion workflows and processor contracts implement the added retention floor?",
               "Rule 8(1)'s changed conditional syntax requires legal review. These duties are in the delayed-commencement group. The draft sub-rule (3) user-account definition moved to final Rule 2; comparing its excerpt with the new retention sub-rule does not mean that definition was abolished."),
    "rule-10": ("Authorized-entity wording moves from maintenance to issuance; examples clarify the parent/adult verification workflow.",
                "What information is necessary to verify a parent without excessive collection?",
                "The draft source rule contains both children and disability provisions; the final splits them."),
    "rule-11": ("A functional inability-despite-support condition is added to the second disability-definition limb.",
                "How will platforms avoid incorrectly requiring guardian consent?",
                "A diagnosis alone should not be treated by this tool as a legal-capacity finding. This is a split of draft rule 10."),
    "rule-13": ("The obligation now covers technical measures including algorithmic software, and the transfer-related committee has a stated composition.",
                "What measures and methods will an impact assessment actually examine?",
                "This duty concerns Significant Data Fiduciaries; it is not a general AI licensing rule."),
    "rule-14": ("The final text introduces ninety-day grievance language and changes rights-request mechanics. The sentence is awkward; practitioner readings concern grievances.",
                "How will the grievance mechanism implement the period and escalation?",
                "Do not describe this as a universal ninety-day deadline for every access, correction or erasure request."),
    "rule-15": ("The transfer rule is recast around processing under the Act, while government requirements remain relevant.",
                "Which orders and sector-specific restrictions govern this transfer?",
                "Read section 16 of the Act. This is not proof of unrestricted international transfers."),
    "rule-16": ("The rule is substantially retained, but the parent Act limits the research exemption to data not used for a decision specific to a Data Principal.",
                "Does the actual research workflow satisfy the statutory condition?",
                "Read section 17(2)(b) of the Act and the changed Second Schedule."),
    "rule-23": ("The section 36 sentence is removed from the rule, but statutory power remains in the Act; confidentiality language is restructured.",
                "What statutory basis and purpose does an actual information order assert?",
                "A removed cross-reference is not proof that statutory power disappears."),
    "schedule-second": ("The standard expands from accuracy to completeness, accuracy and consistency.",
                        "How are public-sector and research datasets checked for completeness and consistency?",
                        "This standard does not prove that a particular dataset is faulty."),
    "schedule-third": ("Thresholds and periods are retained; the social-media definition's source changes.",
                       "Which class, threshold and purpose exception applies to the platform?",
                       "Flattened PDF table reading order creates false token differences. No automatic table highlighting is shown."),
    "schedule-fourth": ("Real-time child-location and expanded protective information/service/advertisement purposes are added conditionally.",
                        "Who establishes necessity, safety and boundaries for location tracking?",
                        "These are exemptions from specified section 9 obligations, not all privacy duties or a general targeted-ad permission."),
    "schedule-seventh": ("The schedule acquires a linkage to the general retention rule while retaining its information-purpose framework.",
                         "Which authorized person and purpose supports a specific demand?",
                         "A listed purpose is not evidence of a specific information demand or deployment."),
}
corrections = [
    {"id":"CR-01","provisionId":"rule-1","locator":"p. 24, line 22","before":"of this Gazette","after":"in the Official Gazette","note":"Rule 1(3), first occurrence."},
    {"id":"CR-02","provisionId":"rule-1","locator":"p. 24, line 24","before":"of this Gazette","after":"in the Official Gazette","note":"Rule 1(4), second occurrence."},
    {"id":"CR-03","provisionId":"rule-13","locator":"p. 29, line 44","before":"Department","after":"Departments","note":"Committee definition; exact targeted phrase."},
    {"id":"CR-04","provisionId":"rule-23","locator":"p. 32, line 4","before":"given in such","after":"given in such order","note":"Completes the information-order wording."},
    {"id":"CR-05","provisionId":"schedule-first","locator":"p. 34, line 1","before":"everybody","after":"every body","note":"Corporate ownership disclosure."},
    {"id":"CR-06","provisionId":"schedule-first","locator":"p. 34, line 26","before":"(18 or 2013)","after":"(18 of 2013)","note":"Specified Companies Act citation only."},
    {"id":"CR-07","provisionId":"schedule-fourth","locator":"p. 38, line 2","before":".","after":";","note":"Advertisement definition terminator only."},
    {"id":"CR-08","provisionId":"schedule-fourth","locator":"p. 38, lines 1–15","before":"(a) to (f)","after":"(a) to (g)","note":"Seven definition labels in the Schedule's note, not global replacement."},
]
def corrected(identifier, text):
    if identifier == "rule-1":
        assert text.count("of this Gazette") == 2
        text = text.replace("of this Gazette", "in the Official Gazette")
    if identifier == "rule-13":
        assert "Department of the Central Government" in text
        text = text.replace("Department of the Central Government","Departments of the Central Government")
    if identifier == "rule-23":
        assert "given in such." in text
        text = text.replace("given in such.", "given in such order.")
    if identifier == "schedule-first":
        assert "everybody corporate" in text and text.count("(18 or 2013)") == 1
        text = text.replace("everybody corporate", "every body corporate").replace("(18 or 2013)", "(18 of 2013)")
    if identifier == "schedule-fourth":
        beginning, note = text.split("Note: In this Schedule, —", 1)
        assert "2019 (35 of 2019)." in note
        note = note.replace("2019 (35 of 2019).", "2019 (35 of 2019);", 1)
        matches = list(re.finditer(r"\(([a-f])\) “", note))
        assert len(matches) == 7
        for i, match in reversed(list(enumerate(matches))):
            note = note[:match.start()] + f"({chr(97+i)}) “" + note[match.end():]
        text = beginning + "Note: In this Schedule, —" + note
    return text

draft_pages = [28,28,28,29,29,30,30,31,32,32,33,34,34,34,35,35,35,36,36,36,37,37,37,38,41,42,44,46,49,51]
final_pages = [24,24,24,25,25,26,26,27,27,27,28,29,29,29,30,30,30,30,30,31,31,31,32,32,34,35,36,38,40,40]
featured = {"rule-8","rule-14","rule-13","schedule-fourth","rule-7","rule-11","schedule-second","rule-1"}
provisions = []
for index, (row, observation) in enumerate(zip(raw, coverage)):
    identifier = row["final_id"]
    summary = re.sub(r"\[Draft\].*$", "", observation["reviewed_observation_with_source_links"]).strip()
    interpretation, question, caution = details.get(identifier, (
        "This record documents continuity or a wording/procedural change. Significance must be assessed in its legal and operational context.",
        "Does this wording or its linked schedule change how the provision is implemented?",
        "Analyst review is not legal advice. No claim of actual compliance or real-world harm is made."))
    ft = clean(row["final_text"])
    dt = clean(row["draft_text"])
    def between(text, start, end=None):
        chunk = text[text.index(start):]
        return chunk.split(end,1)[0].strip() if end and end in chunk else chunk
    before_excerpt, after_excerpt = dt[:1100], ft[:1100]
    if identifier=="rule-8":
        before_excerpt = between(dt, "(3) In this rule")
        after_excerpt = between(ft, "(3) Without prejudice", "Illustration.")
    elif identifier=="rule-7":
        before_excerpt = between(dt, "(a) a description", "(b)")
        after_excerpt = between(ft, "(a) a description", "(b)")
    elif identifier=="rule-13":
        before_excerpt = between(dt, "(3) A Significant", "(4)")
        after_excerpt = between(ft, "(3) A Significant", "(4)")
    elif identifier=="rule-14":
        before_excerpt = between(dt, "(3) Every", "(4)")
        after_excerpt = between(ft, "(3) Every", "(4)")
    elif identifier=="schedule-second":
        before_excerpt = between(dt, "(d) Processing", "(e)")
        after_excerpt = between(ft, "(d) Processing", "(e)")
    elif identifier=="schedule-fourth":
        before_excerpt = between(dt, "4. For ensuring", "Note:")
        after_excerpt = between(ft, "4. For the determination", "Note:")
    provisions.append({
        "id":identifier,"label":observation["final_provision"],"title":titles[index],
        "draftLabel":observation["draft_counterpart"],"type":types[index],"actor":actors[index],
        "summary":summary,"interpretation":interpretation,"question":question,"caution":caution,
        "draftText":dt,"finalText":ft,"correctedText":corrected(identifier, ft),
        "beforeExcerpt":before_excerpt,"afterExcerpt":after_excerpt,
        "draftPage":draft_pages[index],"finalPage":final_pages[index],
        "reviewStatus":"Analyst-reviewed extracted English text; not independent legal review",
        "featured":identifier in featured,
        "correctionIds":[c["id"] for c in corrections if c["provisionId"]==identifier],
    })
documents = [
    ("draft","Consultation draft","G.S.R. 02(E)","3 January 2025","Gazette dated 3 January 2025","Draft","https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf","draft.txt","22 rules · 7 schedules. Consultation, not enacted duties."),
    ("final","Notified final Rules","G.S.R. 846(E)","13 November 2025","Gazette dated 13 November; MeitY listing says 14 November 2025","Notified / phased","https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf","final.txt","23 rules · 7 schedules. Not all duties commence together."),
    ("corrigendum","English-text corrigenda","G.S.R. 892(E)","10 December 2025","Gazette dated 11 December; MeitY listing 16 December 2025","Correction","https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf","corrigendum.txt","8 directed substitutions. Preserve the as-printed version."),
    ("commencement","Act commencement instrument","G.S.R. 843(E)","13 November 2025","Gazette dated 13 November; publication-date basis disputed","Commencement","https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf","commencement.txt","Separate instrument for the parent Act's phased commencement."),
]
sources=[]
for identifier,title,instrument,date,publication,status,url,snapshot,description in documents:
    data = (HERE/"public"/"snapshots"/snapshot).read_bytes()
    sources.append({"id":identifier,"title":title,"instrument":instrument,"documentDate":date,
                    "publication":publication,"status":status,"url":url,"snapshot":f"snapshots/{snapshot}",
                    "hash":hashlib.sha256(data).hexdigest(),"hashType":"SHA-256 of extracted UTF-8 text; not original PDF bytes",
                    "description":description,"checked":"4 October 2026"})
dataset={"title":"Digital Personal Data Protection Rules, 2025","checked":"4 October 2026",
         "sources":sources,"provisions":provisions,"corrections":corrections}
(OUT/"policy.json").write_text(json.dumps(dataset,ensure_ascii=False,indent=2))
(HERE/"public"/"policy-data.json").write_text(json.dumps(dataset,ensure_ascii=False,indent=2))
print(OUT/"policy.json")
print(f"Built {len(provisions)} provisions, {len(corrections)} corrections, {len(sources)} source records.")
