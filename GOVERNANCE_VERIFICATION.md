# AI Watch: linked governance research release verification

Research cutoff 5 October 2026; governance layer v1.0.0, existing system registry v1.3.0. The implementation is in [commit 46ad586](https://github.com/nawaaaaaAaar/ai-watch-india/commit/46ad58618da73e2a4e2b9c7697e4b7a4124abdd5). This cycle adds a research-data layer and only the navigation, evidence views and download controls needed to expose it; it adds no systems and does not launch a public website.

## Inventory and preservation

- **Instrument records**: 52 document/version records, grouped into 44 curated families. There are 37 central/national or independent-judiciary records and 15 subnational documents from 14 state/union-territory jurisdictions.
- **Complete coding**: 260 slots, exactly five per instrument: oversight, evaluation, procurement, redress, accountability/data. Unknown and contextual slots remain present; these are not 260 established safeguards.
- **Provenance**: 56 official source records, 289 bounded selected excerpts, 56 instrument-source associations and 14 directed instrument/version relationships.
- **Deployment links**: 95 typed associations connecting 26 instruments to 54 existing systems, with policy evidence and registry assertion/source anchors. Twenty-six instruments remain without an included defensible system association. Link strength and scope limits are retained rather than force-linking them.
- **Coverage and decisions**: All 37 jurisdictions screened, 320 domain rows and 13 selected candidate decisions. There are 157 search receipts/948 hits and 136 retrieval/recovery receipts, including failures and OCR provenance.
- **Unchanged registry**: All 144 existing system families, all 1,728 accountability assertions and every one of the 389 original public/registry files are byte-preserved. The 144 system_keys rows are a projection for joins, not new systems. Original registry ZIP, JSON and SQLite hashes are unchanged.
- **Exports**: Eleven CSV tables, lossless structured JSON, SQLite with foreign keys, schema SQL/JSON, eight runnable SQL examples, all 52 dossiers, 56 bounded source snapshots, methods, codebook, one concise analysis, curation inputs, research receipts, quote audit and deterministic archive. The manifest lists 136 payload files; the archive adds its manifest and checksum.

## Verification performed

All **176 automated tests passed**, including the earlier 152 tests and 24 governance-specific tests. They validate keys, scalar and embedded-array links, 52×5 coverage, the 37-jurisdiction frame, dates/status distinctions, outline-only review, source snapshots, quote audits, conditional associations, SQLite integrity/foreign keys, all SQL examples, archive inventory and every earlier registry file hash.

The local production bundle passed **224 recorded browser assertions**. These include all 52 instrument routes checked for five coding slots, exact primary-source URL and displayed status; search and all three filter types; combined filters, reset and empty-state caveats; the named court/system/backlink workflow; related-version navigation; unlinked-system and unknown-instrument states; 37 expandable coverage entries; JSON network failure/retry; and HTML-download rejection.

Actual local browser downloads covered all eleven CSVs, governance ZIP/JSON/SQLite, methods, codebook, analysis, SQL/schema, logs, manifest, baseline, one full dossier and one selected snapshot. Core files and the manifest were re-downloaded after final package normalization. The recorded local download attempts include successful repeats, not 35 unique payload types. Original notebook JSON/CSV/Markdown exports were exercised after adding rule 8, and a fresh registry JSON download matched the original bytes.

Desktop and 375px views were checked, with catalogue light/dark screenshots and a mobile dossier screenshot. Native filters and reset worked on mobile; the page body did not overflow horizontally. The dense catalogue retains a deliberately horizontally scrollable table on narrow screens. Theme screenshots were taken after transitions settled; transient screenshots were not mistaken for final contrast failures. No browser page errors were recorded.

The existing private app was updated in place, preserving asset identity. It passed **22 hosted assertions**, including catalogue/filter/reset, 37 coverage rows, a five-slot instrument dossier, named system association/backlink, twelve original system fields, draft and staged-commencement wording, the 144-system explorer and mobile filtering/reset/viewport fit. Actual hosted ZIP, JSON, SQLite, system-link CSV, coverage CSV, analysis and method downloads matched local bytes. No signed private preview URL is embedded in the repository report or research package.

A fresh remote checkout of commit 46ad586 ran `npm ci`, offline `npm run package:governance`, all 176 tests and the production build successfully. The resulting working tree was clean and the governance ZIP, JSON and SQLite hashes matched the original build exactly. Reproduction makes no search/model calls and requires no research credentials; it validates the curated release, not every source's underlying truth.

## Final integrity hashes

| File | SHA-256 |
|---|---|
| Governance complete-governance.zip | `100ebfa52d919fa2e2de5daa14b87e1a3ef8582ceda72818811a6642f47b68e5` |
| Governance data.json | `d231c33fb616a3204207c692fdaae2b7eef2c525d3e5d5be33a1f0d00c10632c` |
| Governance dataset.sqlite | `cc55320e68fde019ae88129487094704ede63268b235a2c25b445ef6cbd117a8` |
| Unchanged registry complete-registry.zip | `7b3c4c5af158f4570863f0db8f7f48b63008718e0f26151932340abbc069a26a` |
| Unchanged registry data.json | `59b93500019144ce28db5228b5144a39f83bcd4448034c5de538b322bcea3a81` |
| Unchanged registry dataset.sqlite | `77d317a8065c16f7f38636cbd470957819f0948dd83bc0e31feb8e7e07c8b30d` |

## Problems caught, fixes and remaining warnings

The complete search receipt set initially omitted the forty follow-up query receipts when assembling its log; those were restored before packaging, giving the reproducible 157-query total. The packager's dimension assertion initially used “Accountability” instead of the actual “Accountability and data” label; it was corrected rather than dropping or duplicating a field. Every coverage row now explicitly states that bounded screening is not proof of absence, including jurisdiction-specific gap notes. The Aadhaar consolidation note was corrected to the actual 15 December 2025 wording rather than its filename date; Kerala's unrelated KSPACE date was not treated as an IT-policy adoption date.

The SQL test harness initially split at a semicolon inside a comment; it now uses SQLite's complete-statement parser. Browser test selectors were corrected for combined heading text and repeated source-download links. A long headless download sequence timed out after twenty successful governance downloads; the remainder and final core files were verified in a fresh browser context. These harness retries are disclosed, and no timed-out action was counted as a successful download.

Generated Markdown trailing blank lines were normalized before the final archive and clean-checkout verification. The existing application still has Vite's large-chunk warning: its main JavaScript bundle is about 1.63 MB minified/337 kB gzip. Governance data is fetched separately, but this release does not claim to solve the earlier policy desk's bundle size or to have undergone a comprehensive accessibility/performance audit.

## Research boundaries

Forty-seven instruments were coded from full retrieved text with selected provisions; General Financial Rules used the procurement window of its full text. Four records remain official-outline/announcement-only, and detailed underlying text remains unresolved for those records. Cached recovery, failed retrievals and Rajasthan's documented scanned-PDF/OCR fallback remain visible. Selected Rajasthan pages were visually checked; this is not authentication or legal review of every original page.

Coding is LLM-assisted and single-analyst, not independent recoding. Selected quotations have normalized exact-membership and per-URL budget checks; these checks do not prove every interpretive summary correct. No independently verified operational/compliance observations were added. Drafts, recommendations, constituted bodies, published policies, enacted texts and historical mandates must not be pooled as equivalent safeguards.

The geographical screen is systematic but bounded, follow-up depth is uneven, and included documents are not a national census. A zero coverage count, unlinked system or unknown provision is not a finding of absence or wrongdoing. Scope associations do not determine legal applicability, device classification or compliance. Primary documents and detailed limits are exposed for researchers to challenge the coding.

No public launch, paid services, external enquiries or information-request submissions occurred. The cycle is complete within this documented collection and release scope; the next evidence task is independent recoding and targeted verification of implementation records, not another automatic doubling of systems.
