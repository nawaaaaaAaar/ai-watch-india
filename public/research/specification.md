# AI Watch India: Product Specification

This specification describes a proposed policy-change workspace for journalism, governance research and decision preparation. It is an implementation plan, not a claim that the application has already been built or user-validated.

## Problem statement

The target problem is turning multiple official policy versions into an accurate, inspectable account of what changed and what remains uncertain. The worked DPDP example contains split/renumbered provisions, new retention language, changed recipient-specific duties, schedule changes and later corrections, demonstrating why a simple PDF summary or raw text diff is insufficient. [Draft Rules](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf)

Proposed primary users are digital-policy journalists and researchers; secondary users are public-interest organizations, legislative/research staff and people preparing organizational decisions. The frequency and cost of this problem have not been measured for these users, so the launch validation must establish both.

The product promise is: **find an important policy change, verify its source and limits, and turn it into a usable brief**. The name can remain AI Watch India, while the initial collection includes digital rules that materially affect algorithmic governance; scope should follow user tasks rather than force every document into an AI label.

## Goals

Goals below are proposed measurable outcomes, not achieved results. Baselines must be recorded before asserting improvement.

- **Accuracy:** At least 90% correct completion of a predefined comparison-task set by pilot users, with zero high-severity unsupported claims in reviewed exports.
- **Efficiency:** At least 25% lower median time to a correct, source-linked brief than a measured manual-reading baseline.
- **Evidence access:** At least 90% of pilot users can locate the original clause supporting a finding without facilitator help.
- **Return value:** At least three of an initial eight target users voluntarily return for another substantive task within two weeks.
- **Maintenance:** Each release reports reviewed coverage and source-check failures rather than presenting partial ingestion as comprehensive.

## Non-goals

- **Automated legal advice:** No individualized compliance verdict or definitive legal interpretation generated without qualified review.
- **All-India/all-policy coverage:** No promise of exhaustive national ingestion at launch; publish the exact collection and review coverage.
- **Autonomous publishing:** No generated allegations, social posts, external messages or automated public briefs.
- **Enterprise policy administration:** No staff acknowledgements, internal policy rollout or organization-wide compliance suite in the first release.
- **AI-first interface:** No general-purpose chatbot as the main experience; the core must work when model access is unavailable.

## User stories

- **Journalist:** As a digital-policy reporter, I want the changed wording and original pages together so that I can check a proposed story without relying on a summary.
- **Policy researcher:** As a researcher, I want renamed, split and moved clauses mapped across versions so that a numbering change does not look like a deleted obligation.
- **Decision preparer:** As someone writing a meeting brief, I want the actor, duty, exception and commencement basis visible so that future or conditional provisions are not described as immediately applicable.
- **Editor:** As an editor, I want evidence and interpretation separately reviewable so that an unsupported implication can be corrected without losing the factual change record.
- **Contributor:** As a contributor, I want to submit a correction with a source and reason so that changes improve the record without silently overwriting history.
- **Sensitive-workspace user:** As a researcher with unpublished material, I want local/private comparison by default and explicit control over external processing so that a document is not exposed by an ordinary action.

## Requirements

### P0: Complete first-release workflow

P0 is deliberately limited to one end-to-end workflow, rather than a national platform. Upload automation, live monitoring and expansive AI assistance are not prerequisites for first value.

