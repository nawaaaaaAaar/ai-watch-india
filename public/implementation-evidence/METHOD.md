# Implementation and procurement evidence: method

AI Watch implementation-evidence layer v1.0.0, checked 5 October 2026. This is a purposive ten-case deepening of the existing registry, not a new census, independent operational audit or legal-applicability assessment.

## Fixed population and selection

The 144 existing system families and the 52-document governance layer are frozen. The builder checks every earlier public registry and governance file against `baseline-layers.json` before packaging; it never writes to either folder. Bridge tables contain existing keys, not new system or instrument records.

Twelve existing candidates were screened: railway elephant IDS, railway VSS, NHAI DAS, Adalat.AI, CAG PARAS, CAG PARAKH, Safe Kerala, UPSC face authentication, Madukkarai elephant surveillance, IGMS, AskDISHA and MuleHunter.AI. Each received five comparable initial queries covering procurement, implementation/funding, evaluation/human review, redress and recent status, followed by two follow-up queries. Twelve further targeted queries pursued source chains. The retained search logs contain 96 queries and 575 hits. Queries, returned leads and failures are exported; search ranking is not a sampling frame.

The first ten candidates were retained because a bounded combination of official procurement material, orders, implementation accounts or accountable institutional sources could deepen their records. AskDISHA and MuleHunter.AI were deferred after screening, not classified as lacking evidence. Selection was not random, sector-balanced or based on operational success. CAG PARAS and PARAKH share one platform procurement; two existing family links do not become two procurements or independent corroboration.

## Retrieval, extraction and review

Official issuer websites, public-sector procurement portals, government-hosted releases, a district-court packet and the named state implementer's account were prioritised. Original URLs are attached to each selected excerpt. The packet's embedded supplier letter is supplier evidence hosted by a court, not a court certification of every supplier claim.

Fresh retrieval was attempted first, with cached SDK recovery when necessary. Each included document records retrieval basis, cache flag and SHA-256 of the reviewed extracted text. The hash is not authentication of the original PDF binary. Some successful responses contained cookie-only text and were not used as substantive evidence. Retrieval receipts retain errors and recovery phases. One earlier TCIL-only fetch was overwritten by the final batch script; the exported ledger is a retained-receipt log, not a claim to capture every network attempt.

LLM-assisted extraction generated 172 provisional observations from 36 documents. Analyst curation retained 124 observations from 33 documents, narrowed quotations, rejected cross-system material, corrected selected-passage mismatches and reviewed their paraphrases and limits. This is not independent second-review. The quote audit verifies whitespace-normalised membership of every selected excerpt in the reviewed extraction; it does not verify a source's truth, completeness, OCR accuracy or a paraphrase's legal interpretation.

For the large TCIL/NHAI RFP, IGMS RFP and Tamil Nadu policy note, extraction used targeted retrieved-text windows rather than exhaustive review of every clause. Other sources were reviewed for selected passages, not audited in full. No document-wide claim that a provision does not exist is made.

The Safe Kerala order's Malayalam font extraction is badly damaged. Original PDF operative pages 4–5 were visually inspected for funding, revised PMC/procurement and monitoring-linked payment clauses. Its selected numeric/English tokens are not a complete transcription; paraphrases are explicitly limited, not certified translations. Historical cabinet-note status and unverified Malayalam passages were not promoted into findings. Kurnool's damaged session-day text is retained as uncertain rather than corrected into a definitive event date.

## Units, links and evidence strength

- **Observation**: one dated or explicitly undated documentary statement, requirement, invitation or account, with a separate limitation. A document may support several observations.
- **Case association**: an existing system family linked to an observation. Contextual audit orders and general platform complaint/privacy routes are labelled contextual; named components are not silently equated to all installations.
- **Governance association**: an existing typed governance link, anchored to both the retained instrument evidence IDs and implementation observations. Exact primary-URL overlap is distinguished from inherited conditional relevance. No association certifies compliance.
- **Financial observation**: a source-stated estimate, sanction, bid security, reported cost or payment arrangement. These are not interchangeable, converted into spending, or summed.
- **Party observation**: a source-stated name and role, not a resolved corporate-identity register. Invitation, technical support, implementation account and supplier training letter remain distinct.

Evidence strength is categorical, not a numerical credibility score: formal prescribed requirement; procurement-stage invitation; first-party reported activity/outcome; implementer's historical account; institutional contextual evidence. Document type does not turn a claimed outcome into an independently verified one. No retained observation establishes independent outcome verification.

The ten dimensions are procurement, contracts/awards, funding, supplier, implementation, evaluation, human oversight, redress, data safeguards and operational status. All 100 case-by-dimension rows remain present. An empty observation list means “not established in the reviewed corpus,” not “does not exist.” An award described inside an implementation account remains an account, not an original award instrument. Contracts/awards coverage deliberately distinguishes such accounts from original executed documents.

## Reproduction and limits

Run `npm ci && npm run package:implementation && npm test && npm run build` in a clean repository checkout. Packaging is offline and deterministic, using frozen curation, source fingerprints, quote checks and baseline keys. It reproduces the release bytes, not future web retrieval results. The archive includes all twelve linked CSV tables, JSON, SQLite, runnable SQL, ten dossiers, selected excerpts, frozen inputs, logs, method, codebook and analysis, with a checksummed manifest.

Original full articles and PDF binaries are not mirrored. Public snapshots contain at most 250 selected words per original source URL; complete source text was reviewed privately where retrievable. Cached pages may lag the live issuer and official reports may be inaccurate or obsolete. Undated pages are not assigned the checking date as an event date. Tender deadlines and scheduled training are not evidence they occurred.

The old registry is unchanged even where this layer supplies qualifications or conflicting chronology. Researchers should join the new observations to old assertions and inspect their dates, scope and strength rather than silently overwrite them. Major remaining gaps include original awards and contracts, payments, acceptance reports, actual human-review logs, mismatch handling and AI-specific remedies. No external enquiry, paid service, public launch or independent reviewer was part of this cycle.
