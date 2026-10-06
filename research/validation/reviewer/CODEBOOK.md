# Independent-review coding rules

Schema v1.0.0. This rubric is frozen for the second pass but was operationalised after the original dataset release; it was not preregistered before the first analyst's research. If a definition is defective, record the defect and a proposed alternative rather than changing the schema mid-pass.

## Nominal variables

- **dimension**: choose the primary documentary subject: Procurement; Contracts and awards; Funding; Supplier; Implementation; Evaluation; Human oversight; Redress; Data safeguards; Operational status. Multiple subjects may coexist; record secondary subjects in notes. Do not equate primary-dimension allocation with exclusive relevance.
- **claim_type**: Procurement invitation; Requirement / specification; Official reported activity; Official reported outcome; Implementer account of award / agreement; Embedded supplier claim; General institutional route; Other / mixed; Not established. Classify the source's speech act, not whether you believe it is true. An invitation is not an award; an account of an agreement is not the original agreement.
- **evidence_strength**: Formal prescribed requirement; Procurement-stage invitation; First-party reported activity or outcome; Implementer's historical account; Institutional contextual evidence; Other / mixed; Not established. These are source/stage categories, not an ordinal quality score. Hosting, issuer identity and clause function can differ; explain mixed roles rather than assuming institutional hosting makes every embedded statement official.
- **current_version_match**: Document-specific; no wider version or coverage inference; Not established; Current deployed version established; Different version established; Unclear. The first category confines the statement to its document; it does not assert a match to a current installation. The taxonomy combines version and scope, so record which construct drove your choice and propose a split if needed.
- **independent_outcome_verified**: Established; Not established. “Established” requires evidence in the reviewed material that the named version's outcome was independently verified, with attribution and evaluation context. “Not established” is not a claim that no independent study exists elsewhere.
- **date_precision**: Day; Month; Year; Interval / other; Not established. This applies to the document date, not the date of an embedded event.
- **document_association_scope**: Named-system or component evidence; Institutional/platform context; Association not defensible; Unclear. A named family/component link does not establish continuity across all versions or deployments. General agency documents may be contextual only; reject a proposed pairing if the text does not support it.
- **coverage_presence**: Relevant evidence in reviewed corpus; Not established in reviewed corpus; Unclear. Count requirements, accounts and context where relevant, while noting their limits. This is evidence availability, not a yes/no safeguard, implementation or effectiveness finding. Cases can have multiple relevant dimensions per passage.
- **governance_link_type**: Common original primary document; Inherited, expressly qualified governance association; Association not defensible; Unclear. The second category means defensible jurisdiction/domain or conditional relevance; it does not require accepting an earlier association. Describe your own scope basis in notes.
- **compliance_verified**: Established; Not established. A policy direction, recommendation or common URL alone is insufficient to establish implementation or compliance.

## Dates, financial stages and qualitative reconstruction

**event_date** and **document_date**: code the date relevant to this task, with “Unknown” when a sufficient review does not establish it. Preserve day/month/year precision and stated intervals; explain planned versus completed events and publication versus effective dates. Exact-string agreement tests formatting/selection consistency, not legal or temporal validity.

**amount_text**: independently transcribe relevant source monetary text without merging prices, securities, sanctions, payments, taxes or different scopes. If several amounts matter, preserve the distinction in notes. Exact-string comparison is diagnostic only: equivalent differently formatted amounts require adjudication.

**finance_stage**: JSON array drawn from Estimate; Bid security; Authorised cost / sanction; Reported cost / price; Payment arrangement; Verified expenditure; Not established. Multiple stages are permitted. “Not established” cannot be combined with another label. A payment schedule is not disbursement, a sanction is not spending, and an implementer-stated price is not an inspected original executed contract.

**unit notes**: independently reconstruct the statement and its limits; identify parties, their roles, identity uncertainty, human authority and any general versus AI-specific remedy. These are free-text findings, not automatically scored categories. Explain insufficient excerpts, cross-source contradictions and alternative dimension allocations. Nominate missing evidence or new passages for the same ten cases.

## Shared decision discipline

Do not infer absence from an omitted excerpt, procurement from deployment publicity, effectiveness from a target, legal obligations from a guideline, or a supplier award from an invitation or launch attendance. Conversely, do not suppress positive evidence merely because it is an account: record its stage and attribution. No category should be chosen to agree with presumed earlier findings.

Complete a few fictional practice examples with the coordinator if needed, using material unrelated to these ten cases. Any training or discussion must be disclosed; practice examples are excluded from agreement. Do not view or discuss real-unit disagreements until your pass is frozen.
