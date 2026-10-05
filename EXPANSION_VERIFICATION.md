# AI Watch India: Edition 02 Expansion Verification

Verified 5 October 2026. This document records the curated expansion, not a certification of legal advice or nationwide policy coverage.

## Delivered scope

| Collection | Comparison units | Research briefs | Official source records | Directed English corrections |
|---|---:|---:|---:|---:|
| Original DPDP | 30 | 12 | 4 | 8 |
| Synthetic-media amendments | 14 | 10 | 6 | 2 |
| AI governance guidelines | 12 | 8 | 3 | 0 |
| Total | 56 | 30 | 13 | 10 |

The expansion adds 26 comparison units and 18 substantive briefs. Units represent mapped provisions or themes, not 56 separate policies or claims of original discovery. The original DPDP wording and record identifiers remain unchanged.

The synthetic-media collection maps the five amending rules into 14 comparison units, using the October 2025 consultation draft, February 2026 notification and English corrigenda, prior-law and corrected consolidated context, and the official FAQ. Additions not proposed in the draft explicitly use prior-law context instead of invented draft wording. Primary instruments: [consultation draft](https://www.meity.gov.in/static/uploads/2025/10/9de47fb06522b9e40a61e4731bc7de51.pdf), [notified amendments](https://www.meity.gov.in/static/uploads/2026/02/f55fe52418b03f58b0669f6a8bc03b6d.pdf) and [corrigenda](https://www.meity.gov.in/static/uploads/2026/03/20c30107195f68865104dd4e16176f4d.pdf).

The AI collection maps the six numbered consultation recommendations and four main parts of the published framework into 12 thematic units. This is recommendation lineage, not a one-to-one legal redline; annexes, glossary and references are not scored as separate changes. Primary texts: [consultation report](https://indiaai.s3.ap-south-1.amazonaws.com/docs/subcommittee-report-dec26.pdf) and [published guidelines](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf).

## Executed checks

- **Automated suite:** All 30 tests passed, including the original 12 and 18 expansion tests. Coverage includes inventory, unchanged original wording, snapshot hashes, source membership of all new quotes and mapped segments, localized corrections, proper prior-law links, legal-status labels, printed-page locators, filters, exports, notebook compatibility and packaged briefs.
- **Data validation:** Both original and expanded inventories passed. The downloadable combined dataset equals the application merge.
- **Browser execution:** 169 explicit successful assertions on the development application. All 26 new comparison pages were opened and their later-source URLs checked; the 12 AI pages were checked for disabled automatic lineage diff.
- **Filtering and navigation:** Comparison scopes of 30/14/12/56, contribution scopes of 12/10/8, source scopes of 4/6/3, and correction scopes of 8/2/0 passed. Search, combined constraints, no-match states, resets, timelines, missing records and unknown routes were exercised.
- **Evidence and downloads:** All 18 new individual briefs, three family bundles, the combined 30-brief bundle and nine new snapshots downloaded through the UI. Downloaded snapshot hashes matched the recorded extracted-text hashes. Original/corrected SGI mapped text differed as intended and restored through a full cycle.
- **Working notebook:** Mixed DPDP/SGI/AI selection, reordering, local review, preview, Markdown and CSV exports, JSON export/import and original version-one notebook compatibility passed. Invalid JSON left the existing notebook unchanged.
- **Corrections and failure handling:** Local proposal draft download, Escape dismissal, modal keyboard cycling and restored focus passed. A simulated HTTP 503 displayed the download failure notice; dismissal and a successful retry were checked.
- **Responsive and theme checks:** Captures of the seven views plus a second comparison were taken at 1440px and 375px. Light/dark home captures were reviewed. No page-level horizontal overflow was found at those widths; the comparison also passed resized 720px, 820px and 1000px checks. These are responsive-layout checks, not a comprehensive assistive-technology or native browser-zoom audit.
- **Runtime and privacy observations:** No JavaScript page errors and no POST requests were observed during the browser checks. Imported notebooks and review text were processed locally; no proposal was submitted.
- **Build and dependencies:** TypeScript and Vite production builds passed; `npm audit --omit=dev` reported zero known vulnerabilities in the checked dependency tree. Vite reports a large-chunk advisory: the evidence-bearing JavaScript bundle is about 1.23 MB uncompressed / 266 KB gzip. This is not a performance certification.

## Fixes made during verification

Cross-collection navigation could retain an unrelated collection scope. The selection now follows the opened record when scoped, while an intentionally selected all-collection view remains available. The earlier-source label now avoids calling prior law or every consultation report a draft.

The DPDP publication warning no longer appears in an AI-only or synthetic-media-only source scope. Source-library links distinguish the original DPDP study, expansion study and DPDP parent Act rather than implying one parent statute governs all three collections.

Bulk repeated automatic downloads may trigger Chromium's browser-level download throttling. Individual downloads succeeded; QA refreshed between repeated download cases where needed.

## Reproduction

```sh
npm ci
python scripts/build_expansion.py
node scripts/package-briefs.mjs
npm run validate:data
npm test
npm run build
```

The expansion builder uses included source snapshots and curated anchor mappings; it does not require fresh network extraction. Hashes establish integrity of extracted UTF-8 text, not original PDF binaries or certified bilingual accuracy.

## Boundaries and remaining work

This completes two additional curated collections, not a live monitoring service. Interpretation is single-analyst work, not independent legal review, and the collection does not certify the complete later-amendment or court-order chain. Publication, commencement, recommendation and implementation are kept distinct.

The SGI register includes two directed English replacements; Hindi substitutions are outside the English comparison. The AI framework's proposed institutions, action-plan horizons and suggested mechanisms are not evidence of operational implementation. Printed page locators are not guessed PDF-page offsets.

No paid services, interviews, information requests, correction submissions or public website launch were undertaken. Practical usefulness still needs testing with journalists and policy researchers; technical checks do not establish user demand.

## Repository and preview verification

A fresh local clone of expansion commit `6e2f735b3b3b546df3a6e7175f305b434db5cee9` passed dependency installation, expansion regeneration, brief packaging, both validators, all 30 tests and the production build. Regeneration left its tracked working tree clean. The implementation was pushed to [the repository](https://github.com/nawaaaaaAaar/ai-watch-india/commit/6e2f735b3b3b546df3a6e7175f305b434db5cee9).

The existing private preview was updated in place, not launched publicly. Sixteen additional hosted-browser assertions passed: three family cards, SGI scope, AI status and disabled diff, mixed selection and source-linked export, all-brief and family downloads, snapshot integrity, expansion-study download, correction scopes, mobile fit, dark mode, no runtime errors and no observed POST requests. Hosted captures were taken at desktop and mobile widths.

The development count is 169 successful assertions and the hosted count is 16. These are explicit browser checks, not 185 independently designed automated test cases or an accessibility certification.
