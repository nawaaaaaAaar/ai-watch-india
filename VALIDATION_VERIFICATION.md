# AI Watch: methodological-validation pack verification

This release prepares a second researcher to challenge the ten implementation/procurement cases. It does not complete independent recoding, certify source claims or estimate empirical reliability. The system registry remains at 144; no systems, instruments or procurement findings were added to the underlying datasets.

## Release inventory and handoff

- **Reviewer pack:** `public/validation/reviewer-pack.zip`, with fourteen archive entries, including twelve payload files and manifest/checksum. It contains ten case identities, 39 unique original-source URL records, 169 bounded source fragments, eight candidate governance-instrument references, 316 review units and 992 blank long-format rating positions.
- **Coordinator kit:** `private-validation/manager-kit.zip`, with seventeen archive entries, including fifteen payload files and manifest/checksum. It includes original reference codes, linkage key, qualitative reference, twelve explicitly retrospective financial-stage projections, comparison tooling, synthetic tests and a 33-observation source-check sample.
- **Review variables:** fourteen variables, thirteen comparable with the existing first-analyst reference and one diagnostic-only coverage variable. The 992 assigned positions comprise 892 comparable and 100 diagnostic positions. These are task counts, not independent observations or completed ratings.
- **Task types:** 124 observations, 33 document-date tasks, 36 case-source association tasks, 100 case-dimension coverage tasks, twelve financial tasks and eleven governance-link tasks. Shared documentary observations remain unique rather than being duplicated for each associated case.

Give the second researcher only the reviewer ZIP. Keep the coordinator kit and comparison outputs separate until the independent submission is frozen. The coordinator kit is Git-ignored and outside `public/`; it was not pushed to GitHub or included in the production website bundle. It is supplied privately to the owner and can be rebuilt locally.

## What is and is not blinded

Reviewer forms contain no prior assigned values, original interpretations, baseline codes, linkage key or original dataset identifiers. Tasks use opaque, deterministically shuffled identifiers and require independent reconstructions, evidence anchors, source-access records, an exposure declaration and nominations of omitted or insufficient evidence.

This is conclusion-blinding, not identity-, sampling- or access-control blinding. System names and original URLs are necessary for verification; existing public analyses remain discoverable. The first analyst selected the ten cases and bounded excerpts. A reviewer with prior exposure must disclose it, and cannot be described as an unexposed blinded coder. Deterministic masking is not a secrecy mechanism.

Source fragments are capped at 250 selected words per original URL. Opening-context inputs preserve source-text hashes and membership checks, but hashes authenticate frozen extracted text, not PDF binaries or institutional truth. Original documents are linked, not mirrored. Missing context, version drift, unavailable originals or damaged Malayalam extraction may require unresolved/unreadable ratings and additional passages nominated by the reviewer.

## Construct defect and other weaknesses to test

The old coverage flag records primary-dimension allocation; the review rubric asks whether relevant evidence occurs anywhere in the case corpus. These are not equivalent constructs. The engine therefore labels their matches/disagreements diagnostic only and suppresses coverage kappa. Comparable coverage reliability requires a fresh first-analyst recoding under the same rubric, frozen as a new version before comparison.

Other priority risks are overlapping primary dimensions; evidence-strength categories that mix document authority, speech act and procedural stage; event versus publication/effective dates; version-versus-scope judgments; retrospective financial-stage projections; supplier/entity identification; general versus system-specific oversight/redress; and governance association versus legal applicability or demonstrated compliance. Constant “Not established” verification flags cannot supply informative reliability merely through matching labels.

The full critique is `research/validation/methodological-weaknesses.pplx.md`; the sixteen-row vulnerability register is `research/validation/vulnerable-variables.csv`. The review is designed to test construct clarity, interpretation and source sufficiency, not only transcription.

## Comparison and adjudication

