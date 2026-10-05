# Release QA inventory

This inventory covers the complete curated release and the user's request for at least ten concrete contributions. Check results are recorded after execution, not inferred from implementation.

## User-visible claims and required checks

| Claim/control | Functional check | Visual states |
|---|---|---|
| Complete collection | 30 final records, split mappings, four sources, eight corrections. | Desk, full comparison navigation, source list. |
| Twelve contributions | Inspect all 12, download an individual and the complete bundle. | Contribution index desktop/mobile. |
| Navigation | All seven routes, direct deep links, invalid-route fallback. | Each page desktop/mobile. |
| Search and filters | Matching search, no-match, reset, combined actor/type, continuity. | Results and empty state. |
| Compare | As-printed/corrected full cycle, highlights off/on, focused/full text, split rule and table. | Retention, Rule 1 correction, Fourth Schedule, full text. |
| Evidence | Official-page links and hash/snapshot details resolve to intended targets. | Side-by-side panels and source-integrity disclosure. |
| Brief selection | Add/remove from desk and compare; reorder/remove within brief. | Selected and empty states. |
| Export | Markdown preserves sources/caveats/notes; CSV valid; notebook round-trip. | Download status and readable preview. |
| Local review | Required reviewer/note; checked and disputed; historical events retained. | Saved-event state and validation. |
| Corrections | Open, close/Escape, validation, download draft; no automatic submit. | Modal, focus trap and error state. |
| Notebook import | Valid restores session; invalid/version/oversize preserves existing state. | Success and error states. |
| Session clearing | Selection/reviews cleared only locally; export guidance visible. | Cleared brief. |
| Theme | Light -> dark -> light, no blocked storage APIs. | Desk and comparison in both modes. |
| Privacy | No document-content POST, model calls, analytics or private state published. | Method, privacy note, network observation. |
| Accessibility | Keyboard focus, labelled controls, modal cycle, mobile fit and zoom. | Desktop, 375px and enlarged UI. |
| Downloadable research | Study, specification, snapshots and structured collection exist. | Source/method download controls. |

## Exploratory scenarios

- Search a multi-word term, filter to an empty result, navigate a different selected record, reset and verify the prior selection persists correctly.
- Import a malformed or forged notebook after writing review notes; ensure the existing notebook is unchanged.
- Switch corrected/printed while expanding a corrected schedule, then export its brief; confirm quotes retain their labelled as-printed origin.
- Select multiple provisions, reorder/remove them, switch routes/theme, save/import and verify sequence and notes.

## Status

Functional, visual and responsive checks were executed. All 12 automated tests and 57 explicit browser assertions passed; the scope, results and remaining boundaries appear in `VERIFICATION.md`.

## Edition 02 expansion inventory

The following controls and claims require new execution rather than being inferred from edition 01:

- Three collection cards, lineage disclosures and collection-specific deep links.
- 56 total comparison records; family scopes of 30/14/12.
- 30 total contribution cards; family scopes of 12/10/8 and corresponding downloads.
- 13 source records; family scopes of 4/6/3, correct official URLs and snapshots.
- Ten English corrections; family scopes of 8/2/0 and explicit empty state.
- Prior-law comparisons labelled correctly, with prior-law rather than draft URLs.
- AI recommendation status, printed-page locators, disabled automatic diff and no invented corrected-version control.
- SGI original/corrected/full/focused cycles with both directed citations.
- Mixed-family selection, review, reordering, Markdown/CSV export and notebook round-trip; older notebook compatibility.
- Search across evidence, combined filters, no-match state and reset.
- Packaged file-download success, simulated failure fallback and notice dismissal.
- Desktop/mobile captures for all routes, dark theme, enlarged layout, keyboard modal cycling and no horizontal overflow.
- No observed runtime errors or private-content POSTs.

Edition 02 execution passed 30 automated tests and 169 explicit development-browser assertions. Detailed results and boundaries are recorded in `EXPANSION_VERIFICATION.md`; production-preview checks are recorded separately there.
