# AI Watch: institution-and-system dataset release verification

Dataset v1.0.0, checked 5 October 2026. The implementation is committed at [686be2d6c6f0299d39d7531b02261adae5e75551](https://github.com/nawaaaaaAaar/ai-watch-india/commit/686be2d6c6f0299d39d7531b02261adae5e75551). This report verifies the defined data/software release, not national completeness, institutional truth, operational safety, legal compliance or researcher demand.

## What changed

The primary homepage now explores named public-service systems and responsible institutions. A system dossier exposes all twelve accountability fields, source excerpts, typed observations and unresolved questions. The earlier policy desk, implementation ledger, six case files, source library, corrections, old archive and private policy notebook remain accessible as supporting work.

New registry records are not added to the old policy-provision denominator or notebook IDs. All existing curated data JSON and the edition-05 archive are byte-unchanged in the implementation commit. Website branding remains AI Watch with India explicitly identified; no global coverage claim, public launch, paid service or outbound enquiry was made.

## Release inventory

These are different database units, not independent contributions or a nationally representative sample:

| Table | Records | Meaning |
|---|---:|---|
| systems | 18 | Named selected systems/services; six inherited and twelve new |
| institutions | 21 | Source-stated institutional labels, not registry-certified legal identities |
| system_institutions | 21 | Responsible/operator/partner roles with provenance |
| system_links | 1 | Developer-reported integration, not certified current contract |
| deployments | 20 | Dated, undated, historical and expected observations; not twenty confirmed current installations |
| procurements | 3 | Allocation, announced historical contract and news-reported regional award |
| evaluations | 5 | One prospective field-study record, one specification and three inherited evaluation-related descriptions |
| metrics | 12 | Study results, usage bounds, specification, workflow and multi-intervention claims |
| controls | 10 | Source-described safeguards/routes, not ten tested implemented controls |
| policies | 2 | Curated direct system documents only |
| system_policy_links | 2 | Qualified direct relationships |
| assertions | 216 | All twelve fields for each of eighteen systems |
| evidence | 125 | Unique selected normalized excerpts |
| evidence_links | 372 | Many-to-many provenance links, not independent corroborations |
| sources | 50 | Used source records with original URLs, date/type and snapshot hashes |
| issues | 15 | Unresolved numerical, scope, current-status or evaluation distinctions |
| candidate_decisions | 26 | Eighteen included and eight excluded/context decisions in this round |

Fourteen cases have explicit AI source attribution, including vendor/editorial descriptions rather than necessarily official validation. Four qualified biometric/analytics contexts lack established system-specific AI identification in reviewed records. These are separately filterable; the category does not rank model quality or safety.

The twelve new profiles are Digi Yatra, BHASHINI, Kisan e-Mitra, Bharat-VISTAAR, AskDISHA, ADVAIT, Project Insight, Railway elephant IDS, Telangana PLCS, RTA FEST, e-Paarvai and the descriptively labelled BMC–Qure.ai TB pilot. Exact product/version identity in the municipal pilot remains unverified.

## Research and coding verification

The round logs 62 discovery/follow-up/recency queries and 312 returned discovery hits. The search log includes thin query/title/URL receipts, not republished copyrighted article text. Retrieval receipts preserve blocked documents and SDK date metadata that was not silently accepted.

Twenty-nine new selected sources were read and curated. New excerpt selections were checked for normalized membership in fetched originals and limited to 250 unique selected words per source. The six inherited cases retain their earlier reviewed source selections, converted to the same twelve-assertion structure. Source snapshot hashes cover excerpt files, not original PDF binaries.

Source-date handling was reviewed, including a source-stated September BHASHINI date conflicting with SDK metadata, Project Insight's 19 July 2016 announcement, an IRCTC exchange filing of a historical report, and explicitly metadata-based PLCS dating. System latest-record dates are derived from their linked dated sources, not from successful operation.

The review preserved clinically important e-Paarvai specificity alongside accuracy, Railway IDS requirements rather than achieved error rates, usage lower bounds rather than unique users, allocations rather than spending, and Kisan e-Mitra's unreconciled “resolved” versus “responded to” query wording. Refer to the source-cited research note; coding these distinctions is not proof of causal harm or system failure.

No second independent coder, inter-rater agreement, interviews, site inspection, citizen-level records, current model tests or completed RTI response process is claimed. Unknowns are research limits, not findings of nonexistence.

## Automated and data integrity checks

All **107 automated tests passed**, including the original 87 tests and twenty new registry tests. Tests cover:

- **Coverage**: eighteen unique system IDs, twelve assertions each, correct metadata counts and valid primary keys.
- **Relationships**: system/institution/source foreign keys and generic provenance links, including source trails for documented/partial assertions.
- **Claim limits**: exact publication/date basis, expected versus achieved go-live, diagnostic sample/specificity, normative alarm denominator, multi-intervention attribution, typed amounts and usage bounds.
- **Exports**: formula-neutralized filtered CSV, all dossiers, bounded excerpts, source hashes, research receipts and rejected foreign validation.
- **Database/package**: SQLite integrity and foreign-key checks, runnable SQL, ZIP CRC and every manifest payload hash.
- **Regression**: existing dataset, corrections, source hashes, notebooks and export/security tests continue to pass. Two historic UI-label assertions were updated for the new title/navigation; their underlying behaviours remain tested.

`npm run build` passes. The inherited main JavaScript bundle remains approximately 1.61 MB uncompressed / 333 kB gzip and emits Vite's size warning; this release does not claim a comprehensive performance optimisation or independently audited accessibility/security review.

## Browser and hosted verification

Browser checks exercised the explorer search, sector/stage/attribution and combined filters, source-date sorting, reset, honest no-result state, filtered CSV, all eighteen dossier routes and their twelve fields. Evidence disclosure exposes the original URL/date/type; dossier downloads, source snapshots, seventeen table CSVs, documents, logs, JSON, SQLite and ZIP were checked through actual browser downloads.

Supporting routes were revisited. Missing-system and unavailable-dataset states give an explanation and working return/retry controls. Desktop 1440px and mobile 375px views were inspected; the table scrolls independently without whole-page horizontal overflow. Light and settled dark surfaces were reviewed, including the source and method pages.

The QA journal records 135 successful development/production browser assertions and one caught development-download failure; seven successful hosted download-byte checks also appear in that journal, so the totals are not independent. Nineteen dedicated hosted checks passed with zero captured page errors, including final ZIP, SQLite and JSON byte equality, clinical context, filters, mobile views and a preserved policy comparison.

### Download problem found and fixed

A destructive SQLite rebuild briefly invalidated the development server's public-file cache, which returned SPA HTML for a database request. The compiler now creates a temporary database and replaces the final file atomically. The global download handler rejects HTML fallbacks instead of labelling them successful research downloads. Final production and hosted SQLite downloads match the source database SHA-256.

Two high-speed multi-download bursts timed out in Chromium; subsequent individual retries succeeded and their bytes matched. These retries are documented rather than treated as source retrieval failures. Dark-mode screenshots were retaken after computed background transitions settled, preventing transient mixed-theme captures.

## Reproduction and package completeness

A fresh no-hardlink checkout of the implementation commit ran `npm ci`, `npm run package:registry`, all 107 tests and the production build. `git status --porcelain` was empty afterwards. Its registry archive and SQLite checksums matched the originals, so no network retrieval, model keys or original research-machine files are needed to reproduce the curated package.

The complete registry ZIP contains **95 payload files plus its manifest and manifest checksum**: 97 entries, 297,651 bytes. These include the seventeen CSVs, full JSON, SQLite, schema, eighteen dossiers, fifty selected source snapshots, protocol, codebook, research note, SQL, logs and reproducible corpus-count output. Original PDF binaries and full copyrighted articles are linked, not mirrored.

```text
complete-registry.zip
SHA-256 47871b472e3a3f7a67a0b3dfd45cfef41f2773e6be67bd882f6818955a9febe5

dataset.sqlite
SHA-256 256a265d88cc5ecc83877089b170875b652cbcbccdb32bcdd80908603b411507
```

## Sign-off and boundary

The defined linked-data release is implemented, reproducible, committed and tested in the existing private preview. It is a coherent exploratory dataset rather than a claim that all Indian AI information is collected.

Research value is not established by a green build or record counts. The release supports source-traceable analysis now; independent recoding, a systematic institution/geography sampling frame and real researcher use remain necessary before stronger population-level or product-value claims.
