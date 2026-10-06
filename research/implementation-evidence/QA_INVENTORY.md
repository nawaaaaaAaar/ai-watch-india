# Implementation-layer QA inventory

## Claims and data checks

- **Fixed layers**: hash all 528 earlier files; registry keys remain 144 and governance keys 52.
- **Selected research**: ten existing cases, 33 documents, 124 observations, 100 dimension slots; inspect all case pages and strengths, unknowns, source limits.
- **Joins**: scalar SQL foreign keys, array IDs, source URLs and eleven inherited governance links; follow system and governance navigation.
- **Stage distinctions**: targets versus results, bid invitations versus awards, sanction versus spending, old UPSC tender versus own app, shared CAG EOI, unresolved IGMS chronology and Legsys identity.
- **Exports**: all twelve CSV tables, JSON, SQLite, SQL queries, dossiers, source snapshots, method, codebook, analysis and manifest; actual download hashes.
- **Reproducibility**: clean checkout packages identical ZIP, JSON and SQLite; foreign-key/integrity and executable query checks.

## User controls and states

- **Search**: initial ten, matching subset, empty search, reset to ten; combined with dimension and strength.
- **Dimension filter**: known and empty dimensions; reset. Unknown dimensions still appear on every dossier.
- **Strength filter**: every category and combinations; reset.
- **Evidence expansion**: inspect quotation, locator, cache flag, extraction/review scope and source link; close and reopen.
- **Downloads**: static proxy-compatible download handler; ZIP/JSON/SQLite/CSV/Markdown/SQL/checksum downloads return original bytes, not HTML.
- **Theme**: light/dark/return light with settled screenshot; mobile 375px and desktop 1440px, no page overflow.
- **Load failure**: intercept new layer request, visible retry, successful retry; earlier records still accessible.
- **Unknown route**: existing unselected family and invalid key show explicit bounded-selection message, not a fabricated case.
- **Regression**: old registry filters, old governance pages, notebook export and navigation still work.

## Visual and exploratory checks

Inspect initial list, filtered/empty state, dense case with expanded evidence, downloads, original-system backlink and governance destination. Capture desktop and mobile screenshots and inspect clipping/contrast/readability separately from DOM counts. Explore a nonselected system and a combined filter that has no result; recover using reset. Test the new layer failure/retry without changing old datasets. Original external source targets are verified against curation; live external issuer pages may remain inaccessible.
