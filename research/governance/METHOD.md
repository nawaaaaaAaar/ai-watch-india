# AI Watch: linked India AI governance layer

Release 1.0.0; research cutoff 5 October 2026. This is a source-linked, exploratory governance dataset, not a legal opinion, national policy census or operational audit. The existing system registry remains version 1.3.0 with 144 system/service families; this cycle adds no systems.

## Question and units

The research question is: what formal governance texts can be connected to the purposes, jurisdictions and documentary histories of the existing system records, and what do those texts actually say about oversight, evaluation, procurement, redress and accountability? An instrument record is a reviewed document/version, not necessarily a unique policy family. Drafts, final texts, corrections, consolidated copies, commencement notifications and predecessor documents remain separate, connected through instrument_relationships and instrument_family.

There are 52 instrument records: 37 central/national or independent-judiciary records and 15 subnational records from 14 jurisdictions. They include national AI strategies and responsible-AI guidance, constituting orders, state AI policies/strategies, AI-specific regulator material, deployment-relevant cross-cutting instruments and one named-system court order. They do not all impose AI-specific legal duties. General procurement, biometrics, data protection, cybersecurity and clinical guidance were included where their subject matter provides a concrete deployment-governance connection.

## Coverage and screening

The fixed geographical screening frame is the Centre, all 28 states and all eight union territories. Each subnational jurisdiction received two initial AI-policy/strategy searches. Central searches covered AI governance, responsible AI, public procurement, data protection, synthetic media, biometrics, banking/securities regulation, health and judicial use. Follow-up searches resolved primary text, adoption, dates, corrigenda and recent sector guidance. The retained search log contains 157 query receipts and 948 result hits; the retrieval log contains 136 attempts/recovery receipts, including errors and OCR provenance.

The coverage register records each of the 37 jurisdictions even when no instrument was included. Follow-up depth varies with leads and retrieval success. “No instrument included” means none was verified and included by this bounded procedure, not that the jurisdiction has no policy. The 13 candidate-decision rows document important exclusions/deferments; they are not an exhaustive adjudication of every search hit. Search leads remain available separately. This is not a complete Gazette crawl, legislative database, ministry census or collection of every general law affecting AI.

Inclusion requires an identifiable government/official issuing-body source and a formal policy, strategy, guideline, regulation, constituting decision, procurement requirement or similar governance instrument with a material AI-deployment connection. Four records are deliberately outline/announcement-only: TPEC, ICMR ethical guidance, the draft National Data Governance Framework and Uttarakhand's announced mission. No detailed clauses were invented for them. Forty-seven other records were coded from full retrieved text; the General Financial Rules record used the procurement chapter window of the retrieved full text.

Examples of deferred material include inaccessible UGC guidance, March 2024 MeitY advisories available only through secondary mirrors, and state announcements without a verified underlying order. School AI curricula, investment promotion and generic digital programmes were not automatically treated as AI-deployment accountability instruments. State IT policies were included only with a stated AI connection, with general incentive/administrative mechanisms clearly distinguished from safeguards for affected people.

## Primary sources and extraction

Search results identify candidates; substantive coding uses fetched official document text or explicitly labelled official outlines. Original primary URLs, retrieval basis, cached status, retrieved-text character count and SHA-256 are recorded. Fresh retrieval failures were followed by supported cached recovery where available. A successful cached extraction is neither proof of current availability nor current legal force.

Rajasthan's initial official presentation was not treated as the full policy. Its actual 53-page scanned policy was located through the official site. After the supported content fetch failed, the official binary was retrieved as a documented fallback and OCRed. Selected accountability and procurement/redress pages were visually checked against page images. OCR/page numbering and this limited visual check are disclosed; this is not page-by-page legal authentication of the entire PDF.

Full fetched text and original PDF binaries are not mirrored in the public package. It contains bounded selected-excerpt snapshots, source URLs, retrieved-text hashes and attempt receipts without raw full-page content. A hash of retrieved text is not a hash or authentication of the original document binary. The 289 evidence rows are selected passages, not a full-text corpus; selected quotations are capped at 250 words per original URL. Normalized exact text membership was checked, retaining footnote/OCR artefacts rather than silently repairing quoted wording.