| Requirement | Acceptance criteria | Dependencies |
|---|---|---|
| Official document family | Given a seeded policy family, when opened, then each document shows issuer, instrument identifier, status, language, official URL, document date, publication metadata, retrieval time and integrity provenance; unknown fields are explicit. | Verified acquisition and metadata review. |
| Immutable evidence | Given an acquired document, when a later source changes, then a new version is recorded and the prior object is preserved; binary and extracted-text hashes are distinguished. | Storage and acquisition worker. |
| Version relationships | Given a draft clause split into two final clauses, when compared, then both descendants appear with their shared source; the system does not call one descendant a wholly new duty solely because its number changed. | Reviewed mapping schema. |
| Clause-aware comparison | Given the seeded pair, when compared, then all final rules and schedules have a coverage state, including unchanged and unresolved; the default view may filter but never hide total coverage. | Extraction and reviewed alignment. |
| Evidence view | Given a change card, when its evidence is opened, then old/new excerpts, original pages or page links, clause IDs and text-layer warnings are visible. | Source-to-span mapping. |
| Corrected-text view | Given the final Rules plus corrigenda, when toggling as-printed/as-corrected, then each applied correction is attributed to its instrument and locator; underlying print is unchanged. | Correction layer and validation. |
| Text versus analysis | Given a card with commentary, when viewed or exported, then quoted text, analyst interpretation and reporting questions are separately labelled. | Structured card model. |
| Commencement context | Given an instrument using relative commencement, when dates are shown, then the formula, base-date source and calculation status are visible; disagreement cannot be silently resolved. | Event/date model and reviewer. |
| Review workflow | Given a candidate finding, when a reviewer approves it, then identity/role, timestamp and rationale are recorded; unapproved candidates remain conspicuously unreviewed. | Authentication and audit log for editorial deployment. |
| Search and filters | Given a query or actor/type filter, when applied, then the result set and total coverage update predictably; zero results shows a genuine empty state rather than generated content. | Local search index. |
| Brief builder | Given selected reviewed findings, when exported, then the Markdown brief contains exact locators, full source URLs, interpretation labels, uncertainty, date basis and review state. | Export templates and stable IDs. |
| Corrections channel | Given a reader reports an error, when submitted, then it enters a moderation queue and does not immediately rewrite a public finding. | Form/service or reviewed repository-issue flow. |
| Safe default | Given private text or files, when comparison starts, then nothing is sent to a model or published without an explicit choice; session data can be cleared. | Local processing or clearly disclosed private storage. |
| Failure transparency | Given a failed fetch, unreadable page, malformed table or unresolved mapping, when opened, then the workflow records the problem and blocks a “complete/verified” label. | Typed job states and release checks. |

### P1: Validated follow-ups

- **Local PDF/text comparison:** Given two supported files, when parsed, then progress, page coverage and limits are visible; unsupported/encrypted files fail safely. This follows the curated release because arbitrary-document structure needs separate validation.
- **Opt-in monitoring:** Given a selected official family, when a new source object is detected, then it creates an unreviewed candidate and notification draft, not an automatic published conclusion. Durable monitoring is a later explicitly authorized workstream.
- **Collaboration:** Given multiple reviewers, when edits conflict, then the system requires resolution rather than last-write-wins on evidence.
- **Annotated page overlays:** Given an evidence span, when viewed, then the page highlight corresponds to stored coordinates and can be independently checked.
- **Structured decision notes:** Given a change, when an action note is added, then owner, question and dependency are separate from legal text; no action is automatically taken.

### P2: Optional extensions

- **Assisted alignment/explanations:** Model suggestions cite supplied spans, remain candidates and are rejected if quoted text cannot be verified verbatim.
- **Hindi and other-language layers:** Translations retain source language and reviewer information; no claim of bilingual equivalence until validated.
- **Collection API:** Serve public reviewed records with version IDs, provenance and uncertainty fields, not only generated summaries.
- **Cross-policy dependency graph:** Link statutes, rules, orders, specifications and judgments after the relationship is verified.

## Success metrics and validation

### Measurement design

Recruit eight target participants: ideally four journalists, two policy researchers and two people preparing governance decisions. Recruitment and interviews have not yet occurred; participation should be voluntary and research materials should not require disclosure of confidential work.

Use a counterbalanced task study: participants perform comparable tasks with manual reading and with the proposed desk, varying order to limit learning effects. Include a separate existing-comparison-tool condition where feasible; record baseline completion time before claiming savings.

Score against an analyst-reviewed answer key. Suggested tasks are to identify the new retention clause, distinguish individual/Board breach-location requirements, map the split consent provision, identify one conditional exemption, apply a corrigendum, and explain the commencement uncertainty.

| Metric | Measurement | Proposed gate |
|---|---|---|
| Correct task completion | Scored answer key; unresolved legal questions credited when correctly identified as unresolved. | At least 90%. |
| Severe unsupported claims | Editorial audit of exported briefs; severity rubric defined before testing. | Zero. |
| Time to correct brief | Median elapsed time for successfully completed equivalent tasks. | At least 25% improvement over recorded baseline. |
| Source-location success | Can participant find the quoted original clause unaided? | At least 90%. |
| Actual usefulness | Participant identifies a real reporting/decision use and uses or requests another comparison. | Qualitative evidence, not only “looks good” feedback. |
| Voluntary return | Another substantive task within two weeks, excluding prompted walkthroughs. | At least three of eight. |
| Maintenance burden | Reviewer time per publishable finding, source failure rate and backlog age. | Set sustainable limits after pilot data; no invented baseline. |

