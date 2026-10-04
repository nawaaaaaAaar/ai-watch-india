# AI Watch India: Policy Change Desk

## Executive assessment

A useful first product is a source-backed policy comparison workspace for journalists, policy researchers and decision-makers: inspect changes between official versions, separate legal text from interpretation, check when a provision takes effect, and export a defensible briefing. The recommended contribution is a better workflow, not a claim to have invented policy tracking or document comparison.

The worked example compares the January 2025 draft Digital Personal Data Protection Rules with the November 2025 notified Rules, then incorporates the December corrigenda and the separate Act commencement notification. The draft has 22 rules and seven schedules; the final has 23 rules and seven schedules, including a split of the draft's combined child/disability consent rule into two final rules. [MeitY draft Rules](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [MeitY final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

The strongest examples are a new general retention provision, new ninety-day grievance language, a broader technical-measures obligation for Significant Data Fiduciaries, expanded children's-data exemptions, and the need to distinguish notification from commencement. These are demonstrable comparison tasks, not hypothetical interface features. [MeitY final Rules, rules 1, 8, 13 and 14 and Fourth Schedule](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

The recommended decision is **proceed to a bounded, working product**, but not to an automated national policy observatory. Relevance and a technically tractable first workflow are supported; demand, willingness to return, willingness to pay and superiority over existing tools are not yet established. The first release should serve a small set of official document families exceptionally well, with a complete document-to-reviewed-brief workflow.

## Scope and evidence standard

### What this study covers

The scope is the English text of both official Rules documents, all final rules and schedules, all eight substitutions directed by the December corrigenda, and the companion Act commencement instrument. Selected provisions of the parent Act are included where reading a rule alone would produce a misleading conclusion. [Draft Rules](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) [Act commencement notification](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf) [DPDP Act](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)

“Complete coverage” here means every final provision has an explicitly reviewed counterpart or split relationship and a coverage classification. It does not mean a certified legal redline of every character, a bilingual legal audit, proof of nationwide compliance, or an exhaustive search of every subsequent court order and Gazette issue.

Research was conducted on 4 October 2026. Current-year searches and the ministry's document listing were checked; the listing contains the Rules, a corrigendum and related implementation instruments, but that observation does not establish that no other relevant instrument exists. [MeitY document listing](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa)

### Method and confidence

