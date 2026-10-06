# Agreement measurement protocol

This protocol measures reproducibility of coding once a second researcher supplies independent ratings. It does not measure documentary truth, deployed-system effectiveness or national prevalence, and it reports no empirical agreement until a second pass exists.

## Paired denominator and missingness

The tool joins on opaque `unit_id` and `variable`, with one row per assignment. Only pairs with both statuses `coded` enter a variable's agreement denominator; unresolved, unreadable, not-applicable, pending and absent responses are counted and exported separately. Substantive “Unknown”/“Not established” codes remain categories and are not treated as missing ratings. Complete-case kappa is a deliberate computational choice, not an assumption that unavailable sources are missing at random; selection into complete pairs must be disclosed ([de Raadt et al., Kappa Coefficients for Missing Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC6506991/)).

Coverage is an explicit exception: legacy A measured primary-dimension allocation, whereas the new review audits relevant corpus evidence. Its matched pairs and disagreement table are construct diagnostics, not intercoder reliability; the engine disables kappa and separates diagnostic pairs from comparable pairs. A first-analyst pass using the same corpus-presence rubric, frozen before comparison, and a versioned schema change are required before calling that variable an intercoder agreement measure.

Original fragment observations are counted once, not once per system association. Document, case-source association, coverage, finance and governance tasks have distinct unit types and separate variable denominators. Source/case profiles expose shared evidence; they do not make correlated ratings independent.

## Nominal agreement

For each nominal variable, the tool returns the number paired, diagonal agreement count, confusion table, coder marginal counts, observed agreement and unweighted Cohen's kappa. It computes \(P_o=n_{\mathrm{equal}}/n\), \(P_e=\sum_c p_{A,c}p_{B,c}\), and \(\kappa=(P_o-P_e)/(1-P_e)\), using both coders' marginal distributions ([Hallgren, Computing Inter-Rater Reliability for Observational Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC3402032/)).

With no complete pairs, observed agreement and kappa are null. If \(P_e=1\), kappa is null with a constant-category warning even when observed agreement is one; near-degenerate distributions are flagged. The published verification flags have no positive variation, so their agreement can be uninformative. Category prevalence and differing coder marginals affect kappa, and high agreement is not the same as construct validity ([Hallgren](https://pmc.ncbi.nlm.nih.gov/articles/PMC3402032/)).

No automatic “good,” “moderate” or “acceptable” threshold is applied. Interpret the distribution, definitions, evidence access and disagreement substance; cross-variable and cross-sample kappa comparisons need caution because category base rates differ ([de Raadt et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC6506991/)).

## Exact fields and sets

Event/document dates and source amount text use exact equality after whitespace normalisation. This measures reproducible date selection/transcription, not semantic equivalence, monetary comparability or legal interpretation. Differently formatted equivalent dates/amounts remain disagreement candidates for adjudication; malformed totals are not repaired by the tool.

Financial-stage arrays use order-insensitive set equality and per-pair Jaccard overlap, \(|A\cap B|/|A\cup B|\). The tool reports mean Jaccard among complete pairs plus exact-set agreement; it does not apply a nominal kappa to arbitrary sets or impose an ordinal ranking on financial stages. “Not established” is a substantive singleton, not an empty set.

## Reproducibility and limits

The standard-library implementation exports JSON summaries, CSV metrics, confusion cells, paired disagreements, unresolved/unpaired rows, an adjudication form and source-level disagreement profiles. It validates labels, row keys, schema version, coded-row rationales/anchors, and status/value consistency before calculating anything. Output hashes and input fingerprints identify exactly which files were compared.

Training simulations are labelled synthetic and excluded from research results. Pre-adjudication A/B files remain immutable; consensus is a separate export. There are no significance tests, causal claims or naive row-wise confidence intervals: selected cases are not random, documents are shared and many ratings depend on the same text. A future inferential design would need a sampling frame and a defensible dependence structure rather than treating every excerpt as an independent draw.
