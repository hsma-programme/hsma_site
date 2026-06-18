<!-- ===== hsma_2/H2_2001_understanding_delays_in_MH_in_Devon/index.qmd ===== -->

---
title: "Using modelling to understand the delays in mental health services in Devon"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Mental Health
  - "NHS 10-year plan shifts: Hospital to Community"
categories:
  - Discrete Event Simulation (DES)
  - "NHS 10-year plan shifts: Hospital to Community"
  - NHS
author:
  - name: Simon Wellesley-Miller
    affiliation: Devon Partnership NHS Trust
organisations:
  - Devon Partnership NHS Trust
image: "2001.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    This project aimed to support Crisis Cafes,  offering an alternative service for those in a mental health crisis. Using modelling and data science, it will look at activity diversion, capacity needs, demand, and resource allocation. Seven models for Barnstaple, Exeter, and Torquay were created, demonstrating system demand and capacity, aiding resource planning and financial decisions.
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

The aim of this project was to look at the resourcing to support the establishment of Crisis Cafes - an alternative place for people who are in a mental health crisis to go rather than utilising out of hours, emergency or inpatient services.

Crisis Cafes provide increased choice and additional capacity to meet the needs of those in mental health crisis and provide early intervention which could avoid escalation of mental health needs.

The aim of this project was to try to answer the following questions using modelling and data science approaches :
-	How much activity can be diverted to the cafés?
-	What capacity will be needed to achieve a robust service?
-	What and where is the demand?
-	How to match demand and capacity
-	Given the limited resources available how many sites to commission and how to allocate,
-	How to determine suitable catchment areas?

Seven versions of model were created, for the localities of Barnstaple, Exeter, and Torquay. Separate data and models were built for each locality for weekdays and weekends. Pathways were modelled for each service.

The model helped demonstrate the demand and capacity of the system, allowing for appropriate resources to be planned to support the cafes, and associated financial decisions to be made.


<!-- ===== hsma_2/H2_2002_RCHT_eldercare_worksforce_mapping_frailty_pathway/index.qmd ===== -->

---
title: "RCHT Eldercare workforce mapping to identify needs and alternatives to cover the frailty pathway"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Frailty
categories:
  - Discrete Event Simulation (DES)
  - Frailty
  - NHS
author:
  - name: Claire Westoby
    affiliation: Royal Cornwall Hospitals NHS Trust
organisations:
  - Royal Cornwall Hospitals NHS Trust
image: "2002.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    After hospital admission, 12% of people over 70 experience reduced daily living abilities. Those with deteriorated balance and mobility in the first 48 hours had a 17.1% relative risk of death within 14 days. This project aimed to determine frailty workforce placement to impact more patients, reduce length of stay, and improve care quality. The model simulated patient pathways involving frailty nurses and doctors.
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

After a hospital admission, 12% of people over 70 experience a reduction in their ability to undertake daily living activities. Older people who saw a deterioration in their balance and mobility in their first 48 hours of hospital admission had a relative risk of death within fourteen days of 17.1%

The aim of this project was to determine where to base the existing frailty workforce in order to impact as many patients as possible and reduce their length of stay, as well as improving the quality of care and patient experience?

The model simulated the pathway from patient arrival, being seen by frailty nurse, and then either being admitted or discharged. Those that were admitted were then seen by a frailty doctor.


<!-- ===== hsma_2/H2_2003_ML_outpatient_client_utlilisation/index.qmd ===== -->

---
title: "Artificial Ian – can a machine learning tool learn when it is necessary to cancel surgery at Derriford Hospital?  And can we use geographic modelling methods to improve outpatient clinic utlilisation in the community?"
techniques:
  - Machine Learning
areas:
  - "NHS 10-year big bet: AI to drive productivity"
categories:
  - Machine Learning
  - "NHS 10-year big bet: AI to drive productivity"
  - NHS
author:
  - name: Simon Philpott
    affiliation: University Hospitals Plymouth NHS Trust
organisations:
  - University Hospitals Plymouth NHS Trust
