# Edition 05 QA inventory

Signoff target: all stored data accessible, exact full-record dossiers, reproducible checksummed archive, substantive evidence updates and explicit remaining gaps. No national-census claim, public launch, paid services or automatic enquiries.

## Functional checks

- **Data room inventory:** all 72 records, 46 sources, 185 evidence items, ten corrections and 140 limitations; scope note and manifest semantics remain visible.
- **Record index:** each of five collection filters, query, reset, empty state, non-contribution record, inspect navigation and full-dossier download.
- **Gap register:** each entry-kind filter, collection interaction, query, reset, zero-results disclaimer, source links and records-to-verify disclosure.
- **Downloads:** actual binary ZIP download compared byte-for-byte with local artifact; archive checksum; manifest; every register; original raw data; full dossier and study. No HTML fallback substituted for data.
- **Integrity:** every manifest file size/hash, all ZIP CRCs and payloads, exact JSONL records, all 72 dossier JSON blocks, source hashes, no private notes, deterministic regeneration.
- **New evidence:** national abstract/full-manuscript boundary; March/April dates; study-versus-deployment funding; historical RMP/grievance guidance; court-guidance jurisdiction/time limits; contextual statute not an extra contribution.
- **Regression:** ten routed views, all source filters/new snapshots, original corrected/printed toggle, original comparisons, six case matrices, implementation requests, notebook save/import, mixed-five-family Markdown/CSV and correction drafting.
- **Privacy/runtime:** no POST or private-note upload, no new browser storage, no application page errors.

## Visual checks

Desktop 1440×900, smaller desktop 1280×800, mobile 375×812 and tablet widths. Inspect ten views, both themes, data-room first viewport, register region, record index, gaps, filtered and empty states, updated health/court matrices, notes and modal states.

Check overflow, sidebar reachability with ten navigation entries, long source labels, readable placeholder contrast, compact status badges, primary ZIP action and visible corpus boundary. Scrolling is intended for the long research desk; internal navigation scrolling must not make a control unreachable.

## Exploratory scenarios

- Search a record whose title does not match but whose limitations do, then recover with reset; zero records must not falsely imply zero evidence gaps.
- Download a non-contribution dossier, select it with a case from another family, export/reimport the notebook and confirm all record fields remain in the fixed dossier.
- Follow new clinical study evidence into the source library and confirm abstract-only labels survive snapshot/export.
- Filter a narrow gap type and navigate back without mistaking that filter for evidence completeness.

Historical edition 04 reports remain historical, not overwritten with current counts. Signoff report will state actual new test and browser-check totals after execution.
