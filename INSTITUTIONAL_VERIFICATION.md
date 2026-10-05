# AI Watch: institutional research release verification

Release 1.1.0, checked 5 October 2026. The institutional research, linked dataset, source-recheck ledger, exports and private preview are implemented. This verifies the defined release, not a national census, independent recoding or operational effectiveness.

Implementation: [institutional research commit](https://github.com/nawaaaaaAaar/ai-watch-india/commit/ad529a46dae7ce9ba141be840fd4f08778863ed7). Methods and detailed source-linked findings are in [the institutional study](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/INSTITUTION_STUDY.md).

## Research and release inventory

| Item | Count or boundary |
|---|---|
| Named systems/services | 36: 18 original seed records plus 18 institutional-round additions |
| Institution records | 32, source-stated labels rather than certified legal identities |
| Fixed documentary frame | Five ministries plus the independent Supreme Court |
| Frame-associated system records | 26; ten earlier records retained outside the frame |
| Second-round searches | 24 comparable frame queries plus 12 candidate follow-ups; 228 discovery hits |
| Second-round retrieval receipts | 29; twenty sources used in curated additions/context |
| Used source records | 70 total |
| Exact selected evidence excerpts | 187 |
| Claim/observation-to-evidence links | 705, not 705 systems |
| Accountability assertion slots | 432: all twelve fields for every system |
| Evidence status | 89 documented, 181 partial, 159 not verified, three conflicting |
| AI classification | 29 explicit source attributions, six qualified algorithmic/biometric contexts, one evaluation-infrastructure unit |
| Candidate-decision records | 56 included, context or deferred decisions in the reviewed corpus |
| Baseline source rechecks | 50 source records and 125 original excerpt selections |
| Baseline assertion triage | 216 slots; source-availability/text matching, not independent semantic recoding |
| Machine-readable tables | 21 CSV tables, full JSON, SQLite and column schema |
| Packaged dossiers | 36, each retaining all twelve fields |
| Research ZIP | 141 payload files plus manifest and manifest checksum: 143 entries |

The twenty new used source selections were checked against fetched source text and the unique selected-word budget. Existing policy collections are separately retained, not added to the system-count denominator.

## Source recheck outcome

Fresh retrieval plus raw-HTML fallback re-located 68 of 125 original excerpts. Twenty-seven baseline sources re-located all their selected excerpts, twenty failed fresh retrieval and three had partial extraction matches. Unresolved selections were subsequently re-located through cached extraction, with that basis recorded separately.

A cached match does not establish present live availability. A timeout, cookie-only page or parser mismatch does not demonstrate a withdrawn claim. AskDISHA wording was narrowed to its historical authorized-partner observation rather than infer current affiliation from a missing extraction.

This is a same-analyst source review and automated availability triage. No independent second coder, inter-rater agreement, institutional response or participant testing is claimed.

## Automated and clean-checkout checks

- All 115 automated tests passed, including historical policy invariance, every accountability slot, source quote/hash integrity, identifier uniqueness, reference integrity, typed metrics, frame membership, source-recheck distinctions, candidate decisions, archive CRC and manifested payload bytes.
- TypeScript checking and the production Vite build passed. The inherited main JavaScript chunk remains approximately 1.61 MB minified, 333 KB gzip; Vite emits its large-chunk warning. This is not presented as a fully performance-optimised release.
- A fresh local clone of the committed implementation installed dependencies with `npm ci`, rebuilt the package, passed all 115 tests and built production successfully. Rebuilding left the clone's tracked files unchanged.
- JSON relationships and SQLite foreign keys were checked. The database builder uses atomic temporary-file replacement, preserving the earlier binary-download fix.
- `git diff --check` passed with `core.whitespace=cr-at-eol`, because generated CSVs intentionally use standard CRLF line endings.

## Browser and visual checks

The production bundle passed 144 recorded local browser assertions and 19 additional hosted-preview assertions. Individual receipts are retained in `research/registry/QA_LOCAL.json` and `QA_HOST.json`; the pre-test coverage inventory is `QA_INSTITUTIONAL.md`.

Local checks covered all 36 system routes and all twelve dimensions; each institutional filter; the ten outside-frame records; all three AI classes; combined filtering; date sorting; empty-result/reset behavior; unknown identifiers; dataset failure and successful retry; expanded evidence; and all 21 CSV table download controls. Archive, SQLite, JSON, research documents and audit-file browser downloads were compared to the generated bytes. Filtered CSV output retained six health-frame rows.

Supporting policy routes and a notebook Markdown export were exercised. The HTML-fallback download guard was deliberately triggered and rejected HTML instead of producing a false CSV. Automated tests additionally preserve the earlier policy corpus and notebook semantics.

Hosted checks covered the displayed 36-record release, all six frame filters, the single infrastructure unit, a twelve-field dossier, 21 table controls, supporting policy navigation and seven actual downloads. Hosted ZIP, SQLite and JSON bytes matched the originals.

Desktop at 1440 × 1000 and mobile at 375 × 812 were inspected for the explorer, data room and new dossier. The settled dark theme, filtered state, expanded evidence and institutional-frame cards were inspected separately. No page-level horizontal overflow, clipped primary action, unreadable long institution labels or broken evidence layout was found in these tested states; the narrow data table and mobile navigation intentionally scroll horizontally within their containers. The initial dark screenshot caught a transition rather than the settled theme, so it was recaptured after computed colors settled.

Test-harness retries were retained as process limitations: the first route loop incorrectly used pathname URLs rather than this static application's hash routes; one download burst hit Chromium's automatic-download timing; one helper attempted a data-room control while still on the explorer; a duplicate intentional candidate-register control needed a scoped/first locator; and the intercepted dataset-failure test needed a reload to cause a fresh fetch. These were corrected and rerun. They are not counted as passing assertions or as newly discovered product defects.

## Final package identity

ZIP SHA-256:

```text
6aaf64a5cf5a217eaa3be3c0a7ccff34d535c76fe0bd8b8ade6fc576c38ef293
```

SQLite SHA-256:

```text
72054dc3d297882fffc2fcfaa663992c23703819e21bb35198d8c2c49ba0379b
```

The manifest hashes selected excerpt snapshots and distributed payloads, not original PDF binaries or entire external sites. The verification report and browser receipts are outside the data ZIP to avoid a self-referential manifest; the ZIP itself includes the protocol, codebook, study and research/source logs.

## Remaining research limits

The bounded frame is more systematic than the original purposive seed, but it is not exhaustive institutional disclosure or representative national sampling. Public statements, vendor/editorial claims, specifications and usage totals remain different evidence types. CCTNS version/timing conflict, CROPIC data-declaration tension, screening-yield comparator uncertainty and product-specific oversight/redress gaps remain unresolved.

The substantive examples and original URLs are available in [the source-cited study](https://github.com/nawaaaaaAaar/ai-watch-india/blob/main/research/registry/INSTITUTION_STUDY.md). No public launch, paid service, external enquiry or submission of citizen/child data was undertaken. Genuine independent recoding still requires another human reviewer; this release prepares traceable data for that work rather than pretending it has happened.
