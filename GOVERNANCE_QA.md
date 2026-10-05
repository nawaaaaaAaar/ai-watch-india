# Governance release QA inventory

The signoff covers the linked research layer, not legal accuracy assurance or a national census. Data validation and browser checks have different purposes; both must pass before release.

## Claims and corresponding checks

- **Frozen registry**: Compare all 389 prior public/registry payload hashes, 144 system rows and 1,728 assertion slots. Spot-check explorer, system page, old notebook and registry downloads.
- **Complete structured layer**: Validate 52 instruments, five slots each, 37 coverage rows, source/evidence/relationship keys, typed links and both provenance halves. Run SQLite integrity/foreign-key checks and all SQL examples.
- **Research caveats exposed**: Check draft, adopted, staged commencement, historical term, outline-only and unknown dates in rendered dossiers. Confirm source snapshots/primary URLs, conditional associations and explicit named direction remain visible.
- **Discovery**: Search title/domain, jurisdiction/status/type filters individually and together, reset and empty state. Check count and rendered rows agree.
- **Navigation**: Catalogue to instrument, instrument to named system, system backlink to instrument, related-version link and data-room entry. Unknown instrument and unlinked system have non-invented explanations.
- **Downloads**: Actual browser downloads for ZIP, JSON, SQLite, every CSV and selected dossier/snapshot/method/analysis/SQL. Hash core downloads against local bytes. Verify ZIP integrity and file inventory.
- **Coverage**: All 37 jurisdictions visible, expandable query details and zero-inclusion caveat. CSV retains the same coverage rows.
- **Error recovery**: Force governance JSON network failure, show retry and successful recovery. Simulate HTML returned as a download and verify rejection/notice, then retry successful download.
- **Visual/accessibility**: Desktop and 375px viewport screenshots, light/dark modes, no body horizontal overflow, labelled filters and keyboard navigation. Preserve existing visual system, no cosmetic redesign.
- **Hosted and reproduction**: Update existing private asset only; fresh hosted page, filters, detail/backlink and core download hashes. Clean checkout, offline packaging, all tests and production build, identical governance archive and unchanged original registry hashes.

## Exploratory scenarios

Combine an incompatible jurisdiction/type filter to produce zero results, then recover with reset. Visit a system without a policy association and verify it does not imply no law applies. Break a download response and ensure the app does not save an HTML error as research data. Review Sikkim/Maharashtra together to detect simplistic title-based status coding.

Actual results, failures fixed and remaining limits are recorded in GOVERNANCE_VERIFICATION.md. No policy compliance or independent-review claim follows from passing browser tests.