- **Primary text first:** Official extracted English text was read, with rule and schedule locators retained. Print page references below follow the page markers in those documents; the original PDF links remain the verification route.
- **Structured inventory:** The extraction produced 22 draft rule blocks, 23 final rule blocks and seven schedule blocks in each version. A programmatic count and mapping check passed; all 30 final provision records were subsequently examined.
- **Mechanical comparison:** Whitespace and recurring Gazette headers were normalized for a token diff. Raw text was retained, and neither punctuation differences nor a machine-generated diff were treated automatically as substantive legal change.
- **Editorial review:** Changes were classified by textual evidence, possible significance and required follow-up. This is analyst review, not legal-counsel certification.
- **Correction handling:** The original final print and the corrigendum are distinct evidence objects. Corrections are recorded below rather than silently replacing the historical text.
- **Cross-checking:** Major changes were checked against practitioner analysis, without substituting that analysis for the official text. [Shardul Amarchand Mangaldas analysis](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/) [PwC analysis](https://www.pwc.in/assets/pdfs/news-alert/regulatory-insights/2025/pwc_india_regulatory_insights_16_november_2025_meity_notifies_digital_personal_data_protection_rules_2025.pdf)

The companion JSONL is reproducible raw comparison material, not a ready-to-publish legal assessment. In particular, flattened tables create apparent insertions and deletions when cell reading order changes; those artifacts were not promoted to findings.

## Why this example is relevant

The Rules contain duties concerning notices, security, breaches, retention, children's data, significant fiduciaries and rights handling. They also govern public-sector processing standards and information-calling mechanisms, making them relevant to public administration and reporting as well as organizational preparation. [Final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

AI Watch India need not be restricted to documents titled “AI policy.” The final significant-fiduciary rule expressly covers “technical measures including algorithmic software,” providing a concrete connection to algorithmic governance; that is not the same as a comprehensive AI statute or a rule covering every AI developer. [Final Rules, rule 13(3)](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

The useful question is therefore not “Can a model summarize this PDF?” It is “Can a person accurately locate what changed, understand its limits, and carry evidence into a decision or a reported story?”

## Worked findings

### Commencement is a separate comparison dimension

**Textual finding:** The draft left the commencement date for much of the framework blank; the final supplies three groups: rules 1, 2 and 17–21 on publication, rule 4 one year after publication, and rules 3, 5–16, 22 and 23 eighteen months after publication. The corrigendum replaces “of this Gazette” with “in the Official Gazette” in both delayed-commencement clauses. [Draft, rule 1, p. 28](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 1, p. 24](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda, items (i)(a) and (i)(b)](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf)

**Interpretation:** A page describing these duties as already universally operative would mislead readers. A trustworthy interface needs both “notified” and “commencement basis,” not a single published-date badge.

**Date conflict:** The instrument is dated 13 November 2025, while the ministry's document listing and PIB describe publication/notification on 14 November; practitioner commentary also differs, with PwC using 13 November and Shardul Amarchand Mangaldas using 14 November as the base. These competing presentations should be shown rather than silently harmonized. [Final Gazette](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [MeitY listing](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa) [PIB explanation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190655&reg=3&lang=2) [PwC](https://www.pwc.in/assets/pdfs/news-alert/regulatory-insights/2025/pwc_india_regulatory_insights_16_november_2025_meity_notifies_digital_personal_data_protection_rules_2025.pdf) [Shardul Amarchand Mangaldas](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/)

**Product treatment:** Display the official formula as authoritative text. Label 13/14 November 2026 and 13/14 May 2027 as alternative calculations pending confirmation of the publication-date basis, rather than publishing a compliance countdown as settled legal advice.

### A general minimum-retention provision is added

**Textual finding:** Draft rule 8(3) defines “user account”; final rule 8(3) instead requires retention of “such personal data, associated traffic data and other logs of the processing” for “a minimum period of one year from the date of such processing,” for Seventh Schedule purposes. It also provides for erasure afterward unless further retention is required under another law or notified by the Government. [Draft, rule 8, p. 31](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 8(3), p. 27](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

The final illustration explicitly says an e-book platform must retain transaction-related personal data and logs for at least one year even if the individual deletes her account; a second illustration addresses a cloud processor. Practitioner analysis independently identifies the general obligation as additional to the draft. [Final, rule 8 illustrations, p. 27](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Shardul Amarchand Mangaldas](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/)

**Interpretation:** This is not merely a rewrite of the existing security-log language: draft rule 6 already contained a one-year retention requirement for its specified security purposes. Distinguish the new rule 8 duty from that retained provision. [Draft, rule 6(1)(e)](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rules 6(1)(e) and 8(3)](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Reporting lead:** How do organizations reconcile erasure workflows, the new retention floor and processor contracts? Request actual retention policies and implementation plans; the textual addition alone does not prove excess retention or an unlawful practice.

### Grievance language introduces a ninety-day limit

**Textual finding:** Draft rule 13(3) referred to publication of the organization's grievance-response period without specifying a numerical ceiling; final rule 14(3) adds “within a reasonable period not exceeding ninety days” and prominent publication language. The final sentence is awkwardly drafted, while practitioner commentary reads it as a maximum grievance-response/redressal period. [Draft, rule 13(3), pp. 34–35](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 14(3), p. 30](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Shardul Amarchand Mangaldas interpretation](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/) [PwC interpretation](https://www.pwc.in/assets/pdfs/news-alert/regulatory-insights/2025/pwc_india_regulatory_insights_16_november_2025_meity_notifies_digital_personal_data_protection_rules_2025.pdf)

**Interpretation:** The safe summary is “new ninety-day language for the grievance mechanism.” It is not a verified universal ninety-day deadline for every access, correction and erasure request.

**Reporting lead:** Ask how complaint systems will implement the period and what happens at escalation. Do not label an organization non-compliant merely because a future-commencing rule differs from its present policy.

### Algorithmic due diligence becomes broader technical-measures due diligence

**Textual finding:** Draft rule 12(3) refers to “algorithmic software deployed”; final rule 13(3) says “technical measures including algorithmic software adopted.” The annual impact-assessment and audit duties remain in the corresponding first two sub-rules. [Draft, rule 12, p. 34](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 13, p. 29](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** The textual scope extends beyond algorithmic software, but the duty is framed for Significant Data Fiduciaries, not every organization using software. It does not by itself create a public algorithm register.

**Reporting lead:** What technical measures will assessments cover, and what evidence will support the “not likely to pose a risk” verification? Obtain the relevant designation and audit methodology before applying the duty to a named entity.

### Localisation-related committee membership is specified

**Textual finding:** The draft and final both contain a government-specified-data transfer restriction for Significant Data Fiduciaries; final rule 13(5) additionally specifies committee membership, including ministry officials and optionally officials of other central ministries/departments. The December corrigendum changes “Department” to “Departments,” but does not direct a correction to the ministry name printed in the paragraph. [Draft, rule 12(4)](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 13(4)–(5), p. 29](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda, item (ii)](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf)

**Interpretation:** Describe the committee definition as new detail, not the whole transfer restriction as new. Whether particular data is restricted depends on further specifications and applicable law.

**Reporting lead:** Seek the committee constitution, recommendations and ensuing specifications. The tool should link these dependencies instead of treating a future government choice as already made.

### Children's-data exemption adds real-time location and expands protective content filtering

**Textual finding:** The final Fourth Schedule Part B adds a purpose covering determination of a child's real-time location, restricted to tracking in the interests of safety and protection or security. It also changes the detrimental-content exemption from “information” to “information, service or advertisement.” [Draft, Fourth Schedule Part B, p. 45](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, Fourth Schedule Part B, p. 37](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** These are conditional exemptions from specified section 9 obligations, not a blanket permission to collect any children's data or serve targeted advertisements. The inherited education and school-transport exemptions should not be presented as new additions. [Draft, Fourth Schedule Part A](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 12 and Fourth Schedule](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Reporting lead:** Who determines necessity and safety, and what limits are implemented in location services? Ask for use cases and controls; do not infer actual deployment from an exemption.

### Disability consent is separated and a functional condition is added

**Textual finding:** The draft combines child and disability consent in rule 10; the final creates separate rules 10 and 11. In final rule 11(2)(d)(ii), the definition adds the condition that the individual, despite adequate and appropriate support, is unable to take legally binding decisions; that condition was not in the draft's corresponding second limb. [Draft, rule 10(3)(f), pp. 33–34](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 11, pp. 28–29](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** A diagnosis is not, by this wording alone, sufficient to determine the guardian-consent position under that limb. Questions about legal capacity and guardianship require individual legal context, not automatic classification by the website.

**Reporting lead:** What procedures prevent platforms from wrongly demanding a guardian's consent? Consult disability-rights expertise and affected people before claiming the rule solves or creates a particular access barrier.

### Breach location is removed from the individual notice, not the Board notice

**Textual finding:** Draft rule 7(1)(a) includes timing and location in the description to affected individuals; the final deletes “and location” there. Final rule 7(2)(a) retains location in the notice to the Board, and the detailed Board-report clock remains seventy-two hours, subject to an allowed extension. [Draft, rule 7, pp. 30–31](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 7, p. 26](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** “Location disclosure removed” is overbroad without identifying the recipient. The tool must model the actor, recipient and sub-clause, not only highlight deleted words.

**Reporting lead:** Why do the two notice channels differ, and how will an organization explain a breach to individuals? This is a policy-design question, not proof that location must be withheld.

### State/research standards add completeness and consistency

**Textual finding:** Second Schedule clause (d) changes reasonable efforts to ensure “accuracy” into reasonable efforts to ensure “completeness, accuracy and consistency.” The schedule is referenced by state-processing rule 5 and research-exemption rule 16 in the final numbering. [Draft, Second Schedule, p. 41](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, Second Schedule, pp. 34–35](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** This is a changed quality standard, not simply a renumbered appendix. For research exemptions, the parent Act also requires that the personal data not be used to take a decision specific to a Data Principal, a restriction that a rule-only summary could miss. [DPDP Act, section 17(2)(b)](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)

**Reporting lead:** Which administrative datasets or research workflows will test completeness and consistency? Evidence about specific failures must come from separate reporting.

### Security duties receive applicability qualifiers

**Textual finding:** Final rule 6 adds “wherever applicable” to the computer-resource access-control clause and the processor-contract clause, while retaining the broader reasonable-security duty and other listed measures. It also changes some illustrative language from “including” to “such as.” [Draft, rule 6, p. 30](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 6, p. 26](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** This does not establish a blanket small-business exemption from security. Classification should be “qualification added; applicability needs assessment,” not “security protections abolished.”

**Reporting lead:** What facts determine applicability in a given architecture or contractual relationship? Ask for the organization's rationale and technical controls.

### Notice specificity and cross-border wording need nuanced treatment

**Textual finding:** Rule 3 changes “specified purpose” to “specified purpose or purposes” and the goods/services/uses description from “itemised” to “specific”; the personal-data description remains itemised. Final rule 15 recasts the draft transfer rule around data processed under the Act, while retaining the condition concerning government requirements about making data available to foreign states or controlled persons/entities. [Draft, rules 3 and 14](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rules 3 and 15](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

**Interpretation:** The notice wording merits review, but cannot safely be summarized as permission for unlimited bundled consent. Nor does rule 15 prove unrestricted foreign transfers: the parent Act preserves government restriction powers and laws imposing greater protection or transfer restrictions. [DPDP Act, section 16](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)

**Reporting lead:** Compare actual notice designs or government orders against the provisions. A word-level diff should not manufacture a categorical legal conclusion.

### Information-calling provisions are restructured

**Textual finding:** Draft rule 22 is final rule 23; its explicit sentence tying compliance to section 36 is removed, non-disclosure is placed in a separate sub-rule, and an IT Act intermediary definition is added. A corrigendum completes the phrase “given in such” as “given in such order”; the Seventh Schedule now also references the new retention rule 8(3). [Draft, rule 22 and Seventh Schedule](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 23 and Seventh Schedule](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda, item (iii)](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf)

**Interpretation:** Deletion of the cross-reference is not proof that the government loses its statutory information power; section 36 remains in the parent Act. The system should expose the deletion and statutory dependency without speculating about legal invalidity. [DPDP Act, section 36](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)

**Reporting lead:** Examine an actual order and its asserted statutory basis before assessing a specific demand. Do not publish private demands or affected identities without appropriate review.

## Full provision-coverage register

The register covers all 23 final rules and seven final schedules, including continuity and low-significance changes, so the evidence base is not limited to attractive headline examples. “No material change identified” is an analyst assessment of the reviewed English text, not a claim of character identity. [Draft Rules](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

| Final provision | Draft counterpart | Reviewed observation and classification |
|---|---|---|
| Rule 1 | Rule 1 | Blank date replaced by phased commencement; later corrigendum affects terminology. Timing change. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 2 | Rule 2 and dispersed definitions | Named definitions assembled, including user account and verifiable consent. Consolidation, not evidence that the concepts are all new. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 3 | Rule 3 | Purpose pluralization and itemised-to-specific service-description wording; data list remains itemised. Wording/scope review. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 4 | Rule 4 | Registration, obligations, inquiry and suspension/cancellation structure retained; commencement handled separately. No material body change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 5 | Rule 5 | Express section 7(b) enabling sentence removed; schedule-compliance duty retained and sub-rules rearranged. Restructure; statutory limits still need reading. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 6 | Rule 6 | Applicability qualifiers and illustrative wording added; one-year security-purpose provision retained. Qualified obligation. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 7 | Rule 7 | Location removed from individual-notice description, retained for Board; user-account definition relocated. Recipient-specific deletion plus consolidation. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 8 | Rule 8 | New general retention floor and examples; sub-rule (1) adds “or” and rearranges conditional syntax. Addition; conditional wording requires legal review. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 9 | Rule 9 | Publication of contact information and inclusion in rights responses retained. No material change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 10 | Child portion of rule 10 | Child-only rule; authorized-entity definition uses issuance instead of maintenance; examples clarify parent's identity and adulthood. Split and verification wording. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 11 | Disability portion of rule 10 | Separate rule and added inability-despite-support condition in the second definition limb. Split and scope condition. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 12 | Rule 11 | Exemption mechanism retained, while Fourth Schedule changes materially. Renumbered body; linked schedule change. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 13 | Rule 12 | Technical-measures scope broadened and committee composition specified; audit/DPIA structure retained. Broadened obligation and definition addition. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 14 | Rule 13 | Prominent publication, broader rights-request wording, ninety-day grievance language, email/mobile identifiers; some “published” particulars become “required” particulars. Several mechanics changes. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 15 | Rule 14 | Transfers rephrased around data processed under Act; foreign-state availability condition retained. Scope/wording review, not automatic liberalization. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 16 | Rule 15 | Research/archiving/statistics exemption rule substantially retained; read parent Act condition and changed standards. Continuity with dependency. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 17 | Rule 16 | Vacancy/absence/constitution protection now refers to both selection committees, rather than just sub-rule (1). Governance scope clarification. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 18 | Rule 17 | Service terms continue by reference to Fifth Schedule. No material body change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 19 | Rule 18 | Meetings, quorum, voting, ratification and inquiry periods retained. No material change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 20 | Rule 19 | Digital-office mechanism retained with grammatical rephrasing. No material change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 21 | Rule 20 | Deletes express reference to appointment “in such manner” as government may specify by general/special order; prior approval retained. Procedural wording change. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 22 | Rule 21 | Digital filing recast; explicit website-publication references for procedure/payment system removed. Procedural transparency wording change, not proof publication will cease. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Rule 23 | Rule 22 | Information-calling mechanism restructured, section 36 sentence deleted and intermediary definition added. Later order-phrase correction. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| First Schedule | First Schedule | ₹2 crore net-worth condition, registration framework and consent-manager obligations retained; print errors corrected later. No material framework change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Second Schedule | Second Schedule | Completeness and consistency added alongside accuracy. Quality-standard expansion and updated cross-references. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Third Schedule | Third Schedule | Classes, thresholds, exceptions and three-year formula retained; social-media definition switches to incorporation of 2021 IT Rules definition. Definition-source change; cell order is not substance. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Fourth Schedule | Fourth Schedule | Location purpose added; detrimental information scope extends to services/ads; clinical-establishment definition loses express armed-forces extension and incorporates statutory definition; other definition references refined. Material and definition changes. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Fifth Schedule | Fifth Schedule | Salary and service-benefit structure retained; cross-reference and minor wording changes. No material change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Sixth Schedule | Sixth Schedule | Deputation and service-term structure retained; associated rule reference updated. No material change identified. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |
| Seventh Schedule | Seventh Schedule | Adds rule 8(3) linkage; State-use entry expressly says personal data of a Data Principal; first entry specifies section 17(2)(a). Dependency and precision changes. [Draft](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) |

## Complete corrigendum register

The corrigenda is dated 10 December 2025 within a Gazette issue dated 11 December, while the ministry lists the item with a 16 December publication entry. These are distinct metadata fields, not interchangeable dates. [Official corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) [MeitY listing](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa)

| Correction | Official print locator | Printed text | Directed replacement | Treatment |
|---|---|---|---|---|
| CR-01 | p. 24, line 22 | “of this Gazette” | “in the Official Gazette” | Commencement wording. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-02 | p. 24, line 24 | “of this Gazette” | “in the Official Gazette” | Commencement wording. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-03 | p. 29, line 44 | “Department” | “Departments” | Committee terminology. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-04 | p. 32, line 4 | “given in such” | “given in such order” | Completes information-order phrase. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-05 | p. 34, line 1 | “everybody” | “every body” | Fixes corporate-ownership disclosure wording. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-06 | p. 34, line 26 | “(18 or 2013)” | “(18 of 2013)” | Corrects statutory citation at the specified locator only. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-07 | p. 38, line 2 | “.” | “;” | Punctuation in definition note. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |
| CR-08 | p. 38, lines 1–15 | “(a) to (f)” | “(a) to (g)” | Relabels seven definition-note items; not a licence for global replacement. [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf) |

The product should preserve a three-way chain: draft, final as printed, final as corrected. It should never “repair” other perceived typos silently merely because one nearby typo has an official correction.

## Metadata discrepancies and evidence gaps

### Consultation totals differ across official explanations

The PIB explainer says 6,915 inputs were received; the ministry's status summary says 6,951 comments and submissions were processed through MyGov and also describes other consultation channels. The sources do not establish why these totals differ. [PIB explanation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190655&reg=3&lang=2) [MeitY status summary](https://www.meity.gov.in/static/uploads/2026/01/a49c50414777afc2af0b8d59dafacd60.pdf)

This is a potential clarification question, not evidence of dishonesty or a new scoop. A source-backed briefing should either omit the disputed count or quote each with its attribution and scope.

### Consultation summaries are not amendments

The ministry summary lists requests for changes, including automated-decision explanations, human intervention and more detailed notices. Those entries describe feedback, not duties enacted merely by their inclusion in the document. [MeitY status summary](https://www.meity.gov.in/static/uploads/2026/01/a49c50414777afc2af0b8d59dafacd60.pdf)

A policy timeline must distinguish a stakeholder request, an official consultation summary, a draft clause, a final rule, a correcting instrument and a commencement instrument. Treating all as equivalent “policy updates” is a foreseeable misinformation failure.

### Current court status is not certified here

A current independent timeline reports constitutional litigation and describes later implementation dates as computed interpretations; it also discusses a reported proposal to alter rollout timing while noting that it had not located an amending instrument. That record is useful as a lead, but this study did not obtain a complete current primary court-order chain. [Independent DPDP timeline](https://dpdprules.org/timeline)

No assertion is made here that every later court order, amendment, designation or exemption has been ruled out. Any live compliance conclusion or publication concerning litigation should refresh those primary instruments before release.

### Text extraction is not original-document archiving

The research pipeline stores extracted text and comparison records, not a verified immutable binary archive of the PDFs. No PDF-byte hash or visual page-verification claim is made for this study.

The machine diff exposed a table-reading-order problem in the Third Schedule. A production parser must retain cell coordinates and row structure; it cannot count flattened-text differences as an exhaustive legal redline.

## A newsroom-ready worked brief

### Suggested working headline

“Final data-protection rules add a retention floor and change grievance and technical-risk provisions.” This is a drafting suggestion, not an exclusive discovery; practitioner analyses have already discussed important parts of the change. [Shardul Amarchand Mangaldas](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/)

### Publishable factual core

Compared with the January draft, final rule 8 adds a general minimum one-year retention provision for personal data, associated traffic data and processing logs for specified purposes, with illustrations addressing deleted accounts and processors. [Draft, rule 8](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final, rule 8(3)](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

The final text adds ninety-day grievance language, broadens Significant Data Fiduciary due diligence to technical measures including algorithmic software, and adds a conditional real-time child-location exemption. [Final, rules 13(3), 14(3) and Fourth Schedule](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf)

The Rules specify staged commencement rather than bringing all substantive provisions into effect together; a December corrigendum corrects eight passages of the English print. [Final, rule 1](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf)

### Questions to pursue before publication

- **Government:** Confirm the publication-date basis for calculated commencement dates and explain the different consultation-input counts.
- **Privacy/technical experts:** Explain the interaction of purpose limitation, the retention floor and security-log requirements.
- **Organizations and processors:** Supply implementation plans, deletion exceptions and contractual allocation of retention responsibility.
- **Disability-rights specialists:** Assess how consent workflows should respect the added functional condition and supported decision-making.
- **Children's-rights specialists:** Explain safeguards necessary to apply safety/location exemptions proportionately.
- **Affected people:** Describe actual experiences, with informed consent and protection of identity where necessary.

These questions have not been sent, and no interview findings are claimed. The brief is a source-backed desk-research product awaiting reporting and editorial review, not a finished investigative article.

## Alternatives and differentiation

This is a bounded adjacent/substitute assessment, not an exhaustive market census or a hands-on performance ranking. Published capabilities were checked on each product's own page; undocumented capabilities are unknown rather than absent.

| Alternative | Verified capability | Implication for AI Watch India |
|---|---|---|
| PolicyDhara | Open-source Indian development-policy tracking covering consultation drafts, parliamentary material and enacted instruments, with research/news separated. [PolicyDhara](https://varnasr.github.io/PolicyDhara/) | Do not sell a policy-feed dashboard as novel; specialize in reviewed comparison-to-brief tasks. |
| dpdprules.org | Source-linked DPDP reference with all rules/schedules, corrected/original wording and explained commencement status. [Rules reference](https://dpdprules.org/rules) | A DPDP explainer or date-status page alone is insufficient differentiation; build across document families and comparative work. |
| Draftable Compare | Side-by-side/redline comparison, moved-text detection, OCR, notes/tags and multiple exports are advertised. [Draftable](https://www.draftable.com/draftable-legal-compare) | Notes, exports and moved-text detection are table stakes, not exclusive innovations. |
| Diffchecker | Document comparison includes rich/plain/image views, OCR, moved-content detection and exports; its page describes browser PDF comparison and offline desktop options. [Diffchecker](https://www.diffchecker.com/word-pdf-compare/) | Privacy-preserving comparison is also an existing capability; policy context must supply additional value. |
| Ruleguard | Policy lifecycle management includes versions, approval, distribution, acknowledgement, reviews and regulatory mapping. [Ruleguard](https://www.ruleguard.com/solutions/policy-and-document-management-software) | Do not compete initially with enterprise policy administration; focus on public-policy analysis and reporting. |
| Analyst plus spreadsheet | A practical substitute proposed for validation: a person assembles links, changes and notes manually. | Compare actual task accuracy and time against this baseline, not only against doing nothing. |

The proposed differentiator is the combination of **official document lineage, clause-aware comparisons, commencement/dependency context, explicit uncertainty, and reviewed reporting/decision outputs** in an accessible Indian digital-policy workspace. That combination is a product hypothesis, not a verified market gap or proof that competitors cannot provide it.

## Contribution and feasibility

### What would constitute a contribution

- **Practical contribution:** A journalist or policy researcher completes an accurate evidence-backed brief faster, with fewer missed qualifications.
- **Public-interest contribution:** Curated change records remain inspectable, correctable and reusable without requiring trust in a generated paragraph.
- **Research contribution:** A reviewed dataset of version mappings, difficult changes, table cases and correction chains enables reproducible evaluation.
- **Governance contribution:** Changes to actors, duties, exceptions and implementation stages are made visible without inventing causal effects or compliance findings.

Public benefit depends on actual use and maintenance, not on the number of scraped documents. A smaller reliable collection would be preferable to a broad unreviewed feed.

### What makes implementation tractable

The first release can work without a language-model API: curated official documents, deterministic extraction and diffing, human-reviewed classifications, filterable case pages and structured exports. Optional AI can assist candidate alignment and phrasing, but must not manufacture quotes or decide publication.

The hard parts are document structure, version relationships, amended/corrected text, trustworthy editorial review and source maintenance. These need explicit product states and tests rather than a chatbot covering over failures.

### What is not yet established

No target-user interviews or usability tests were conducted. No claim is made about saved minutes, conversion, repeat use, willingness to pay or broad newsroom demand.

No production ingestion service, public website or repository commit was created during this research scope. The companion specification defines what should be built and how to decide whether it is genuinely better.

## Build recommendation and decision gates

Build one complete workflow around the DPDP document family first: open the policy family, choose versions, inspect corrected and original text, review every provision, select changes, and export a source-backed brief. Keep it usable without AI generation and make unreviewed material visibly distinct from approved analysis.

Before calling the product validated, run a small counterbalanced comparison against manual reading and at least one existing comparison tool. Proposed gates are at least 90% accuracy on predefined factual tasks, no high-severity unsupported assertion in final briefs, a median task-time improvement of at least 25% against measured baseline, and observable voluntary repeat use by multiple participants; these are targets, not results.

Proceed if the complete workflow helps people do the task better and the source/review burden is maintainable. Narrow or stop if it merely reproduces existing summaries, fails on document structure, or requires more editorial work than the intended users can sustain.

The conclusion is conditional but concrete: this can become a relevant journalism and policy tool if source lineage, review discipline and task performance are its core product. A news aggregator, a generic PDF chatbot or a “risk score” dashboard would not deliver the same contribution.
