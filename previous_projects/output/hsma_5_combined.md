<!-- ===== hsma_5/h5_5002_nlp_drug_content/index.qmd ===== -->

---
title: "Using Natural Language Processing to detect drug related content within free text "
categories:
  - Natural Language Processing (NLP)
  - Named Entity Recognition
  - Police
techniques:
  - Natural Language Processing (NLP)
  - Named Entity Recognition
areas:
  - Police
author:
  - name: Lauren Szarvas
  - name: Holly Dale
  - name: Tom Haddock
image: "5r2xrx9d.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to detect drug-related content in datasets using Natural Language Processing to automate text classification. Initial findings were promising, though tested only on dummy data. If successful, the model could be adapted for other crime types.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=7j8_DlMoaSc&t=22s
    icon: fa-brands fa-youtube
---

---
# Organisations of project contributors have been left out intentionally
# Please do not re-add!
---

Since the amount of data being collected and stored has increased significantly, datasets are often reviewed manually, particularly when free text fields are present. This project focussed specifically on the detection of drug-related content, following the announcement of the Governments 10-year drugs plan in December 2021. If successful, this could then be adapted and applied to further crime types at a later date.

The aim was to create a model that would be able to make predictions on future datasets by classifying each piece of text into drug/non-drug related content, to prevent manual coding of the data. To achieve this, the team used a machine learning technique known as Natural Language Processing, to train various models on the structure of text and any patterns in language.

The team created a model pipeline to automate this process end-to-end. Initial findings suggesting these techniques could be rather successful, however, it has only been possible to test this on dummy data at present. If this were to be implemented as a permanent solution, this could potentially be made available to the wider policing community through the development of a Streamlit app, which could greatly assist in reducing the amount of data and time taken to review each dataset manually.

