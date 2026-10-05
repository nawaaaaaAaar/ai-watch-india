# AI Watch: 144-family release verification

Release 1.3.0, documentary cutoff 5 October 2026. This release doubles the preserved 72-record registry to 144 named institution-linked system/service families. It does not claim 144 independently verified live AI deployments, a national census, representative prevalence or independent duplicate coding.

The research and application implementation is [commit b416be27387f1061620fda5ef569aaefde79a2dc](https://github.com/nawaaaaaAaar/ai-watch-india/commit/b416be27387f1061620fda5ef569aaefde79a2dc). Read the [complete scaling study](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/SCALING_STUDY.md), [protocol](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/PROTOCOL.md) and [codebook](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/CODEBOOK.md) before pooling observations.

## Final inventory

| Linked table | Rows |
|---|---:|
| systems | 144 |
| institutions | 133 |
| system_institutions | 168 |
| system_links | 5 |
| deployments | 131 |
| procurements | 7 |
| evaluations | 9 |
| metrics | 23 |
| controls | 22 |
| policies | 5 |
| system_policy_links | 5 |
| assertions | 1,728 |
| evidence | 410 |
| evidence_links | 2,412 |
| sources | 197 |
| issues | 40 |
| candidate_decisions | 191 |
| institution_coverage | 6 |
| coverage_systems | 26 |
| source_rechecks | 50 |
| assertion_rechecks | 216 |

Institution rows are source-stated labels, not independently certified legal owners. There are 197 source records but 196 unique original URLs. A source used in a different research round can have a separate version-specific record; this distinction is not hidden in the count.

All twelve accountability slots are retained for each family. The 1,728 classifications comprise 305 Documented, 686 Partial, 734 Not verified and three Conflicting sources. These classify documentary support, not institutional safety or completeness. Unknowns mean unestablished in this reviewed corpus, not proof that a safeguard or record does not exist.

The four cohorts contain 18, 18, 36 and 72 records. The original fixed six-institution frame remains associated with 26 records; 118 are outside it. The AI-qualification register distinguishes 129 explicit source attributions, 14 qualified algorithmic/biometric contexts and one AI-evaluation infrastructure record. Explicit attribution can come from a developer or journalist; it does not certify the actual model.

## Research controls

The expansion records 591 queries, 2,511 returned search leads and zero query errors. It retains 228 retrieval receipts, including 41 explicit failed receipts. These count attempts, not necessarily unique URLs, and nominally successful banner-only or incomplete extracts are separately annotated. Cached recovery and default cache-enabled extraction are distinguished from fresh retrieval requests.

All 78 selected new source records have bounded quotations checked for normalised membership in fetched full text. Selections are capped at 250 words per original URL across earlier and newly used versions. Source dates use documentary body dates where established; publisher metadata is labelled and undated pages are not assigned invented dates. Complete scraped pages, copyrighted articles and original PDF binaries are not redistributed in the registry.

Every prior row value in all 21 tables is frozen in `BASELINE_1_2_0.json` and checked by recursive canonical hashing. New cohorts, source records and relationships are additions rather than silent revisions of the previous release. Historical exclusion decisions remain as historical decisions when this broader cohort explicitly includes a different kind of infrastructure.

## Substantive checks beyond row counts

- **MuleHunter**: developer documentation supports a bank-local processing boundary and a specific no-bank-to-RBIH-PII statement; separate I4C collaboration reporting is not erased to make a blanket no-data-sharing claim. The source type is developer technical documentation, not independent reporting. ([RBIH documentation](https://docs.rbihub.in/mule-hunter), [I4C collaboration report](https://government.economictimes.indiatimes.com/news/secure-india/i4c-and-rbih-join-forces-to-combat-cyber-fraud-with-ai-technology/131059334))
- **Poshan authentication**: 97.01% administrative eKYC/facematching completion is not face-recognition accuracy or proof of ration receipt; device-cache clearing is not complete server-retention evidence. ([Government record](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2247561&reg=3&lang=1))
- **Adalat AI**: the Andhra Pradesh order's 1 October mandate, recorded-reason exception and technical fallback are preserved; a mandate is not independently observed courtroom coverage. ([High Court order](https://aphc.gov.in/docs/notification_1785225296_0.pdf))
- **CAG PARAS**: officer final sanction, five-year retention and legal-hold requirements remain requirements in an EOI, not demonstrated awarded-contract controls. ([CAG EOI](https://cag.gov.in/uploads/tenders/tenders-EOI-for-Establishment-of-Sovereign-AI-Platform-for-CAG-of-India-069fb031304a1b8-89068885.pdf))
- **Shiksha Copilot**: the 1,043-teacher and 23-curator study is coded as partner research reviewed at abstract level, not an independent causal evaluation of student achievement. ([Study abstract](https://www.microsoft.com/en-us/research/publication/teacher-ai-collaboration-for-curating-and-customizing-lesson-plans-in-low-resource-schools/))
- **Family identity**: channels, model variants, modules, junctions and installations do not inflate family counts; distinct same-name institutional tools are disambiguated. Odisha's named i3MS dispatch workflow is not relabelled as an independently verified OMPTS product merely because that regulatory terminology appears nearby. ([Odisha presentation](https://mines.gov.in/admin/storage/ckeditor/Odisha_1767944755.pdf))

## Automated and clean-checkout verification

All 152 automated tests passed, comprising the prior 133 tests and 19 scaling tests. These cover linked-table integrity, field completeness, baseline preservation, new-family uniqueness and qualifications, source/quotation boundaries, semantic distinctions, cohort filtering, package contents and the earlier policy corpus.

A fresh clone at the implementation commit ran `npm ci`, `npm run package:registry`, `npm test` and `npm run build` successfully. Dependency installation reported zero vulnerabilities; the deterministic rebuild left no repository changes. The clean clone reproduced all three final hashes below.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| complete-registry.zip | 1,961,066 | `7b3c4c5af158f4570863f0db8f7f48b63008718e0f26151932340abbc069a26a` |
| dataset.sqlite | 1,617,920 | `77d317a8065c16f7f38636cbd470957819f0948dd83bc0e31feb8e7e07c8b30d` |
| data.json | 1,990,596 | `59b93500019144ce28db5228b5144a39f83bcd4448034c5de538b322bcea3a81` |

The ZIP contains 386 payload files, plus its manifest and manifest checksum: 388 entries. It includes all 144 dossiers, every linked table, structured JSON, SQLite, runnable SQL, selected snapshots, methods, studies and research logs. The earlier policy corpus remains separate rather than being double-counted as new deployment records. Verification reports and browser receipts are intentionally outside the archive to avoid self-referential checksums.

The TypeScript/Vite production build passed. Vite continues to warn about a large JavaScript chunk, approximately 1,611.63 kB minified and 334.10 kB gzip; this existing performance limitation has not been represented as solved.

## Browser and hosted verification

The local receipt records 398 distinct passing checks and 38 distinct byte-compared registry downloads. All 144 dossier routes were checked for correct titles and twelve accountability fields. Cohort counts, original-frame boundaries, search, sort, empty results, reset, filtered CSV, unknown routes, evidence expansion, source URLs and retrieval qualifications were exercised.

All 21 linked-table CSVs were exercised on the release candidate. Following final metadata/control edits, the archive, SQLite, JSON, study, quote audit, manifests and core system/relationship tables were downloaded again. The final changed sources, assertions, controls, evidence and evidence-link tables were additionally byte-compared from the deployed preview.

Local checks also exercised dataset-load failure/retry, rejected HTML download fallbacks, successful retry, and earlier policy notebook save/Markdown/CSV/JSON exports. Desktop and 375-pixel mobile light/dark states, dossier navigation, expanded evidence and data-room layouts were checked. Page-wide horizontal overflow was absent; scoped table/navigation scrolling remains intentional. No page errors were recorded.

There was intermittent headless-browser download-event stalling in a long automated batch, including one later keyboard batch. Individual and keyboard retries succeeded; actual saved bytes, rather than just HTTP status or download filenames, were compared. The root cause of the harness event issue is not established, so the report does not claim a flawless first-pass batch.

The existing owned private preview was updated in place. Hosted QA records 33 passing checks and 11 actual downloaded files. The ZIP, SQLite and JSON matched the clean-checkout hashes; the study, quote audit and six linked-table CSVs also matched repository bytes. Eight new dossiers were checked for identity and twelve fields; developer provenance, cached retrieval basis, cohort/frame filters, empty and unknown states, desktop/mobile fit and mobile expanded evidence were inspected. No hosted page errors were recorded.

Machine-readable receipts are [local QA](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/QA_SCALING_LOCAL.json) and [hosted QA](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/QA_SCALING_HOST.json). An initially incorrect harness expectation for the unknown-state wording was corrected after inspecting the actual state; no application change was required for that assertion.

## Boundaries and next quality step

This completes the requested second doubling within the defined exploratory registry. It does not make the selection exhaustive nationally, the coding independently reviewed, the missing contracts accessible, or the source claims operationally true. Proposed, historical, internal, enabling and qualified contexts must be filtered appropriately for each research question.

No public website launch, paid services or external enquiries were undertaken. The next quality step should be independent recoding against the source pack, with disagreement adjudication and explicit inclusion criteria, rather than assuming that further growth or automated checks establish research validity.
