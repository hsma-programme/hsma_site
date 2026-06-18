<!-- ===== hsma_1/H1_1000_modelling_A&E_flows_to_inform_redesign/index.qmd ===== -->

---
title: "Modelling A & E flows to inform redesign at North Devon District Hospital"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Emergency Departments
  - Patient Flow
categories:
  - Discrete Event Simulation (DES)
  - Emergency Departments
  - Patient Flow
author:
  - name: Nic Harrison
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
image: "1000.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to enhance A&E performance by optimising staffing and bed requirements, focusing on the 4-hour target. Various staffing scenarios were modelled, revealing near-optimal staffing with minor adjustments. Success was achieved through collaborative efforts, meeting the 4-hour target in Q1-Q3 despite increased attendances. The project promoted system-wide improvements and cultural change within NDHT and Devon STP.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

This project aimed to improve the performance of A&E services within the broader hospital system, considering factors such as the 4-hour target, staffing optimization, and bed requirements. The project focused on optimizing staffing within current time constraints to enhance A&E performance and the conversion rate from attendances to emergency admissions.

A base case was established, and various staffing scenarios were modelled, exploring approximately 40 possible configurations. The model was designed to be simple for ease of understanding while also complex enough to track patient types and key hospital processes. The main focus was on identifying pinch points in patient flow and improving 4-hour performance.

The analysis revealed that both nursing and doctor staffing were already close to optimal, but minor adjustments could improve performance. However, unsafe options or those that might affect recruitment and retention were eliminated. Optimizations were found within the current staffing budget, and these scenarios were tested during a “Perfect Fortnight” initiative, alongside 36 other improvement efforts.

The project achieved notable success, with the 4-hour target met in Q1, Q2, and Q3, despite a 6% increase in attendances and a national breach rate of 15%. In response to challenges in meeting the target for Q4, additional investments in doctor staffing were made, which, combined with other changes, helped to achieve the standard.

The project’s success was attributed to a collaborative approach, with the “embedded analysis” for A&E and the role of "modelling ambassadors." The modelling work was shared with six other Trusts in the Devon STP and extended to other operational areas, promoting system-wide improvements. Cultural change within NDHT and Devon STP led to more integrated Business Intelligence (BI) efforts, influencing decision-making and operational practices across the region.


<!-- ===== hsma_1/H1_1001_modelling _resources_to_run_acute_frailty_unit_Cornwall/index.qmd ===== -->

---
title: "Modelling the resources needed to run an acute frailty unit in Cornwall leading to the trust changing their plans"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Frailty
  - Acute care
categories:
  - Discrete Event Simulation (DES)
  - Frailty
  - Acute Care
author:
  - name: Joe Turner
    affiliation: Royal Cornwall Hospitals NHS Trust
organisations:
  - Royal Cornwall Hospitals NHS Trust
image: "1001.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    A discrete event simulation model to identify number of beds to improve care for frail older patients in the first 72 hours of emergency care. A model identified optimal bed numbers, showing an 18-bed unit would meet the 4-hour ED standard for 94% of patients, enhancing outcomes and reducing admissions.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

As part of Royal Cornwall Hospitals Trust work with the Acute Frailty Network to “To improve the care of frail older people in their first 72 hours of emergency care, reducing admissions and number of bed days used whilst also improving the hospital experience.” It was proposed that a frailty assessment unit would achieve better outcomes for frail Patients, through providing specialist staffing and a more suitable environment.

A discrete event simulation was initially created to identify what would be the number of beds required for this frail cohort. This model was developed to include all emergency medical admissions (excepting patients on stroke or cardiac pathways)

The model allowed data to be captured relating to what would be the average bed occupancy on both the proposed frailty assessment unit alongside the existing Medical Assessment Units and what percentage of these patients would meet the 4 hour ED Standard.

## Findings

An 18 Bedded Frailty Assessment unit (FAU) would have an average bed occupancy of 70% allowing for 99% of patients who would suit admission to FAU to be admitted, with 94% of patients waiting for a bed on FAU waiting less than four hour in ED.

A 16 Bedded FAU would have an average bed occupancy of 77% of the time but the number of patients who would breach the four hour ED standard would increase by 8%

## Impact

Proposals have been made relating to reconfiguring wards working with the number of beds suggested in the model as a basis.

Additional pieces of work have been performed to solely model the size of the Medical Assessment unit with.

Discussions for how to improve the bed occupancy whilst maintaining the bed occupancy taken place and have involved allowing expected short stay medical patients to outlie in FAU when occupancy is low.


<!-- ===== hsma_1/H1_1002_modelling_resources_to_reduce_out_of_area_placements_MH/index.qmd ===== -->

---
title: "Modelling resources needed to reduce out of area placements in the Mental Health Acute Care pathway"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Mental Health
  - Patient Pathways