### Go, narrow or stop

Proceed if accuracy gates pass, people use the exported evidence and maintenance is sustainable. Narrow the collection or workflow if only one persona benefits, if extraction dominates the burden, or if users prefer a simple curated brief.

Stop or reposition if the tool merely duplicates summaries, causes high-severity misinterpretations, or fails to outperform the users' existing combination of documents and comparison tools. Positive visual feedback alone does not validate the product.

## Open questions

| Question | Proposed owner | Blocking status |
|---|---|---|
| Is the primary launch persona a journalist or a policy researcher? | Product owner, informed by pilot users. | Blocks final prioritization, not local prototype. |
| Who can independently review consequential legal interpretations? | Editorial owner/qualified adviser. | Blocks public “reviewed legal analysis” positioning. |
| Which binary-archive permissions and reproduction conditions apply to each source? | Editorial/legal review. | Blocks public mirroring, not linking. |
| Should arbitrary uploads stay local or use a disclosed private backend? | Product/engineering owner. | Blocks upload architecture. |
| Is sustained monitoring desired, and through which channel? | Product owner. | Non-blocking for curated release; requires separate authorization. |
| What source list can be maintained reliably? | Editorial/engineering owner. | Blocks claims of coverage, not initial document family. |
| Is an optional model provider approved and affordable? | Product owner. | Non-blocking because the core is deterministic. |
| What is the definitive publication-date basis for the example's calculations? | Official clarification/qualified legal review. | Blocks definitive compliance countdowns, not documented ambiguity. |

## Information architecture and interaction

### Homepage

Lead with “Understand what changed. Verify what matters.” Present available policy families, the latest reviewed changes, collection coverage and last source-check status; do not imply a live national feed.

Every visible number must describe an actual quantity such as reviewed records, unresolved mappings or monitored sources. Do not display fabricated popularity, impact scores or estimated people affected.

### Policy-family page

Show an ordered lineage: consultation draft, notified final, corrigendum and separate commencement instrument. Include the issuer, document status and official links; commentary and news are distinct related materials, not instruments.

The page should let users choose which relationship to inspect. “Latest” alone is insufficient because the relevant question may be draft-to-final, final-to-correction, or wording-to-commencement.

### Comparison workspace

Use a three-panel desktop layout: provision navigation, old/new evidence and a reviewed analysis card. On narrow screens, use tabs with persistent provision identity instead of compressing two unreadable columns.

Provide filters for additions, removals, qualification changes, scope changes, timing, moves/splits, corrections and continuity. An unresolved filter is mandatory; moving content should not be displayed as an unexplained deletion and addition.

### Change-card anatomy

- **Identity:** Stable finding ID, policy family, old/new versions and mapped clauses.
- **Evidence:** Verbatim old/new excerpts, locators and official URLs.
- **Classification:** What changed textually and why it was selected.
- **Interpretation:** Potential consequence, expressly labelled and attributed.
- **Applicability:** Actor/class, recipient, conditions, exceptions and dependencies.
- **Timing:** Official formula, base-date evidence, computed date if defensible, and uncertainty.
- **Reporting questions:** Follow-ups, not allegations or automatically sent requests.
- **Review:** Draft/reviewed/disputed/retracted state, reviewer role and history.

### Brief builder

Allow selection of reviewed findings and arrangement into a report. Export source-linked Markdown first; offer a human-readable copy view and structured JSON/CSV where appropriate, with no invented citations.

Unreviewed findings can be included only through an explicit “working notes” export whose status is carried into the file. A public briefing must not lose uncertainty or source metadata during export.

## Technical design

### Recommended staged architecture

Start with a static public reader and curated structured data, plus an offline/local preparation pipeline. This makes a useful published collection possible without accounts, secret keys, model calls or a public file-upload service.

When arbitrary uploads are validated, add local PDF/text parsing where practical; if a backend is required, use a narrow extraction service, job queue and private storage with a disclosed retention policy. Do not start with an unrestricted URL-fetch endpoint.