image: "2003.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    This project aimed to use AI approaches to improve surgical cancellation decisions, addressing poor patient experiences. The model struggled due to insufficient data. A second project used geospatial visualisation (QGIS) to assess community outpatient clinic demand, finding increasing waiting lists and poor clinic utilisation, leading to improved patient booking into Peripheral Sites.
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

On the day surgical cancellations can offer a poor patient experience - there can be multiple cancellations for some patients, and in early 2018 University Hospitals Plymouth NHS Trust ranked as one of the worst for cancellations.  The aim of this project was to explore whether AI approaches could be used to create a model that can inform decision making around cancellations, sooner.

There were three key questions for the Machine learning model to answer:
-	Should I cancel a patient today?
-	How many patients should I cancel?
-	Which patient/s should I cancel?

A model was trained but performance was poor – there was insufficient data to allow the model to be able to replicate the human decision making taking place.

As a second project, the Trust used geospatial visualisation approaches (using QGIS software) to explore demand for community outpatient clinics.  The work found that there were increasing waiting lists and poor utilisation of clinics.  These results were used to improve their ability to book appropriate patients into Peripheral Sites.


<!-- ===== hsma_2/H2_2004_reducing_delays_glaucoma_treatment_Torbay/index.qmd ===== -->

---
title: "Reducing the delays to glaucoma treatment at Torbay Hospital"
techniques:
  - Discrete Event Simulation (DES)
  - "NHS 10-year plan shifts: Sickness to Prevention"
areas:
  - "NHS 10-year plan shifts: Sickness to Prevention"
  - Opthalmology
categories:
  - Discrete Event Simulation (DES)
  - Opthalmology
  - NHS
author:
  - name: Maria Moloney-Lucey
    affiliation: Devon County Council
  - name: Hayley Lewis
    affiliation: NHS South, Central and West CSU
organisations:
  - NHS South, Central and West CSU
image: "2004.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    This project assessed if the Glaucoma pathway increased treatment delays and blindness risk. The model showed reducing visual field check times had little impact on waiting times, but adding a second Photo & Scan machine nearly eliminated queues for this part of the pathway.
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

The aim of this project was to use modelling approaches to assess whether the current configuration of the Glaucoma pathway at Torbay Hospital was increasing delays in treatment, and thus increasing the risk of blindness.

The modelling found that reducing the amount of time visual field checks took (which were perceived to be a bottleneck) had little predicted impact on waiting times.  The model also found that adding a second Photo & Scan machine virtually eliminated queues for this part of the pathway.


<!-- ===== hsma_2/H2_2005_optimise_catheter_lab_efficiency_predict_stoke_bed_demand/index.qmd ===== -->

---
title: "Using modelling to optimise catheter lab efficiency and predict stroke bed demand"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Hospitals
  - Demand & Capacity
categories:
  - Discrete Event Simulation (DES)
  - Demand & Capacity
  - NHS
author:
  - name: Richard Barrett
    affiliation: Royal Cornwall Hospitals NHS Trust
organisations:
  - Royal Cornwall Hospitals NHS Trust
image: "2005.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    This project supported a business case for reconfiguring Acute Stroke Unit beds using a Discrete Event Simulation model. The model assessed patient cohorts, pathways, and bed requirements. It also aimed to improve Cardiac Catheter Labs' efficiency, addressing a 13% capacity loss and reducing patient delays.
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

This project was to be used to support a business case being prepared for reconfiguring beds on the Acute Stroke Unit in line with the Peer review recommendations

A Discrete Event Simulation model was developed to represent the entire pathway. The model took into account four different cohorts of patients and based on historic activity data, applied Inter arrival time distributions to each cohort, branched patients proportionally through the various pathways and applied variable lengths of stay dependant on diagnosis and discharge destinations.  The model included a range of parameters that could be modified between simulations to assess various scenarios and their impact on bed requirements.

The project also explored using modelling to improve the efficiency of the Cardiac Catheter Labs.  The trust had two labs each running two scheduled 4 hour lists per day Mon-Fri, but for numerous reasons the lists were not being utilised efficiently with consequential impacts on both inpatient and elective time from referral to procedure. During 2017 this resulted in an average list duration of 208 minutes representing a 13% loss of capacity. If this lost capacity could be eliminated/reduced this would:
•	Reduce overall length of stay for emergency patients waiting for lab procedures which in turn will help with overall hospital flow.
•	Improve patient pathways
•	Tackle patient delay for elective diagnostics/interventions which is in line with core Trust Objectives.

