# AI Watch India: Public-Service Search Scope

Review completed 5 October 2026, India date. This log defines the scope of negative findings: “not verified” means not established by the records retrieved and reviewed here, not “does not exist.” No agency, supplier, court registry, patient, candidate or complainant was contacted.

## Selection and search design

The six cases were chosen to test a range of consequential public-service contexts: examination identity, cybercrime complaint administration, judicial translation, judicial research assistance, clinical support and police investigation. SUPACE is a deliberate experimental counterexample, not an additional claim of live deployment. This is purposive case research, not a representative sample or national census.

Each case was searched and assessed against the same twelve dimensions: owner/purpose; decision role/affected people; deployment/date; procurement/supplier; funding/contract; data/integration; evaluation/error rates; human review/overrides; privacy/retention; complaints/appeal; public outputs/access; and current-status limits. All 72 slots remain in the downloadable matrix, including unresolved ones.

Initial searches used six case-specific queries with 2026 deployment/tender/evaluation constraints. Follow-up searches covered thirteen narrower questions on contract awards, failure alternatives, privacy, winner selection, classification appeals, court translation disclaimers, final versus draft court guidance, clinical validation, supplier records, police procurement and rollout.

Exact initial queries:

- UPSC AI face authentication deployment tender 2026
- I4C CyberGuard AI complaint classification deployment 2026
- Supreme Court SUVAS translation human validation 2026
- Supreme Court SUPACE deployed judges artificial intelligence 2026
- eSanjeevani AI clinical decision support 2026 evaluation
- Maharashtra MahaCrimeOS AI police deployment 2026

Exact follow-up queries:

- UPSC face authentication January 2026 press release
- UPSC biometric facial recognition contract award 2025 2026
- UPSC facial authentication failure candidates alternative privacy policy
- IndiaAI CyberGuard hackathon winners evaluation 2025
- I4C CyberGuard AI classification privacy appeal accuracy
- SUVAS translation committee disclaimer authoritative English judgment
- SUPACE Supreme Court artificial intelligence white paper experimental 2026
- Supreme Court AI regulations final adopted September 2026
- eSanjeevani clinical decision support prospective evaluation validation
- eSanjeevani clinical decision support vendor procurement privacy complaints
- MahaCrimeOS AI Maharashtra government police tender contract
- MahaCrimeOS AI Amaravati 12 police stations evaluation 2026
- MahaCrimeOS AI police grievance privacy surveillance

Search results were discovery leads, not proof. Original source content was fetched before quoted findings were compiled. The selected corpus adds fifteen source records and reuses the existing July government integration statement for CyberGuard.

## Retrieval issues and exclusions

- **UPSC October record:** two Page.aspx retrievals returned cookie-only content. The [4 October PressReleaseDetail record](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1) yielded the substantive body and date; no finding rests on the cookie-only responses.
- **Court draft status:** recency searches did not verify a later final instrument or routine SUPACE use. The retained [June consultation document](https://cdnbbsr.s3waas.gov.in/s3ec0490f1f4972d133619a60c30f3559e/uploads/2026/06/2026060342.pdf) is labelled draft, not binding law.
- **Evaluation transfer:** a [local ICMR brief](https://nihrjodhpur.icmr.org.in/uploads/policybriefs/1782386587_1.PolicyBrief_Telemedicine.pdf) recommends future eSanjeevani integration; its metric was not transferred to the deployed national CDSS.
- **Policing scale:** the [vendor feature](https://news.microsoft.com/source/asia/features/a-race-against-time-maharashtra-police-get-an-ai-copilot-to-fight-cybercrime/), [customer story](https://www.microsoft.com/en-in/aifirstmovers/FY26CrimeOS) and [Indian Express report](https://indianexpress.com/article/explained/mahacrimeos-ai-maharashtra-10418600/) differ on 23/25 pilot stations; no government-confirmed completed statewide inventory was retrieved.
- **Secondary commentary:** court commentary and older telemedicine commentary were read for context, but did not override more precise official descriptions or establish current operational performance.
- **Search noise:** results about unrelated overseas court AI rules and broad programme budgets were excluded from Indian system-specific findings.

## Unresolved record queue

For each case, the twelve-field matrix and brief specify missing records and their limits. Priority next records are current executed contracts, model/version inventories, acceptance reports, independent error distributions, adverse-decision and override SOPs, device/processor/retention terms, and usable correction or appeal procedures.

No tenders were treated as awards, no winners as contracted suppliers, no programme usage as accuracy, no draft safeguards as implemented controls, and no historical local process as a universal national rule. A later official record may resolve or change any of these bounded findings.

## Reproduction

The repository preserves the curated source selection, exact normalized quotations, source URLs, source types, dates, locators, selected-excerpt snapshots and hashes. Run `python scripts/build_public_services.py`, then `node scripts/package-briefs.mjs`, `npm run validate:data` and `npm test`. The builder asserts quote membership and retains every dimension.

The new snapshots are selected excerpts, not full copyrighted page archives or PDF binaries. Hashes authenticate these extracted UTF-8 snapshot files only; they do not certify source authenticity, original PDF bytes or the truth of a source's claims.

## Edition 05 completeness follow-up

Eleven additional focused searches returned 64 distinct discovery URLs. The thin discovery register retains query, title and URL rather than treating search excerpts as verified source text.

- UPSC face authentication mismatch SOP 2026
- UPSC face authentication mobile privacy retention policy
- CyberGuard I4C production evaluation model 2026
- I4C CyberGuard procurement award tender
- SUPACE Supreme Court deployment final AI regulations 2026
- SUVAS translated judgments disclaimer correction process
- eSanjeevani clinical decision support accuracy evaluation
- eSanjeevani patient grievance complaint clinical consultation
- MahaCrimeOS government order procurement contract
- MahaCrimeOS police rollout September 2026
- India AI public services model cards appeal audit

A title/DOI follow-up located the national clinical implementation-study abstract and declarations. Five additional public-service sources were read and added: that abstract, two developer accounts, circulated translation guidance and historical telemedicine practice guidance. The parent DPDP Act was separately retrieved as contextual extracted text, not another case or contribution.

The full clinical manuscript was blocked through the content-fetch route and its article page was blocked in a browser. The current eSanjeevani support page was blocked through both routes. No functioning form, full manuscript, independent numeric accuracy or current remedy was inferred from the partial retrieval.

The new case fields preserve the March/April integration descriptions, study-funding versus deployment-budget boundary, historical versus current safeguard boundary and local versus national validation distinction. The full case register remains six cases and twelve dimensions per case; the source count rises from fifteen to twenty public-service records.

Read `data-completeness-study.md`, `completeness-retrieval.csv` and `completeness-discovery.jsonl` alongside this historical initial search log. Run `npm run package:data` to regenerate current briefs, dossiers, registers and the archive, then validation, tests and build.
