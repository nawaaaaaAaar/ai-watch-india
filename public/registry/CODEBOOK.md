# AI Watch: institution-and-system data codebook

Version 1.3.0, India documentary cutoff 5 October 2026. Read the protocol before drawing inferences; the 144 families combine seed, institutional, broadening and scaling cohorts, not a national census or 144 verified live AI deployments.

## Fourth-cohort interpretation

`research_round` values 1.0.0, 1.1.0, 1.2.0 and 1.3.0 select 18, 18, 36 and 72 records respectively. `system_kind` distinguishes citizen-facing service, internal decision support, enabling/foundation infrastructure, statutory-body information, private redevelopment communication and historical research/defence capability. Exclude inappropriate units before describing deployment patterns.

New `sources.retrieval_basis` and `sources.is_cached` report the actual extraction/recovery basis. Missing values on old rows do not mean fresh live verification; consult inherited source-recheck/log scopes. Repeated original URLs can have different release-specific source records; count records and unique URLs separately. `snapshot_sha256` covers selected UTF-8 excerpts, not original PDF authentication.

All 1,728 assertion slots are retained. `Not verified` is not a negative finding; `Partial` carries version, timing and enforcement limits. The older source/assertion recheck tables cover only their original baseline, not all new fields. New checksums validate original row preservation and quoted-text membership, not independent coding agreement.

## Files and identifiers

`data.json` includes metadata plus twenty-one table arrays. Each corresponding CSV is UTF-8 with a header; blank fields represent null, never zero. SQLite preserves nulls and enforced non-polymorphic foreign keys. JSON is authoritative for native types; CSV formula-like leading strings receive an apostrophe for spreadsheet safety. `schema.json` lists actual columns. Primary keys are the first column of each table.

Stable system identifiers are manual labels; other IDs use deterministic SHA-256 prefixes of the defining text. These are database identifiers, not company numbers or official registration IDs. A changed defining observation can acquire a new ID; do not treat hashes as proof of source truth. `evidence_links` uses a generic record type/key relationship validated by the builder and tests.

## Core tables

- **systems**: `system_id`, name, owner institution ID, sector, jurisdiction, documentary stage, latest dated record, AI basis/class, checking date and selection/unit notes. Explicit AI attribution includes vendor/editorial sources: it does not mean government or independent validation. Ten qualified biometric/analytics contexts lack established system-specific AI identification in the reviewed records; BODH has a separate evaluation-infrastructure class. `frame_id` is a documentary association, not ownership. `research_round` distinguishes the eighteen 1.0.0 seed, eighteen 1.1.0 institutional and thirty-six 1.2.0 broadening additions. `system_kind` prevents evaluation infrastructure from masquerading as clinical use. A stage is documentary attribution, not a site visit. `legacy_id` links the six inherited cases; null for new cases.
- **institutions**: institution ID, name and legal-identity qualifier. Names remain as stated; historical `L & T Infotech Ltd` is not silently replaced by a current corporate successor. Multi-agency responsibility stays in roles rather than being guessed into a single vendor.
- **system_institutions**: role ID, system ID, institution ID and source-backed role. Technical partnership does not establish an executed current procurement agreement.
- **system_links**: relation between two included systems, with source and limits. A developer-reported BHASHINI integration is not a reviewed live contract.
- **deployments**: event/observation ID, system ID, event date, date precision, documentary stage, place and description. Null events can hold a mixed-date narrative or an undated interface observation without assigning an invented launch date. Separate May and August airport availability is chronology, not two different Digi Yatra systems.

## Procurement, evaluation and safeguards

- **procurements**: record ID/type, system, reported agreement/award date, amount in INR, amount type, supplier label/institution if established, description and current-deployment linkage limit. Records include an allocation, an announced signed historical contract, a news-reported regional award, an official developed-cost statement and a cabinet-approved estimate. These are not five independently verified executed current contracts. `189900000` INR is the disclosed arithmetic sum of 7.85 and 11.14 crore, not a national IDS budget. Delhi's approved estimate is not spending; SANJAY's official developed cost is not reconciled expenditure.
- **evaluations**: record ID, system, evaluation type, sample number/unit, setting, current-version match, result summary and optional evidence status. A specification row explicitly says “not measured”; inherited cases retain evaluation-related descriptions with their gaps. Count or filter actual study types before any study inventory claim.
- **metrics**: record ID, system, metric name, numeric value, optional `value_upper`, unit, kind, measurement scope, denominator and value qualifier. CATB's reported 12–16% range is stored as numeric lower/upper values, not as diagnostic accuracy. A “more than” lower bound is not an exact observed value. A maximum specification threshold is not an observed error rate. A study's total sample is not automatically the denominator of every diagnostic metric.
- **controls**: source-described safeguard, source/implementation basis, description and optional evidence status. Historical requirements, published grievance contacts and human oversight language are not verified enforcement or successful remedies.
- **policies**: policy ID/title and documentary status, only for curated direct system documents in this registry. Not an exhaustive law inventory.
- **system_policy_links**: system-policy relationship with limits and source. Related earlier policy collections remain outside this dataset's system denominator. This table does not assert every provision is applicable or complied with.

