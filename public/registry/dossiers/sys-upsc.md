# AI Watch: UPSC face authentication

India institution-and-system dataset v1.0.0. Checked 2026-10-05; analyst-coded documentary evidence, not an operational audit.

## Owner & purpose

Evidence status: Documented. UPSC with technical support from NeGD; exam identity authentication.

> The face authentication application has been developed and implemented by UPSC with technical support from the National e-Governance Division (NeGD) of Ministry of Electronics and IT.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, implementation and developer.

## Decision role & affected people

Evidence status: Partial. Mobile identity matching concerns examination candidates; detailed adverse-decision rules are not verified.

> Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates.
>
> [UPSC centenary current-status explanation](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1); 4 October release, examination reform.
> It works on any Android smartphone, and invigilators used their own mobile phones for the purpose, thereby reducing hardware costs and easing the logistical burden.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, mobile workflow.

## Deployment & date

Evidence status: Documented. A September 2025 pilot and scaled use on 24 May 2026 are officially reported, with about 5.50 lakh candidates.

> Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates.
>
> [UPSC centenary current-status explanation](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1); 4 October release, examination reform.

## Procurement & supplier

Evidence status: Partial. A 2024 PSU tender covered biometrics, facial recognition, QR scans and AI CCTV; the June record describes in-house development. The contract link between them is unverified.

