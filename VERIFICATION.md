# AI Watch India: Release Verification

The curated first release was built and checked on 4 October 2026. This report documents executed checks, not independent legal approval or proof of audience demand.

## Release scope

The application contains seven workspace views, all 30 final DPDP Rules provisions (23 rules and seven schedules), four official source instruments, eight targeted corrections and twelve distinct downloadable policy-research briefs. It is a complete curated collection, not a live national monitor or arbitrary-document upload service.

## Executed verification

- **Automated tests:** `npm test` passed all 12 tests, with zero failures. Checks cover inventory, extracted-text hashes, exact focused quotations, split provision mappings, key finding distinctions, targeted corrections, filters, citation-preserving exports, notebook validation, spreadsheet-formula safeguards and all twelve briefs.
- **Dataset validation:** `npm run validate:data` passed: 30 complete records, eight corrections and four source objects.
- **Reproduction:** `python scripts/build_dataset.py` and `node scripts/package-briefs.mjs` regenerated the collection and briefs successfully; tests and validation were rerun afterward.
- **Production build:** `npm run build` passed TypeScript checking and Vite bundling. The static bundle requires no model key or application backend.
- **Dependencies:** `npm audit --omit=dev` reported zero vulnerabilities at verification time. This is a point-in-time package advisory check, not a security certification.
- **Browser workflows:** 57 explicit Playwright assertions passed in Chromium with zero observed JavaScript runtime errors.

## Browser coverage

The 57 checks exercised selection across routes, all 30 provision links, multi-word search, combined filters, empty results, full/focused excerpts, printed/corrected cycles, word-highlighting cycles and table handling. Every one of the twelve contribution evidence pages opened; an individual brief and the complete bundle were downloaded and their contents inspected.

All four extracted source snapshots downloaded successfully, integrity disclosures opened, and source URLs pointed to the intended official domain. The study, specification and structured data downloads were inspected. The eight-row correction register and invalid-route/provision fallbacks were checked.

Brief checks included selecting, reordering in both directions, disabled boundary controls, removal, preview on/off, Markdown and CSV downloads, review-note preservation, notebook export/import and local clearing. Invalid-version, malformed and oversized imports were rejected without replacing the current selection; additional forged-state cases are covered by unit tests.

Correction-proposal checks included opening, closing, Escape, forward/backward focus trapping, restored focus, HTTPS validation and a downloaded draft. No proposal was automatically submitted. Checked/disputed review events were retained; short-note validation was exercised.

Seven routes were captured at 1440px desktop and 375px mobile widths and checked for document-level horizontal overflow. Light/dark/light transitions, home and comparison dark-mode screenshots, a mobile modal and a 200% CSS-scaled layout were checked. These checks are not a screen-reader audit or cross-browser certification.

Observed browser requests included no document-content POSTs. Notebook state remains in memory; the application does not use browser persistent storage, external model calls or analytics. Google Fonts and user-opened external links remain disclosed dependencies.

## Issues resolved during verification

- The desk's add-to-brief buttons were prevented from stretching to the height of their grid row.
- A retention-comparison alignment note now explains that the draft user-account definition moved to final Rule 2. Mechanical highlighting must not suggest that this definition was abolished; the same caution is preserved in exported briefs.
- Dark-mode captures were retaken after the short color transition settled, rather than interpreting an in-transition screenshot as a final visual state.

## Remaining boundaries

The original PDF binaries are linked, not mirrored; snapshot hashes cover extracted text only. English wording and interpretation were reviewed by a single analyst, not independently approved by legal counsel. The collection preserves the unresolved publication-date basis and does not certify calculated compliance deadlines, all later amendments or current court status.

There has been no independent usability study, adoption test or newsroom validation. Twelve source-backed outputs meet the release's contribution count, but should not be described as exclusive discoveries or twelve separate policy-family investigations.

The working application, data, source snapshots, research, briefs and reproduction instructions are included in the repository. Paid services, scheduled monitoring, authenticated editorial collaboration and a permanent public-domain launch are outside this curated release.
