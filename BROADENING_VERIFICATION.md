# AI Watch: seventy-two-system release verification

Release 1.2.0, 5 October 2026. The requested doubling is complete: 36 additional named system/service families bring the registry from 36 to 72. This report records research scope, preservation, reproducibility and application checks; it does not certify institutional effectiveness, legal compliance or national completeness.

## Release and evidence inventory

The implementation is recorded in [the release commit](https://github.com/nawaaaaaAaar/ai-watch-india/commit/dcb54e3bc7a3b48c100b40b02fb549224a146538). The complete source-linked findings and all thirty-six additions are in [the broadening study](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/BROADENING_STUDY.md).

| Linked table | Records |
|---|---:|
| systems | 72 |
| institutions | 76 |
| system_institutions | 93 |
| system_links | 4 |
| deployments | 59 |
| procurements | 5 |
| evaluations | 8 |
| metrics | 20 |
| controls | 14 |
| policies | 2 |
| system_policy_links | 2 |
| assertions | 864 |
| evidence | 302 |
| evidence_links | 1,561 |
| sources | 119 |
| issues | 29 |
| candidate_decisions | 102 |
| institution_coverage | 6 |
| coverage_systems | 26 |
| source_rechecks | 50 |
| assertion_rechecks | 216 |

Institution rows are source-stated institution labels, not an independently resolved legal-entity register. Deployment rows are documentary observations, including plans and historical statements, not 59 certified operational deployments. Sparse procurement, evaluation and control tables contain established observations only; the twelve-field assertions table retains unknowns for every system.

All 864 accountability slots remain present: 161 are coded Documented, 369 Partial, 331 Not verified and three Conflicting sources. “Documented” means that the statement has documentary support, not independent validation of what the institution claims. AI attribution is also qualified: 61 records have explicit source attribution, ten are algorithmic/biometric context with unestablished model-specific AI attribution, and one is evaluation infrastructure.

## Research completion and quality checks

- **Discovery and retrieval**: The new round records 153 queries, 693 returned discovery leads and 100 retrieval receipts, including three failures. Forty-nine new used sources support coding; a retrieved page is not automatically a used source, and a search snippet is not coded evidence. See [search receipts](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/BROADENING_SEARCH.json) and [retrieval receipts](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/BROADENING_RETRIEVAL.json).
- **Excerpt checks**: Every selected passage from the 49 used new sources was checked against its retrieved text. Each new source remains within the 250-unique-word selection budget; hashes identify the retrieved text used for checking and the separately published selected snapshots. This is text-membership checking and single-analyst interpretation, not an authenticity audit or independent semantic recoding. See [the quote audit](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/BROADENING_QUOTE_AUDIT.json).
- **Preservation**: A regression test projects every earlier row onto its earlier columns and compares its canonical checksum with the frozen 1.1.0 baseline. All earlier table rows and values survive; the new research-round column adds cohort information without rewriting their findings. Earlier policy collections retain their different units and are not added to the system count. See [the preservation baseline](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/BASELINE_1_1_0.json).
- **Cohorts and duplicates**: The original 18 records, the 18 institutional additions and the 36 broadening additions are separately identified. The original six-institution frame still associates 26 records; it is not reused as a representative denominator for the new sectors and states. Legacy Trinetra/YAKSH, regional iRASTE deployments and internal MahaVISTAAR channels are not extra systems. Generic DAKSH and K-SMART umbrella claims remain deferred. See [the protocol](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/PROTOCOL.md).
- **Interpretation checks**: Tests preserve the distinction between Delhi's approved estimated cost and spending/award, Safe Kerala's processing suspension and cameras being off, iOncology's historical benchmark and clinical validation, iRASTE's observational outcome and causality, and tender quality requirements and demonstrated compliance. NUWR's developer is not borrowed from an adjacent catalogue project; Rajasthan silicosis workflow rhetoric is not invented diagnostic accuracy. See [the broadening regression tests](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/tests/broadening.test.mjs).

The original fifty-source recheck and 216 assertion triages retain their earlier scope. They are not fresh checks of every one of the current 119 sources. No second researcher has independently recoded the release, and no inter-rater agreement is claimed.

## Automated and browser verification

All 133 automated tests pass in both the working repository and a clean checkout. The clean checkout ran `npm ci`, `npm run package:registry`, `npm test` and `npm run build`; rebuilding left no tracked changes and reproduced the same archive, database and complete JSON.

The local production bundle passed 343 recorded browser assertions. These include all 72 dossier titles and their twelve fields, every sector/stage/attribution option, six original-frame options, the 46 outside-frame records, combined filters, search/reset/sorting, all 21 table download controls, the full package and principal research downloads, source snapshots, dossier exports and a filtered CSV with cohort identifiers. Supporting policy routes and notebook selection/Markdown export remain functional. See [local browser receipts](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/QA_BROADENING_LOCAL.json).

Off-happy-path checks covered dataset-fetch failure and retry, unknown identifiers, empty search results and HTML fallback rejected rather than downloaded as SQLite. No unexpected JavaScript page errors were recorded. Desktop and mobile explorer, data room and a long-heading/expanded-evidence dossier were inspected; light and dark themes were inspected, and mobile views did not overflow the document width. The wide table and navigation retain their intentionally scoped scrolling.

The updated private hosted preview passed 34 additional assertions. Actual browser-downloaded ZIP, SQLite, JSON, latest study/logs/audit, selected table files and a full dossier matched their local bytes; key new dossiers retained all twelve dimensions and evidence expansion worked. Hosted search, frame filtering and mobile width were checked, with no unexpected page errors. See [hosted browser receipts](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/QA_BROADENING_HOST.json).

During test development, nested-object canonicalisation and some browser expectations were corrected rather than changing preserved data to satisfy an incorrect test. An unpaced download burst hit browser download throttling; the SQL download and remaining controls were rechecked individually/with pacing. These receipts establish successful application checks, not independent research review.

## Complete package and integrity

The research ZIP contains 231 checksummed payload files plus its manifest and manifest checksum, 233 files in total. It includes all 72 dossiers, 21 CSV tables, JSON, SQLite, schema, runnable SQL, selected source snapshots, methods, all rounds' research logs, quote audit and the preservation baseline. Verification/browser reports remain in the repository outside the research package to avoid recursive package hashes.

The following SHA-256 values matched the working build, clean-checkout build and actual hosted browser downloads:

| File | SHA-256 |
|---|---|
| complete-registry.zip | `365d8e367f4425f9ebfa79af3f9dfbcd9f3382d664ddb82d377ee8aabf3fc4c8` |
| dataset.sqlite | `e856fbc0279740a83c594214f6734ba93de7a977c57496b0bde891f5587d7a95` |
| data.json | `26ff1bc7bcc1600adc994eabba9fc3cba94a8a3d77123c560b0884eea0450c6c` |

Checksums establish byte identity, not original-source authenticity or the truth of reported outcomes. Full copyrighted articles, original PDF binaries and citizen-level data are not mirrored; original URLs remain attached to the selected excerpts.

## Remaining boundaries

This is the complete defined 72-record exploratory release, not every Indian AI system or every administrative record. Selection remains purposive and single-analyst; many contracts, model versions, retention policies, independent error-rate studies and appeal outcomes remain unestablished. A second researcher and user-demand validation are still needed before claiming a validated research resource.

The production build passes TypeScript and Vite, but Vite still warns about the large bundled supporting-policy code chunk, approximately 1.61 MB minified and 334 KB gzip. No formal performance/accessibility audit or production service-level guarantee is claimed. No public website launch, paid infrastructure, external institutional enquiries or outreach occurred.