Meetings with the booking teams enabled the creation of a process flow diagram which highlighted a convoluted process from initial referral to eventual scheduling of procedures.


<!-- ===== hsma_2/H2_2006_improving_ambulance_response_times/index.qmd ===== -->

---
title: "Improving ambulance response times for life-threatening emergencies using simulation modelling"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Ambulance
categories:
  - Discrete Event Simulation (DES)
  - Ambulance
  - NHS
author:
  - name: Fiona Willmott
    affiliation: South Western Ambulance Service NHS Trust (SWAST)
organisations:
  - South Western Ambulance Service NHS Trust (SWAST)
image: "2006.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Category 1 ambulance calls are life-threatening, making up 8% of calls in the South West in 2018. The project aimed to reduce response times by reserving resources for these calls. A discrete event simulation model was created to determine the optimal resource allocation, balancing the needs of high and low acuity patients.
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

Category 1 ambulance calls are the most serious. They are immediately life threatening and, in 2018, approximately 8% of calls in the South West fell into this category. After the triage the call is passed to the dispatchers who co-ordinate the available resources and aim to meet these response times.
The response time is the time from the call being made to the arrival of an appropriate ambulance resource on scene. At the beginning of 2018, the ambulance trust was not meeting these times and our number one priority was to reduce the time taken to get to category 1 calls.

The aim of this project was to explore what would happen if dispatchers reserved a portion of resources for the higher acuity calls.  Specifically :
•	What is the optimum level of resources to “hold back” in order to meet the needs of category 1 patients?
•	What impact would this have on the lower acuity patients?
•	What is the optimum balance between these two?

A discrete event simulation model was built which could specify a certain number of resources to reserve for category 1 calls. When a call comes in, if it is category 1 call it is allocated an ambulance as soon as one is available. If it is any of the other lower priority categories, an ambulance will only be allocated if this will leave at least the reserved number of ambulances available.


<!-- ===== hsma_2/H2_2007_can_ambulance_dispatch_codes_determine_if_really_needed/index.qmd ===== -->

---
title: "Can ambulance dispatch codes be used to determine when an ambulance is really needed?"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Ambulance
  - "NHS 10-year big bet: AI to drive productivity"
categories:
  - Discrete Event Simulation (DES)
  - Ambulance
  - "NHS 10-year big bet: AI to drive productivity"
  - NHS
author:
  - name: Jessica Lynde
    affiliation: South Western Ambulance Service NHS Trust (SWAST)
organisations:
  - South Western Ambulance Service NHS Trust (SWAST)
image: "2007.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    This project aimed to rank dispatch codes by clinical acuity using Machine Learning, incorporating PPI group insights on medical history and co-morbidities. Phase 1 used call-taker info and Logistic Regression to optimise accuracy, leading to phase 2 algorithm generation. The active risk stratification model increased HART team utilisation, leading to a trial of Enhanced Hear and Treat.
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

The aim of this project was to rank dispatch codes by typical clinical acuity of the patients in those codes using Machine Learning approaches.  The project incorporated the views of a PPI group who helped to highlight the importance of patient medical history and co-morbidities in the model.

Phase 1 of the model used call-taker info (dispatch code and other items) plotted against conveyance. A series of Logistic Regression models was trained to test out optimal sample sizes and model regularisation, to boost accuracy. This led to Algorithm generation for phase 2, to test whether the scoring methodology in the Risk Stratification model could locate codes ‘not requiring an ambulance’.

The risk stratification model is in active use, increasing HART team utilisation, and leading to a trial of Enhanced Hear and Treat.  The project allowed for a balanced pragmatic approach by senior decision makers.


<!-- ===== hsma_2/H2_2008_reducing_waiting_times_spinal_patients/index.qmd ===== -->

---
title: "Reducing waiting times for spinal patients using simulation modelling"
techniques:
  - Machine Learning
