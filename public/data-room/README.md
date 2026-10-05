# AI Watch India: Complete Curated Data Bundle

This bundle contains every stored record in the five-collection desk, all catalogued snapshots, all packaged research and all selected briefs. It is complete within that stated corpus, not a national census or a full archive of each institution's records.

## Contents and interpretation

- **Structured data:** `combined-data.json` is the full application merge; individual collection JSON files preserve their data structures, and the parent Act is context only.
- **Record dossiers:** `data-room/dossiers/` contains 72 readable dossiers, including the 26 records not selected as contribution briefs. Each ends with all stored record fields as JSON.
- **Registers:** coverage, sources, evidence excerpts, corrections and limitations have CSV exports; JSON/JSONL exports preserve nested values.
- **Original raw comparison:** raw DPDP machine differences remain research inputs, not certified legal findings.
- **Snapshots and research:** selected excerpts or extracted text are labelled by source scope. Original URLs remain in the catalogue; full copyrighted articles and original PDF binaries are not included.
- **Integrity:** `data-room/manifest.json` lists every payload file's size and SHA-256. Verify its separate checksum, then verify payload bytes. Download the external `archive-sha256.txt` to verify the ZIP itself.

No private notebook notes, user identities, application dependencies or paid-service credentials are included. Application source and tests are in the repository, not this data archive.

## Reuse boundaries

Citation does not confer copyright or licence rights in third-party material. The bundle does not grant a blanket licence to government documents, articles, research abstracts, vendor accounts or developer submissions; check the original source's terms before redistribution.

The included schema and scripts describe reproducibility rather than legal, clinical or operational certification. Preserve source URLs, dates, types, excerpt limits, uncertainty and correction lineage when reusing the data; do not turn “not verified” into “does not exist.”
