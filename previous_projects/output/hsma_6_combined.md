<!-- ===== hsma_6/H6_6000_core20plus50_ml_explainable_ai_mental_health_dnas/index.qmd ===== -->

---
title: "Using Machine Learning and Explainable AI to predict and understand mental health appointment DNAs to reduce inequalities"
techniques:
  - Machine Learning
  - Geographic Modelling
  - Travel Times
  - Explainable AI
areas:
  - Mental Health
  - Non-attendance Prediction
  - Inequalities
  - Community Mental Health
categories:
  - Machine Learning
  - Geographic Modelling
  - Travel Times
  - Explainable AI
author:
  - name: Heath McDonald
    affiliation: Lancashire and South Cumbria NHS Foundation Trust
organisations:
  - Lancashire and South Cumbria NHS Foundation Trust
image: "6000.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project uses machine learning to explore correlations whether there is a correlation between missed mental health appointments and factors like deprivation, age, ethnicity, and travel distance. Reducing non-attendance can significantly impact waiting lists.
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

As a provider of Mental Health Services for SMI, Lancashire & South Cumbria NHS Foundation Trust is committed to helping to deliver the aims of Core20Plus5. Core20PLUS5 is a national NHS England approach to inform action to reduce healthcare inequalities at both national and system level.

The aim of this HSMA project is to use machine learning to help understand whether there is a correlation between failed attendance of mental health outpatient appointments and deprivation, or whether this could be being influenced by other factors (features) such as age, ethnicity, the distance travelled to get to those appointments etc.

With constantly growing waiting lists. anything we can do to reduce non-attendance can have a significant impact on these.

The project idea is to develop a Machine learning model to investigate whether there is a relationship between travel distance and method and appointment attendance. The project will also use explainable AI to help users understand what the results mean.


<!-- ===== hsma_6/H6_6001_DES_modelling_non_elective_flow/index.qmd ===== -->

---
title: "Discrete Event Simulation modelling of Non-elective flow"
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Patient Flow
  - Non-elective Admissions
  - Emergency Departments
  - Same-day Emergency Care
categories:
  - Discrete Event Simulation (DES)
  - Streamlit
  - Patient Flow
  - Emergency Departments
  - Same-day Emergency Care
author:
  - name: Helena Robinson
    affiliation: Countess of Chester Hospital NHS Foundation Trust
organisations:
  - Countess of Chester Hospital NHS Foundation Trust
image: "6001.PNG"
title-block-banner: ../../banner.png
repo: Y
page-layout: full
grid:
  sidebar-width: 0px
  body-width: 1100px
  margin-width: 300px
  gutter-width: 1.5rem
toc: false
pub-info:
  abstract: |
    Poor patient flow in Emergency Departments leads to long admission waits and poorer patient outcomes. Strategies include increasing beds and reducing discharge delays. This project uses Discrete Event Simulation to explore bed numbers, length of stay, and Same Day Emergency Care impacts on ED waits, aiming to optimise patient flow.
  links:
  - name: Video
    url: https://youtu.be/0DUx5hhxjoA?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/helenajr/Non-Elective-Flow-Simulation
    icon: fa-brands fa-github
  - name: App
    url: https://non-elective-flow-simulation-coch.streamlit.app/
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://drive.google.com/file/d/1BIUDaDfDp2cj6EF19908XQ4eB7h9GMCp/view?usp=drive_link
    icon: fa-solid fa-person-chalkboard
---

Poor patient flow is leading to long waits for admission in Emergency Departments. This means there is poor performance against all the key ED wait metrics for the hospital and more importantly, there is evidence that long waits for admission in ED are associated with poorer outcomes for patients.

The two main strategies employed to tackle this problem is

- increasing the number of beds (by creation of escalation beds)
- trying to decrease discharge delays (reducing length of stay).

Additionally, with the Same Day Emergency Care (SDEC) facility, it is unclear how the number of people admitted through this facility impacts the waits of those in ED.

This projects aimed to answer questions such as:

- Given x beds, how far does admitted length of stay have to reduce to meet particular waiting time targets for those queuing in ED? (Evidence based target)
- If we open 15 beds but keep admitted length of stay the same, what is the impact on ED waiting times and the various targets? (Evidence for a particular management strategy)
- What is the optimum number of people to stream from ED to SDEC to minimise ED waits? (Evidence for a particular management strategy)

This project created Discrete Event Simulation model(s), using HSMA training, to provide evidence for the questions above.

The team also created a friendly user interface that stakeholders can try out scenarios and help understand how the model works.

### Talks