areas:
  - Reducing Backlogs
categories:
  - Machine Learning
  - Reducing Backlogs
  - NHS
author:
  - name: Claire White
    affiliation: Somerset NHS Foundation Trust
  - name: Laura Copp
    affiliation: Somerset NHS Foundation Trust
  - name: Ramya Peter
    affiliation: NHS England
organisations:
  - NHS England
  - Somerset NHS Foundation Trust
image: "2008.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Routine reporting revealed increasing wait times for spinal patients, with elective patients waiting too long for treatment decisions due to factors like more appointments, diagnostic tests, and a complex pathway. A discrete event simulation of the spinal pathway looked at referral routes and wait times, showing variation in patient queues per consultant for further investigation.
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

Routine reporting exposed a continuing increase in the time spinal patients were waiting, and  elective spinal patients were waiting too long for a decision to be made on their treatment plan. There were many contributing factors such as increased appointments, diagnostic tests and a complicated pathway

A discrete event simulation of the spinal pathway was developed, which looked at the referral routes in and wait times between appointments.  The model demonstrated some variation across the number of patients in the queues per consultant for further investigation.


<!-- ===== hsma_2/H2_2009_testing_intervention_to_reduce_continuing_healthcaare_assesessment_backlog/index.qmd ===== -->

---
title: "Testing interventions to reduce the Continuing Healthcare Assessment backlog"
techniques:
  - System Dynamics
areas:
  - Reducing Backlogs
categories:
  - System Dynamics
  - Reducing Backlogs
  - NHS
author:
  - name: Ryan Worth
    affiliation: NHS South, Central and West CSU
organisations:
  - NHS South, Central and West CSU
image: "2009.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    A System Dynamics model was developed to show the rated of system flow and interdependencies of components in the system. The model aids Clinical Commissioning Groups planning and decision-making, supporting future demand management.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url: https://insightmaker.com/insight/6eo34fBaxCxf6Grx6KFCZg/CHC-Model-v1-RW
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

In the first quarter of 2017/18 the number of people waiting longer than 28 days for their Continuing Healthcare (CHC) Assessment was 54.3 per 50,000 compared to the national average of 10.2 per 50,000.

A System Dynamics model was built to show the rates of system flow and interdependencies of components in the system.

The model found that :
•	There were 171 waiting for Decision Support Tool (DST), 51 waiting for Decision and 1009 CHC Eligible.
•	Numbers waiting for DST were predicted to reach controlled levels during Quarter 1 of 19/20.
•	A reduction in numbers awaiting Decision was only predicted to occur following a complete reduction in those waiting DST.

The model was made available freely using InsightMaker - CHC Model v1 RW | Insight Maker

Quote from Programme Manager:
“The model provides a visual understanding of our waiting list and supports CCG infrastructure and resource planning for future levels of demand. It supports commissioning decision making and helps to focus the team in specific areas within the system.”


<!-- ===== hsma_2/H2_2010_develop_model_understand_delays_to_discharge/index.qmd ===== -->

---
title: "Developing a model to understand delays to discharge"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Discharge
  - Hospitals
categories:
  - Discrete Event Simulation (DES)
  - Discharge
  - Hospitals
  - NHS
author:
  - name: Rohan Kandasamy
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
image: "2010.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The hospital faces increasing bed pressures, with over 100 medically fit patients often waiting for discharge due to social care and rehabilitation delays. This project aimed to create a Discrete Event Simulation model to estimate patient length of stay based on demographics, comorbidities, and social care needs, experimenting with scenarios like reducing placement times and accelerating discharge for frail patients.
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

The hospital is under ever-increasing bed pressures; at any one time, over 100 medically fit patients can be waiting for discharge. Some of this delay is due to provision of social care, some of this delay is due to ongoing rehabilitation (physio/occupational therapy workup).

The aim of this project was to create a Discrete Event Simulation model that attempted to estimate an individual patient’s length of stay (LOS) based on patient demographics, comorbidities and previous admission history, as well as the patient’s social care need.

The model experimented with various scenarios, including reducing placement times, and accelerated discharge for frail patients.

