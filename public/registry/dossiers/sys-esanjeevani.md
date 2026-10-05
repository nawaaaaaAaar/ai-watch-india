# AI Watch: eSanjeevani clinical decision support

India institution-and-system dataset v1.1.0. Checked 2026-10-05; analyst-coded documentary evidence, not an operational audit. System kind: Public-service system. Selection: Purposive exploratory seed.

## Owner & purpose

Evidence status: Documented. C-DAC Mohali developed the national platform; the parliamentary record describes CDSS functionality.

> Further, the AI based Clinical Decision Support System (CDSS) available on this platform also enables a systematic capture of the diseases symptoms through a detailed patient assistance form, and identification of possible diseases.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); Parliamentary CDSS explanation.
> eSanjeevani is an indigenous, cloud-native telemedicine platform developed by C-DAC Mohali to address critical healthcare accessibility challenges, including the shortage and uneven distribution of healthcare professionals, limited access to specialist care in rural and remote areas, and gaps in continuity of care.
>
> [C-DAC eSanjeevani product description](https://cdac.in/index.aspx?id=product_details&productId=eSanjeevaniNationalTelemedicineService); Product brief.

## Decision role & affected people

Evidence status: Documented. Possible diseases and specialist referral support are presented to a doctor at the hub end, affecting patient consultations.

> Further, the AI based Clinical Decision Support System (CDSS) available on this platform also enables a systematic capture of the diseases symptoms through a detailed patient assistance form, and identification of possible diseases.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); Parliamentary CDSS explanation.
> It also makes recommendation of a specialist doctor through a ‘rule engine’ and offers a differential diagnosis of possible diseases to the doctor at the hub end, thus facilitating connect of the patients with specialists as well as aiding consultations.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); Rule engine and hub-doctor workflow.

## Deployment & date

Evidence status: Conflicting sources. The parliamentary response dates integration to April 2023 and usage through July 2026; the developer page says March 2023. These descriptions may refer to different components/stages; they are not silently reconciled.