{{< video https://youtu.be/0DUx5hhxjoA?feature=shared >}}

### App

Click [here](https://non-elective-flow-simulation-coch.streamlit.app/) to open the app in a new window.

```{=html}
<iframe width='1050' height='700' src='https://non-elective-flow-simulation-coch.streamlit.app/?embed=true' title='Non-elective Flow App'></iframe>
```


<!-- ===== hsma_6/H6_6002_GM_healthcare_worker_vaccination_uptake/index.qmd ===== -->

---
title: "Geographic and Boosted Tree Modelling of Healthcare worker vaccination uptake"
techniques:
  - Geographic Modelling
  - Machine Learning
areas:
  - Vaccination
  - COVID-19
  - Workforce
categories:
  - Geographic Modelling
  - Machine Learning
  - Vaccination
  - COVID-19
  - Workforce
author:
  - name: Yasmin Ibrahim
    affiliation: NHS England
organisations:
  - NHS England
image: "6002.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    There is a decreasing uptake of COVID and flu vaccinations among healthcare workers. Identifying patterns by staff uptake, gender, ethnicity, deprivation, and other factors can help. Using geographic and boosted tree modelling, along with regression analysis, can capture these patterns and provide useful data for stakeholders to address the issue.
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

There is low uptake of Healthcare Workers for COVID and Flu, which is in many Trusts decreasing with each season.

Trusts and regions, as well as NHS England policy teams would benefit from identifying patterns among healthcare workers: staff uptake, gender, ethnicity, deprivation, frontline status, age group, eligibility (in another cohort other than healthcare worker status).

Using a mixed-method approach. Geographic modelling of healthcare worker uptake by Trust, ICB and region, and boosted tree modelling of the data to capture patterns in the data and reduces bias and variance. Regression modelling would also be useful to produce data tables to present to stakeholders (e.g. odds ratios for logistic regression).


<!-- ===== hsma_6/H6_6003_DESmond_62_day_prostate_cancer_pathway/index.qmd ===== -->

---
title: "DESmond: Discrete Event Simulation and Artificially Intelligent Forecasting: Modelling a Prostate Cancer Pathway"
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Cancer
  - Waiting Times
categories:
  - Discrete Event Simulation (DES)
  - Streamlit
  - 2-week Wait
  - Cancer
  - Waiting Times
author:
  - name: Jake Wilson
    affiliation: Great Western Hospitals NHS Foundation Trust
organisations:
  - Great Western Hospitals NHS Foundation Trust
image: "6003.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project aims to develop a Discrete Event Simulation model to predict demand and identify potential bottlenecks using live data. This model could help reallocate resources proactively, helping to ensure people have the fastest possible treatment.
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

Prostate cancer pathways involves numerous activities such as triaging, imaging, biopsies as well as multiple decisions along the way. The smooth running of the pathway relies upon having the necessary resources allocated each of these events e.g. biopsy clinics, access to imaging etc.

We want to develop a system which can anticipate the demand for resources, dependant on the number of referrals and resources allocated.

The aim is

- to create a Discrete Event Simulation model to model the current pathway
- to feed live data into the model in order to predict where bottlenecks might occur
- make use of forecasting methods to predicts what changes are needed in resource allocation

The project outcome will be a simulation model with an interactive, web app based interface and a dashboard which illustrates key metrics.


<!-- ===== hsma_6/H6_6005_Improving_ambulance_care/index.qmd ===== -->

---
title: "Improving ambulance care via fast feedback from Quality Care Indicators"
techniques:
  - Machine Learning
  - Natural Language Processing (NLP)
  - Sentiment Analysis
areas:
  - Ambulance
categories:
  - Machine Learning
  - Natural Language Processing (NLP)
  - Sentiment Analysis
  - Ambulance
author:
  - name: Phil King
    affiliation: South Central Ambulance Service NHS Foundation Trust (SCAS)
  - name: James Wise
    affiliation: South Central Ambulance Service NHS Foundation Trust (SCAS)
organisations:
  - South Central Ambulance Service NHS Foundation Trust (SCAS)
image: "6005.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project aims to improve ACQI data quality and provide rapid feedback using a tool to analyse free text fields, capture sentiment, categorize incidents, and assess treatment appropriateness. This tool could be shared with other Ambulance Trusts and serve as a backup for to manually review data. It will also predict rule changes and their impact on scores.
  links:
  - name: Video
    url: https://youtu.be/zKZv3zWcXzc?feature=shared
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
  - name: Slides
    url: https://docs.google.com/presentation/d/1q1rPYhehziILwtqK9yrtFaU6JklD2c3M/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

Our aim is to improve Ambulance Clinical Quality Indicators (ACQI) data quality and rapidly provide feedback from all ACQI records. There is potential for this tool to be shared with other Ambulance Trusts using the same or similar data collection techniques. This would be achieved with a tool that can analyse free text fields to complete missing data, capture the sentiment of clinical notes, categorise the type of incident and assess if the treatment given was appropriate. It could be utilised as a backup process to manually reviewing data should there be a resourcing issue within the team. It will also evidence if any changes could be made to the clinical records to improve data capture.

We would like to consider how the free text could be searched to find positive and negative statements that impact if a record passes or fails a measure within each ACQI. In addition, creating a tool that would predict any changes to the 'rules' and their impact on the scores.

{{< video https://youtu.be/zKZv3zWcXzc?feature=shared >}}


<!-- ===== hsma_6/H6_6006_DES_childrens_ADHD_diagnosis_and_treatment/index.qmd ===== -->

---
title: "Discrete Event Simulation modelling of childrens ADHD diagnosis and treatment"
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Neurodiversity
  - Paediatric
  - Waiting Lists
  - Waiting Times
categories:
  - Discrete Event Simulation (DES)
  - Neurodiversity
  - Streamlit
  - Paediatric
  - Waiting Lists
  - Waiting Times
author:
  - name: Heath McDonald
    affiliation: Lancashire and South Cumbria NHS Foundation Trust
organisations:
  - Lancashire and South Cumbria NHS Foundation Trust
image: "6006.PNG"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project uses Discrete Event Simulation to model the children's ADHD diagnostic and treatment pathway, aiming to reduce waiting times and lists. It proposes a new pathway with preliminary diagnostic testing to ensure accurate ADHD assessments. The model will evaluate the impact of these changes and may extend to include 1:1 and group session appointments.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=EmfpThPdXKo
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/MightyAtom220474/ADHD-Pathway-DES
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://drive.google.com/file/d/15AsF2U4BnsXbbGQRxIcFkDW130j4JiaF/view?usp=drive_link
    icon: fa-solid fa-person-chalkboard
---

This project is using Discrete Event Simulation to model the children's ADHD diagnostic and treatment pathway. The model will be used to identify delays and potential strategies to reduce waiting lists and waiting times for children accessing treatment.

The current assessment process is lengthy, proposing a new pathway that would include undertaking some of the diagnostic testing before undertaking a more comprehensive testing so that there is more confidence that patients who have assessments have ADHD.

The model will capture the changes to the pathway to assess the potential impact of these changes on waiting times and will also capture formal diagnosis and medication titration aspects of the pathway. The model may be extended to look at further 1:1 and group session appointments.

{{< video https://www.youtube.com/watch?v=EmfpThPdXKo >}}


<!-- ===== hsma_6/H6_6007_Modelling_eye_injection_pathways/index.qmd ===== -->

---
title: "Modelling eye injection pathways"
techniques:
  - Agent Based Simulation (ABS)
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Opthalmology
categories:
  - Agent Based Simulation (ABS)
  - Discrete Event Simulation (DES)
  - Streamlit
  - Opthalmology
author:
  - name: Luke Herbert
    affiliation: Surrey and Sussex Healthcare NHS Trust
organisations:
  - Surrey and Sussex Healthcare NHS Trust
image: "6007.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    The project aims to develop a flexible simulation model to optimise anti-VEGF treatment strategies in ophthalmology. It will use dual modelling frameworks, a modular design, and an interactive dashboard. The model will analyse clinical effectiveness, costs, and resource requirements, adapting to new treatments. The objective is to provide a tool to improve patient outcomes and optimize resource use and costs.
  links:
  - name: Video
    url: https://youtu.be/0OKev_kbQEc?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/lh/vegf-1
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

This project aims to develop a comprehensive and flexible simulation model to optimise anti-VEGF treatment strategies in ophthalmology. The model will address the complex challenges in anti-VEGF treatments, including frequent injections, multiple treatment options, and diverse strategies, whilst considering the significant resource consumption and high costs associated with these treatments.

Key features of the project include:

- Dual modelling approach using Mesa and SimPy frameworks to determine the most suitable platform.
- Modular design to accommodate various treatment strategies, drug efficacies, and clinic capacities.
- User-friendly interface with interactive dashboards for stakeholders to explore different scenarios.
- Analysis of clinical effectiveness, costs, and resource requirements for various treatment approaches.
- Adaptability to incorporate new drugs and treatment paradigms as they emerge.

Project Objectives: The project aims to provide a tool for data-driven decision-making in ophthalmology clinic management, potentially improving patient outcomes whilst optimising resource use and costs.

{{< video https://youtu.be/0OKev_kbQEc?feature=shared >}}


<!-- ===== hsma_6/H6_6008_Modelling_GP_phone_calls/index.qmd ===== -->

---
title: "Modelling GP Phone calls"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - 111 Service
  - Emergency Departments
  - Primary Care (GP)
categories:
  - Discrete Event Simulation (DES)
  - 111 Service
  - Emergency Departments
  - Primary Care (GP)
author:
  - name: Sarah Blincko
    affiliation: NHS England
organisations:
  - NHS England
image: "6008.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
  links:
  - name: Video
    url: https://youtu.be/zeYG0EJ83bA?feature=share
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
  - name: Slides
    url: https://docs.google.com/presentation/d/1RlFY3GLDJg4r89WZ1QNGWaeBT5Fa-sp2/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

This project will use Discrete Event Simulation to model patients' navigation of GP vs 111 services and assess the knock-on effect for Emergency Departments.

{{< video https://youtu.be/zeYG0EJ83bA?feature=share >}}


<!-- ===== hsma_6/H6_6009_ML_to_predict_future_fraility/index.qmd ===== -->

---
title: "Using machine learning models to predict future frailty"
techniques:
  - Machine Learning
areas:
  - Frailty
  - Older Adults
categories:
  - Machine Learning
  - Frailty
  - Older Adults
author:
  - name: Emil Frances-Chi
    affiliation: NHS West Yorkshire ICB
  - name: Sid Kumar
    affiliation: NHS West Yorkshire ICB
organisations:
  - NHS West Yorkshire ICB
image: "6009.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project uses machine learning to estimate future frailty in the Wakefield District and identify key predictive features. It aims to plan resource allocation based on evidence, using two years of linked data. The project will also explore predicting other long-term conditions and produce reports and a user interface for stakeholders.
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

This project will use machine learning methods to estimate the size of the Wakefield District population who will likely be frail in 2 / 3 / 4 years time, and to understand the key features used to predict whether a person will become frail in the near future at a local level.

Planning for future population health needs

- The ability to plan and design resource allocation (e.g. beds available) in an evidence-based manner is a crucial and consistent priority within the ICB
- There is soon to be approximately 2 years’ worth of linked data, allowing us to begin building and evaluating the use of ML-based techniques aiming to predict the future prevalence of various LTCs or conditions
- Pending the outcomes of this project, we anticipate there to be future scope to adapt similar approached and apply learning to predicting the future prevalence of other LTCs such as diabetes, hypertension, CVD conditions, respiratory conditions and so forth

The project will produce reports from the work and potentially a dashboard or other user interface.


<!-- ===== hsma_6/H6_6010_Understanding_drivers_of_increased_length_of_stay/index.qmd ===== -->

---
title: "Understanding drivers of increased length of stay"
techniques:
  - Casual Analysis
  - Machine Learning
  - Explainable AI
  - Synthetic Data
  - Streamlit
  - System Dynamics
areas:
  - Length of Stay
  - Inpatients
  - Understanding Drivers
categories:
  - Casual Analysis
  - Machine Learning
  - Explainable AI
  - Synthetic Data
  - Streamlit
  - System Dynamics
  - Length of Stay
  - Inpatients
  - Understanding Drivers
author:
  - name: Jake Kealey
    affiliation: NHS North Central London ICB
organisations:
  - NHS North Central London ICB
image: "6010.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    NCL has seen a rise in long Length of Stay (LoS) over the past 5 years, causing system strain. This project aims to develop a causal model to identify factors affecting LoS and estimate the impact of interventions. Key aims include building qualitative and quantitative models of LoS and modelling changes in response to interventions.
  links:
  - name: Video
    url: https://youtu.be/SH4geMXr8a8?feature=shared
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
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

North Central London (NCL) has observed a consistent increase in long Length of Stay (LoS) over the past 5 years. Increasing length of stay means a higher capacity is needed for the same demand which causes system strain.

Stakeholders are interested in understanding why length of stay has increased within NCL so that that can introduce appropriate measures to reduce it.

This project proposes to develop a causal model that can be used to identify relations between admission features, operations and length of stay. The model will be used to understand site level drivers to estimate the potential impact of proposed interventions.

Key Aims:

- To build a qualitative model of the drivers of Length of Stay in acute providers in NCL
- Build a quantitative model(s) of LoS
- Model changes in LoS in response to interventions (stretching)

{{< video https://youtu.be/SH4geMXr8a8?feature=shared >}}


<!-- ===== hsma_6/H6_6011_Forecasting_modelling_for_A&E_attendance/index.qmd ===== -->

---
title: "Forecasting modelling for A&E attendance"
techniques:
  - Forecasting
  - Reproducible Analytical Pipelines (RAP)
areas:
  - Emergency Departments
  - Demand & Capacity
  - Seasonality
categories:
  - Forecasting
  - Reproducible Analytical Pipelines (RAP)
  - Emergency Departments
  - Demand & Capacity
  - Seasonality
author:
  - name: Yu Qiao
    affiliation: Liverpool University Hospitals NHS Foundation Trust
organisations:
  - Liverpool University Hospitals NHS Foundation Trust
image: "6011.PNG"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aims to forecast A&E attendances 6 weeks in advance, considering seasonal patterns. This helps manage limited resources, plan staffing levels, and assess the need for escalation during abnormal events. Using Time Series Forecasting and a Repeatable Analytical Pipeline, the project addresses the unpredictability of A&E demand influenced by various factors.
  links:
  - name: Video
    url: https://youtu.be/uywbayhnass?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Case Study
    url: https://hsma.co.uk/impact_posters/Forecasting%20AE%20attendance.png
    icon: fa-solid fa-file-lines
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
  - name: Slides
    url: https://docs.google.com/presentation/d/1XaDSIpQDPCXDF7sBMhYlOwdyPSa66VR7/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

The aim of this project was to forecast future A&E attendances 6 weeks in advance, accounting for seasonal patterns.

## Original project brief

NHS A&E is under pressure nationwide for a long-time and often we do not know what lies ahead of us to manage the limited resources available and understand when interventions and helps are needed. This is in addition to seasonal pressures.

Currently A&E has a challenging time looking ahead and manage staffing level needed to match the demand. Furthermore, this can help staff to assess if an escalation process is needed when the abnormal events occur.

A&E is known for its unpredictability in demand that varies with seasonal trend, location, population, weather and various of other factors.

This project will use Time Series Forecasting methods and a Repeatable Analytical Pipeline for Deployment.

## Case Study

![](../../../impact_posters/Forecasting%20AE%20attendance.png){.lightbox}

## Video

{{< video https://youtu.be/uywbayhnass?feature=shared >}}


<!-- ===== hsma_6/H6_6012_Using_classification_modelling_to investigate_changes_in_ HRG/index.qmd ===== -->

---
title: "Using classification modelling technques to investigate changes in Healthcare Resources Group (HRG) coding over time"
techniques:
  - Machine Learning
  - Explainable AI
areas:
  - Clinical Coding
  - Costs
categories:
  - Machine Learning
  - Explainable AI
author:
  - name: Chris Todd
    affiliation: NHS England
organisations:
  - NHS England
image: "6012.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project will use classification modelling and explainable AI to identify changes in complexity and comorbidity categorisation over time, ensuring accurate cost pressure insights.
  links:
  - name: Video
    url: https://youtu.be/zeYG0EJ83bA?feature=shared
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
  - name: Slides
    url: https://docs.google.com/presentation/d/1fGS1mKo8BrF_I4wy5AAzjDsdETnUaFnE/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

The Medium-Term Activity Projections (MTAP) model produces a set of baseline activity and price-weighted contact projections to 2040/41 for NHS England for some types of activity. As part of the MTAP project, we want to provide insight into the cost pressure based on this projected activity. Modelling the absolute cost is not possible, so one widely used approach to modelling cost pressure is using cost or price ‘weights’ for distinct and specific activity types. Changes in the ratios of different activity types are captured by the sum of the weighted activity.

Healthcare Resource Group (HRG) codes are used in the NHS to categorise types of inpatient activity by assigning one of around 3,000 5-digit codes. The first 4 digits indicate the primary treatment or reason for care, e.g. primary hip replacement, and the 5th digit capturing complexity and comorbidities through the recording of secondary diagnoses. However, in recent years there has been a huge increase in the recording of secondary diagnoses with the introduction of Electronic Patient Records (EPR), but there is a hypothesis that this change does not represent a real increase in patient co-morbidity, and ‘coding creep’ is present.

To deal with this, National Cost Collection (previously known as Reference Costs) data is used to look at the relationship over time between the proportion of activity in each complexity category (the 5th character of the HRG) and the change in the average relative cost of each HRG. The hypothesis is that if increases in the proportion of more complex patients are real, then this should not lead to a reduction in the average relative cost of those HRG.

This research project proposes to identify whether the key factors influencing the complexity and comorbidity categorisation (CCC) have changed over time by:

1. Training a classification model  to predict CCCs, using secondary diagnoses in the patient records as input features.  The model will be trained on data for a given year, e.g. 2016/17, and the model performance for other time periods (e.g. 2022/23) will be compared. A significant change in performance may indicate that the factors influencing CCC have changed. If the 2016/17 performance gradually decreases over time as the use of EPR have been increasing, it could support the coding drift hypothesis.

2. Using explainable AI methods to identify the key factors driving classification in two time periods to assess if there has been a significant change.

3. Use classification modelling approach to identify the key factors driving the prediction of HRG CCC and actual costs using National Cost Collection data over a given time period. If the HRG codes are reflective of reality, features should have similar relative importance in each model.

{{< video https://youtu.be/zeYG0EJ83bA?feature=shared >}}


<!-- ===== hsma_6/H6_6013_Modelling_bed_occupancy_acute_ward/index.qmd ===== -->

---
title: "Modelling bed occupancy on an Acute Ward"
techniques:
  - Forecasting
  - Machine Learning
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Length of Stay
  - Inpatients
  - Bed Occupancy
  - Demand & Capacity
categories:
  - Forecasting
  - Machine Learning
  - Discrete Event Simulation (DES)
  - Streamlit
  - Length of Stay
  - Inpatients
  - Bed Occupancy
  - Demand & Capacity
author:
  - name: Rey Tan
    affiliation: Royal United Hospitals Bath NHS Foundation Trust
organisations:
  - Royal United Hospitals Bath NHS Foundation Trust
image: "6013.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    The project aims to develop a tool for time series forecasting of bed occupancy using historical data, incorporating seasonality and growth. A web-based app will simulate acute bed models, including variables like closed beds and additional capacity. Using machine learning and discrete event simulation, the tool will aid decision-making and provide reliable daily forecasts.
  links:
  - name: Video
    url: https://youtu.be/SH4geMXr8a8?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/ReyTan8/Project---DES-Vidigi
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

The aim of this project is to develop a tool to perform time series forecasting on bed occupancy based on historical data, incorporating variables like seasonality and growth. To build a web-based application that enables end users to simulate acute bed model, with the ability to include variables like closed beds, additional capacity, community availability etc, in turn aiding decision making.

The problem:

- Current bed occupancy forecast is done on Excel based on historical monthly averages
- High level position but lacking in flexibility
- Daily bed model is manually tweaked, and unable to simulate possible outcome

Using Machine learning and discrete event simulation the aim is for the project to predict values close to actual measures. For the user to utilise the web app on a day to day basis and find it a reliable tool for decision making.

{{< video https://youtu.be/SH4geMXr8a8?feature=shared >}}


<!-- ===== hsma_6/H6_6015_Forecasting_the_supply_of_medical_doctors/index.qmd ===== -->

---
title: "Forecasting the supply of medical doctors"
techniques:
  - Forecasting
areas:
  - Workforce
categories:
  - Forecasting
  - Workforce
author:
  - name: Sara Fundu
    affiliation: The Royal College of Pathologists
organisations:
  - The Royal College of Pathologists
image: "6015.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project aims to forecast the regional demand for medical doctors, considering factors like trainees and population. It will plot a graph showing the current supply versus demand. Additionally, it will simulate outcomes under different scenarios, such as changes in trainee numbers or population health, to better understand and address the gap.
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

The problem: Not enough medical doctors by region and we need to establish the gap between what we have and what we need.

The Aim: Forecast medical doctors required by region, taking into account relevant factors for example, trainees coming in, population etc.

The Output: To plot a graph to show our current supply and what we demand.

Bonus would be to be able to simulate outcome of demand, if input is amended to reflect different scenarios i.e. number of trainees decreases or population ill health increases etc


<!-- ===== hsma_6/H6_6016_Optimising_the_location_of_breast_cancer_diagnostic_services/index.qmd ===== -->

---
title: "Optimising the location of Breast Cancer diagnostic services across Devon"
techniques:
  - Geographic Modelling
  - Travel Times
areas:
  - Cancer
  - Women's Health
categories:
  - Geographic Modelling
  - Travel Times
  - Cancer
  - Women's Health
author:
  - name: Gill Baker
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Brandon Jones
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Kat Pamatmat
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
image: "6016.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Over 6000 patients are referred annually for fast-track breast symptom diagnosis at RD&E and NDDH. Increasing referrals and limited infrastructure necessitate building or extending diagnostic units. The project aims to determine optimal locations for additional services to minimize patient travel time and reduce costs, using data science to map demand and calculate travel distances and benefits.
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

Over 6000 patients a year are referred to Royal Devon & Exeter Hospital (RD&E) and North Devon District Hospital (NDDH) for fast-track breast symptom diagnosis. The fast-track clinic requires a clinician, a mammography team and a consultant radiologist/radiographer plus support staff. The imaging needs to take place in specialised rooms. As population and awareness of breast cancer increases there are increasing referrals and the current infrastructure at both RD&E and NDDH will not be sufficient to meet future demand. It is therefore necessary to build a new breast diagnostic unit or extend an existing one. It is likely to be prohibitively expensive to build at both NDDH and RD&E. At present specific GP surgeries refer patients to either NDDH or RD&E. However, the two hospitals are now managed as part of a single NHS Trust called RDUH. Each hospital requires breast diagnosis infrastructure on site as it is used for inpatient and emergency admissions as well as for elective diagnosis services so we need at least two breast diagnosis centres but data science may be used to help determine whether there is a value in building a third centre and/or diverting referrals from specific GPs to one of the existing units.

The aim of this project is to determine where additional breast diagnostic services should be placed to minimise overall travel time for patients whilst reducing infrastructure and running costs.

Objectives include the following:

- To map breast referral demand by GP and calculate the weighted average distance and/or travel time from each GP to RD&E, NDDH and a potential central location.
- To calculate the percentage of patients who would benefit from a central location.
- To calculate the shortest distance/travel time from each GP to the three locations and determine the reduction or increase in mileage if patients were diverted from their current default hospital to one of the other two centres.


<!-- ===== hsma_6/H6_6017_Referral_to  treatment_waiting_times_for_Neurosurgical_patients/index.qmd ===== -->

---
title: "Referral to treatment waiting times for Neurosurgical patients"
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Surgical
  - Neurology
  - Waiting Lists
  - Waiting Times
categories:
  - Discrete Event Simulation (DES)
  - Streamlit
  - Surgical
  - Neurology
  - Waiting Lists
  - Waiting Times
author:
  - name: Andrew Sharrock
    affiliation: The Walton Centre NHS Foundation Trust
organisations:
  - The Walton Centre NHS Foundation Trust
image: "6017.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project models the neurosurgical patient pathway to predict waiting list changes and treatment wait times. It aims to add user interaction to explore how capacity adjustments affect waiting times and track patients waiting over 52 weeks each month.
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

This project will aim to model the pathway for Neurosurgical patients, and to explore, based on current waiting times,

- will the waiting list grow or reduce
- how long patients may wait for treatment

The aim is to add user interaction, to see how an increase/reduction in capacity affects waiting times. Also to be able to see how many patients are waiting over 52 weeks at each month end.


<!-- ===== hsma_6/H6_6018_predicting_risk_of_injurious_falls/index.qmd ===== -->

---
title: "Predicting the risk of injurious falls in older people with atrial fibrillation"
techniques:
  - Machine Learning
  - Explainable AI
areas:
  - Older Adults
categories:
  - Machine Learning
  - Explainable AI
  - Older Adults
author:
  - name: Anneka Mitchell
    affiliation: University Hospitals Plymouth NHS Trust
organisations:
  - University Hospitals Plymouth NHS Trust
image: "6018.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Atrial fibrillation (AF) increases stroke risk, and anticoagulation reduces this risk but can cause bleeding. Despite guidelines, many clinicians avoid prescribing anticoagulants to those at risk of falls. This project explores using machine learning to predict injurious falls in older AF patients and aims to develop a tool to personalize anticoagulant treatment based on falls risk.
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

Atrial fibrillation (AF) is a common cardiac arrhythmia which increases the risk of stroke.

Anticoagulation is very effective in reducing stroke risk but can increase the risk of bleeding, a much feared consequence of anticoagulation is bleeding on the brain. National and international guidance states that anticoagulation should not be withheld because of falls as the benefits still outweigh the risks but many clinicians choose not to prescribe these medications to people who fall or those at risk of falls because they don’t believe the evidence supports this recommendation.

The initial stage aims of this project is to explore if machine learning techniques can be used to develop a model that can predict injurious falls in older people with AF and determine what features are important.

The longer term aim of this project is to ascertain whether a tool could be developed to personalise anticoagulant treatment based on falls risk to help clinicians and patients make more informed treatment decisions.


<!-- ===== hsma_6/H6_6019_clinical_coding_automation/index.qmd ===== -->

---
title: "Clinical coding automation using Natural Language Processing"
techniques:
  - Natural Language Processing (NLP)
areas:
  - Clinical Coding
categories:
  - Natural Language Processing (NLP)
  - Clinical Coding
author:
  - name: Sid Kumar
    affiliation: NHS South West London ICB
organisations:
  - NHS South West London ICB
image: "6019.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project aims to use Natural Language Processing (NLP) to automate the prediction of ICD-10 or OPCS-4 codes from doctor/patient notes, currently done manually. Initially focusing on 3-character ICD-10 chapters, it will eventually predict full 4-character codes. Collaborating with a provider, the project will streamline coding and improve accuracy.
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

The aim of this project is to use Natural Language Processing (NLP) to predict ICD-10 or OPCS-4 codes from doctor/patient notes, automating a task currently done manually by the clinical coding team.

Initially, we'll predict 3-character ICD-10 chapters, with the goal of eventually predicting full 4-character codes. Collaborating with a provider that has access to these notes, this project will streamline coding and improve accuracy.


<!-- ===== hsma_6/H6_6020_modelling_111_option_2_call_centre/index.qmd ===== -->

---
title: "Modelling 111 option 2 call centre"
techniques:
  - Discrete Event Simulation (DES)
  - Forecasting
  - Streamlit
  - Quarto
areas:
  - 111 Service
  - Telephone-based Services
  - Staffing Level Optimisation
categories:
  - Discrete Event Simulation (DES)
  - Forecasting
  - Streamlit
  - Quarto
  - 111 Service
  - Telephone-based Services
  - Staffing Level Optimisation
author:
  - name: Richard Hall
    affiliation: Norfolk and Suffolk NHS Foundation Trust
organisations:
  - Norfolk and Suffolk NHS Foundation Trust
image: "6020.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project aims to improve two struggling 111 call centres for mental health patients in Norfolk and Suffolk. It will develop a DES model to compare staffing approaches and determine the resources needed for safe service. Additionally, a tool will be created to ensure safe rosters by inputting current rosters and forecasting call levels.
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

We operate 2 separate 111 call centres for mental health patients (for both Norfolk and Suffolk). These are both set up in different ways (one fully staffed with ‘qualified’ B6s, the other with junior staff who escalate to qualified staff when needed), but both are struggling with their performance.

Many callers abandon their calls before they can be reached and there are serious concerns about clinical safety. A piece of work is underway to transform these services, and a piece of demand and capacity analysis is required to ensure the best possible staffing model is in place, both in terms of structure and resource levels.

The aim of this project is to build a Discrete Event Simulation model to compare both staffing approaches and identify the level of resources required to safely staff the service. Further aims would be to build a useful helper tool to ensure planned rosters are safe, users could input current rosters again a forecasted level of calls and the model would show the potential effects of this.


<!-- ===== hsma_6/H6_6021_predicting_future_demand_renal_replacement_therapy/index.qmd ===== -->

---
title: "Predicting the future demand for Renal replacement therapy"
techniques:
  - Forecasting
areas:
  - Renal
  - Dialysis
categories:
  - Forecasting
  - Renal
  - Dialysis
author:
  - name: Sandhya Radha Krishnakumar
    affiliation: NHS England
organisations:
  - NHS England
image: "6021.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Kidney disease is projected to be the fifth leading cause of premature deaths globally by 2040. Rising demand for dialysis and transplants exceeds capacity in England. The project aims to develop a model using forecasting techniques to predict future demand and address it by increasing home dialysis or introducing a new dialysis centre.
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

The problem: Kidney disease is projected to be the fifth leading cause of premature deaths globally by 2040. With people living longer and having more comorbidities, the demand for dialysis and transplants is rising and exceeding capacity. In England, the system is at full capacity for in-centre dialysis, requiring immediate action and a long-term strategy to optimise care.

The result: Incorporate forecasting techniques to predict the future demand based on population prediction (data available in ONF and prevalence data available in QOF).

The aim: To develop a model to help tackle this demand - either increasing home dialysis or introducing a new dialysis centre


<!-- ===== hsma_6/H6_6023_predicting_gestational_diabetes_using_ML/index.qmd ===== -->

---
title: "Predicting Gestational Diabetes and other maternity-related conditions using machine learning"
techniques:
  - Machine Learning
  - Streamlit
areas:
  - Diabetes
  - Maternity
  - Women's Health
categories:
  - Machine Learning
  - Streamlit
  - Diabetes
  - Maternity
  - Women's Health
author:
  - name: Rochelle Francis-Reid
    affiliation: Epsom and St Helier University Hospitals NHS Trust
organisations:
  - Epsom and St Helier University Hospitals NHS Trust
image: "6023.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project aims to use machine learning to predict gestational diabetes and other maternity-related conditions early in pregnancy, enabling timely interventions and personalised care. It will develop a predictive model, an interactive web app for clinicians to input patient data and receive predictions, and reports on the model's accuracy and effectiveness.
  links:
  - name: Video
    url: https://youtu.be/zeYG0EJ83bA?feature=shared
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
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

Maternity-related conditions, such as gestational diabetes, can have significant impacts on the health of both the mother and baby if not identified early. Current approaches often detect these conditions after symptoms appear, potentially delaying important interventions. This project aims to use machine learning to predict the likelihood of developing gestational diabetes and other related conditions early in pregnancy, allowing for timely interventions and personalised care.

The aim of this project is to develop a machine learning model that predicts the likelihood of gestational diabetes and other maternity-related conditions based on patient data. The model will serve as a decision support tool for clinicians to provide proactive and personalised care, improving health outcomes for mothers and babies.

The project will generate :

- A machine learning predictive model.
- An interactive web app or interface for clinicians to input patient data and receive predictions.
- Reports outlining the model's predictions, accuracy, and effectiveness.

{{< video https://youtu.be/zeYG0EJ83bA?feature=shared >}}


<!-- ===== hsma_6/H6_6024_Streamlit_app_for_theographs_of_patient_journeys/index.qmd ===== -->

---
title: "Developing a streamlit app for creating Theographs of patient journeys"
techniques:
  - Data Visualisation
areas:
  - Patient Pathways
categories:
  - Streamlit
  - Theographs
  - Data Visualisation
  - Patient Pathways
author:
  - name: Suprasad Gavhane
    affiliation: NHS North of England CSU (NECS)
organisations:
  - NHS North of England CSU (NECS)
image: "6024.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    The project aims to create an open-source application for generating interactive theograph visuals to understand patient/client journeys. It will be a generic tool requiring minimal data fields, usable in various healthcare or social care settings.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/sp-necs/TheoGraph
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

The aim of this project is to create an open source application to generate interactive theograph visuals to understand a patients'/clients' journey through a system.

The goal is to make a generic application requiring the minimum of data fields so it can be used in different healthcare or social care settings (working with dynamic 'Event_Type' values).

More information about theographs can be found [here](https://www.nuffieldtrust.org.uk/resource/a-10-year-story-visualising-patient-journeys).


<!-- ===== hsma_6/H6_6025_Modelling_delays_in_breast_head_neck_cancer_pathways/index.qmd ===== -->

---
title: "Modelling delays in breast, head and neck cancer pathways"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Cancer
  - Women's Health
  - Waiting Times
categories:
  - Discrete Event Simulation (DES)
  - Cancer
  - Women's Health
  - Waiting Times
author:
  - name: Michael Baser
    affiliation: NHS England
  - name: Laura Webster
    affiliation: NHS England
  - name: Lizzie Augarde
    affiliation: NHS England
organisations:
  - NHS England
image: "6025.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    The project uses DES to model post-diagnosis pathways for breast and head and neck cancer. It aims to identify delays and treatment variations across England, focusing on two key steps - time from neoadjuvant SACT to surgery or radiotherapy, and time from surgery to first adjuvant treatment.
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

Breast cancer and head and neck cancer are two common cancer sites, where the main clinical pathway is surgery, followed by adjuvant radiotherapy or chemotherapy. Clinical feedback has reported large waits after surgery and often before the point of referral to e.g. the radiotherapy department.

Our project is using Discrete Event Simulation to model the post-diagnosis pathway for breast and head and neck cancer. The model will be used to identify mid-pathway delays and treatment variation across England with the aim to report on two clinically important steps in the clinical pathway:

1. time from neoadjuvant SACT to surgery or radiotherapy (RT)
2. time from surgery to first adjuvant treatment (either RT or SACT)


<!-- ===== hsma_6/H6_6026_Modelling_secondary_care_psychological_therapy_flow/index.qmd ===== -->

---
title: "Developing a DES Model for a Mental Health Hub"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Mental Health
  - Community Mental Health
  - Waiting Times
categories:
  - Discrete Event Simulation (DES)
  - Mental Health
  - Community Mental Health
  - Waiting Times
author:
  - name: Helen Wharam
    affiliation: Hampshire and Isle of Wight Healthcare NHS Foundation Trust
  - name: Nathan Hack
    affiliation: Hampshire and Isle of Wight Healthcare NHS Foundation Trust
organisations:
  - Hampshire and Isle of Wight Healthcare NHS Foundation Trust
image: "6026.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project models the Portsmouth Mental Health Hub using Discrete Event Simulation to assess call waiting times, durations, and staff utilisation. As demand grows, the model and web-based app will inform resource planning and service improvements, helping ensure timely, effective support for individuals seeking mental health advice and guidance.
  links:
  - name: Video
    url: https://youtu.be/GlEoH8B3CHE?feature=shared
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
  - name: Slides
    url: https://docs.google.com/presentation/d/1Da6UyQcS1glQF5urB7OzzkKDOhEoLL1n/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

The Mental Health hub in Portsmouth is a relatively new service. It acts as a call centre providing signposting, advice and guidance to those who contact them.

Current service capacity to answer and manage calls was based on estimates of anticipated demand. Routes into the service are now being expanded and demand will potentially grow.

This project will use Discrete Event Simulation to model call waiting times, call duration and resource utilisation.

A web based app will be developed to support ongoing service development.

{{< video https://youtu.be/GlEoH8B3CHE?feature=shared >}}


<!-- ===== hsma_6/H6_6032_Identifying_unpaid_carers/index.qmd ===== -->

---
title: "Identifying unpaid carers in Norfolk"
techniques:
  - Geographic Modelling
  - Mapping
  - Regression
  - Geostatistics
areas:
  - Unpaid Carers
  - Council
categories:
  - Geographic Modelling
  - Mapping
  - Regression
  - Geostatistics
  - Unpaid Carers
  - Council
author:
  - name: Elli Kontostoli
    affiliation: Norfolk County Council
organisations:
  - Norfolk County Council
image: "6032.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Unpaid carers face mental health risks, loneliness, and isolation. The project will identify carer locations using geographic modelling and predict high-need areas with regression models, focusing on older populations and unpaid carers.
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

There are thousands of unpaid carers. Among many other risks, unpaid carers are likely to experience poor mental health, loneliness and isolation. Supporting the mental and physical health and well-being of carers is essential. The organisation wants to introduce them to communities services, social groups or something that they can talk to and get help with the difficulties of taking care of somebody.

The aim of this project is to identify places that carers live and to show how many we will capture by placing services.

The project will begin with geographic modelling/mapping to show locations. It may then continue on to modelling to predict high unpaid carers or areas with older population and unpaid carers.


<!-- ===== hsma_6/H6_6033_111_downstream_forecasting/index.qmd ===== -->

---
title: "111 Downstream forecasting"
techniques:
  - Machine Learning
  - Forecasting
  - Discrete Event Simulation (DES)
areas:
  - 111 Service
  - Telephone-based Services
categories:
  - Machine Learning
  - Forecasting
  - Discrete Event Simulation (DES)
  - 111 Service
  - Telephone-based Services
author:
  - name: Dominic Rowney
    affiliation: NHS North of England CSU
organisations:
  - NHS North of England CSU
image: "6033.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project aims to develop a model predicting the place, time, and volume of downstream activity from 111 calls, deployed as a secure API. It integrates with an existing UEC webapp, using weekly patient-level 111 call data and near-live feeds.
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

The aim of this project is to develop a model that, based on incoming 111 calls, predicts the likely place, time and volume of downstream activity due to these calls.  This will deployed as a secure API that allows users to pass cumulative daily 111 figures and receive downstream predictions of likely activity by location, time and type.

There is an existing UEC webapp that takes in values from various APIs and supplies the values to strategic and operational decision makers across various areas. In the North East there is 111 call data that comes in weekly that is patient level and has things like disposition / complaint / time, this is linkable to other datasets to allow to outcome such as admission post attending A&E.  There is also a near live feed which gives 5-15 minute values for the (cumulative) number of 111 calls in a day.


<!-- ===== hsma_6/H6_6034_Forcasting_blood_donation_sesion_capacity/index.qmd ===== -->

---
title: "Forecasting blood donation session capacity"
techniques:
  - Machine Learning
  - Streamlit
areas:
  - Blood & Transplant
  - Non-attendance Prediction
categories:
  - Machine Learning
  - Streamlit
  - Blood & Transplant
  - Non-attendance Prediction
author:
  - name: Sam Plimmer
    affiliation: NHS Blood and Transplant
organisations:
  - NHS Blood and Transplant
image: "6034.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Blood donation sessions face issues with cancellations, non-attendance, and medical rejections, leading to missed donations. This project aims to develop a Machine Learning tool to predict actual attendance and assess additional capacity. It will also build a web app for users to review current session capacity and manage bookings effectively.
  links:
  - name: Video
    url: https://youtu.be/zeYG0EJ83bA?feature=shared
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
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

Blood donation sessions have limits of how many people will be able to attend a session.  Bookings for sessions often don’t convert into actual donations due to cancellations, non-attendance and medical rejections.  These missed collections represent a lost opportunity to successfully bring someone in to donate.

The aim of this project is to:

1.	Develop a Machine Learning-based predictive tool to assess, of the current bookings made for a session, what proportion of these are likely to take place, and if there is room for additional capacity
2.	Build a web based app that demonstrates the above and allows users to review current available capacity at each session

{{< video https://youtu.be/zeYG0EJ83bA?feature=shared >}}


<!-- ===== hsma_6/H6_6035_web_app_to_recommend_appropriate_tech_enabled_care/index.qmd ===== -->

---
title: "Developing a web app to recommend appropriate technology enabled care"
techniques:
  - Streamlit
  - Python
areas:
  - Older Adults
  - Costs
categories:
  - Streamlit
  - Costs
  - Pythn
  - Older Adults
author:
  - name: Radia Woodbridge
    affiliation: Torbay and South Devon NHS Foundation Trust
organisations:
  - Torbay and South Devon NHS Foundation Trust
image: "6035.png"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Technology Enabled Care (TEC) supports independence and health and social care. This project aims to develop a web app providing comprehensive, user-friendly guidance on TEC equipment. It will serve as a one-stop platform for health professionals, carers, and individuals, enhancing personal safety, independence, and reducing the burden on health and social care systems.
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

The growing importance of Technology Enabled Care (TEC) in today's health and social care environment, especially with the increasing aging population and the need for cost-effective solutions to enhance quality of life, has led professionals to incorporate TEC in the individuals’ health and care assessment. TEC devices like personal alarms, sensors, fall detectors, remote health monitoring, and other assistive technologies are used to support individuals, particularly older adults, people with disabilities, or those with health conditions, in maintaining independence and ensuring safety in their daily lives.

Technology enabled care can increase choice in maintaining independence, stay connected with family and friends and enhance social and mental activity.

However, many professionals, carers and individuals are unfamiliar with the wide range of TEC options available, making it difficult to choose the right equipment.  In addition, information about TEC equipment is scattered across different platforms making it difficult to access comprehensive, up-to-date guidance in one place.

The aim of this project is to develop a web app that will :

- Serve as a one-stop platform providing details, user friendly guidance on TEC equipment.
- The app would be useful for Torbay and South devon Trust’s health and social care professionals, carers, and individuals who need support with TEC equipment, creating a bridge between technology and users who want to remain independent and safe in their homes.
- The app can provide a platform to keep users updated with the latest innovations.
- The app will empower users with comprehensive guides on TEC equipment, enabling them to make confident choices that enhance personal safety and independence
- Health and social care professionals will have access to a reliable resource to recommend the right TEC solutions for patients, enhancing their ability to deliver personalised care.
- By encouraging the use of TEC, the app contributes to reducing the burden on health and social care systems and cares, enabling more people to remain safely at home.

Future, further extension of this project will include exploring predicting cost savings and change on staff capacity based on TEC usage.


<!-- ===== hsma_6/H6_6036_Forcasting_demand_RDUH_breast_care_services/index.qmd ===== -->

---
title: "Forecasting demand in RDUH breast care services and the impact of urban development"
techniques:
  - Discrete Event Simulation (DES)
  - Forecasting
  - Streamlit
areas:
  - Cancer
  - 2-week Wait
categories:
  - Discrete Event Simulation (DES)
  - Forecasting
  - Streamlit
  - Cancer
  - 2-week Wait
author:
  - name: Gill Baker
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Brandon Jones
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Kat Pamatmat
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
image: "6036.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Between 2011 and 2021, the population served by Royal Devon & Exeter Hospital grew by 13%, doubling the national average, leading to long waiting lists. This project aims to develop a forecasting tool for breast services to predict referrals and service demand, inform workforce planning, and justify infrastructure expansion. It will also predict geographical demand changes for optimal service locations.
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

Historically there has been a lack of data science or accurate forecasting in developing capacity. Between 2011 and 2021 the growth in the population served by the Royal Devon & Exeter Hospital rose by 13% which was twice the average national population growth. This increase in demand was not met by sufficient increase in physical infrastructure or capacity. This led to significant waiting list problems with RD&E having some of the longest waiting patients in the country. Exeter and surrounding areas have high housing targets and predict further growth as well as significant growth in an ageing population.

This project aims

- To develop a demonstrator forecasting tool (using breast services as an example) which is made available through a StreamLit app to predict referrals and service demand.
- To use this tool to demonstrate the impact of specific housing developments on service demand to inform workforce planning and to provide data to justify s106 payments from developers to support NHS infrastructure expansion.
- To predict changes in geographical demand and thus feed into project in understanding optimum locations for services on the 10-20 year timescale.

The project objectives are

- To look at the growth in referrals for breast services and predict future clinic capacity required to meet 2WW targets.
- To separate the increase in referrals due to population growth from that due to changes in demographics and referral patterns (due to patient education and increasing incidence of cancer).
- To create a model of growth based on assumptions about population growth and changes in demographics to obtain best and worst case scenarios in terms of demand.


<!-- ===== hsma_6/H6_6037_mapping_health_inequalities/index.qmd ===== -->

---
title: "Mapping health inequalities, depreviation, ethnicities and crime across the UK"
techniques:
  - Geographic Modelling
  - Mapping
areas:
  - Inequalities
  - Crime
  - Police
  - Demographics
categories:
  - Mapping
  - Inequalities
  - Geographic Modelling
  - Demographics
  - Crime
  - Police
author:
  - name: Abhinav Jindal
    affiliation: NIHR Clinical Research Network
organisations: 
  - NIHR Clinical Research Network
image: "6037.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
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

The aim of the project is to use ONS data around ethnicities of population, health index England, Deprivation data from QOF, and overlay the same with crime statistics at a geographical scale to try and prove a relationship and the hypothesis of a link.


<!-- ===== hsma_6/H6_6039_NLP_to_automate_classification_congenital_anomaly/index.qmd ===== -->

---
title: "Applying Natural Language Processing to automate the extraction and classificiation of congenital anomaly diagnoses from free text and genetic data"
techniques:
  - Natural Language Processing (NLP)
  - Streamlit
areas:
  - Congenital Anomilies
  - Genetic Data
categories:
  - Natural Language Processing (NLP)
  - Streamlit
  - Congenital Anomilies
  - Genetic Data
author:
  - name: Charlotte Eversfield
    affiliation: National Disease Registration Service (NDRS)
  - name: Jack Anderson
    affiliation: National Disease Registration Service (NDRS)
  - name: Claire Welsh
    affiliation: National Disease Registration Service (NDRS)
  - name: Clarice Quinn
    affiliation: National Disease Registration Service (NDRS)
organisations:
  - National Disease Registration Service (NDRS)
image: "6039.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project aims to use Natural Language Processing to automate and standardise extraction and classification of Congenital anomaly diagnoses under ICD10 code Q87.8 which are manually classified from free text, risking errors and inefficiency. To validate diagnoses with genetic data by defining a data linkage method.
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

Congenital anomaly diagnoses can be submitted to the National Congenital Anomaly and Rare Diseases Services (NCARDRS) under an unspecific and uninformative ICD10 code of Q87.8. Q87.8 is broadly defined as ‘Other specified congenital malformation syndromes, not elsewhere classified’, with diagnosis detail submitted in free text data. As a result, classification of these diagnoses into more specific syndromes is currently handled manually by reviewing free text fields from data submissions from hospitals such as discharge letters. This manual review is time consuming and risks human error, duplication of effort, and poor standardisation of rules/methods applied for extraction and classification.

Additionally, diagnoses submitted from discharge letters are only ‘probable’ or ‘suspected’ and therefore need to be validated via genetic testing data. However, there currently is no defined method of data linkage between the discharge letters and genetic data which means diagnoses cannot be confirmed. Providing accurate data on congenital anomaly diagnoses which have been validated by genetic testing data is crucial for disease surveillance reporting.

The aims of this project are:

1.	To use Natural Language Processing (NLP) to automate and standardise the extraction and classification of suspected ICD10 Q87.8 congenital anomaly diagnoses from free text.
2.	To use genetic data to validate these suspected diagnoses, which will include defining a data linkage method between the two datasets.


<!-- ===== hsma_6/H6_6040_benefit_of_MECC_using_ABS/index.qmd ===== -->

---
title: "Modelling the benefit of MECC (Making Every Contact Count) Training using agent based simulation"
techniques:
  - Agent Based Simulation (MECC)
  - Streamlit
areas:
  - Making Every Contact Count (MECC)
  - Population Health
categories:
  - Agent Based Simulation (MECC)
  - Streamlit
  - Making Every Contact Count (MECC)
  - Public Health
  - Smoking
author:
  - name: Dominic Rowney
    affiliation: NHS North of England CSU
  - name: Luke Herbert
    affiliation: Surrey and Sussex Healthcare NHS Trust
  - name: Sam Vautier
    affiliation: Somerset NHS Foundation Trust
organisations:
  - NHS North of England CSU
  - Surrey and Sussex Healthcare NHS Trust
  - Somerset NHS Foundation Trust
image: "6040.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    Making Every Contact Count (MECC) is an e-learning program for health and social care staff to promote healthy lifestyles. This project uses Agent Based Simulation to model MECC's impact on behaviors like smoking, drinking, and exercise.
  links:
  - name: Video
    url: https://youtu.be/U6-_3q_CZtA?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/DomRowney/Project_Toy_MECC
    icon: fa-brands fa-github
  - name: Website
    url: https://domrowney-project-toy-mecc-streamlit-appapp-alcohol-cqzaxu.streamlit.app/
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://drive.google.com/file/d/1X_JizOXHMrseAvxSSZWE3YGXuuSo5okM/view?usp=drive_link
    icon: fa-solid fa-person-chalkboard
---

Making Every Contact Count (MECC) is an e-learning programme in which health and social care staff are encouraged to use various interactions with patients to open conversations about healthy lifestyles and wellbeing.

The aim of this project is to use Agent Based Simulation to model the behavioural dynamics and success rates on lifestyle factors (such as smoking, drinking, exercise) of MECC interventions, and thereby try to understand the potential impact of MECC training.

{{< video https://youtu.be/U6-_3q_CZtA?feature=shared >}}


<!-- ===== hsma_6/H6_6041_patients_risk_integrated_neighbourhood_teams/index.qmd ===== -->

---
title: "Identifying which patients are most at risk for an outcome across integrated neighbourhood teams"
techniques:
  - Machine Learning
  - Explainable AI
  - Streamlit
  - Geographic Modelling
areas:
  - Demographics
  - Public Health
categories:
  - Machine Learning
  - Explainable AI
  - Streamlit
  - Geographic Modelling
  - Demographics
  - Public Health
author:
  - name: Rachel Christie
    affiliation: North West London ICB
organisations:
  - North West London ICB
image: "6041.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Population health management uses segmentation to categorise people by health status and needs. However, generic segments may not identify high-risk groups effectively. This project aims to create a tool to identify at-risk patient groups across different geographies, focusing on outcomes like emergency admissions, vaccination rates, and screening uptake.
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

Population health management often use population segmentation to categorise the population according to health status, health care needs and priorities. This approach recognises that groups of people share characteristics that influence the way they interact with health and care services.

However, generic population segments may not break down the population into specific enough areas in order to identify which populations are most at risk of an outcome and, therefore, who to target for intervention and where the biggest gains in intervention could be made. Identifying which patient characteristics carry the biggest risk most often comes from clinical expertise and is not data-driven.  When data is considered, there is often “too much” data to look into, requiring expertise on where to start. Additionally, different geographies want to know who is most at risk in their patch and often want to be able to view the data at their geography or for their primary care network.

There is a need for a way to identify which patient characteristics carry the biggest risk for an outcome across different geographies.

The aim of this project is to create a tool to identify which patient groups are most at risk for an outcome at different geographies. The outcomes will align in the NWL INT outcomes which include:

- Emergency admissions due to fall in over 65s
- Not being vaccinated
- Not taking up screening
- Emergency admissions for ambulatory care sensitive conditions

Machine Learning and Explainable AI approaches will be used to build the tool and outputs.


<!-- ===== hsma_6/H6_6043_smoking_cessation_success/index.qmd ===== -->

---
title: "Predictive modelling for smoking cessation success"
techniques:
  - Machine Learning
  - Explainable AI
  - Causal Analysis
areas:
  - Smoking
  - Public Health
  - Council
categories:
  - Machine Learning
  - Explainable AI
  - Causal Analysis
  - Smoking
  - Public Health
  - Council
author:
  - name: Ryan Hutchings
    affiliation: Dorset Council
  - name: Khetha Mngomezulu
    affiliation: Dorset Council
organisations:
  - Dorset Council
image: "6043.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Smoking cessation remains challenging despite public health efforts. This project aims to develop a predictive model to identify individuals likely to quit smoking based on demographics and behaviours. It will uncover key predictors and effective pathways using machine learning algorithms like logistic regression, decision trees, random forests, and neural networks, evaluating each for accuracy and interpretability.
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

Smoking is a leading cause of preventable diseases and deaths worldwide. Despite numerous public health campaigns and interventions, smoking cessation remains a significant challenge. Understanding the factors that contribute to successful smoking cessation can help in designing more effective interventions.

Certain pathways may suit individuals needs differently and thus have different likelihoods of success. This model will help to show which demographics and pathways are most effective at achieving a successful quit.

The primary goal of this project is to develop a predictive model that identifies individuals likely to stop smoking based on their demographics and/or behaviours. Additionally, the project aims to uncover key predictors that can possibly influence smoking cessation, providing insights into the traits and behaviours that contribute to quitting smoking and which pathways offer better results for people.

Several machine learning algorithms will be considered, including logistic regression, decision trees, random forests, and neural networks. Each algorithm will be evaluated for its predictive accuracy and interpretability.

Depending on the complexity of the data to be used, we will also consider employing ensembled methods to leverage the power of different models on one dataset.


<!-- ===== hsma_6/H6_6044_Population_segmentation_GP_registered_Dorset/index.qmd ===== -->

---
title: "Population segmentation of GP-registered population in Dorset"
techniques:
  - Machine Learning
  - Unsupervised Learning
areas:
  - Primary Care (GPs)
categories:
  - Machine Learning
  - Unsupervised Learning
  - Primary Care (GPs)
author:
  - name: Rhianna Everett
    affiliation: Dorset Intelligence and Insight Service
  - name: James Roberts
    affiliation: Dorset Council
organisations:
  - Dorset Council
  - Dorset Intelligence and Insight Service
image: "6044.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project aims to develop a machine learning-based population segmentation model for the GP-registered Dorset population, using multiple characteristics including healthcare utilisation. The goal is to identify segments based on care needs to inform service design, enhancing patient understanding and improving resource allocation.
  links:
  - name: Video
    url: https://youtu.be/SH4geMXr8a8?feature=shared
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
  - name: Slides
    url: https://docs.google.com/presentation/d/1rRlb6pDf89Tph7sNj5r8xN5NdeD84P7d/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

The aim of this project is to create a machine learning-based population segmentation model for the GP-registered Dorset population using multiple characteristics including primary and secondary healthcare utilisation.

We want to identify population segments based on care needs to inform service design.

This has the potential to provide enhanced patient understanding leading to improved resource allocation.

{{< video https://youtu.be/SH4geMXr8a8?feature=shared >}}


<!-- ===== hsma_6/H6_6045_Forecasting_NHS_Planning_Performance_metrics/index.qmd ===== -->

---
title: "Forecasting NHS planning and performance metrics"
techniques:
  - Forecasting
areas:
  - NHS
categories:
  - Forecasting
  - NHS
author:
  - name: Sam Wheeler
    affiliation: NHS Bath and North East Somerset, Swindon and Wiltshire ICB
  - name: Sally Cherrington
    affiliation: NHS Bath and North East Somerset, Swindon and Wiltshire ICB
organisations:
  - NHS Bath and North East Somerset, Swindon and Wiltshire ICB
image: "6045.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project aims to create a robust forecasting approach for NHS Planning metrics, improving system planning and operational management, and ensuring consistent adoption across the system to aid decision-making.
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

The ICB leads on development of Operational Planning submissions to NHS England on an annual basis. This involves development trajectories against various activity and performance metrics, usually covering the next 12 months (e.g. ICB-level A&E attendances).  Analysts are often asked to forecast these measures forward based on historic information. The system’s approach to this is often very basic and crude and, partly because of this, organisations often use their own, different approaches which are often open to manipulation.

The aim of this project is to develop an approach to forecasting the main NHS Planning performance and activity metrics, which is more robust than existing, crude techniques and can form the basis of System Planning. To develop an approach that, given it’s more robust, will be consistently adopting across our system to aid decision makers with both planning but also operational management at system level.


<!-- ===== hsma_6/H6_6046_Proactive_Patient_attendance_prediction/index.qmd ===== -->

---
title: "Proactive Patient Attendance Prediction: Enhancing Healthcare Efficiency through Attendance Forecasting"
techniques:
  - Machine Learning
areas:
  - Non-attendance Prediction
  - Outpatients
categories:
  - Machine Learning
  - Non-attendance Prediction
  - Outpatients
author:
  - name: Peter Andrews
    affiliation: Barts Health NHS Trust
organisations:
  - Barts Health NHS Trust
image: "6046.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    At Barts Health NHS Trust, 12% of outpatient appointments are missed monthly, wasting over 10,000 hours of clinical resources. Missed appointments can lead to extended waiting lists and patient deterioration. This project aims to develop a machine learning model to forecast non-attendance, a patient contact capture tool, and integrate the model into enterprise reports.
  links:
  - name: Video
    url: https://youtu.be/WNtIIWA_IYg?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/WX-BIU/Outpatient-DNAs
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://drive.google.com/file/d/16aa7B_4a4i3IxZv7Cf_7GGSnVoab23i_/view?usp=drive_link
    icon: fa-solid fa-person-chalkboard
---

Every month ~ 12% of outpatient appointments are not attended at Barts Health NHS Trust. This equates to over 10 thousand hours of clinical input, space and equipment that is not being used optimally to progress patients’ treatments or manage ongoing care.

If a patient does not attend, they could be placed back on a waiting list for an extended period which increases the risk of further deterioration or more severe progression of their condition that may result in them needing emergency care. The deterioration of the patient could have long term impacts on their future health.

This project will develop :

- Machine learning model to forecast non-attendance
- Patient contact capture tool
- Integration of machine learning model into enterprise level reports

{{< video https://youtu.be/WNtIIWA_IYg?feature=shared >}}


<!-- ===== hsma_6/H6_6047_RALPulator/index.qmd ===== -->

---
title: "RALPulator : Predicting Robotic-assisted laparoscopic prostatectomy (RALP) operative times from patient letters"
techniques:
  - Machine Learning
  - Natural Language Processing (NLP)
  - Streamlit
areas:
  - Urology
  - Cancer
  - Surgical
categories:
  - Machine Learning
  - Natural Language Processing (NLP)
  - Streamlit
  - Urology
  - Cancer
  - Surgical
author:
  - name: Jake Wilson
    affiliation: Great Western Hospitals NHS Foundation Trust
organisations:
  - Great Western Hospitals NHS Foundation Trust
image: "6047.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project is an app that reads in patient letters ahead of surgery, using Natural Language Processing techniques to extract key information from the text, and then feeds all of that into a Machine Learning model which then predicts how long the Robotic-assisted laparoscopic prostatectomy (RALP) surgery is going to take.
  links:
  - name: Video
    url: https://youtu.be/ZLfEgmVCYJM?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
  - name: Website
    url: https://ralpulator.streamlit.app/
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://docs.google.com/presentation/d/1rXcy9DwziUc21ukOOaWdOcQ9ZV79OGMx/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

This project is building an app that reads in patient letters ahead of surgery, uses Natural Language Processing techniques to extract key information from the text, and then feeds all of that into a Machine Learning model which then predicts how long the Robotic-assisted laparoscopic prostatectomy (RALP) surgery is going to take.

A first version of the app has been developed and deployed, and is available here: <https://ralpulator.streamlit.app/>

Jake is presenting the work to the National Urological Conference in November 2024, and has been invited to present in Perth, Australia in March 2025.

{{< video https://youtu.be/ZLfEgmVCYJM?feature=shared >}}


<!-- ===== hsma_6/H6_6048_Concurrent_treatment_areas_RTT_pathway/index.qmd ===== -->

---
title: "Identifying potential concurrent treatment areas and services that would better support patients with multiple, complex referral to treatment (RTT) pathways."
techniques:
  - Machine Learning
  - Streamlit
areas:
  - Inequalities
  - Patient Pathways
categories:
  - Machine Learning
  - Streamlit
  - Inequalities
  - Patient Pathways
author:
  - name: Amaia Imaz Blanco
    affiliation: NHS England
  - name: Sean Aller
    affiliation: NHS England
organisations:
  - NHS England
image: "6048.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
  links:
  - name: Video
    url: https://youtu.be/SH4geMXr8a8?feature=shared
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
  - name: Slides
    url: https://docs.google.com/presentation/d/1YXuROx59dIm9JUYWMuMbhh8A14UGov8X/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

The aim of this project is to use machine learning approaches to support analysis of patients with multiple concurrent RTT pathways, focusing particularly on healthcare inequalities.

The intention is to build a model that could identify/predict/suggest colocated services as well as points at which patients start having concurrent pathways.

{{< video https://youtu.be/SH4geMXr8a8?feature=shared >}}


<!-- ===== hsma_6/H6_6052_GM_specialist_palliative_end_of_life_care/index.qmd ===== -->

---
title: "Geographical mapping in specialist palliative and end of life care"
techniques:
  - Mapping
  - Geographic Modelling
areas:
  - End-of-life Care & Hospices
  - Demographics
categories:
  - Geographic Modelling
  - Mapping
  - Demographics
author:
  - name: Helen Cameron
    affiliation: Ashgate Hospice
organisations:
  - Ashgate Hospice
image: "6052.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    This project aims to use geographic mapping with national health and census data to assess if we are caring for a fair represent the population. It will map some characteristics to include cancer/non-cancer status and protected characteristics like gender, sexual orientation, religion, and ethnicity. This understanding can support funding for specific areas and target referrals from underrepresented groups.
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

Using national health and census data, the aim of this project is to use geographic mapping to show if we are caring for a fair representation of our population. The two populations to be mapped would be based on the same characteristics to include cancer/non-cancer status, protected characteristics such as gender, sexual orientation, religion, ethnicity.

This would help us to understand our population and could be used to support funding for specific geographical areas or targeting referrals from underrepresented groups.


<!-- ===== hsma_6/H6_6055_DES_modelling_Hyperacute_Acute_Stroke_Pathway/index.qmd ===== -->

---
title: "DES Modelling of The Hyperacute / Acute Stroke Pathway - Patient and Economic Outcomes"
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Stroke
categories:
  - Discrete Event Simulation(DES)
  - Streamlit
  - Stroke
author:
  - name: John Williams
    affiliation: Maidstone and Tunbridge Wells NHS Trust
organisations:
  - Maidstone and Tunbridge Wells NHS Trust
image: "6055.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    Stroke prevalence in the UK is forecasted to increase by 40-60% from 2021 to 2030, straining hospitals and society. This project aims to develop a discrete simulation model to optimise the Hyperacute/Acute stroke pathway, improving patient outcomes, reducing costs, and enhancing economic benefits. It will analyse variables like staffing and operating hours
  links:
  - name: Video
    url: https://youtu.be/ThltRNDt9k8?feature=shared
    icon: fa-brands fa-youtube
  - name: Article
    url: https://arc-swp.nihr.ac.uk/news/transforming-stroke-care-through-simulation-how-one-hsma-graduates-model-could-save-over-2-million-annually/
    icon: fa-solid fa-newspaper
  - name: Code
    url: https://github.com/jfwilliams4/des_stroke_project
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://docs.google.com/presentation/d/18iYB7-1nJOU_3Nr0gHVSPVSsEy-VDgdz/edit?usp=drive_link&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

In the UK the prevalence of stroke among the population is set to increase, with some forecasts putting this between 40-60% from 2021 to 2030. This increase will not only put pressure on hospitals but also on all of society.

The Hyperacute stroke setting is an extremely time critical. The quicker treatment can be delivered the better a patient's outcome. In the Acute setting, therapy takes centre stage in rehabilitating patients, with the initial few weeks being the most impactful for the patient’s recovery.

Post stroke, patients can suffer with extreme changes to their function and wellbeing. The more severe the post stroke disability the more intensive and expensive care is needed.

The aim of this project is to develop a discrete simulation model to observe the potential effects of differing variables (such as staffing / operating hours of pathways and services) within the Hyperacute / Acute stroke pathway have on the following :

- Patient flow and medical outcomes of those patients
- Direct costs and savings made to the stroke unit itself
- The health economic costs / benefits associated with any change

{{< video https://youtu.be/ThltRNDt9k8?feature=shared >}}


<!-- ===== hsma_6/H6_6056_Redrawing_NW_Ambulance_dispatch_boundaries/index.qmd ===== -->

---
title: "Redrawing North West Ambulance dispatch Boundaries"
techniques:
  - Geographic Modelling
areas:
  - Ambulance
categories:
  - Geographic Modelling
  - Ambulance
author:
  - name: Charlotte Anderson
    affiliation: North West Ambulance Service NHS Trust
  - name: Dorota Scott
    affiliation: North West Ambulance Service NHS Trust
  - name: Kristian Boote
    affiliation: North West Ambulance Service NHS Trust
organisations:
  - North West Ambulance Service NHS Trust
image: "6056.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    North West Ambulance Service (NWAS) has three dispatch suites in Manchester, Preston, and Liverpool, with dispatch areas mainly based on postcodes. Changes in the landscape and increased emergency demand have led to unequal resource distribution, causing delays. This project aims to generate evidence to redraw boundaries to ensure equitable resource allocation across the three areas.
  links:
  - name: Video
    url: https://youtu.be/BONCgiiFfHc?feature=shared
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
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

Within North West Ambulance Service (NWAS), there are three dispatch suites which are based in Manchester, Preston and Liverpool. Each of the sites has a number of dispatch areas which are split geographically, based mainly on postcodes, for the purposes of dispatching emergency resources.

The geographical areas have not been reviewed for many years and in that time, there have been changes to the landscape of the areas. There have also been hospital and ambulance station closures and relocations. Over the years, there have been increases in the number of emergency ambulances to meet the demand.

Today’s issue is that the dispatch areas do not have parity in terms of how many emergency resources each are controlling and in how many allocations are made by each dispatcher. This has resulted in some dispatch areas being overwhelmed with incidents to allocate which ultimately leads to delays in responding to patients.

The aim of this project is to generate evidence to redraw these boundaries to make it more equitable across the three areas.

{{< video https://youtu.be/BONCgiiFfHc?feature=shared >}}


<!-- ===== hsma_6/H6_6058_ml_tool_to_predict_dnas/index.qmd ===== -->

---
title: "Building a Machine Learning tool to predict Did Not Attend (DNA) events"
techniques:
  - Machine Learning
  - Streamlit
areas:
  -
categories:
  - Machine Learning
  - Streamlit
author:
  - name: Barney Rumbold
    affiliation: Blackpool Teaching Hospitals NHS Foundation Trust
organisations:
  - Blackpool Teaching Hospitals NHS Foundation Trust
image: "6058.png"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract:
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/BarnabyRumbold/logistic_regression_streamlit_app
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
---

This project is developing a machine learning-based tool that looks at the likelihood outpatient Did Not Attend (DNA) incidences across different services/demographics.

The tool could hopefully be shared with providers to provide guidance on how to reduce DNAs.


<!-- ===== hsma_6/H6_6060_optimising_resourcing/index.qmd ===== -->

---
title: "Optimising Same Day Emergency Care (SDEC) Resourcing"
techniques:
  - Discrete Event Simulation (DES)
  - Emergency Departments
areas:
  -
categories:
  - Discrete Event Simulation (DES)
  - Emergency Departments
author:
  - name: Hannah Thould
    affiliation: University Hospitals Bristol and Weston NHS Foundation Trust
organisations:
  - University Hospitals Bristol and Weston NHS Foundation Trust
image: "6060.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract:
  links:
  - name: Video
    url: https://youtu.be/Yck3vOioRdQ?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/hthould/acute_take_des
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url: https://docs.google.com/presentation/d/1fGS1mKo8BrF_I4wy5AAzjDsdETnUaFnE/edit?usp=sharing&ouid=104927246423235110137&rtpof=true&sd=true
    icon: fa-solid fa-person-chalkboard
---

This project will model Same Day Emergency Care (SDEC) and Emergency Department (ED) pathways at University Hospitals Bristol and Weston NHS Foundation Trust.

The project aims to use Discrete Event Simulation to ascertain

1. optimum parameters for SDEC and ED pathways
2. the effect of different doctor numbers
3. the optimum size for SDEC

{{< video https://youtu.be/Yck3vOioRdQ?feature=shared >}}


<!-- ===== hsma_6/H6_6061_analysis_forecasting_hospital_referrals/index.qmd ===== -->

---
title: "Analysis and forecasting of referrals into hospital"
techniques:
  - Forecasting
areas:
  -
categories:
  - Forecasting
author:
  - name: Andrew Sharrock
    affiliation: The Walton Centre NHS Foundation Trust
organisations:
  - The Walton Centre NHS Foundation Trust
image: "6061.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
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

This project will use Python and forecasting approaches to analyse growth in referrals into the hospital.


<!-- ===== hsma_6/H6_6062_primary_care_load_management_tool/index.qmd ===== -->

---
title: "Developing a primary care load management tool"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Primary Care (GP)
categories:
  - Discrete Event Simulation (DES)
  - Primary Care (GP)
author:
  - name: Chris Lewis
    affiliation: The Park Medical Practice
organisations:
  - The Park Medical Practice
image: "6062.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    A GP practice had peak call wait times of 60 minutes. Adding more staff improved this, but lower utilisation was then seen during quieter periods. This project will model the telephone system and call handlers' workload to optimise resourcing, producing a web app to test different scenarios.
  links:
  - name: Video
    url: https://youtu.be/AUNmuPFnq4c?feature=shared
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/clexp/Primary_Care_Load_Management_Tool
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url:
    icon: fa-solid fa-file-contract
  - name: Slides
    url:
    icon: fa-solid fa-person-chalkboard
---

A GP practice serving 35,000 patients experiences peak call wait times of 60 minutes. While increasing staffing levels has reduced these wait times, this approach can result in periods of lower utilization during quieter times.

This project aims to develop a comprehensive model of the telephone system and call handler workload patterns. The goal is to create an analytical tool that can evaluate telephone resource allocation and identify opportunities for operational optimization.

A web-based application will be developed to enable testing of various staffing scenarios and resource allocation strategies.

{{< video https://youtu.be/AUNmuPFnq4c?feature=shared >}}


<!-- ===== hsma_6/H6_6063_modelling_talking_therapies_clinical_pathway_using_des/index.qmd ===== -->

---
title: "Modelling the Talking Therapies clinical pathway using a Discrete Event Simulation"
techniques:
  - Discrete Event Simulation (DES)
areas:
  - NHS Talking Therapies (Formerly IAPT)
categories:
  - Discrete Event Simulation (DES)
  - NHS Talking Therapies (Formerly IAPT)
author:
  - name: Heath McDonald
    affiliation: Lancashire & South Cumbria NHS Foundation Trust
organisations:
  - Lancashire & South Cumbria NHS Foundation Trust
image: "6063.PNG"
title-block-banner: ../../banner.png
status: Active
repo: Y
pub-info:
  abstract: |
    The NHS Talking Therapies programme, supports NICE guidelines for treating anxiety and depression. The aim is to develop a Discrete Event Simulation to model patient flow through the new clinical pathway. This project will identify potential waiting list build-ups due to increased referrals into Talking Therapies.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/MightyAtom220474/IAPT-Pathway-DES
    icon: fa-brands fa-github
  - name: Website
    url:
    icon: fa-solid fa-globe
  - name: Paper
    url: https://drive.google.com/file/d/15AsF2U4BnsXbbGQRxIcFkDW130j4JiaF/view?usp=drive_link
    icon: fa-solid fa-file-contract
---

According to the Office of National Statistics (ONS), almost one fifth of adults in the UK experience anxiety or depression. The Depression Report (Layard, 2005) identified psychological therapies as vital in the treatment of anxiety and depression. In October 2007, the UK government announced a large-scale programme to improve psychological health in the population: Improving Access to Psychological Therapies (IAPT).
Following 15 years of delivery, the programme underwent a national rebrand and was re-named in early 2023 as “NHS Talking Therapies for anxiety and depression”. The NHS Talking Therapies programme supports the NHS in implementing National Institute for Health and Clinical Excellence (NICE) guidelines for the treatment of those experiencing common mental health problems such as depression and a range of anxiety disorders, providing Talking Therapies services within the framework of a stepped care approach.

Lancashire & South Cumbria NHS Foundation Trust recently reviewed its pathway in line with National Recommendations for how Talking Therapies services should be delivered.

The aim of this project is therefore to develop a Discrete Event Simulation to model the flow of patients through this new Talking Therapies clinical pathway incorporating the entire clinical pathway – Screening & Assessment, Step 2 and Step3, and modelling patient flow both within and between all the elements of the pathway in an effort to identify any areas of potential waiting list build up resulting from the increased numbers of referrals into Taking Therapies that are being received.


<!-- ===== hsma_6/H6_6065_automating_injury_coding_using_language_models/index.qmd ===== -->

---
title: "Automating injury coding using language models"
techniques:
  - Natural Language Processing (NLP)
  - Machine Learning
areas:
  - Clinical Coding
categories:
  - Natural Language Processing (NLP)
  - Machine Learning
  - Clinical Coding
author:
  - name: James Lai
    affiliation: Imperial College Healthcare NHS Trust
organisations:
  - Imperial College Healthcare NHS Trust
image: "6065.png"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Traumatic injuries are common in emergency care and a leading cause of death and disability in working-age individuals. Patients undergo clinical assessments, blood tests, and CT imaging upon arrival. Major trauma centres (MTCs) are funded based on injury severity, requiring accurate coding. The HSMA project aims to train a language model to generate injury codes from free-text radiology reports.
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

Traumatic injuries are a very common presentation to emergency care and the leading cause of death and disability in the working-age population. Patients can sustain multiple injuries to varying locations and of varying severity.

On arrival at the emergency department. The injured patient will have a clinical assessment and blood tests to evaluate the degree of injuries. Once stabilised after arrival in the emergency department, the acutely injured patient will require CT imaging to guide clinical management. Clinical imaging is where most of the injuries are detected.

Major trauma centres (MTCs) are funded to deliver activity. The injury casemix and severity for each MTC is reported centrally, and centres are funded for the delivery of major trauma activity, with an increased tariff for patients with a higher injury severity score (ISS), reflecting the severity of injury. Therefore, accurate coding is required to reflect the injury case mix a centre receives and attract the appropriate tariff for the delivery of major trauma activity.

The aim of the HSMA project is to train a language model to take free-text radiology report inputs and generate an injury code based on the free-text information provided.


<!-- ===== hsma_6/H6_6066_evaluating_impact_of_community_diagnostic_centres/index.qmd ===== -->

---
title: "Evaluating the Impact of Community Diagnostic Centres on Health Inequalities and Patient Access to Diagnostic Services"
techniques:
  - Geographic Modelling
  - Streamlit
  - Python
areas:
  - Community Diagnostic Centres (CDCs)
categories:
  - Geographic Modelling
  - Streamlit
  - Python
  - Community Diagnostic Centres (CDCs)
author:
  - name: Felix Mukoro
    affiliation: NHS England
organisations:
  - NHS England
image: "6066.png"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract: |
    Community Diagnostic Centres (CDCs) aim to expand diagnostic capacity and improve access, but their equitable distribution is unclear. This project will assess CDCs' impact on patient access and health inequalities by analysing socio-demographic, geographic, and utilisation data.
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

The introduction of Community Diagnostic Centres (CDCs) aims to expand capacity and bring diagnostics closer to communities, ideally reducing waiting times and improving access. However, whether these benefits are being equitably distributed remains unclear.

Evidence is needed to quantify the true effect of these centres, including their impact on groups that might experience challenges in accessing timely diagnostic services (e.g., those in deprived areas, rural communities, or with limited transport).

This project seeks to investigate whether CDCs have effectively improved patient access, and reduced health inequalities. By combining socio-demographic, geographic, and utilisation data, this project aims to identify areas and populations still underserved by diagnostics and propose strategies for equitable service provision.

This project and output will feed into the overall CDC Programme Evaluation/Review which was recently commissioned by the CDC Programme national team and the Department of Health and Social Care (DHSC).

The aims of this project are to :
- Quantify how the phased opening of CDCs has changed overall diagnostic capacity and waiting times.
- Assess how the roll-out of CDCs has influenced access to diagnostic services across diverse socio-demographic groups and geographical areas.
- Determine whether health inequalities in diagnostic utilisation or waiting times have lessened post-CDC introduction.


<!-- ===== hsma_6/H6_6067_applying_manipulating_id_rules_specialised_services/index.qmd ===== -->

---
title: "Applying and manipulating identification rules for specialised services"
techniques:
  - Streamlit
  - Python
areas:
  -
categories:
  - Streamlit
author:
  - name: Emma Keeley
    affiliation: Arden and GEM CSU
organisations:
  - Arden and GEM CSU
image: "6067.png"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
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

Specialised service lines are identified using Prescribed Specialised Services (PSS) Tool and returned as a field within the SUS dataset. Each year there are changes to the rules and a new tool is provided. The PSS tool is a black box, so there is no access to the manipulate the rules within the tool. The IR rules are hierarchical, a patient can meet the criteria for multiple service lines but is assigned the service line that is highest in the hierarchy. Due to the hierarchy, a change in one rule can cause movement between specialised / non-specialised but also changes within final service line. SUS inpatient and outpatient tables combined contain in excess of 2 billion rows, understanding changes across service lines requires processing all of the data and is therefore slow analysis in SQL. 

The aim of this project is to build a tool that will allow application and manipulation of the IR rules to the SUS datasets. The output will show movement between specialised / non-specialised, movement between service lines and changes in delegated/non-delegated services. As SUS is a patient level dataset there is opportunity to look at changes in patient demographics caused by amendments to the IR rules. As many of the services lines have associated provider eligibility lists, the output should also show changes in travel time for patients. There is potential to be able to analyse the elements of the rule criteria that have been met to assign the service code, this will help determine if there are redundant elements of the rules.


<!-- ===== hsma_6/H6_6069_wordclouds_referral_information/index.qmd ===== -->

---
title: "Generating wordclouds from referral information"
techniques:
  - Natural Language Processing (NLP)
areas:
  -
categories:
  - Natural Language Processing (NLP)
author:
  - name: Rebecca Marshall
    affiliation: University Hospitals Coventry and Warwickshire Trust
organisations:
  - University Hospitals Coventry and Warwickshire Trust
image: "6069.png"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
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

The aim of this project is to use Natural Language Processing techniques to extract commonly used information in the referral reason of referral order forms. 

Often large paragraphs of free text are written here, but the service would find it useful to understand what are some of the most common reasons for referral.


<!-- ===== hsma_6/H6_6070_machine_learning_hospital_readmissions/index.qmd ===== -->

---
title: "Using Machine Learning techniques to predict Hospital Readmissions"
techniques:
  - Machine Learning
  - Explainable AI
areas:
  -
categories:
  - Machine Learning
  - Explainable AI
author:
  - name: Rebecca Marshall
    affiliation: University Hospitals Coventry and Warwickshire Trust
organisations: 
  - University Hospitals Coventry and Warwickshire Trust
image: "6070.PNG"
title-block-banner: ../../banner.png
status: Active
pub-info:
  abstract:
   The Trust averages 480 emergency 30-day readmissions monthly. This exploratory project aims to use Machine Learning to predict readmissions and identify key factors. It will assess the accuracy of different approaches using current Trust data, potentially guiding future work in this area.
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

Each month, the Trust has, on average, 480 Emergency 30-day readmissions (7.7%). My aim is to use Machine Learning techniques to try predict who will get readmitted and identify any key factors which make it more likely for someone to be readmitted.

At this stage, it is an exploratory project that will look more at what level of accuracy is possible to achieve with different approaches from the data currently held by the trust, and may inform future direction of work in this area.

