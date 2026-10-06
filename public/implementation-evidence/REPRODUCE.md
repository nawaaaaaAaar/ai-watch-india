# Reproducing implementation evidence

Use a clean repository checkout and run `npm ci && npm run package:implementation && npm test && npm run build`. The builder reads frozen inputs in research/implementation-evidence and the unchanged registry/governance layers. It performs no network calls. This ZIP is the new layer, not the full 144-family registry or governance archive; join keys are included. See METHOD.md for retrieval and scope limits.