Suggested implementation choices are TypeScript for the interface and schemas, a conventional React/Vite reader, and a Python extraction/comparison pipeline. These are design recommendations, not claims about installed or approved services.

### Pipeline

```text
Official source discovery
  -> approved acquisition and immutable document record
  -> extraction with page/geometry coverage
  -> language and document-structure segmentation
  -> candidate version mapping
  -> deterministic text/table differences
  -> candidate finding classification
  -> human evidence and interpretation review
  -> validated public records
  -> comparison UI and source-linked brief export
```

No stage may skip directly from scraped text to a public legal conclusion. Retry errors, incomplete pages and unresolved mappings remain explicit artifacts rather than disappearing from the collection.

### Minimum data model

| Object | Required fields |
|---|---|
| PolicyFamily | ID, title, jurisdiction, topic, issuer, collection status, latest source check. |
| DocumentVersion | ID, family ID, instrument type/number, status, document date, publication date and its evidence, official URL, acquisition time, binary hash if acquired, language, correction relationship. |
| ExtractedSpan | Document ID, page, clause path, text, coordinates if available, extraction method/version, extracted-text hash, quality flags. |
| VersionMapping | From/to spans, relationship type, candidate score if used, reviewer state, reason. |
| ChangeFinding | Stable ID, mappings, verbatim excerpts, change type, actor, recipient, condition, interpretation, sources, unresolved questions, review state. |
| Correction | Instrument ID, target document, exact locator, before/after strings, application state, reviewed target match. |
| CommencementEvent | Provision set, official formula, base-date candidates, cited instruments, computation method, confirmed/computed/disputed state. |
| ReviewEvent | Subject ID, action, reviewer role/ID, timestamp, rationale, predecessor revision. |
| Brief | Selected finding IDs/revisions, title, export date, review status, disclaimer, source references. |

Use stable internal IDs instead of assuming a rule number uniquely identifies the same provision across versions. A draft rule can map to multiple final provisions.

### Diff and alignment rules

- **Normalization:** Preserve raw text; remove only explicitly recognized layout artifacts in a derived layer. Dates, amounts, negations, exceptions, names and numbering must not be discarded as noise.
- **Alignment:** Use headings, clause paths and similarity to propose mappings; human review confirms split/merge/moved relationships.
- **Tables:** Compare identified cells and row keys, not flattened reading order. Flag structural ambiguity instead of generating confidently wrong change counts.
- **Safety-sensitive tokens:** Highlight changes to “shall,” “may,” “unless,” “except,” “and,” “or,” numbers, periods and actor/recipient definitions, but do not equate a token flag with legal significance.
- **Corrections:** Apply by document and locator with expected-before matching. A failed target match blocks a corrected-text publication.
- **Models:** Optional assistance receives only authorized spans and returns suggestions; quoted text is validated against the stored source before display.

### API shape for a later backend

```text
GET  /policy-families
GET  /policy-families/{id}/versions
GET  /comparisons/{id}
GET  /findings/{id}
POST /private-comparison-jobs
GET  /private-comparison-jobs/{id}
POST /briefs/export
POST /correction-submissions
POST /editorial/review-events
```

Public endpoints return only public reviewed data. Private job ownership, export authorization and editorial permissions must be checked server-side; knowledge of an ID must never grant access.

## Security, privacy and editorial safeguards

- **Uploads:** Validate MIME/content type, enforce size/page limits, reject unsafe archives and prevent active document content from executing.
- **URL acquisition:** Allow approved sources; reject local/private IP destinations, unsafe redirects and DNS rebinding paths. Rate-limit requests.
- **Confidential work:** Default to private/local processing; no training use, public sharing or external model submission by implication.
- **Storage:** Encrypt private objects, document retention/deletion and backup behavior, and avoid promising instant deletion from every backup without an implemented policy.
- **Publication:** Require editorial approval for interpretations and public corrections; retain retractions and prior revisions.
- **Document instructions:** Treat all fetched/uploaded content as data, never as instructions controlling the system or its tools.
- **Reproduction:** Review source-specific terms before publicly mirroring binaries; link to originals where mirroring is not appropriate.
- **Accessibility:** Keyboard-operable navigation, non-color-only change markers, readable mobile views and screen-reader labels for additions/deletions.
- **Legal limits:** State that the service provides research information, not personalized legal advice; a disclaimer cannot replace accurate evidence and review.