categories:
  - Discrete Event Simulation (DES)
  - Mental Health
  - NHS
author:
  - name: Karl Vile
    affiliation: Devon Partnership NHS Trust
organisations:
  - Devon Partnership NHS Trust
image: "1002.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Devon Partnership NHS Trust explored changes to its Urgent Care Pathway to reduce system pressure and avoid out-of-county care. Process mapping and a simulation model identified a need for additional beds. Key findings included high occupancy rates, the necessity to reduce demand and lengths of stay, and the importance of increasing bed numbers to enhance patient care and workforce efficiency.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

The research question for Devon Partnership NHS Trust was 'How would Devon Partnership NHS Trust need to change its Urgent Care Pathway in order to reduce pressure in the system and send no patients out of county for care.’
Process mapping was undertaken to understand the system and 3 years of anonymous patient level information (from October 2013 to September 2016) was collected on the care pathway, from referral to discharge.

A simulation model was developed and a number of scenarios were tested to assess the impact on the system of changes in demand for beds, lengths of stay and delayed discharge, and the number of inpatient beds in the system.

There were a number of key findings, which are described later in this paper, including :

-	There is a pressure in the mental health urgent care system, equivalent to 47 beds.
This pressure is managed by purchasing out of area beds and also by running the urgent care system above desired capacity. This means that wards routinely run at above 100% occupancy ; place of safety and extra care areas are used to hold patients whilst waiting for a bed ; leave beds can be backfilled and crisis house beds are spot purchased in some localities.
-	Both the out of area spend and the extent to which the existing capacity is running ‘hot’ needs to be addressed to reduce the pressure in the system. This will enhance care for patients and the workforce.
-	There is no one solution and a reduction in demand, lengths of stay (including delayed discharge) combined with an increase in the number of beds is required.
-	There are not enough beds in the system.
-	DPT inpatient wards have relatively high occupancy levels, often above 100%, and low lengths of stay. This provides high throughput per bed compared to alternatives, such as step down or out of area beds. As a consequence closing any DPT beds could result in a higher cost alternative.


<!-- ===== hsma_1/H1_1003_modelling_impact_strategies_to_improve_weekend_discharge/index.qmd ===== -->

---
title: "Modelling the impact of various strategies to improve weekend discharge rates"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Discharge
categories:
  - Discrete Event Simulation (DES)
  - Discharge
  - NHS
author:
  - name: Ryan Hunneman
    affiliation: University Hospitals Plymouth NHS Trust
organisations:
  - University Hospitals Plymouth NHS Trust
image: "1003.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Ensuring continuous inpatient bed availability is crucial for emergency and non-elective care. Discharge rates vary. Process mapping and Discrete Event Simulation (DES) identified bottlenecks and improved discharge pathways. Changes led to increased weekend discharges and better communication, positively impacting the discharge process, especially for complex patients.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

## The problem

Ensuring the continuous flow of inpatient bed availability for emergency and non-elective beds within the Acute Hospital setting is critical in enabling access to specialist and emergency treatment for patients. Variation in discharge rates across the seven-day week impact on the availability of inpatient beds both at the weekend and the start of the working week; typically weekends and Mondays are the worst performing days for discharge – this creates operational issues each week and has a negative impact on access to services and key operational performance standards.

## Method

-	Initial stakeholder mapping and analysis
-	Creation of project teams for Complex Discharges and Weekend Discharges
-	Process mapping of multiple discharge pathways for simple and complex discharges
- Analysis of critical steps to discharge including key delays and process step timings
-	Modelling of discharge pathways using Discrete Event Simulation (DES) software

## Results

The modelling process of identifying discharge pathways, key staff groups required, delays to process steps and the communication flow through the discharge process both during the week and at the weekend was very beneficial to identifying improvements in the discharge process. Whilst the overall process was very complicated to model using DES, identifying which bottlenecks were evident and visualising the entire process was very valuable.

## Impact

The changes made as a result of the modelling process and through the strategy groups formed to implement changes have seen positive results; this has contributed to increased discharges at the weekends and improved communication flows through the discharge process which has had a very positive effect on the whole discharge process especially for complex patients.


<!-- ===== hsma_1/H1_1004_modelling_impact_regionalisation_cardiac_arrest_centres/index.qmd ===== -->

---
title: "Modelling the impact of regionalising cardiac arrest centres"
techniques:
  - Geographic Modelling
areas:
  - Cardiology
  - Discharge
categories:
  - Georgraphical Modelling
  - Cardiology
  - Discharge
  - NHS
author:
  - name: Jess Lynde
    affiliation: South Western Ambulance Service NHS Trust (SWAST)
  - name: Hannah Trebilcock
    affiliation: South Western Ambulance Service NHS Trust (SWAST)
  - name: Sarah Black
    affiliation: South Western Ambulance Service NHS Trust (SWAST)