The standard-library comparison script joins unique unit-variable keys, validates allowed values and required rationales, and rejects duplicate/unknown keys, incompatible reviewer identities and malformed submissions. Explicit unresolved/unreadable/pending statuses are unpaired rather than imputed. Substantive “Unknown” or “Not established” labels remain distinct from missing ratings.

Nominal variables receive observed agreement, Cohen's kappa, marginals and confusion tables; exact-date/amount comparisons are explicitly format-sensitive, and financial-stage sets receive exact agreement and Jaccard similarity rather than nominal kappa. No aggregate quality score, universal threshold, naive row-wise confidence interval or significance test is reported. Category prevalence and nonrandom missingness can affect interpretation, and agreement does not establish validity ([Hallgren](https://pmc.ncbi.nlm.nih.gov/articles/PMC3402032/), [de Raadt and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC6506991/)).

Qualitative reconstruction, parties, human oversight and remedies require human source review rather than string-similarity scoring. The coordinator workflow reviews disagreements, unresolved items, nominations and a preselected source-check sample, including matching ratings. Adjudication records causes, evidence, rationale, named decision-maker, date and both coder acknowledgements. Consensus is a separate export; initial responses and pre-adjudication agreement are retained. Decisions do not automatically modify AI Watch.

## Verification results

- **Preservation:** all 619 frozen files match their original hashes: 605 prior public registry/governance/implementation-evidence files and fourteen application-source files. System count is unchanged.
- **Automated suite:** all 214 Node tests passed locally and in the remote checkout. The suite includes a runner for 24 Python synthetic statistical/adjudication tests; those are not an additional independent research pass.
- **Archive workflow:** all ten extracted-archive checks passed, including standalone synthetic tests, blank-form handling, keyed joins, diagnostic coverage suppression, one deliberately changed label, separate consensus and unchanged initial input bytes.
- **Empty submission:** the real reviewer template has zero paired ratings; observed agreement and kappa remain null, with a waiting-for-second-review state. All completed responses used for verification were synthetic fixtures only.
- **Reproduction:** a fresh remote checkout rebuilt both archives byte-for-byte and left tracked files clean. An explicit regression test also rebuilds across Python hash seeds 101 and 202.
- **Blinding and packaging:** reviewer ZIP has no baseline/key/prior classifications; both ZIPs match their payload manifests. Rebuilding refuses to overwrite edited responses or unknown files in a pack folder.
- **Build:** TypeScript and Vite production build passed. Existing JavaScript/CSS bundle names remain unchanged; the pre-existing approximately 1.64 MB JavaScript chunk warning remains. No coordinator key, baseline CSV or owner ZIP appears in the website bundle.

The first clean-checkout attempt exposed unordered-set iteration in the coordinator archive. Sorting candidate instrument and source-anchor identifiers fixed the defect; the cross-hash-seed test guards against recurrence. No cosmetic UI work or deployment was performed, so the existing private preview is unchanged. No public launch, paid services or external enquiries occurred.

## Reproduction commands and checksums

Implementation commits: [initial pack](https://github.com/nawaaaaaAaar/ai-watch-india/commit/7e22fe6bddae108683907c8407cecb6f1eda696f) and [deterministic ordering fix](https://github.com/nawaaaaaAaar/ai-watch-india/commit/02263403297f299a3050a091261d622cb9b29678).

```sh
npm ci
npm run package:validation
npm test
python scripts/verify_validation_archives.py
npm run build
sha256sum public/validation/reviewer-pack.zip private-validation/manager-kit.zip
```

Reviewer ZIP SHA-256: `0ed63e9afc9c5e52bf685d1876759d0784ce6872c224d00cc8718ef501f1fdf6`

Coordinator ZIP SHA-256: `c7be278f1456ba410db8756516701a359829a7680b48dfb587e2d3832fd6c476`

For an actual returned submission, follow `research/validation/manager/COORDINATOR.md` and `AGREEMENT_METHOD.md`. Freeze reviewer files and their hashes before unblinding; retain the exposure declaration and source-access log. This cycle is complete as a verified review infrastructure release, not a completed independent validation study.
