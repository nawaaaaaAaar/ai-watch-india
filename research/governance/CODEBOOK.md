# AI Watch governance-layer codebook

Version 1.0.0, cutoff 5 October 2026. The first column of each table is its primary key. Arrays in JSON become JSON text in SQLite/CSV; nulls remain null in JSON/SQLite and empty in CSV. Do not count bridge rows, links, evidence excerpts or document versions as systems.

## Tables and interpretation

- **instruments**: One reviewed document/version. instrument_id is stable within the curated release; instrument_family groups known version chains, not a universal legal taxonomy. jurisdiction and jurisdiction_level identify territorial/institutional scope; an independent court is not a ministry. issuing_body is source-stated. instrument_type distinguishes strategy, guidance, rules, correction, order and procurement text.
- **instrument_domains**: Domain tags per instrument, used for discovery, not automatic legal applicability. domain_id joins instrument_id.
- **provisions**: Exactly five slots per instrument: Oversight, Evaluation, Procurement, Redress, Accountability and data. provision_id and instrument_id join the instrument; presence distinguishes a textual clause, contextual topic and not-established material. summary interprets only the reviewed text; provision_force inherits document legal effect. locator and evidence_id anchor a relevant passage when available. unknown_basis preserves missing/not-reviewed information. implementation_verified is false throughout this release.
- **sources**: Official primary URLs, titles, source type, is_cached, retrieval_basis, reviewed_text_sha256 and retrieved_characters. These hashes describe retrieved/extracted text, not original PDF bytes. snapshot is a bounded excerpt file added by the package builder.
- **instrument_sources**: Instrument/source relationship, including auxiliary official status records. Additional status evidence does not convert an outline-only record into full-text review.
- **evidence**: Selected quotation, locator, supports category, source_id, instrument_id and optional provision_id. Metadata passages also support scope/status/dates. A quote is not necessarily a normative clause.
- **system_links**: instrument_id to existing system_id, with link_type, rationale and applicability_determination. instrument_evidence_ids anchor the policy half; system_assertion_ids, system_source_ids and system_source_urls anchor the registry half. Arrays are validated against their respective release. A link means documented relevance at the stated strength, not certified applicability, compliance or implementation.
- **instrument_relationships**: Directed version/correction/implementation-reference relationships. Endpoints must exist; relation and note preserve whether a text replaces, corrects, consolidates or references another instrument. A technical-guidance reference does not automatically make the entire guidance statutory.
- **jurisdiction_coverage**: All 37 screened jurisdictions, initial query counts, included records and bounded-search limits. Inclusion count zero is not an absence claim.
- **candidate_decisions**: Thirteen important included/deferred/excluded candidate determinations with reasons. This is a selected decision register, not every search hit.
- **system_keys**: Immutable projection of all 144 existing system IDs, names, sectors, jurisdictions and owner IDs, with registry_version 1.3.0. This bridge permits joins without modifying the registry or reproducing all its assertions.

## Temporal and legal fields

instrument_date uses ISO day, month or year precision where established; date_precision states the precision, and date_text retains the actual source wording. date_basis explains that a source date, resolution date and Gazette publication can differ. A null or partial date must not be filled from a URL filename or upload folder.

document_status describes the reviewed document: draft/consultation; adopted/formally constituted; enacted/notified; historical/predecessor; historical mandate/renewal unverified; regulatory advisory; published recommendations/professional guidance/state strategy; procurement requirements/award unverified; and published/proposed/launch records with unverified adoption or commencement. legal_effect qualifies prescriptiveness independently. Do not recode every “published policy” as enacted law.

operative_status and commencement_text preserve explicit commencement dates or uncertainty. They distinguish staged commencement, superseded predecessors, drafts, conditional notification and unverified renewal. implementation_status is separate: none of this layer independently verifies operational activity, compliance, actual audits, expenditure or effectiveness. checked_date is the coding cutoff, not the last date a body operated.

review_depth differentiates full retrieved text with selected provisions coded, the General Financial Rules procurement window, and official-outline-only review. current_status_limit records version/adoption/retrieval caveats. coding_method identifies LLM-assisted extraction and single-analyst review rather than independent recoding.

## Joining and checking

Use system_links.system_id = system_keys.system_id. To inspect deployment evidence, join that key to systems in the separate registry database; parse system_assertion_ids and join to assertions.assertion_id. instrument_evidence_ids join evidence.evidence_id and then sources.source_id. Inspect the text and rationale before determining whether a jurisdiction/domain association applies to a specific implementation.

In SQLite, boolean fields are INTEGER 0/1. Arrays can be expanded with json_each. Primary and scalar foreign keys are declared in schema.sql and enforced during building; embedded array references are checked by the builder. queries.sql demonstrates status-aware and force-aware analyses without treating raw counts as prevalence.

CSV cells whose text begins with a spreadsheet formula trigger are prefixed with an apostrophe. JSON and SQLite are the canonical lossless structured representations. SHA-256 manifest entries validate payload bytes; baseline-registry.json checks that the earlier corpus is unchanged. quote-audit.json records normalized quotation membership and the per-URL excerpt budget, not the correctness of every interpretive summary.