## Coding and provenance

- **assertions**: assertion ID, system, accountability field, narrowly worded value, evidence status, checking date and coding basis. Every system has twelve slots, so omissions are not hidden. An empty evidence link for `Not verified` is an explicit research gap, not a fabricated supporting source.
- **evidence**: unique normalized selected excerpt, source ID and analyst locator. Excerpts are text selections, not OCR-certified full documents; use the original URL for full context.
- **evidence_links**: link ID, record table, record primary key and excerpt ID. Many-to-many: a claim can have several sources and one excerpt can support several observations. Join through this table; do not count links as independent corroborating sources.
- **sources**: ID, original URL/title, source type, source-stated publication date or null, date basis, checked date, selected-snapshot path/SHA-256 and hash basis. Hashes cover selected text snapshots, not original PDF bytes. Retrieval metadata and unreviewed links are recorded separately in the log.
- **issues**: source-backed uncertainty, numerical inconsistency, unresolved scope or evaluation/current-status limit. Missing evidence is not a wrongdoing finding.
- **candidate_decisions**: included/context/excluded candidate and reason; not a national candidate universe or complete inclusion-flow diagram.

## Institutional coverage and rechecks

- **institution_coverage**: fixed frame ID, institution ID/name, four base-query dimensions, date, completed-search status and boundaries. Five ministries plus the independent Supreme Court, not all government bodies.
- **coverage_systems**: associative table linking 26 records to the six frame entries. Ten earlier cases remain outside the frame as context. This association is not an ownership or exhaustive-coverage assertion.
- **source_rechecks**: fifty baseline-source fresh retrieval/text-match attempts, raw HTML fallback and separate cached retries. `matched_excerpts` counts fresh cleaned/raw matches; `cached_retry_matches` does not promote archived extraction to current availability. Nested excerpt decisions retain clean/raw outcomes. Null/error is not a correction finding.
- **assertion_rechecks**: structural/source-availability triage of all 216 baseline assertion slots, not independent semantic recoding of the expanded 432 fields. Explicit unknowns remain unknown. Claims can retain valid earlier documentary evidence even when current retrieval fails.

`INSTITUTION_SEARCH.json` and `INSTITUTION_RETRIEVAL.json` are thin second-round receipts. `SOURCE_RECHECK.json` duplicates the baseline recheck register as a convenient standalone file. None republishes full original articles or PDFs.

## Accountability field meanings

The fixed order is owner/purpose; decision role/affected people; deployment/date; procurement/supplier; funding/contract; data/integration; evaluation/errors; human review/overrides; privacy/retention; complaint/appeal; public outputs/access; current-status limits. “Documented” establishes the documentary statement as worded, not effectiveness or compliance. “Partial” records a meaningful unresolved limit. “Not verified” means not established in the reviewed material. “Conflicting sources” preserves unreconciled descriptions.

## Safe joins and calculations

`systems → assertions → evidence_links → evidence → sources` reproduces a coded statement's source trail. Filter `record_type='assertions'` before joining assertion IDs. Other tables use their own record types. `queries.sql` contains runnable examples and warns against counting many-to-many links as systems.

Monetary values are INR, not crores unless explicitly in narrative; `1 crore = 10,000,000`. Do not sum allocations with award values or compare budgets whose components and periods differ. Usage measures are not unique people. No pooled accuracy statistic is valid across metrics with different tasks, samples, thresholds or model versions.

## Rights, privacy and reuse

Repository code follows any repository licence actually supplied; this release does not invent a licence for upstream documents or grant rights it does not own. Use research coding with attribution to the release and respect original-source rights. Only limited selected excerpts and hashes are redistributed; original PDFs/articles are linked, not mirrored. No citizen-level personal dataset is included. Do not turn published contacts into automated complaint submissions.

## Versioning and validation

Rebuild using `npm run package:registry`, then `npm test` and `npm run build`. The offline builder uses the checked-in curated inputs and inherited source corpus; no API keys or network retrieval are required. The checksummed archive includes the research docs and receipts. Reproduction establishes that data and outputs match the release, not that a deployment is safe, operational today or independently audited.