{{< video https://www.youtube.com/watch?v=7j8_DlMoaSc&t=22s >}}


<!-- ===== hsma_5/h5_5003_des_bottlenecks_amu/index.qmd ===== -->

---
title: "Using Discrete Event Simulation to model the bottlenecks in the Acute Medical Unit pathway"
categories:
  - Discrete Event Simulation (DES)
  - Streamlit
  - Acute Medical Unit (AMU)
  - Emergency Departments
  - Acute Care
  - Hospitals
  - NHS
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Acute Medical Unit (AMU)
  - Emergency Departments
  - Acute Care
  - Hospitals
author:
  - name: Becky Crofts
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Kayleigh Haydock
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
image: "cd4dqcnc.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    In this project, a computer simulation of the acute medical pathway in a Devon trust was created, along with an interactive tool allowing parameters such as the staffing levels to be changed. This allowed staff to explore the optimum levels of resourcing, enabling risk-free testing of staffing and resource changes before committing to these changes in the real-world.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=_3j0xC_yCKQ
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/BeckyCrofts/amu_modelling
    icon: fa-brands fa-github
---

The team’s project was to create a computer model of part of the acute medical pathway in their hospital trust. As part of this process patients come in with non-surgical emergencies, like an abnormal heart beat, and they’re triaged to decide the best route of care for them. In some cases that will be an admission to hospital, but increasingly this may involve alternatives that combine just a few hours in hospital with close follow up and perhaps even forms of remote monitoring, like monitoring their heart through a mobile app.

The aim of this project was to model part of the acute medical pathway in this hospital trust, simulate how the system currently works, and investigate whether there is optimal allocation of staff and resources. The benefit of this model is it allows for changing parameters such as adding extra staffing to see what impact that has on the pathway. Testing these changes in the real-world costs time and money, while computer simulation allows you to trial these changes with minimal cost and no risk.

The model isn’t validated yet, but when it is it’ll be handed over to users (e.g. clinicians and managers) to support them in making decisions about staffing or resourcing. They’ll be able to test those changes mentioned above without risk before proceeding to a real-world test of change.

{{< video https://www.youtube.com/watch?v=_3j0xC_yCKQ >}}

[Access the Github Repository](https://github.com/BeckyCrofts/amu_modelling)


<!-- ===== hsma_5/h5_5004_effect_complex_discharge_delays_acute_perform/index.qmd ===== -->

---
title: "Modelling the effect of complex discharge delays on acute performance"
categories:
  - Discrete Event Simulation (DES)
  - Discharge
  - Hospitals
  - Patient Flow
  - Acute Care
  - Inter-service Interactions
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Discharge
  - Hospitals
  - Patient Flow
  - Acute Care
  - Inter-service Interactions
author:
  - name: Hannah Perkins
    affiliation: University Hospitals Plymouth NHS Trust
organisations:
  - University Hospitals Plymouth NHS Trust
image: "il8e1h81.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Hospitals face increasing A&E wait times, ambulance delays, and growing waiting lists, partly due to inefficient patient discharges. This project modelled patient flow in and out of acute hospitals, focusing on discharge delays.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=nrUkRha_5F0&t=1s
    icon: fa-brands fa-youtube
---

Hospitals across the country are struggling to provide patients with the care they need in a timely manner. Increasing waiting times in A&E departments, long waits for ambulances and growing waiting lists are all examples of these issues. A possible cause of these issues is the difficulty in discharging patients from acute hospital beds efficiently, due to lack of onward care capacity. Timely discharges are crucial to patient care, to get the right care in the right place at the right time.

A previous PenCHORD project, IPACS, looked at understanding the capacity required in social and community care to facilitate timely flow out of acute hospitals. This project was based on IPACS, and extended the scope to include elective inpatient waiting lists and patients in the emergency department.

The aim of the project was to model flow of patients into and out of an acute hospital site, with particular focus on how delays to complex discharges affect patients waiting to come into the hospital. The results from this project will help to articulate how the issues in discharging patients from an acute hospital bed affect emergency care performance (time spent in A&E and ambulance handover time) as well as waiting lists for elective inpatient care. A discrete event simulation was created to model patient flow through an acute facility and into community/social care.

{{< video https://www.youtube.com/watch?v=nrUkRha_5F0&t=1s >}}


<!-- ===== hsma_5/h5_5005_des_elective_surgery_pathways/index.qmd ===== -->

---
title: "Discrete Event Simulation to model elective surgery pathways"
categories:
  - Discrete Event Simulation (DES)
  - Streamlit
  - Elective Surgery
  - Waiting Times
  - Surgical
  - Hospitals
  - NHS
techniques:
  - Discrete Event Simulation (DES)
  - Streamlit
areas:
  - Elective Surgery
  - Waiting Times
  - Surgical
  - Hospitals
author:
  - name: Dominic Allen
    affiliation: Guy’s and St Thomas’ NHS Foundation Trust
organisations:
  - Guy’s and St Thomas’ NHS Foundation Trust
image: "81ntpmry.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project created a Discrete Event Simulation to model elective surgery pathways. This tool optimises surgical pathways and provides a ready-made format for creating interactive webapps, benefiting future HSMA participants and other interested users.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=prKoVH2DeyU&t=3s
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/gasman-dom/gstt_hands_waitlist_st
    icon: fa-brands fa-github
  - name: Website
    url: https://gstt-hands-waitlist.streamlit.app/
    icon: fa-solid fa-globe
---

The aim of the project was to create a Discrete Event Simulation in SimPy to model elective surgery pathways, which could be used to model changes to a pathway and their impact on waiting times. This was accomplished and realised as an interactive webapp using Streamlit.

The project is FOSS and is available for anyone to use in the future to model their own surgical pathways or other waiting lists. Future HSMA participants, and anyone else who is interested, will be able to modify this model into a format useful to their organisation.

This will provide possible opportunities for the optimisation of surgical pathways, and also provide a ready-made format for future HSMA participants to create interactive SimPy-based webapps without having to “reinvent the wheel.”

{{< video https://www.youtube.com/watch?v=prKoVH2DeyU&t=3s >}}


<!-- ===== hsma_5/h5_5006__ml_inequities_hospital_procedure_access/index.qmd ===== -->

---
title: "Using Machine Learning to estimate inequities in access to hospital procedures"
categories:
  - Inequalities
  - Planned Admissions
  - Machine Learning
  - APC Dataset
  - NHS
techniques:
  - Machine Learning
areas:
  - Inequalities
  - Planned Admissions
  - APC Dataset
author:
  - name: Benjamin Mouncer
    affiliation: NHS, Norfolk County Council
organisations:
  - Norfolk County Council
image: "t3xhyl8e.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to determine disparities in accessing planned hospital appointments by calculating true admission rates for high deprivation areas. They found that minimal public data and simple models were insufficient. Future work includes creating synthetic data and exploring additional features like emergency admissions.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=NXGYKKPntO8&list=PLgHO2TgIJXdl1MvfkwCGJ6n8_1EYCSzex&index=4
    icon: fa-brands fa-youtube
---

The aim of this project was to determine on an ICB, LTLA and UTLA the overall level of disparity in accessing planned appointments in hospital. The team did this for each high deprivation LSOA calculating the true rate of planned hospital admissions.

They learnt that estimating equity in planned admissions may be possible but not with a minimal set of public data and simple machine learning models.

They put these findings into practice by building in a way to quantify the confidence interval of a machine learning model is essential to effectively use them in real world environments. They also found combining multiple years of data can work with low quality datasets. Of the datasets used the age distribution of an area was the most consistently predictive feature encountered.

One avenue for progression with this project is the creation of synthetic data to have each person within an area as a row of data. Model complexity must increase to create viable models if they even exist. Other feature sets could be explored such as the emergency admissions, type of planned admissions and other variable synthesised from the HES APC dataset.

{{< video https://www.youtube.com/watch?v=NXGYKKPntO8&list=PLgHO2TgIJXdl1MvfkwCGJ6n8_1EYCSzex&index=4 >}}


<!-- ===== hsma_5/h5_5008_multiobjective_neonatal_optimisation/index.qmd ===== -->

---
title: "Modelling the location of neonatal critical care units in North West England"
categories:
  - Mapping
  - Location Optimization
  - Discrete Event Simulation (DES)
  - Streamlit
  - Neonatal
techniques:
  - Mapping
  - Location Optimization
  - Discrete Event Simulation (DES)
areas:
  - Neonatal
  - Inpatients
  - Hospitals
author:
  - name: Duncan Galletly
    affiliation: North West Neonatal operational Delivery Network (NWNODN)
organisations:
  - North West Neonatal operational Delivery Network (NWNODN)
image: "m6ij2sto.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project explored the optimal location for 22 neonatal care sites in North West England, using an algorithm that balanced travel time, distance, NICU care episodes, and admission numbers. A discrete event simulation model and dashboard were created to explore various scenarios, aiding stakeholder decision-making.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=Fsn_PTGCERI&list=PLgHO2TgIJXdl1MvfkwCGJ6n8_1EYCSzex&index=8
    icon: fa-brands fa-youtube
---

In this project, the optimum location for 22 neonatal care sites across North West England was explored.

The algorithm chosen gave equal weighting to the goals of

- minimising average travel time
- maximising the proportion of people within 30 minutes
- minimising the maximum possible distance travelled
- maximising the number of care episodes taking place in level 3 NICU units
- maximising the minimum number of admissions per year (i.e. trying to avoid units with very low numbers of admissions)
- minimising the largest number of admissions per year (i.e. trying to avoid units with very high numbers of admissions)
- maximising the proportion within 30 mintues and in level 3 NICU units

This was then built into a discrete event simulation model and a dashboard, allowing a range of scenarios to be explored by stakeholders.

![](assets/2024-10-24-16-56-01.png)

{{< video https://www.youtube.com/watch?v=Fsn_PTGCERI&list=PLgHO2TgIJXdl1MvfkwCGJ6n8_1EYCSzex&index=8 >}}


<!-- ===== hsma_5/h5_5009_network_analysis_diagnostics_ae/index.qmd ===== -->

---
title: "Network Analysis of diagnostic procedures in A&E setting"
categories:
  - Network Analysis
  - Plotly Dash
  - Emergency Departments
  - Diagnostic Procedures
  - ECDS Dataset
  - NHS
techniques:
  - Network Analysis
  - Plotly Dash
areas:
  - Emergency Departments
  - Diagnostic Procedures
  - ECDS Dataset
author:
  - name: Hamzah Shami
    affiliation: NHS England
organisations:
  - NHS England
image: "akzr6q9d.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project aimed to analyse the relationship between different diagnostic procedures in A&E using NHS ECDS data. A web tool was developed to provide insights into diagnostic procedure usage across the country. The tool will allow users to explore graphic visualisations and accompanying analytics.
  links:
  - name: Code
    url: https://github.com/HamzahJShami/HSMA5
    icon: fa-brands fa-github
---

In A&E a patient can be given one or more diagnostic procedures. These can be as simple as the various blood test or more complicated procedures like an MRI test. The aim of this project was to look at the relationship between the different investigations. Hamzah pulled data from the NHS ECDS and created a series of graphs based by A&E provider.

The aim of the project become to create a web tool that can provide insight in how diagnostic procedure are used in A&E departments across the country. Hamzah learnt a lot about graph analysis and the connection between clinical theory and analytical process.

Hamzah is now working on creating a web tool that allows users to explore the graphic visualisation as well as some analytics that accompany the graphs.


<!-- ===== hsma_5/h5_5010_health_equity_audits_cdc/index.qmd ===== -->

---
title: "Creating a tool to automatically generate health equity audits for Community Diagnostic Centres"
categories:
  - Community Diagnostic Centres (CDCs)
  - Inequalities
  - Streamlit
  - Automation
  - Health Equity Audits
  - NHS
  - Reproducible Analytical Pipelines (RAP)
techniques:
  - Streamlit
  - Automation
  - Reproducible Analytical Pipelines (RAP)
areas:
  - Health Equity Audits
  - Community Diagnostic Centres (CDCs)
  - Inequalities
author:
  - name: Sarah Houston
    affiliation: UCL Partners Health Innovation
  - name: Deborah Newton
    affiliation: Reading Borough Council
organisations:
  - UCL Partners Health Innovation
  - Reading Borough Council
image: "2d2d6s0i.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project aimed to create a tool to perform a health equity audit for Community Diagnostic Centres (CDCs) in England. The tool will identify healthcare inequalities, suggests data improvements, and supports local CDCs in understanding their impact. Developed using Python and Streamlit, it allows for easier comparison and sharing of learning across regions, with potential applications beyond CDCs.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=tavZS5MmwOA
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/SarahHoustonGH/Diagnostic_HealthEquityAudit
    icon: fa-brands fa-github
---

Community diagnostic centres (CDCs) have been launched across England to tackle the diagnostic backlog and address healthcare inequalities. CDCs and commissioners struggle to identify their baseline of healthcare inequalities and monitor their impact going forwards. This leads to resourcing constraints on teams in the short term and risks minimising the CDC’s impact on healthcare inequalities in the long term. As these are emerging services, the quality of data collected by them to understand their impact is unclear. This impact can be estimated through a health equity audit, however this is usually and long and manual process.

The aim of the project was to create an open source and shareable tool to:

- Perform a health equity audit to identify where the service may be having an impact on healthcare inequalities

- Identify where data may be incomplete or poor quality, and automatically suggest evidence-based strategies to improve the data

This has been achieved through development of Python code to process data and a Streamlit app to present data. This project involved developing a toolkit to explore inequalities for multiple sites. Through trialling this toolkit with dummy data for different sites we have developed metrics would be most suitable to identify different regions.

The team would like to further develop the tool to make it more widely applicable and include more robust analysis of inequalities. They are planning to engage with local and national stakeholders of CDCs to demonstrate the tool and gather feedback. They are also planning to implement changes suggested by the Patient and Public Involvement Group (PenPEG).

The tool itself, at a minimum, will support a local CDC to understand their local impact on healthcare inequalities and address areas of concern where relevant. It’s an example to demonstrate the power of open-source techniques and data in healthcare inequalities. If adopted by multiple regions, it would allow different regions to generate similar outputs which would allow for easier comparison and sharing of learning. The code developed could also be easily adapted and reused for other healthcare services beyond CDCs.

{{< video https://www.youtube.com/watch?v=tavZS5MmwOA >}}


<!-- ===== hsma_5/h5_5012_forecasting_demand_clock_starts/index.qmd ===== -->

---
title: "Forecasting Demand – Investigating approaches to forecast clock starts"
categories:
  - Forecasting
  - Clock Starts
  - Demand & Capacity
  - Prophet
  - ARIMA
  - Machine Learning
  - Waiting Lists
  - NHS
techniques:
  - Forecasting
  - Prophet
  - ARIMA
areas:
  - Clock Starts
  - Demand & Capacity
  - Waiting Lists
author:
  - name: Jane Kirkpatrick
    affiliation: NHS England
  - name: Mathew Ojo
    affiliation: NHS England
  - name: Lyndsey Allen
    affiliation: NHS North of England CSU (NECS)
  - name: Luke Asante
    affiliation: NHS North of England CSU (NECS)
  - name: Evelyn Koon
    affiliation: NHS England
organisations:
  - NHS England
  - NHS North of England CSU (NECS)
image: "43fcmhsi.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to explore and evaluate different forecasting methods for NHS England's clock starts, moving beyond Excel-based scenario modelling. The team tested various models and suggested translating the Excel model into Python and obtaining more data to improve demand forecasting and manage wait lists.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=Obzos_OfyEw
    icon: fa-brands fa-youtube
---

Within the organisation (NHS England) forecasting for clock starts is currently done using scenario-based modelling in Excel. This limits how much data can be used to make forecasts, and the techniques that can be deployed. There was a desire to explore other forecasting methods to see if they could obtain more accurate forecasts, and also to valid the forecasts that are being made using the existing model. Understanding demand is important to manage wait lists, which is a high priority for the NHS, hence the interest in modelling clock starts.

The aim of the project was to explore different ways of forecasting demand, evaluate their performance and offer suggestions as to how forecasting could be done in the future.

The team carried out exploratory data analysis to understand differences between different data types and the differences in the patterns of demand for different subgroupings. They built a codebase that loaded the required data and ran model functions for Naïve, ARIMA, Prophet and a combination of Linear Regression and Random Forest. They evaluated the performance of these models to each other, and the modelling technique currently used. They also made some progress on rebuilding the current excel model in Python.

They found that while the more performant models that we used performed well (produced low error metrics), they generally didn’t perform as well as the model currently used within the organisation. This suggested that a helpful next step of the project might be to complete the work of translating the excel model into python and doing further work to understand if they can get more data to better understand the drivers of demand beyond just time series.

{{< video https://www.youtube.com/watch?v=Obzos_OfyEw >}}


<!-- ===== hsma_5/h5_5013_understanding_excess_mortality/index.qmd ===== -->

---
title: "Understanding Excess Mortality in Dorset"
categories:
  - Streamlit
  - PCMD Dataset
  - Forecasting
  - Public Health
techniques:
  - Streamlit
  - Forecasting
areas:
  - PCMD Dataset
  - Public Health
author:
  - name: Eleanor Jeram
    affiliation: Public Health Dorset
  - name: Lee Robertson
    affiliation: Public Health Dorset
  - name: Wilson Otitonaiye
    affiliation: Public Health Dorset
organisations:
  - Public Health Dorset
image: "l8j81ti4.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to improve access and service experience through Dorset ICS's Health Inequalities programme. It focused on defining and measuring excess mortality, identifying unexpected mortality trends, and understanding driving factors.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=e4wYE9tphVk
    icon: fa-brands fa-youtube
---

The project was based on the Dorset ICS (Integrated Care Systems) Health Inequalities programme aim to improve access, enhance the experience of services for everyone. Through this and the ICP (Integrated Care Partnership) integrated care strategy supporting early intervention and prevention approaches, reducing the variation in how well people are supported with long-term conditions. This in turn reduces excess mortality.

The aim of the project was to understand and build on the definition of excess mortality and how the baseline is measured. Identifying periods of unexpected mortality (increases and decreases) to understand factors which may be driving changes.

The team learnt that the discrepancies of measuring expected mortality through five year rolling averages removes the impact of seasonality on mortality resulting in hidden trends; with seasonality patterns varying across different underlying causes. The output of the project will allow for differing definitions of expected mortality, providing a base line and forecast moving forward. In addition, different cohorts of the population are considered in line with the Public Health objectives and priorities.

The team are hoping to further develop their StreamLit app to make sharing and access available to the wider team – building questions and bringing in wider subject matter expertise.

:::{.callout-tip}
“HSMA was an invaluable opportunity, I was impressed by how much the three members of the team learnt and the development of advanced analytics and forecasting. The hands-on approach in the course has resulted in instant results in our understanding of excess mortality”
- Natasha Morris, Public Health Intelligence Team Leader
:::

{{< video https://www.youtube.com/watch?v=e4wYE9tphVk >}}


<!-- ===== hsma_5/h5_5014_workforce_turnover_drivers/index.qmd ===== -->

---
title: "Investigating factors impacting NHS workforce retention"
categories:
  - Plotly Dash
  - Staff Turnover
  - Workforce
  - Regression
  - Machine Learning
  - NHS
techniques:
  - Plotly Dash
  - Regression
  - Machine Learning
areas:
  - Staff Turnover
  - Workforce
author:
  - name: Marie Rogers
    affiliation: NHS England
  - name: Richard Pilbery
    affiliation: Yorkshire Ambulance Service NHS Trust
organisations:
  - NHS England
  - Yorkshire Ambulance Service NHS Trust
image: "f1haee9r.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    This project aimed to work out which factors are the biggest drivers of staff turnover using regression modelling on staff workforce figures as well as other local factors such as employment. This was turned into a dashboard for internal use.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=yYnkdsM5HHo&list=PLgHO2TgIJXdl1MvfkwCGJ6n8_1EYCSzex&index=2
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/marierrogers/HSMAproject2023
    icon: fa-brands fa-github
---
This project aimed to work out which factors are the biggest drivers of staff turnover using regression modelling on staff workforce figures as well as other local factors such as employment. This was turned into a dashboard for internal use. However, it was concluded that the currently available data only acccounted for 13% of the variation in turnover seen; more data on other factors is required to explain the patterns seen.

{{< video https://www.youtube.com/watch?v=yYnkdsM5HHo&list=PLgHO2TgIJXdl1MvfkwCGJ6n8_1EYCSzex&index=2 >}}


<!-- ===== hsma_5/h5_5015_des_dorset_rheumatology/index.qmd ===== -->

---
title: "A Discrete Event Simulation Model to reduce Rheumatology waiting times in Dorset"
categories:
  - Discrete Event Simulation (DES)
  - NHS
  - Rheumatology
  - Waiting Lists
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Rheumatology
  - Waiting Lists
author:
  - name: Abby Dewhurst
    affiliation: Dorset Intelligence and Insight Service (NHS Dorset)
  - name: Claire Davies
    affiliation: BCP Council
  - name: Krzysztof Cepa
    affiliation: Dorset Intelligence and Insight Service (NHS Dorset)
organisations:
  - Dorset Intelligence and Insight Service (NHS Dorset)
  - BCP Council
image: "Abby Dewhurst.jpg"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to reduce the Rheumatology waiting list and times in Dorset using Discrete Event Simulation (DES). The team built a DES model and a Streamlit app to simulate capacity changes.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=P6nQle5tgBM&t=1s
    icon: fa-brands fa-youtube
---

The current Referral to Treatment waiting list is at its highest level in NHS history. Identifying methods for reducing the waiting list and waiting times would benefit patient care.

The aim of the project was to look at what changes in capacity, the number of appointments, could be made to reduce the waiting list and waiting times for Rheumatology services in Dorset. This was done using Discrete Event Simulation (DES), which is a technique that models flow through a pathway and can show what happens if changes are made.

During the project the team built a DES model to look at the Rheumatology pathway. They then built an app using Steamlit so that stakeholders can model the impact of capacity changes on the size of the waiting lists and the average waiting time for patients.

They will be presenting the final model and app to stakeholders and getting feedback, adapting if required; then putting it on GitHub to be shared.

{{< video https://www.youtube.com/watch?v=P6nQle5tgBM&t=1s >}}


<!-- ===== hsma_5/h5_5016_inequalities_demographic/index.qmd ===== -->

---
title: "Developing a tool to assess inequalities and demographic coverage of service locations"
categories:
  - Inequalities
  - Streamlit
  - Mapping
  - Travel Times
  - NHS
  - Demographics
techniques:
  - Streamlit
  - Mapping
  - Travel Times
areas:
  - Inequalities
  - Demographics
author:
  - name: Alex Owens
    affiliation: NHS Arden & GEM CSU
  - name: Phoebe Woodhead
    affiliation: Health Innovation Wessex
  - name: Sian Heath
    affiliation: Nottingham University Hospitals NHS Trust
organisations:
  - NHS Arden & GEM CSU
  - Health Innovation Wessex
  - Nottingham University Hospitals NHS Trust
image: "8p2z6i2v.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to empower NHS service providers with a tool to understand their patient population and direct service expansion to underserved groups. It combines geospatial analysis, demographic data, and travel calculations.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=7a1bx1NfyBA&t=3s
    icon: fa-brands fa-youtube
---

This project hopes to empower NHS service providers with a tool that grants a deeper understanding of the population they serve and allows them to direct future service expansion to provide access to underserved groups.

It will provide a nuanced demographic breakdown of the patient population, including age, ethnicity, and deprivation, offering crucial insights into the diversity of healthcare needs within the service area – with potential additions to allow providers to add new demographic information to better understand catchment by the conditions they look to treat.

Undertaking this project gave us a deeper understanding of health modelling methodologies and their practical applications. The team learned to combine geospatial analysis, demographic data, and travel distance calculations to create a dynamic tool for use by NHS service providers.

They will continue developing this tool, adding data sources that collaborating service providers hold, but are unable to publish alongside the open-source code, to better identify underserved groups with specific ailments to be treated. This will allow them to give more precise information to let their new service allocation tool pick more appropriate potential locations for new sites.
They will be presenting the final model and app to stakeholders and getting feedback, adapting if required; then putting it on GitHub to be shared.

{{< video https://www.youtube.com/watch?v=7a1bx1NfyBA&t=3s >}}