organisations:
  - South Western Ambulance Service NHS Trust (SWAST)
image: "1004.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Survival to hospital discharge after out-of-hospital cardiac arrest (OHCA) is around 7-8%. Analysis of the SWASFT Cardiac Arrest Registry showed survival rate variations due to different hospital services. A regional care system could improve survival rates. A collaborative project between ambulance services and hospitals aims to standardise care, addressing gaps and enhancing outcomes through shared data and best practices.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

## Problem

Survival to hospital discharge in patients suffering an out of hospital cardiac arrest (OHCA) has remained nationally at around 7-8% for at least the last 6 years.  Anecdotal evidence suggests that patients are not always conveyed to their nearest cardiac arrest centre.  The analysis of the SWASFT Cardiac Arrest Registry (2015-2016) identified large variation in survival rates for patients conveyed to different hospitals within the South West, possibly due to variation in the services provided.

Current guidelines suggest implementing a regional system of care for OHCA to improve survival rates and neurological outcomes; nonetheless it remains necessary to understand the impact of such a system on journey times and patient survival.

## Method

-	Literature review of the effect of longer travel times on cardiac arrest survival rates
-	Identify the current OHCA patients bypassing their nearest cardiac arrest centre
-	Develop a binomial logistic regression to predict survival rates from patient characteristics, travel time and hospital attended
-	Model the impact of different regional systems of care using a geographical model in Excel
-	Report initial findings at a stakeholder meeting

## Results

The analysis of the SWASFT Cardiac Arrest Registry confirmed that 13% of OHCA patients were bypassing their nearest cardiac arrest centre. The binomial logistic regression identified that patient characteristics (age, gender, UTSTEIN group) and hospital attended had a significant effect on survival rate. Travel time did not affect survival, although the confidence of this effect is limited to the range of travel times included in the available data (maximum 149 minutes).

The geographical model suggests improvements to survival rate are expected from a regional system of care. This is supported by

1. the differences in survival rate between hospitals cannot be explained by differences in patients or travel distances alone, and
2. differences in travel times, within the ranges available in the data, do not appear to affect outcomes of patients.

As with all models there are limitations associated with working assumptions and available data.

## Impact

The sharing of patient data in a collaborative project between ambulance service and regional hospitals would be unprecedented and highly beneficial in understanding regional variations, and perhaps working towards standardization of care.  Understandably, this project has been met with great interest by stakeholders, and they are driving a collective effort to gather data. In addition, the model has already identified gaps in the current standards of care and highlighted the potential gains that could be made from a standardised best practice across all cardiac arrest centres.


<!-- ===== hsma_1/H1_1005_modelling_potential_impact_of_clinical_division_unit_at_RD&E/index.qmd ===== -->

---
title: "Modelling the potential impact of having a Clinical Decision Unit"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Emergency Departments
  - Reducing Backlogs
categories:
  - Discrete Event Simulation (DES)
  - Reducing Backlogs
  - NHS
author:
  - name: Alaric Moore
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
image: "1005.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    A Clinical Decision Unit (CDU) at the Royal Devon & Exeter NHS Foundation Trust (RD&E) would manage ED patients needing up to 12 hours of care. Analysis showed that a 24/7 CDU with 4 cubicles could handle 2% of attendances, improving the 4-hour standard by 1.7%.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

A Clinical Decision Unit (CDU) is a designated area for Emergency Department (ED) patients who require testing, treatment, and observational medical management for up to 12hrs. Only patients that meet well-defined criteria where there is an expectation that the patient should be able to safely return home and avoid hospital inpatient admission should be transferred to a CDU.

The ED at the Royal Devon & Exeter NHS Foundation Trust (RD&E) is one of the only departments in England seeing over 100,000 patients a year without a CDU.

This project sought to identify the optimum size and impact of a potential CDU.

## The method

To understand the patient journey through the department, a pathway map was first produced with the assistance of a multi-disciplinary ED team. In order to understand trends and variation in patient demand, length of stay and potential CDU appropriateness; detailed analysis of anonymised data recorded on the Trust ED system was undertaken.

The ED clinical and managerial team determined that the criteria for CDU inclusion.
A model of the ED pathway was built in Simul8 incorporating the CDU clinical acceptance model and actual data from the whole of 2016.

## The results

With a CDU open 24hrs a day 7 days a week, 99.9% of the time 4 cubicles would be adequate.

In a year, just under 2% of attendances would be appropriate to route to the CDU which would have an impact of improving RD&E performance against the 4hr standard by +1.7%.

These results will be integrated into the ED capital programme business case going to the RD&E Board in June 2017.

