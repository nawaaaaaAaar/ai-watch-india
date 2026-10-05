# AI Watch: institution-and-system research protocol

Version 1.0.0; documentary review cutoff 5 October 2026. This is an exploratory India dataset with 18 purposively selected named systems/services, not a census or probability sample.

## Research question

When institutions describe using AI or an adjacent algorithmic system in an Indian public-service workflow, what documentary evidence can a reader inspect about its role, deployment, suppliers, evaluation, human oversight and redress? The unit is a named service/system linked to institutions, not a policy provision, model, individual citizen, every installation or every inference. BHASHINI is one service with deployment observations, not 800 invented system rows.

The website is an interface to this dataset. Earlier policy comparisons, implementation checkpoints and six case files remain separate supporting collections; they are not pooled into a single statistical denominator.

## Selection and boundaries

- **Inclusion**: an identifiable institution/service and an India public-service role, with inspectable documentary evidence and explicit AI attribution or a clearly qualified biometric/analytics context.
- **Historical evidence**: retained with its date and stage. A historical rollout, pilot or experimental description is not certified as operational in October 2026.
- **Qualified attribution**: biometric identity workflows and analytics platforms are not automatically called model-specific AI. The `ai_class` and `ai_basis` fields keep these cases visible but separately filterable.
- **Exclusions/context**: training repositories, model announcements without a reviewed named public-service deployment, unrelated prototypes, foreign evaluations and existing casebooks are documented in `candidate_decisions`. This register is a record of decisions in this research round, not every candidate in India.
- **Sampling limitation**: this seed extends six previously researched cases with twelve additional cases selected to probe contrasting evidence types and public functions. Sector, language, geography, search visibility and government-hosting biases are substantial. An absence in this dataset does not imply no AI use.

## Search and retrieval

Three rounds cover discovery, component-specific follow-up and recency: 62 queries and 312 returned discovery hits, recorded with URLs and query text in `search-log.json`. Queries sought official deployment descriptions, parliamentary answers, tenders, agreements, terms, studies, current updates and redress evidence. Hits are discovery leads, not coded facts. Search result counts measure retrieval, not comprehensiveness.

Selected pages/PDFs were fetched and read. `retrieval-log.json` records successes and failures, including unaccepted SDK date metadata. The live IRCTC annual-report library was checked in a cloud browser when the cleaned SDK index was stale; the listed 2025–26 PDF could not be retrieved and was not treated as read. A Telangana training-PDF browser fallback returned 404. Those gaps remain explicit.

The six inherited case files retain their earlier reviewed excerpts and original URLs, converted into the same assertion structure. Their prior search history remains in the earlier repository studies, rather than being retroactively claimed as part of these 62 searches.

## Source and date hierarchy

Prefer source-stated dates and document headers over search/SDK metadata. Use null for undated or uncertain publication, distinguish a report date from an event date, and retain month/year precision instead of inventing a day. The historical PLCS publisher date is metadata-based and explicitly flagged as not visible in the extracted body; the IRCTC report date is its exchange filing, not current operation. A source published in 2026 can report an event in 2021. `latest_record_date` is derived from the dated sources linked to the system's assertions/observations, not last successful operation, a live-monitor timestamp or necessarily the date of a deployment.

Parliamentary/agency statements are official documentary evidence, not independent verification of performance. A government-hosted editorial or vendor submission retains that source type. A tender is a requirement, not an award; a signed-contract announcement is not a reviewed executed agreement; an allocation is not spending. Model-specific studies require identity, version, setting and comparator scrutiny before results are applied to another deployment.

## Coding procedure

Every system has all twelve accountability assertions, including explicit unknowns. Each non-empty evidence assertion links many-to-many to exact selected excerpts and their sources. Institution names are source-stated labels, not registry-certified identities. Sector and selection are analyst classifications; responsibility does not imply statutory ownership.

- **Documented**: the reviewed source supports the narrowly written documentary statement.
- **Partial**: related evidence exists but important scope, date, enforcement, version or completeness remains unresolved.
- **Not verified**: the searched/reviewed corpus did not establish the requested detail; not proof that the record, safeguard or remedy does not exist.
- **Conflicting sources**: reviewed descriptions diverge and have not been reconciled. Chronological differences are not automatically conflicts.

Observations preserve type-specific qualifiers. Metrics carry unit, denominator/context, metric kind and numeric qualifier. No safety, readiness, transparency or compliance score is calculated. Coverage labels describe coding/evidence state only.

Selected new excerpts were checked for normalized-text membership against the fetched originals; unique published selections are limited to 250 words per new source. The six inherited cases reuse earlier excerpts. Full papers, PDFs, personal records, complaint data and model outputs are not mirrored.

## Quality controls and reproducibility

The offline builder checks all system/institution/source relationships and generic evidence links, all 216 assertion slots, stable identifiers, SQLite integrity and foreign keys. The package includes JSON, seventeen CSV tables, SQLite, schema, dossiers, queries, selected source snapshots, research receipts and checksums. Rebuilding validates consistency of curated inputs; it does not independently establish the truth of institutional claims.

The release is single-analyst coded. There has been no independent duplicate review, inter-rater reliability measurement, participant interview, live operational inspection, FOI/RTI response collection or user-demand validation. No request was submitted, no purchase/booking made and no personal test data supplied to a service.

## Analysis rules

Descriptive totals refer only to this corpus. Do not infer national prevalence, comparative institutional safety, discriminatory effects, error incidence or causality from disclosure gaps. Separate usage from quality, specifications from results, historical evidence from current assurance, and clinical workflow attrition from diagnostic accuracy. Report contradictions and failed retrieval rather than dropping inconvenient material.

## Updating and corrections

Preserve stable system IDs, add dated observations and sources rather than overwrite history, and record reasoned corrections through versioned repository changes. Re-run offline tests and package checks after edits. A future expansion should use an explicit institution/geographic sampling frame and independent second review before claiming systematic nationwide findings. Contact routes in sources are research evidence, not an invitation to submit unreviewed enquiries automatically.

## Related work and contribution boundary

IndiaAI already publishes [six AI Impact Casebooks](https://impact.indiaai.gov.in/events/released-compendium), and the [DCI Social Protection AI Hub](https://socialprotectionai.org/use-case/IND-001/print) already documents Kisan e-Mitra. This project does not claim to invent deployment tracking or discover every listed system.

The intended contribution is reusable, source-linked coding with distinct observation types and temporal limits. Its empirical usefulness is still to be tested by independent researchers: can they reproduce a finding, join the tables and identify a genuinely consequential evidence gap more efficiently? A larger corpus alone would not answer that question.
