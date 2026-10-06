# Implementation-evidence codebook

Version 1.0.0. Keys join to AI Watch registry v1.3.0 and governance v1.0.0 without modifying either layer. SQL foreign keys enforce scalar joins; JSON-array joins are additionally validated by the builder.

## Tables and units

| Table | Primary key | Unit and interpretation |
|---|---|---|
| cases | system_id | Ten selected existing families; rationale, baseline stage, change in understanding and limits. |
| documents | document_id | Thirty-three original document/page URLs with issuer, source role, dates, scope, retrieval and text hash. Not thirty-three contracts. |
| observations | observation_id | 124 bounded statements, requirements or accounts; document, excerpt, dimension, event date, categorical strength and limitation. |
| case_observations | case_observation_id | 136 links from observations to ten existing systems, with old assertion IDs. Shared CAG observations have two system links. |
| evidence | evidence_id | One selected passage and locator per observation; URL and verification mode. |
| party_observations | party_observation_id | Source-stated party name and role, not independent corporate identity or awarded-vendor status. |
| financial_observations | financial_observation_id | Source-stated monetary text and stage/type; no spending inferred or aggregation permitted. |
| coverage | coverage_id | All ten dimensions for every selected family; observation arrays and specific unresolved-record requests. |
| governance_links | governance_link_id | Eleven retained associations, with existing governance link IDs, instrument evidence IDs and implementation observation IDs. |
| selection_decisions | selection_decision_id | Twelve screened existing candidates; ten included and two deferred, with rationale. |
| system_keys | system_id | Join projection of all 144 existing registry keys; not additional studied cases. |
| governance_keys | instrument_id | Join projection of all 52 existing governance documents; not new policy research this cycle. |

## Field rules

- **document_date / event_date**: ISO day, month or year when established; otherwise null. `date_text`, `date_precision` and `date_basis` distinguish publication, effective date, referenced tender and reported event. Null is not a zero or a checking date.
- **claim_type / evidence_strength**: read together. A prescribed test threshold is not a measured result; first-party timing, coverage and award statements are accounts. Contextual routes are not model-specific redress.
- **independent_outcome_verified**: false throughout this release. This does not assert that independent studies do not exist elsewhere; it means none is established by these retained observations.
- **current_version_match**: identifies continuity limits, especially the older UPSC tender versus the later own application. A common family key alone is not proof of the same contract or model version.
- **quote / verification_mode / passage_match**: the selected excerpt matches the reviewed extraction after whitespace normalisation. Safe Kerala adds a bounded original-page visual check; numeric tokens are not full operative-clause quotations.
- **amount_text / amount_kind**: retain source formatting, including malformed printed totals in the associated statement. Currency is INR; no canonical spending total is computed. Bid securities are not project finance, and sanctions are not disbursements.
- **role_text / identity_resolution**: keep invitation, stated implementer, technical support and training provider distinct. Legsys Foundation and private-limited names remain unresolved; an attended launch does not establish a supplier.
- **coverage.evidence_status**: “Primary records reviewed; strength/stage varies” is not a yes/no compliance finding. “Not established in reviewed corpus” requires inspection of the specific record request.
- **governance_links.link_type**: common original primary document is stronger identity evidence than inherited policy-domain relevance. `applicability_determination` is preserved from the existing governance layer; `compliance_verified` remains false.

## Formats and analysis

CSV array fields contain JSON text. Empty CSV values represent JSON nulls; SQLite nulls remain null and booleans are 0/1. CSV strings beginning with formula-control characters are prefixed with an apostrophe for spreadsheet safety; JSON/SQLite retain the unmodified value. `schema.json` lists columns, array fields and foreign keys.

Use `queries.sql` for stage, case coverage, party/finance and governance joins. Count distinct observation IDs when analysing shared CAG evidence; count distinct document URLs when counting sources. Do not use 144 bridge keys or 52 governance keys as this cycle's research denominator, and do not interpret the ten purposive cases as national prevalence.