> Since its integration in April, 2023 till July, 2026, nearly 30.4 crore eSanjeevani consultations across all States/UTs have been benefited from standardized data capture and nearly 2.13 crore AI based differential diagnosis, ensuring consistency across health and wellness centres.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); April 2023 integration and July 2026 usage.
> CDSS structures telemedicine patient data via eSanjeevani, suggesting diagnoses and treatments in real time. Integrated since March 2023, it supports 350,000 daily consultations across 31 conditions.
>
> [Wadhwani AI healthcare programme page](https://www.wadhwaniai.org/impact/healthcare/); Developer programme page, March integration claim.

## Procurement & supplier

Evidence status: Partial. C-DAC is the platform developer; Wadhwani AI describes collaboration on the CDSS in a developer submission. Executed component contracts, production version and full supplier chain were not verified.

> We also collaborate closely with C-DAC, the technology service provider for the eSanjeevani platform, to ensure that our code is easy to integrate with the existing platform and meets the high standards required for deployment in public healthcare.
>
> [Wadhwani AI eSanjeevani developer submission](https://solve.mit.edu/solutions/73043); Developer submission, C-DAC collaboration.
> eSanjeevani is an indigenous, cloud-native telemedicine platform developed by C-DAC Mohali to address critical healthcare accessibility challenges, including the shortage and uneven distribution of healthcare professionals, limited access to specialist care in rural and remote areas, and gaps in continuity of care.
>
> [C-DAC eSanjeevani product description](https://cdac.in/index.aspx?id=product_details&productId=eSanjeevaniNationalTelemedicineService); Product brief.

## Funding & contract

Evidence status: Partial. The retrieved study declares no funding for that study; this is not a zero-cost deployment claim. CDSS-specific contract, licensing, budget and maintenance expenditure remain unverified.

> This study did not receive any funding.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Research funding declaration, not deployment budget.

## Data & integration

Evidence status: Documented. Patient assistance forms collect symptoms; the privacy policy identifies a C-DAC-managed server. Developer and study descriptions identify a rule-based/knowledge-based form; all deployed components are not thereby identified.

> Further, the AI based Clinical Decision Support System (CDSS) available on this platform also enables a systematic capture of the diseases symptoms through a detailed patient assistance form, and identification of possible diseases.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); Parliamentary CDSS explanation.
> This study, conducted between 2022–2024 by an AI Centre of Excellence of the Government of India, focused on developing, validating, and implementing a knowledge-based CDSS symptom entry Physician Assistance Form (PAF) within eSanjeevani—India’s national teleconsultation platform.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, methods.
> When the Community Health Officer registers patient on eSanjeevani, the following information besides the users' information is collected from the patient and stored on a server operated and managed by C-DAC Mohali – name, gender, age, address, mobile number, Email ID, health records, etc.
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 1(a).
> The SIPF uses a rule-based logical workflow to enable the accurate collection of chief complaints by engaging patients with relevant questions.
>
> [Wadhwani AI eSanjeevani developer submission](https://solve.mit.edu/solutions/73043); Developer submission, rule-based form.

## Evaluation & error rates

Evidence status: Partial. A national implementation-study abstract reports expert-clinician validation and implementation, but independent numeric error rates were not established in the retrieved text and full manuscript access was blocked. A separate local 4,401-record study's 90% figure is not the existing national system's score.

> the AI-driven Clinical Decision Support System (AI-CDSS), which has achieved 90% validation accuracy using 4,401 locally sourced patient records, should be integrated into the eSanjeevani platform
>
> [ICMR local telemedicine research brief](https://nihrjodhpur.icmr.org.in/uploads/policybriefs/1782386587_1.PolicyBrief_Telemedicine.pdf); Local study recommendation, integration proposal.
> Expert clinicians validated the symptom repository, logic flow, and AI-generated diagnoses.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, phase 2.
> The validated CDSS was implemented in eSanjeevani 2.0, providing real-time differential diagnosis and departmental recommendations during assisted and non-assisted teleconsultations.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, phase 3.
> This study, conducted between 2022–2024 by an AI Centre of Excellence of the Government of India, focused on developing, validating, and implementing a knowledge-based CDSS symptom entry Physician Assistance Form (PAF) within eSanjeevani—India’s national teleconsultation platform.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, methods.

## Human review & overrides

Evidence status: Partial. Differential diagnosis is supplied to a hub doctor. Historical practice guidance reserves final prescribing/counselling to an RMP and prohibits AI/ML platforms from independently doing it; actual override, escalation and safety-monitoring SOPs remain unverified.

> Technology platforms based on Artificial Intelligence/Machine Learning are not allowed to counsel the patients or prescribe any medicines to a patient.
>
> [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf); Practice Guidelines section 5.4, AI/ML platforms.
> the final prescription or counseling has to be directly delivered by the RMP
>
> [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf); Practice Guidelines section 5.4, RMP final delivery.
> It also makes recommendation of a specialist doctor through a ‘rule engine’ and offers a differential diagnosis of possible diseases to the doctor at the hub end, thus facilitating connect of the patients with specialists as well as aiding consultations.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); Rule engine and hub-doctor workflow.

## Privacy & retention

Evidence status: Partial. The policy ties some data retention to account existence and further interventions, but excludes medical reports/diagnoses generated in treatment from that clause; no single universal retention period follows.

> All personal information collected from you under Clause 1(a) at the time of registration and later will be retained for as long as your account remains in existence and in sync with telemedicine practice guidelines issued by Niti Aayog/Board of Governors MCI and if any academic or medical or public health and administrative interventions have been commenced under Clause 2, for such period thereafter as is required.
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 3(a).
> Nothing set out herein shall apply to medical reports, diagnoses or other medical information generated by medical professionals in the course of treatment.
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 3(b).

## Complaints & appeal

Evidence status: Partial. The privacy policy has a privacy contact, and historical practice guidance calls for platform grievance mechanisms. A functioning current support form or CDSS clinical-error review/remedy procedure was not verified; the platform support page was blocked during this review.

> Technology Platform must ensure that there is a proper mechanism in place to address any queries or grievances that the end-customer may have
>
> [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf); Practice Guidelines section 5.6, grievance mechanism.
> If you have any suggestions, concerns or queries in relation to this Privacy Policy, you may address them at esanjeevaniopd@cdac.in
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 10.

## Public outputs & access

Evidence status: Partial. Developer, parliamentary and privacy records and a national implementation-study abstract are public; no complete national CDSS model card or independent validation dossier was verified.

> If you have any suggestions, concerns or queries in relation to this Privacy Policy, you may address them at esanjeevaniopd@cdac.in
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 10.
> This study, conducted between 2022–2024 by an AI Centre of Excellence of the Government of India, focused on developing, validating, and implementing a knowledge-based CDSS symptom entry Physician Assistance Form (PAF) within eSanjeevani—India’s national teleconsultation platform.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, methods.
> eSanjeevani is an indigenous, cloud-native telemedicine platform developed by C-DAC Mohali to address critical healthcare accessibility challenges, including the shortage and uneven distribution of healthcare professionals, limited access to specialist care in rural and remote areas, and gaps in continuity of care.
>
> [C-DAC eSanjeevani product description](https://cdac.in/index.aspx?id=product_details&productId=eSanjeevaniNationalTelemedicineService); Product brief.
> Since its integration in April, 2023 till July, 2026, nearly 30.4 crore eSanjeevani consultations across all States/UTs have been benefited from standardized data capture and nearly 2.13 crore AI based differential diagnosis, ensuring consistency across health and wellness centres.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); April 2023 integration and July 2026 usage.

## Current-status limits

Evidence status: Partial. The dated response supports reported integrated use, not independent safety certification or all October operational details. The programme utilisation study raises privacy and access recommendations, but is not a deployed-CDSS accuracy study.

> Efforts should be made to address privacy concerns by implementing robust safeguards, ensuring inclusivity through initiatives by the Government to improve access to technology, and expanding the scope of telemedicine services to cater to a broader range of healthcare needs.
>
> [NHSRC telemedicine utilisation study](https://www.nhsrcindia.org/sites/default/files/2025-09/Telemedicine%20Final%20Report%202025.pdf); Programme utilisation study, concluding recommendations.
> Since its integration in April, 2023 till July, 2026, nearly 30.4 crore eSanjeevani consultations across all States/UTs have been benefited from standardized data capture and nearly 2.13 crore AI based differential diagnosis, ensuring consistency across health and wellness centres.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); April 2023 integration and July 2026 usage.

## Deployments

- **event date**: Unknown / not assigned
- **date precision**: Mixed dates in source-backed narrative; not assigned one go-live date
- **stage**: Official integration reported
- **place**: India
- **description**: The parliamentary response dates integration to April 2023 and usage through July 2026; the developer page says March 2023. These descriptions may refer to different components/stages; they are not silently reconciled.

> CDSS structures telemedicine patient data via eSanjeevani, suggesting diagnoses and treatments in real time. Integrated since March 2023, it supports 350,000 daily consultations across 31 conditions.
>
> [Wadhwani AI healthcare programme page](https://www.wadhwaniai.org/impact/healthcare/); Developer programme page, March integration claim.
> Since its integration in April, 2023 till July, 2026, nearly 30.4 crore eSanjeevani consultations across all States/UTs have been benefited from standardized data capture and nearly 2.13 crore AI based differential diagnosis, ensuring consistency across health and wellness centres.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); April 2023 integration and July 2026 usage.

## Evaluations

- **evaluation type**: Evaluation-related documentary evidence; not verified current performance
- **sample n**: Unknown / not assigned
- **sample unit**: Unknown / not assigned
- **setting**: See assertion and linked source context
- **current version match**: Not established
- **result summary**: A national implementation-study abstract reports expert-clinician validation and implementation, but independent numeric error rates were not established in the retrieved text and full manuscript access was blocked. A separate local 4,401-record study's 90% figure is not the existing national system's score.
- **evidence status**: Partial

> the AI-driven Clinical Decision Support System (AI-CDSS), which has achieved 90% validation accuracy using 4,401 locally sourced patient records, should be integrated into the eSanjeevani platform
>
> [ICMR local telemedicine research brief](https://nihrjodhpur.icmr.org.in/uploads/policybriefs/1782386587_1.PolicyBrief_Telemedicine.pdf); Local study recommendation, integration proposal.
> Expert clinicians validated the symptom repository, logic flow, and AI-generated diagnoses.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, phase 2.
> The validated CDSS was implemented in eSanjeevani 2.0, providing real-time differential diagnosis and departmental recommendations during assisted and non-assisted teleconsultations.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, phase 3.
> This study, conducted between 2022–2024 by an AI Centre of Excellence of the Government of India, focused on developing, validating, and implementing a knowledge-based CDSS symptom entry Physician Assistance Form (PAF) within eSanjeevani—India’s national teleconsultation platform.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, methods.

## Controls

- **control type**: Complaints & appeal
- **implementation basis**: Published description/requirements; not verified live enforcement
- **description**: The privacy policy has a privacy contact, and historical practice guidance calls for platform grievance mechanisms. A functioning current support form or CDSS clinical-error review/remedy procedure was not verified; the platform support page was blocked during this review.
- **evidence status**: Partial

> If you have any suggestions, concerns or queries in relation to this Privacy Policy, you may address them at esanjeevaniopd@cdac.in
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 10.
> Technology Platform must ensure that there is a proper mechanism in place to address any queries or grievances that the end-customer may have
>
> [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf); Practice Guidelines section 5.6, grievance mechanism.

- **control type**: Human review & overrides
- **implementation basis**: Published description/requirements; not verified live enforcement
- **description**: Differential diagnosis is supplied to a hub doctor. Historical practice guidance reserves final prescribing/counselling to an RMP and prohibits AI/ML platforms from independently doing it; actual override, escalation and safety-monitoring SOPs remain unverified.
- **evidence status**: Partial

> the final prescription or counseling has to be directly delivered by the RMP
>
> [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf); Practice Guidelines section 5.4, RMP final delivery.
> Technology platforms based on Artificial Intelligence/Machine Learning are not allowed to counsel the patients or prescribe any medicines to a patient.
>
> [Telemedicine Practice Guidelines](https://esanjeevani.mohfw.gov.in/assets/guidelines/Telemedicine_Practice_Guidelines.pdf); Practice Guidelines section 5.4, AI/ML platforms.
> It also makes recommendation of a specialist doctor through a ‘rule engine’ and offers a differential diagnosis of possible diseases to the doctor at the hub end, thus facilitating connect of the patients with specialists as well as aiding consultations.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); Rule engine and hub-doctor workflow.

- **control type**: Privacy & retention
- **implementation basis**: Published description/requirements; not verified live enforcement
- **description**: The policy ties some data retention to account existence and further interventions, but excludes medical reports/diagnoses generated in treatment from that clause; no single universal retention period follows.
- **evidence status**: Partial

> All personal information collected from you under Clause 1(a) at the time of registration and later will be retained for as long as your account remains in existence and in sync with telemedicine practice guidelines issued by Niti Aayog/Board of Governors MCI and if any academic or medical or public health and administrative interventions have been commenced under Clause 2, for such period thereafter as is required.
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 3(a).
> Nothing set out herein shall apply to medical reports, diagnoses or other medical information generated by medical professionals in the course of treatment.
>
> [eSanjeevani privacy policy](https://esanjeevani.mohfw.gov.in/assets/guidelines/esanjeevani2.0_Private_Policy.pdf); Privacy policy clause 3(b).

## Issues

- **issue type**: Evaluation & error rates
- **description**: A national implementation-study abstract reports expert-clinician validation and implementation, but independent numeric error rates were not established in the retrieved text and full manuscript access was blocked. A separate local 4,401-record study's 90% figure is not the existing national system's score.

> This study, conducted between 2022–2024 by an AI Centre of Excellence of the Government of India, focused on developing, validating, and implementing a knowledge-based CDSS symptom entry Physician Assistance Form (PAF) within eSanjeevani—India’s national teleconsultation platform.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, methods.
> Expert clinicians validated the symptom repository, logic flow, and AI-generated diagnoses.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, phase 2.
> the AI-driven Clinical Decision Support System (AI-CDSS), which has achieved 90% validation accuracy using 4,401 locally sourced patient records, should be integrated into the eSanjeevani platform
>
> [ICMR local telemedicine research brief](https://nihrjodhpur.icmr.org.in/uploads/policybriefs/1782386587_1.PolicyBrief_Telemedicine.pdf); Local study recommendation, integration proposal.
> The validated CDSS was implemented in eSanjeevani 2.0, providing real-time differential diagnosis and departmental recommendations during assisted and non-assisted teleconsultations.
>
> [National eSanjeevani CDSS implementation-study abstract](https://doi.org/10.1101/2025.11.22.25340800); Retrieved research abstract, phase 3.

- **issue type**: Current-status limits
- **description**: The dated response supports reported integrated use, not independent safety certification or all October operational details. The programme utilisation study raises privacy and access recommendations, but is not a deployed-CDSS accuracy study.

> Since its integration in April, 2023 till July, 2026, nearly 30.4 crore eSanjeevani consultations across all States/UTs have been benefited from standardized data capture and nearly 2.13 crore AI based differential diagnosis, ensuring consistency across health and wellness centres.
>
> [Lok Sabha telemedicine/CDSS response](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS284_ZZWF4R.pdf?source=lsapps); April 2023 integration and July 2026 usage.
> Efforts should be made to address privacy concerns by implementing robust safeguards, ensuring inclusivity through initiatives by the Government to improve access to technology, and expanding the scope of telemedicine services to cater to a broader range of healthcare needs.
>
> [NHSRC telemedicine utilisation study](https://www.nhsrcindia.org/sites/default/files/2025-09/Telemedicine%20Final%20Report%202025.pdf); Programme utilisation study, concluding recommendations.

