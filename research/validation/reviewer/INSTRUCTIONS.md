# India AI implementation evidence: independent review

This source-first packet asks you to independently code documentary evidence for ten named system families. It deliberately withholds prior statements, classifications, conclusions, case summaries, selected findings and adjudication judgments. It is not a request to confirm a prior analysis.

## Before coding

Read `CODEBOOK.md` and `variables.json`, then complete `reviewer-declaration.json`. Record prior familiarity, conflicts, relevant language competence, any access to the originating project's findings and whether anyone discussed expected answers with you. Do not consult that project's registry dossiers, analyses, repository, comparison key or coordinator baseline until your pass is locked. Original official source URLs are appropriate to consult; source identities and system names are not blinded.

The excerpts and candidate pairings were selected by the first analyst. This is conclusion-blinding, not a fully blinded sample or an independent evidence search. The shared codebook necessarily supplies category definitions, but no selected-unit answer is prefilled. If you already know earlier conclusions, declare that rather than describing yourself as fully blinded.

## Materials and units

- **cases.csv**: opaque case keys and target names only; names do not certify deployment.
- **sources.json**: original URLs, technical retrieval provenance, selected verbatim fragments and, where available, bounded original-text context. No prior paraphrases or classifications are included.
- **units.csv**: shuffled opaque unit keys, task type, source/fragment pointers and candidate case/instrument IDs. A pairing is a proposition to test, not an established association.
- **instruments.csv**: candidate governance-document IDs and original URLs, with no prior status, legal-effect or applicability code.
- **ratings.csv**: long-format blank responses, one row per unit-variable assignment. Preserve all keys and fill only response fields.
- **unit-notes.csv**: your independent reconstruction, party/role findings, human-review/redress details, secondary dimensions and limits. These qualitative fields are reviewed after unblinding, not treated as automatic semantic agreement.
- **source-access.csv**: record access date, whether the original was inspected, version/drift issues, readability and any additional source fingerprints.
- **nominations.csv**: nominate missing passages, rejected pairings, omitted records or construct problems concerning the same ten families. Do not silently squeeze a new claim into an existing selected fragment.

Observation units are unique documentary fragments, not each case link. Shared sources appear once; two system families may be candidates for the same material. Coverage units are ten case-by-dimension slots for each case; compare the source corpus, not a hidden prior list of observations.

## Coding sequence

First inspect a source and its original page/section, then reconstruct what it establishes in your own words in `unit-notes.csv`. Classify the fragment, distinguish requirements from accounts and outcomes, and record the relevant event date rather than borrowing a filename or access date. For case-source and governance-source pairings, independently decide whether the pairing is defensible and at what scope.

The short excerpts do not necessarily contain every fact required for recoding. Follow original URLs and locators for surrounding text, dates, tables, definitions, versions and exceptions. A successful text retrieval, official hosting or quotation match does not establish an account's truth. If the original is inaccessible and the packet is insufficient, use an unresolved status; do not manufacture a code to complete a form.

For a case's coverage slot, decide whether the reviewed documents establish relevant evidence under that dimension, even if no selected fragment was originally allocated to it. Explain overlapping dimensions and nominate supporting passages. A supplier name can be present without an award; a general complaint route can be present without an AI-specific remedy. The coverage rubric counts relevant reviewed evidence, not verified compliance or operational success.

If text extraction is damaged, do not reconstruct it from a presumed conclusion. Use the original page, appropriate language expertise and recorded access details; otherwise mark the item unreadable/unresolved. Numeric tokens alone are not a complete operative-clause quotation. Separate document changes since collection from disagreement about the same frozen evidence.

## Response rules

Fill `reviewer_id`, `value`, `coding_status`, `rationale`, `evidence_anchor` and `source_access` for each assignment you can complete. `coding_status` is `coded`, `unresolved`, `unreadable`, `not_applicable` or `pending`. Only `coded` rows enter paired agreement calculations. Do not use `not_applicable` merely because a variable is difficult; explain why the task's premise fails.

“Unknown” or “Not established” is a substantive code where permitted, not a blank or a missing rating. Use it only after a sufficient review to conclude that the relevant date/evidence is not established. An inaccessible source is a review limitation, not evidence that a record or safeguard is absent. Keep the value blank for unresolved, unreadable, not-applicable or pending rows.

For financial stages, enter a JSON array of applicable defined labels; mixed stages are allowed. Keep source-stated amount text separately and do not repair a malformed total silently. For exact-date fields use ISO day/month/year where justified; preserve a stated interval as an interval and explain its basis. Do not assign the checking date to an undated event.

The packet contains no completed second-review results or gold answers. Freeze your completed ratings, notes, access log, nominations and declaration together, record their SHA-256 hashes, and return them to the coordinator before seeing any prior codes.
