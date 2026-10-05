# Reproducing the governance layer

Use a clean repository checkout and run `npm ci && npm run package:governance && npm test && npm run build`. The included builder is the source used at scripts/build_governance.py; its frozen inputs belong in research/governance. The separate unchanged public/registry corpus is required for baseline validation and join anchors. This package alone is not the complete deployment registry. Packaging makes no network calls. See METHOD.md and CODEBOOK.md for evidence and scope limits.