> The face authentication application has been developed and implemented by UPSC with technical support from the National e-Governance Division (NeGD) of Ministry of Electronics and IT.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, implementation and developer.
> Tender responses are invited from PSUs for Aadhaar based Fingerprint Authentication/Digital Fingerprint Capturing & Facial Recognition of Candidates, QR Code Scanning of e-Admit Cards and Live AI-based CCTV Surveillance
>
> [UPSC biometric/AI tender specification](https://upsc.gov.in/sites/default/files/Tender-AadhaarQRFaceRecgAI-Corrgn_Eng-180724.pdf); 2024 tender, cover/scope.

## Funding & contract

Evidence status: Not verified. n.a. Awarded supplier, current application budget and contract value were not verified; the tender alone is not an award.



## Data & integration

Evidence status: Partial. Invigilators' Android phones were used. The current data-flow diagram and device/data lifecycle were not verified.

> It works on any Android smartphone, and invigilators used their own mobile phones for the purpose, thereby reducing hardware costs and easing the logistical burden.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, mobile workflow.

## Evaluation & error rates

Evidence status: Partial. UPSC reports six-to-eight-second typical authentication; no independent false-accept/reject or subgroup evaluation was verified.

> The time required for a typical face authentication of a candidate is only about 6–8 seconds, which ensured smooth entry and prevented queuing at examination centres.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, reported timing.

## Human review & overrides

Evidence status: Partial. The older tender requires physical photo verification. The current mismatch/technical-failure SOP was not verified.

> 6.1.11 The Service Provider has to perform physical verification of candidates’ photos with Application Database (provided by UPSC) at the time of security gate entry.
>
> [UPSC biometric/AI tender specification](https://upsc.gov.in/sites/default/files/Tender-AadhaarQRFaceRecgAI-Corrgn_Eng-180724.pdf); 2024 tender clause 6.1.11.

## Privacy & retention

Evidence status: Partial. The older tender specifies encrypted cloud holding for at least one year or 30 days after final results, whichever is later. Applying it to the current mobile system is not established.

> 6.1.12 After the completion of the entire process as per the scope of work, the Service Provider will hold the data on its Secured Cloud Server with 256-bit encryption for a minimum period of one (01) year from the date of the examination or 30 days after the declaration of final result of the examination, whichever is later.
>
> [UPSC biometric/AI tender specification](https://upsc.gov.in/sites/default/files/Tender-AadhaarQRFaceRecgAI-Corrgn_Eng-180724.pdf); 2024 tender clause 6.1.12.

## Complaints & appeal

Evidence status: Not verified. n.a. A system-specific candidate mismatch appeal, deadline and non-biometric fallback were not verified.



## Public outputs & access

Evidence status: Partial. UPSC publishes implementation descriptions; the actual current failure-handling SOP, audit and test report were not obtained.

> Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates.
>
> [UPSC centenary current-status explanation](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1); 4 October release, examination reform.
> The face authentication application has been developed and implemented by UPSC with technical support from the National e-Governance Division (NeGD) of Ministry of Electronics and IT.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, implementation and developer.

## Current-status limits

Evidence status: Partial. The October source confirms reported scaled use, not independently audited accuracy or every current operational detail.

> Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates.
>
> [UPSC centenary current-status explanation](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1); 4 October release, examination reform.

## Deployments

- **event date**: Unknown / not assigned
- **date precision**: Mixed dates in source-backed narrative; not assigned one go-live date
- **stage**: Official deployment reported
- **place**: India
- **description**: A September 2025 pilot and scaled use on 24 May 2026 are officially reported, with about 5.50 lakh candidates.

> Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates.
>
> [UPSC centenary current-status explanation](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1); 4 October release, examination reform.

## Evaluations

- **evaluation type**: Evaluation-related documentary evidence; not verified current performance
- **sample n**: Unknown / not assigned
- **sample unit**: Unknown / not assigned
- **setting**: See assertion and linked source context
- **current version match**: Not established
- **result summary**: UPSC reports six-to-eight-second typical authentication; no independent false-accept/reject or subgroup evaluation was verified.
- **evidence status**: Partial

> The time required for a typical face authentication of a candidate is only about 6–8 seconds, which ensured smooth entry and prevented queuing at examination centres.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, reported timing.

## Controls

- **control type**: Privacy & retention
- **implementation basis**: Published description/requirements; not verified live enforcement
- **description**: The older tender specifies encrypted cloud holding for at least one year or 30 days after final results, whichever is later. Applying it to the current mobile system is not established.
- **evidence status**: Partial

> 6.1.12 After the completion of the entire process as per the scope of work, the Service Provider will hold the data on its Secured Cloud Server with 256-bit encryption for a minimum period of one (01) year from the date of the examination or 30 days after the declaration of final result of the examination, whichever is later.
>
> [UPSC biometric/AI tender specification](https://upsc.gov.in/sites/default/files/Tender-AadhaarQRFaceRecgAI-Corrgn_Eng-180724.pdf); 2024 tender clause 6.1.12.

- **control type**: Human review & overrides
- **implementation basis**: Published description/requirements; not verified live enforcement
- **description**: The older tender requires physical photo verification. The current mismatch/technical-failure SOP was not verified.
- **evidence status**: Partial

> 6.1.11 The Service Provider has to perform physical verification of candidates’ photos with Application Database (provided by UPSC) at the time of security gate entry.
>
> [UPSC biometric/AI tender specification](https://upsc.gov.in/sites/default/files/Tender-AadhaarQRFaceRecgAI-Corrgn_Eng-180724.pdf); 2024 tender clause 6.1.11.

## Issues

- **issue type**: Current-status limits
- **description**: The October source confirms reported scaled use, not independently audited accuracy or every current operational detail.

> Following a pilot at select centres in Gurugram during the NDA & NA (II) and CDS (II) examinations in September 2025, the system was implemented at scale for the Civil Services (Preliminary) Examination on 24 May 2026, covering approximately 5.50 lakh candidates.
>
> [UPSC centenary current-status explanation](https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2317336&reg=48&lang=1); 4 October release, examination reform.

- **issue type**: Evaluation & error rates
- **description**: UPSC reports six-to-eight-second typical authentication; no independent false-accept/reject or subgroup evaluation was verified.

> The time required for a typical face authentication of a candidate is only about 6–8 seconds, which ensured smooth entry and prevented queuing at examination centres.
>
> [UPSC face authentication implementation](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2268879&reg=3&lang=1); 4 June release, reported timing.