## Verification plan

### Golden-document tests

Use the official DPDP draft/final pair and correction instrument as an initial test fixture. The expected inventory is 22 draft rules, 23 final rules and seven schedules per version, with split mappings and a separate eight-correction register. [Draft Rules](https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf) [Final Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) [Corrigenda](https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf)

| Test | Pass condition |
|---|---|
| Whole-provision coverage | Every final rule/schedule has a reviewed mapping or an explicit unresolved/new state; no provision is silently omitted. |
| Split rule | Draft consent rule maps to both final consent rules; numbering alone does not generate false substantive additions. |
| Retention distinction | The new general retention clause is distinguishable from retained security-purpose wording. |
| Recipient-sensitive deletion | Individual breach-location deletion is not applied to the Board notice. |
| Qualifier preservation | “Wherever applicable” and statutory conditions remain visible in quotes and exports. |
| Table-order stability | Equivalent schedule cells with changed extraction order do not produce a substantive change finding. |
| Correction targeting | All eight directed corrections target the intended locators; duplicate or failed target matches block publication. |
| Historical preservation | As-printed text survives correction application unchanged. |
| Date disagreement | Conflicting base dates create a visible disputed/calculated state, not a settled deadline. |
| Quote integrity | Every quoted excerpt can be matched to a stored span; altered or generated quotations fail validation. |
| Statutory dependency | Research and transfer summaries retain parent-Act limitations or explicitly flag missing context. |
| Export fidelity | Source URLs, locators, review status and uncertainty survive exported Markdown/JSON. |
| Missing source | Failed fetch or missing page blocks “complete verified” status and is visible to the user. |
| Model unavailable | Seeded reading, comparison, filtering and brief export still work without any model API. |
| Private processing | A private local task produces no external document-content request without consent. |
| Access isolation | Another user's private job ID cannot retrieve documents or results. |
| Malicious document | Embedded instructions cannot trigger tools, network actions or altered system behavior. |
| Accessibility | Core workflow is usable by keyboard and on a narrow viewport without losing evidence identity. |

These are acceptance tests to implement, not tests claimed as already passed by an application. Only the research inventory/mapping script has been run in this study.

## Release plan and definition of done

### Research package: completed scope

The present package supplies the worked comparison, full provision coverage, correction register, source/interpretation distinctions, competitive context and product specification. It also includes raw machine comparison records with their limitations disclosed.

This is not a production release or a legal opinion. Repository changes, hosting and automated monitoring remain separate implementation actions.

### Complete curated first release

Deliver a working reader with the DPDP family, searchable reviewed findings, original/corrected evidence, version mappings and functioning brief exports. Include automated golden-fixture tests, a documented collection scope, a corrections workflow and a release checklist.

Definition of done: every visible control works; no invented analysis or citations; all 30 final provisions have an explicit state; correction and date caveats are preserved; tests pass; private data is absent from the public bundle; mobile/keyboard checks pass; and deployment/documentation are verified.

### Validation release

Run the planned user study and compare against existing ways of doing the task. Revise based on observed accuracy, task completion and repeat use, then decide whether arbitrary uploads or monitoring is the next useful expansion.

### Cost and ownership boundaries

Use a free-first, model-optional design and do not provision paid hosting or paid APIs without approval. Actual operating costs depend on document volume, OCR, storage, traffic and any chosen model usage; no fixed cost or Computer-credit estimate is asserted.

An editorial owner must maintain source checks and review quality. An engineering owner must maintain extraction/security and tests; both roles may initially be held by one person, but consequential analysis should obtain independent review before public claims of authority.

## Final positioning

The proposed product is not “all AI news in one place.” It is a policy research desk that turns a change in official wording into an inspectable, qualified and reusable reporting or decision artifact.

The strongest reason to build is the concrete workflow demonstrated by the official documents. The strongest reason to remain disciplined is that good comparison, notes, exports and policy tracking already exist; superiority must be earned through better task performance, not asserted through novelty language. [Draftable](https://www.draftable.com/draftable-legal-compare) [Diffchecker](https://www.diffchecker.com/word-pdf-compare/) [PolicyDhara](https://varnasr.github.io/PolicyDhara/) [DPDP reference](https://dpdprules.org/rules)