## Coding, temporal status and unknowns

Provisional structured extraction was LLM-assisted, followed by a single-analyst review, targeted full-text checks, quotation corrections and status/date adjudication. Important corrections included Meghalaya's general policy-operation dispute route, Gujarat's elapsed taskforce mandate, Maharashtra's covering adoption resolution versus a draft-labelled annexure, and Sikkim's draft consultation despite adoption-like wording in the draft. No independent second reviewer has recoded the release.

Each instrument has jurisdiction, issuer, type, date and precision, date wording, document status, legal effect, scope, AI domains, operative-status/commencement wording, implementation status, review depth and current-status limits. Publication, formal adoption, legal commencement and observed implementation are separate questions. Dates are not inferred from upload folders, filenames or search-result timestamps. Partial dates and nulls remain explicit. A publication year is not a verified notification day.

Each instrument retains all five coding dimensions, including unknowns. “Textual provision” means the reviewed text contains a relevant clause, not that the clause is binding, sufficiently protective or implemented. Recommendations and draft clauses inherit their non-operative force. Targets, programme grievance use cases and policy-incentive disputes are context, not automatically evaluation findings or AI-harm remedies. “Not established” refers to the reviewed material, not proven institutional absence.

The DPDP instruments retain staged commencement text without prematurely treating all duties as in force. The synthetic-media amendment preserves its stated effective date. Gujarat's original one-year taskforce term is historical/renewal-unverified at the cutoff. No instrument is labelled operational merely because it has been issued; the layer has no independently verified implementation/compliance observations.

## Linking to the frozen registry

There are 95 instrument-to-system associations. Each includes an instrument-side evidence anchor and existing registry assertion/source anchors, a link type, rationale and applicability limitation. The 144-row system_keys table is a join bridge to the unchanged registry, not 144 new systems. Join on system_id; join existing assertion IDs back to public/registry/data.json or the registry SQLite database.

An explicit named court direction is distinguished from named-system procurement requirements, jurisdictional policy context, conditional cross-cutting scope and draft relevance. General clinical/biometric/data-protection links do not determine device classification, legal scope, factual processing or compliance. A procurement EOI is not an award or implemented control. Regulations addressed to SEBI-regulated entities are not automatically attached to SEBI's own analytic/chatbot tools. Instruments without a defensible system link remain in the catalogue rather than being force-linked to increase coverage.

## Reproduction and reuse

From a clean repository checkout, run `npm ci`, `npm run package:governance`, `npm test` and `npm run build`. Packaging is offline and deterministic, using the frozen curation, methods, logs and baseline hashes in research/governance. It does not need live model/search calls or credentials. This reproduces the curated release, not the original web-search ranking or the legal truth of every source statement.

Download complete-governance.zip, data.json, dataset.sqlite or the individual CSVs from public/governance. JSON preserves arrays and nulls; CSV uses JSON-encoded arrays, empty nullable cells and spreadsheet-formula escaping; SQLite stores arrays as JSON text and nullable values as NULL. schema.json lists columns and foreign-key declarations. queries.sql is runnable against the SQLite database. Source snapshots and 52 instrument dossiers expose both evidence and limitations. The manifest covers each payload file; its checksum and the deterministic ZIP support integrity checks.

The public curation input, builder source, logs and codebook are in the package. A full combined analysis can attach the separately downloaded system registry SQLite database, retaining its own version and provenance. All original public/registry files must match the frozen baseline before packaging; a failed comparison aborts the build.

## Boundaries

Coverage is purposive within a systematic geographical screen, not representative of Indian governance or deployments. The five dimension slots cannot be pooled as a compliance score. Outline-only records, cached recoveries, conditional links, blocked sources, unverified adoption/commencement and single-analyst coding remain visible. Absence of an instrument, link or provision in this collection is not proof of absence outside it. Independent legal review and independent recoding are still needed before high-stakes use.
