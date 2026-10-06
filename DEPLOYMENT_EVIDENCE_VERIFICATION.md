# AI Watch: implementation and procurement release verification

Implementation-evidence layer v1.0.0, checked 5 October 2026. Implementation commit: `752e78aa0dcbc34fc73daa07e25156d203bd567a`; existing private preview updated in place. The cycle deepens a purposive ten-case subset, not the system population, and provides no independent operational or legal assurance.

## Release inventory and preservation

| Unit | Count | Meaning |
|---|---:|---|
| Existing system families | 144 | Unchanged registry population |
| Existing governance documents | 52 | Unchanged governance layer |
| Earlier public files checked | 528 | 389 registry plus 139 governance files, all byte-preserved |
| Selected existing families | 10 | Railway IDS, railway VSS, NHAI DAS, Adalat.AI, CAG PARAS, CAG PARAKH, Safe Kerala, UPSC, Madukkarai elephant surveillance and IGMS |
| Primary document/page records | 33 | Original URLs, roles, date precision, review scope, cache flags and extracted-text hashes |
| Documentary observations | 124 | Requirements, invitations, accounts and expressly qualified contextual evidence |
| Case-observation links | 136 | Shared CAG evidence links to two existing agent families, not two procurements |
| Selected excerpts | 124 | One bounded selected passage per observation |
| Source-stated party observations | 113 | Roles, not independently resolved supplier identities |
| Typed financial observations | 12 | Estimates, sanctions, security, reported costs and payment arrangements, not verified spending |
| Case-by-dimension slots | 100 | All ten dimensions for every case; 44 have no retained observation |
| Governance associations | 11 | Three common-original-document associations and eight inherited qualified links |
| Screened candidates | 12 | Ten included; AskDISHA and MuleHunter.AI deferred after screening |
| Linked CSV tables | 12 | Includes 144 system-key and 52 governance-key bridge projections, not additional researched cases |
| Archive entries | 76 | 74 payload files plus manifest and manifest checksum; ZIP itself is the 77th public layer file |

The separate layer lives in `public/implementation-evidence/`; frozen inputs and research documents are in `research/implementation-evidence/`. The website adds only the `/deployment-evidence` list/case view, source inspection, download controls and system backlinks; existing design, policy notebook and earlier archives remain.

## Research and provenance checks

The retained log records 96 queries, 575 hits and 66 retrieval receipts, including 23 error receipts and cached recoveries. Of 33 included documents, ten use noncached reviewed text and 23 use cached text; a fresh attempt alone is not labelled fresh verification after cached recovery.

LLM-assisted extraction produced 172 provisional observations from 36 documents. The curated set retains 124 observations from 33 documents; duplicate press-release URLs, unrelated FAQ material, portal entries replaced by original documents and off-system observations are not promoted into the release. The quote audit checks selected passages against reviewed text, with no more than 250 selected words per original URL. It does not authenticate source binaries, prove official claims true or independently validate interpretations.

The categorical distribution is 46 formal prescribed requirements, sixteen procurement-stage invitations, 44 first-party activity/outcome accounts, five implementer historical accounts and thirteen institutional-context observations. Independently verified outcomes, spending and compliance remain unestablished, not inferred from these categories.

Large RFP/policy-note review is targeted rather than exhaustive. The original Safe Kerala PDF's operative pages 4–5 received a bounded visual check because Malayalam text extraction is badly damaged; selected numeric/English tokens do not reproduce the full Malayalam clauses. Kurnool's damaged training date, unresolved Legsys entity identity and IGMS's conflicting official launch chronology remain explicit. One earlier identical TCIL fetch was overwritten by the final-batch research script; the retained receipt ledger is not claimed to capture every network attempt.

## Automated and browser verification

- **Automated suite**: all 197 tests passed locally and in the clean checkout, including 21 new implementation-layer tests. Checks cover inventories, unchanged baseline bytes, scalar and array joins, quote receipts, stage distinctions, SQLite integrity/foreign keys, executable SQL, manifest payloads and ZIP contents.
- **Local production-bundle browser QA**: 129 successful assertions. All ten case pages retain ten dimensions; searches, every dimension and strength filter, combined empty states, reset, evidence expansion/collapse, original-system backlinks, a named governance destination, load failure/retry and unknown/deferred routes were exercised.
- **Local downloads**: 28 distinct exported files were downloaded through actual controls and compared to original bytes, including all twelve CSV tables, ZIP/JSON/SQLite/SQL, method, codebook, analysis, provenance/log/checksum files, one complete dossier and a selected-source snapshot. A separate recovery check re-downloaded the manifest after rejecting a simulated HTML response.
- **Hosted preview QA**: 28 successful assertions. These cover all ten case routes, combined filtering/reset, evidence display, governance navigation, the unchanged 144/52 catalogues, active navigation and 375px viewport fit. Eight actual hosted downloads match local bytes: ZIP, JSON, SQLite, coverage CSV, governance-links CSV, analysis, one dossier and one source snapshot.
- **Visual review**: desktop 1440px and mobile 375px list states, light/dark themes, empty state, dense expanded evidence, download section and hosted screenshots were inspected. No unexpected page overflow, clipped controls or unreadable theme contrast was found in reviewed states; horizontal mobile navigation/table scrolling remains intentional.
- **Regression**: old registry filtering, governance navigation, unselected-system disclaimer and source-linked notebook/Markdown exports were checked. The old `scripts/build_implementation.py` policy-ledger builder is byte-restored and unchanged; the new workflow uses `scripts/build_deployment_evidence.py`.

Two browser-harness assertions were corrected: one initially ran before asynchronous links arrived, and one expected an internal provision ID in a Markdown format that does not promise that ID. A unit-filter expectation was also corrected because search includes case summaries as designed. These were test assumptions, not hidden product failures. A builder filename collision was identified and fixed before release; the earlier builder was restored.

## Clean-checkout reproduction and integrity

A fresh remote checkout ran `npm ci`, `npm run package:implementation`, `npm test` and `npm run build`. Packaging made no network calls, produced an empty Git working-tree status and reproduced the hashes below; all earlier frozen files passed the builder's preservation checks.

| File | SHA-256 |
|---|---|
| complete-implementation-evidence.zip | `85893b951df71efb9cc9e732131f3a1a146995e802768be264ddb8da34bebbb7` |
| data.json | `3952e660c9d5fedf186c69244568b0d77267c9bdbb4f7293c3bb6f116b30dcd0` |
| dataset.sqlite | `3cffe22a6e71d4d150dce81aa4956c93c290f370cc5e181853596a4461b8c073` |

The archive contains the new layer and old join keys, not the complete separate system/governance archives. Full original PDFs and copyrighted articles are not mirrored. Reproduction means rebuilding frozen release bytes, not guaranteeing future issuer-page availability or extraction. Vite still warns about the pre-existing large JavaScript bundle; the build succeeds, and no performance benchmark or nationwide completeness claim is made.

## Research use and remaining limits

Start with [the concise implementation analysis](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/implementation-evidence/implementation-findings.pplx.md), then the method, codebook and runnable queries. This cycle makes procurement stage, prescribed human review, version continuity and unresolved records more usable for analysis; original awards/contracts, payments, acceptance reports, actual exception logs, dated coverage inventories, completed independent evaluations and AI-specific redress remain important gaps.

Selection and coding are single-analyst and purposive; all source accounts require appropriate attribution. Policy associations do not establish legal applicability, compliance or operational effectiveness. This completes the defined ten-case deepening, not exhaustive research on all 144 families, and no system count was increased. No paid services, public website launch or external enquiries were undertaken.
