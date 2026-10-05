# AI Watch India: Edition 05 Complete-Data Verification

Completed 5 October 2026, India date. This release audits and exposes the entire stored five-collection corpus, adds reviewed follow-up evidence and updates the existing private preview. It does not launch a public website, claim a national census or certify operational effectiveness.

## Verified inventory

| Inventory | Count | Meaning |
|---|---:|---|
| Collections | 5 | DPDP, synthetic media, governance guidelines, implementation, public-service cases |
| Stored records / full dossiers | 72 | All records, including 26 not selected as contribution briefs |
| Selected contribution briefs | 46 | Editorial outputs, not 72 inflated contributions |
| Catalogued source snapshots | 46 | Forty earlier records, five service follow-ups, one contextual parent Act |
| Directed English corrections | 10 | Eight DPDP and two synthetic-media substitutions |
| Case accountability dimensions | 72 | Six cases × twelve dimensions |
| Flattened evidence items | 185 | Stored excerpts/trails; not 185 unique sources |
| Limitation / queue rows | 140 | 72 record cautions, 58 non-documented case fields, ten implementation queues |
| ZIP payload files | 203 | All manifested curated data, dossiers, research, snapshots and schema |
| ZIP entries | 205 | Payload plus manifest and manifest checksum |

All stored record properties are retained in exact JSONL and the JSON block in each dossier. CSV exports flatten nested values, while the full structured dataset retains them. The raw original DPDP comparison/coverage files are byte-equivalent copies of the original research inputs.

## Implementation and reproducibility

The [edition 05 implementation commit](https://github.com/nawaaaaaAaar/ai-watch-india/commit/2b101faa2c49604a9c96eeb800a99a2fa8ad3af6) adds the complete data room, source follow-up, packaging scripts and tests. Historical edition 04 reports remain historical; current counts are not retroactively substituted into them.

The complete ZIP is 2,130,282 bytes. Its SHA-256 is:

```text
d4232da5b192dd5e2258a856a68e6be7983c69d947ae366caad9b3735f4c8bcc
```

A fresh local clone with no hardlinks ran `npm ci`, all three earlier dataset builders, `npm run package:data`, validation, tests and production build. It produced no tracked changes and exactly the same archive checksum. No local research working directory, live search call or service credential is required to regenerate the checked-in corpus.

```sh
npm ci
python scripts/build_dataset.py
python scripts/build_expansion.py
python scripts/build_implementation.py
npm run package:data
npm run validate:data
npm test
npm run build
```

The schema is included inside the archive as `schema/schema.ts`; application source and dependencies are not in the data ZIP and remain in the repository. Original PDF binaries and full copyrighted articles are not included.

## Test results

- **86 automated tests passed:** exact datasets, original-record preservation, every source hash, quotation membership, bounded statuses, case fields, all 72 dossier JSON blocks, all source/record references, raw-file equality, CSV formula escaping, notebook validation and corrections.
- **Archive tests passed:** every manifested size/hash, separate manifest checksum, ZIP CRC, path safety, every ZIP payload's hash/size and external archive checksum.
- **200 development-browser assertions passed:** all ten routed views at desktop and mobile, all data-room collection and entry-kind filters, search/reset/empty states, disclosures, non-contribution dossier navigation, actual register/ZIP downloads, new snapshot downloads, all six twelve-field matrices, mixed-family notes and exports, invalid-import preservation and notebook roundtrip.
- **29 hosted-production checks passed:** actual binary ZIP and checksum, manifest, non-contribution dossier, eight register downloads, collection/search controls, clinical matrix, all 46 sources, abstract snapshot hash, printed/corrected wording, notebook import and mixed Markdown/CSV export, mobile primary-action fit, theme and runtime checks.
- **Fresh-checkout build passed:** all 86 tests and the full packaging pipeline reproduced without tracked-file changes.
- **Dependency installation audit:** npm reported zero vulnerabilities in the checked lockfile at this run. This is not a security audit.

The static download handler now downloads response blobs rather than converting files to text. Browser-downloaded ZIP bytes match the local artifact exactly on both development and hosted production; Markdown, CSV and snapshots were rechecked after that change.

No application runtime errors or POST requests were observed in the exercised development workflows. Hosted checks observed no application page errors. These observations do not certify every browser, external source or unexercised environment.

## Visual and usability review

Reviewed screenshots of all ten views at 1440×900 and 375×812, plus populated brief, clinical evidence, individual registers, record index, filtered limitations, empty states and both themes. Data-room fit checks also passed at widths 720, 820, 1000 and 1280, and bottom navigation remained reachable at 1280×800.

The first mobile review exposed an overly long scope explanation that hid the primary download below the initial viewport. A prominent top ZIP action and shorter scope note were implemented; the action now fits in the first mobile viewport, including on hosted production.

A screenshot during the short theme colour transition appeared washed out. Reinspection after the transition confirmed intended foreground/surface colours and readable register controls; the settled screenshot, rather than the transitional one, was used for signoff.

No unintended page-level horizontal overflow, long-label clipping or unreachable desktop navigation was observed in the checked states. Long research pages intentionally scroll; the mobile navigation strip intentionally scrolls horizontally within the strip.

## Evidence updates and unresolved access

The new national clinical evidence is explicitly a retrieved abstract/declarations record, not a reviewed full manuscript. Its full manuscript and the current support page could not be inspected successfully, and the current clinical-remedy field remains partial. [National study record](https://doi.org/10.1101/2025.11.22.25340800)

Developer and official March/April 2023 integration descriptions remain visibly different. The study's no-funding declaration is not assigned to national deployment costs. [Developer account](https://www.wadhwaniai.org/impact/healthcare/), [parliamentary response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps) and [study declaration](https://doi.org/10.1101/2025.11.22.25340800)

Historical clinical and court guidance is included without certifying current implementation. Developer collaboration is not presented as an executed procurement award. [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf), [translation guidance](https://cdnbbsr.s3waas.gov.in/s3ec03ac73001b1d44f4925449ce09d9f5/uploads/2023/09/2023092013.pdf) and [developer submission](https://solve.mit.edu/solutions/73043)

The thin discovery log contains 64 distinct returned URLs from eleven queries. Discovery results are not all promoted into verified evidence; source retrieval outcomes, irrelevant-result boundaries and blocked access are documented in the accompanying completeness investigation and retrieval CSV.

## Scope limits

The corpus is complete as packaged, not complete knowledge of India. It remains single-analyst research, without independent legal/clinical review, agency responses, operational audit, representative sampling or user-demand validation.

Executed contracts, current SOPs, model/version inventories, independent performance distributions, budgets and functioning remedy evidence remain unresolved where labelled. These are visible findings about the review's limits, not claims that the records or safeguards do not exist.

The production JavaScript bundle remains data-heavy at approximately 1.59 MB uncompressed / 328 KB gzip and triggers Vite's chunk-size warning. The build succeeds, but constrained-network performance has not been independently measured; no Lighthouse performance score is claimed.

No paid services, public launch, outbound information requests, complaints, source submissions or automatic monitoring were undertaken. Notebook notes remain private session data unless the user intentionally exports them.
