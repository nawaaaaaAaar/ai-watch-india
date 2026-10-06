# AI Watch validation coordinator guide

Distribute only `reviewer-pack.zip` to the second researcher. Keep `manager-kit.zip`, the old analyses, baseline codes, linkage key and comparison outputs separate until the independent pass is frozen. Both archives are owner deliverables, not a combined reviewer handoff.

## Locking and comparison

Record reviewer identity, independence/familiarity declaration, language competence and protocol version. A person already familiar with the published conclusions can still audit them, but must not be reported as an unexposed blinded coder. This public repository does not provide access-control blinding; distribution and exposure declarations are essential.

The opaque key and original-to-review mappings live only in `key.json`. `baseline.csv` is the first analyst reference, not a gold standard. Most values map directly from the published layer; false verification flags are operationalised as “Not established,” not proof of negative outcomes. Financial-stage sets are explicit retrospective first-analyst projections of twelve free-text type fields. Their provenance is documented in `baseline-projections.json`, and disagreements can challenge the projection as well as the source.

The baseline coverage flag records whether an observation was allocated to that dimension in the first release. The review coverage rubric deliberately asks about relevant evidence anywhere in the reviewed case corpus. Disagreement here may reveal a dimension-allocation/coverage construct defect, not simply coder error. Document the mismatch rather than turning an empty slot into evidence of institutional absence.

The engine treats coverage comparisons as construct diagnostics and suppresses their kappa. Do not relabel diagnostic matches as reliability; comparable coverage agreement requires a separate first-analyst recoding under the same new rubric and a versioned reference/schema.

Ask the reviewer to return ratings, qualitative notes, source access log, nominations and declaration before unblinding. Preserve originals and hashes. Run:

```sh
python compare_coding.py \
  --reference baseline.csv --review /path/to/reviewer/ratings.csv \
  --schema /path/to/reviewer/variables.json \
  --units /path/to/reviewer/units.csv --out /path/to/comparison
```

The untouched template produces zero paired ratings and a waiting-for-review report, not a reliability result. Incomplete/unresolved rows are reported separately, not imputed or treated as unknown codes. Missing or duplicate row keys, invalid codes and absent coded-row rationales are errors. For a deliberately incomplete submission use `--allow-partial`; coverage loss is still reported.

## Qualitative validation

After the pass is locked, compare `unit-notes.csv` against `qualitative-reference.json` for reconstruction, parties, human oversight, remedies, version continuity and limits. The tool does not pretend string similarity measures semantic truth. Review nominations for omitted clauses, mismatched units, rejected associations and source drift; additions require explicit review and remain within the ten existing families.

Inspect all disagreements and all unresolved/unreadable items. Also independently check the preselected control sample, including its agreed ratings, because agreement does not establish validity. `control-check-sample.csv` selects one observation per original document deterministically before B's responses are known; those items are not assumed to agree. Record which source review was actually completed, not just the scheduled sample.

## Adjudication workflow

First classify the disagreement cause: definition/construct overlap, source context insufficient, original interpretation, second interpretation, version/date drift, extraction/translation damage, unit association, missing evidence, transcription/formatting, or genuinely unresolved ambiguity. Read the original page and related definitions; record the source anchor and any additional record. Neither coder's seniority nor the majority of repeated units settles the issue.

The comparison tool emits `adjudication-template.csv` with A and B values but no preferred resolution. Both coders discuss only after their initial files are frozen. If unresolved, use a named third researcher with suitable domain/language competence or leave the item unresolved. Preserve both initial values; never replace initial ratings with consensus for agreement measurement.

For each adjudicated row, record `decision` (`resolved` or `unresolved`), `resolved_value`, cause, written rationale, evidence anchor, adjudicator, both acknowledgements and decision date. Resolution requires a valid schema value, source/rationale, named decision-maker and both acknowledgements; acknowledgements record review of the decision, not necessarily assent. If no decision can be supported, do not fabricate consensus.

```sh
python compare_coding.py \
  --reference baseline.csv --review /path/to/reviewer/ratings.csv \
  --schema /path/to/reviewer/variables.json \
  --units /path/to/reviewer/units.csv --out /path/to/comparison \
  --adjudication /path/to/completed-adjudication.csv
```

This emits a separate `consensus.csv` and audit log without changing the reference, review ratings, old registry or agreement denominators. It does not apply decisions to AI Watch automatically. A later release needs an explicit change ledger identifying original IDs, affected claims, reasons and any source/version changes.

## Reporting

Report numbers assigned, coded, paired, unresolved and missing for each variable, source access levels and independent-review exposure. Show nominal observed agreement, Cohen's kappa, marginal distributions, confusion tables and concrete disagreements together. Exact-text date/amount agreement is format-sensitive; set-stage agreement is exact set match plus Jaccard. Do not average them into a quality score.

Shared documents, shared CAG agents, purposive selection, short excerpts and correlated within-source observations preclude treating ratings as independent nationally representative samples. This release uses descriptive agreement without inferential confidence intervals or significance tests. Kappa can be undefined with constant categories; that is not a failed implementation or proof of perfect substantive reliability.
