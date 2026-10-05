# AI Watch India

A complete curated policy-change desk for journalism, governance research and decision preparation. Compare official wording, inspect corrections and uncertainty, and export source-backed working briefs.

## Included in this release

Curated edition 03 adds implementation evidence without launching a public website:

- Four evidence collections: 56 policy-comparison units plus ten implementation checkpoints, 25 official source snapshots and 40 reusable briefs.
- A new implementation ledger separates constitution orders, official status wording, recruitment, partnership processes, project selections, reporting mechanisms, redress and voluntary commitments from verified outcomes.
- Every checkpoint includes multiple source excerpts, a link to its underlying governance recommendation and a records-to-verify checklist.
- Evidence-status and search filters; ten individual briefs and a collection bundle; mixed-policy exports retain the complete documentary trail.
- No implementation score, inferred appointment, inferred spending, invented official correction or automatic submission.
- Study and search-scope documents explain conflicting wording, historical deadlines, extraction limits and negative-finding boundaries.

Edition 02's policy-comparison coverage remains included:

- Three collections, 56 comparisons, 13 official source records and 10 directed English corrections.
- Synthetic-media/platform duties: 14 units cover all five final amending rules; the comparison distinguishes October draft proposals from later additions using prior-law context.
- AI Governance Guidelines: 12 thematic units cover all four main parts and map all six consultation recommendations. This is recommendation lineage, not a certified legal redline or proof of implementation.
- Thirty reusable briefs: the original twelve plus ten SGI and eight AI-governance briefs, individually and in family/all-collection bundles.
- Collection filters on comparison, contributions, sources and corrections; mixed-family exports retain correct sources, status and comparison kind.

The original release's features remain included:

- Complete DPDP Rules draft/final collection: 30 final provisions, explicit split mappings, four official instruments and eight directed corrections.
- Twelve distinct downloadable policy-research contributions, each with evidence, interpretation, caveats and follow-up questions.
- Search, actor/type filters, full provision text, mechanical word highlights and as-printed/as-corrected views.
- Source library with official PDF links, immutable extracted-text snapshots and SHA-256 checks.
- Local review notes and checked/disputed states, saved through notebook export/import.
- Brief selection, reordering and source-linked Markdown/CSV exports.
- Local correction-proposal drafting with a manual GitHub submission path.
- Responsive light/dark interface, keyboard navigation and explicit coverage/verification limits.

This is a curated release, not a national live monitor, legal opinion or claim of exclusive discovery. Its core works without model keys, accounts, paid APIs or a backend.

## Run locally

```sh
npm ci
npm run dev
```

Open the URL printed by Vite. Production builds are portable static files:

```sh
npm run validate:data
npm test
npm run build
npm run preview
```

Deploy the `dist/` directory on a static host. Relative assets and hash routes support subdirectory hosting. No GitHub Actions workflow is enabled, and no paid resource is provisioned.

## Reproduce the curated data

The input comparison and coverage register are in `research/`; four extracted public-document snapshots are in `public/snapshots/`. Rebuild the curated dataset and the twelve briefs:

```sh
python scripts/build_dataset.py
python scripts/build_expansion.py
python scripts/build_implementation.py
node scripts/package-briefs.mjs
npm run validate:data
npm test
npm run build
```

The script contains curated classifications and interpretations; it does not infer authoritative legal conclusions from token differences. Word highlighting is mechanical. Table comparisons avoid automated highlighting because flattened reading order can create false changes.

Original PDF binaries are linked at official sources, not mirrored here. Snapshot hashes verify extracted UTF-8 text only; they do not verify original PDF bytes.

## Editorial limits

The evidence check date is 4 October 2026. English text was reviewed by a single analyst, not independently approved by legal counsel; no exhaustive current court-order or later-amendment chain is certified.

The collection retains the 13/14 November publication-date disagreement and the official relative commencement formulas. It does not turn computed dates into definitive compliance deadlines.

Full sources, findings and limits are in `public/research/study.md`. The broader roadmap and acceptance criteria are in `public/research/specification.md`; P1/P2 monitoring, arbitrary uploads and authenticated multi-user editorial infrastructure are not implied to be part of this curated v1.

The expansion study and coverage register are in `public/research/expansion-study.md`. AI-guideline locators refer to printed pages, not guessed PDF page numbers; automatic lineage highlighting is disabled. SGI corrections are applied to the two directed English locations, not the separate Hindi substitutions. Current court status, all later amendments and institutional implementation are not certified.

## Privacy and session behavior

Selection and reviews live in memory. Export the notebook before reloading and import it to resume; no localStorage, sessionStorage, IndexedDB, cookies, analytics or remote document uploads are used.

Notebook import reads a local JSON file and validates version, IDs and review events. Fonts load from Google Fonts; official-document and GitHub links leave the application when explicitly opened. No private notes are included in public source or automatically sent anywhere.

## Correct a finding

Use a provision's “Propose a correction” control to create a source-linked draft. Download and review the proposal; submit manually through repository issues if appropriate.

For maintainers: update the curated source/observation, regenerate data and briefs, run tests, document review and publish a versioned release. Do not erase original text or silently expand collection coverage.

## Repository structure

```text
shared/schema.ts            Typed data/review model
src/main.tsx                Seven routed workspace views
src/lib.mjs                 Filters, validation and exports
src/data/policy.json        Curated provision/source collection
src/data/expansion.json     SGI and AI-guidelines collections
scripts/                   Dataset, brief and validation pipelines
tests/                     Deterministic data/export/security tests
public/snapshots/           Extracted source snapshots
public/briefs/              Twelve briefs and complete bundle
public/research/            Worked study and product specification
```

See `QA.md` for the control/state inventory, `VERIFICATION.md` for edition 01 checks and `EXPANSION_VERIFICATION.md` for edition 02 checks. A public production-domain launch or durable monitoring schedule requires an explicit deployment choice; the application itself is static and self-contained.
