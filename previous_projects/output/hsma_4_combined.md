<!-- ===== hsma_4/h4_4000_booked_appointments_utc/index.qmd ===== -->

---
title: "The Effect of Booked Appointments on Waiting Times at Urgent Treatment Centres"
categories:
  - Discrete Event Simulation (DES)
  - Urgent Treatment Centres (UTC)
  - Emergency Departments
  - ECDS Dataset
  - Booked Appointments in Walk-in Services
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Urgent Treatment Centres (UTC)
  - Emergency Departments
  - ECDS Dataset
  - Booked Appointments in Walk-in Services
author:
  - name: Alice Waterhouse
    affiliation: NHS England
organisations:
  - NHS England
image: "ultnzucw.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to determine if booked appointments reduce waiting times in Urgent Treatment Centres. Using a Discrete Event Simulation model, it showed that higher percentages of booked appointments led to decreased waiting times.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=W1cK5vVukXc&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=6
    icon: fa-brands fa-youtube
---

The aim of the project was to examine in more detail the question of whether booked appointment times might reduce waiting times in Urgent Treatment Centres (UTC). This was done by considering a “generic” UTC – a kind of average over services of this type which were submitting high quality data to the Emergency Care Dataset.

Data on the paths patients took through these services, how frequently patients arrived and the number of staff present were taken from this data and used to build a Discrete Event Simulation model. The modelled average time taken for initial assessment of the patient, treatment, and any investigations or tests was chosen to give the best fit to actual waiting times. The distribution of patient arrival times was then modified to simulate the introduction of additional booked appointments, leading to a more even spread of patient arrivals throughout the day.

The model showed a decrease in overall waiting times when higher percentages of patients booked a timeslot in advance. This will be used to better inform policy on the number of booked appointments needed to make a significant impact to waiting times. Further analysis is expected to shed light on the impact of different ways of prioritising patients according to both clinical need and whether they have booked in advance.

This is a great test case for the use of Discrete Event Simulation to inform policy and strategy at a national level. It demonstrates the impact that such modelling can have and creates opportunity for similar work in the future, ensuring that decision making is supported by high quality analytical insight.

{{< video https://www.youtube.com/watch?v=W1cK5vVukXc&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=6 >}}


<!-- ===== hsma_4/h4_4001_covid_19_vaccination_demand_capacity/index.qmd ===== -->

---
title: "South East Regional Covid 19 Vaccination Demand & Capacity Modelling"
categories:
  - Forecasting
  - Vaccination
  - Prophet
  - COVID-19
  - Plotly Dash
  - NHS
techniques:
  - Forecasting
  - Prophet
  - Plotly Dash
areas:
  - Vaccination
  - COVID-19
author:
  - name: Charlene Black
    affiliation: NHS South, Central and West CSU
  - name: Adonis Sithole
    affiliation: NHS South, Central and West CSU
  - name: Edward Chick
    affiliation: NHS South, Central and West CSU
  - name: Mayoor Dhokia
    affiliation: Surrey and Borders Partnership NHS Foundation Trust
organisations:
   - NHS South, Central and West CSU
   - Surrey and Borders Partnership NHS Foundation Trust
image: "bk6maxsh.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to create an easy-to-use model for predicting Covid vaccination demand and capacity. Despite data access barriers, the team made progress by using past vaccination data. The tool will help track vaccinations, identify problem areas, and save time and money.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=_AWTVeNqOwM&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=3
    icon: fa-brands fa-youtube
---

The aim of the project was to create an easy to use model for predicting demand and capacity for Covid vaccinations.

During the project the team came up against many barriers, the biggest of which was getting access to the data. The other issue they had with getting the data was the limits imposed on the amount of data you could download in one go, meaning that it was a lengthy process.

They modelled potential update scenarios and have started to work on this and have making great progress. They will use the previous vaccination data, along with the Winter 2022 vaccination data to strengthen the tool, so that following vaccination seasons it can be used more widely. They will look at other vaccinations it could be applied to, such as flu.

This will give users an easy to use tool to keep track of vaccinations and pick up problem areas quickly. It will save time and money on current methods and enable more people to use and understand the vaccination position

{{< video https://www.youtube.com/watch?v=_AWTVeNqOwM&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=3 >}}


<!-- ===== hsma_4/h4_4002_des_adhd_autism_pathway/index.qmd ===== -->

---
title: "Use of Discrete Event Simulation to Tackle Long Waits and a Growing Backlog for Children Requiring Neuro Development Assessment (Autism and ADHD)"
categories:
  - Discrete Event Simulation (DES)
  - Neurodiversity
  - Paediatric
  - Mental Health
  - Demand & Capacity
  - Reducing Backlogs
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Neurodiversity
  - Paediatric
  - Mental Health
  - Demand & Capacity
  - Reducing Backlogs
author:
  - name: Irma Tanovic
    affiliation: Oxford Health NHS Foundation Trust
organisations:
  - Oxford Health NHS Foundation Trust
image: "ur9vxl8p.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to identify bottlenecks in the Autism and ADHD assessment pathway for children and determine changes needed to manage demand and avoid backlogs. The main issue was clinical staffing capacity. Could adding one clinician could maintain a steady state and prevent backlog growth?
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=IuD0tmKtjV4&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=13
    icon: fa-brands fa-youtube
---

The aim of the project was to understand the current pathway to assessment of Autism and ADHD in children, identifying any bottlenecks. We wanted to know what change needed to take place in order to keep on top of ongoing demand levels and see patients within an acceptable time - what do we need to do to maintain a steady state and avoid a backlog from developing?

In addition to maintaining a steady state, we wanted to understand how to eliminate the backlog that has developed as a result of the ongoing demand not being met.

The main bottlenecks were identified and the issue is not at the beginning of the pathway (getting the completed questionnaires back from parents/schools) like it has been suggested at the start of the project, but further down the pathway due to clinical staffing capacity. Furthermore, the developed model shows that recruiting just one extra clinician would result in having a steady state with the backlog not growing. The model also shows possible staffing requirements to remove existing backlog in 1-5 years in addition to keeping a steady state.

The findings and the model demo have been presented to the stakeholders including service managers, clinical and operational leads, service heads and the Trust board, and discussions on plans for how the model is used to support any improvement work in the service is already taking place.

{{< video https://www.youtube.com/watch?v=IuD0tmKtjV4&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=13 >}}


<!-- ===== hsma_4/h4_4003_des_amu_flow/index.qmd ===== -->

---
title: "Using DES to Improve Flow through an Acute Medicine Assessment Pathway"
categories:
  - Discrete Event Simulation (DES)
  - Emergency Departments
  - Patient Flow
  - Inpatients
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Emergency Departments
  - Patient Flow
  - Inpatients
author:
  - name: Helen Young
    affiliation: Nottingham University Hospitals NHS Trust
  - name: Thomas Knight
    affiliation: Sandwell and West Birmingham NHS Trust
organisations:
  - Nottingham University Hospitals NHS Trust
  - Sandwell and West Birmingham NHS Trust
image: "f1haee9r.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    Nottingham University Hospitals' Acute Medicine Assessment areas face high occupancy, causing delays in the Emergency Department. A Discrete Event Simulation showed that if patients left within 16 hours, ED wait times over 6 hours would reduce by 90%. This insight will help quantify additional ward beds needed to improve patient flow and reduce harm.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=TDTyBcVZDUU&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=9
    icon: fa-brands fa-youtube
---

Nottingham University Hosptials has two major Acute Medicine Assessment areas (WB3 and AMRA), where patients can be reviewed before being sent to the most appropriate specialty base ward bed for their needs.

WB3 and AMRA run at very high occupancy levels, and patients frequently wait in the Emergency Department (ED) for a WB3/AMRA bed for more than 6 hours – this is a known cause of delay-related harm. Stakeholders feel that a major constraint is patients waiting in WB3/AMRA who are ready to be moved to a ward bed.

The team wanted to investigate what the impact would be if patients were able to leave WB3/AMRA more quickly. What would this do to the backlog of queues in ED, and how would it affect waiting times there?

A Discrete Event Simulation (DES) was made of the entire Acute Medicine assessment pathway. They then simulated several alternative scenarios in which patients leave WB3/AMRA more quickly after their period of assessment is completed – and were able to see the impact of this in the key metrics.

If all patients left WB3/AMRA within four hours of their request for a ward bed, patients would never have to wait in ED for a WB3/AMRA bed for more than 6 hours. Even if all patients left WB3/AMRA within 16 hours of their request, this would still reduce the number of patients waiting more than 6 hours by 90% - substantially reducing the risk of delay-related harm

We can now start to quantify the number of additional ward beds that would need to be freed up to support this improved flow, and bring these findings to discussions on how/where additional bed days could be released.

{{< video https://www.youtube.com/watch?v=TDTyBcVZDUU&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=9 >}}


<!-- ===== hsma_4/h4_4004_des_cbt_iapt/index.qmd ===== -->

---
title: "Discrete Event Simulation of Cognitive Behavioural Therapy Pathway in an IAPT Service"
categories:
  - Discrete Event Simulation (DES)
  - NHS Talking Therapies (Formerly IAPT)
  - Community Mental Health
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Mental Health
  - NHS Talking Therapies (Formerly IAPT)
  - Community Mental Health
author:
  - name: Katie Brown
    affiliation: Dorset HealthCare University NHS Foundation Trust
  - name: Hannah Carroll
    affiliation: Dorset HealthCare University NHS Foundation Trust
  - name: Andrew Poole
    affiliation: NHS Dorset ICB
  - name: Matthew Chapman
    affiliation: Dorset HealthCare University NHS Foundation Trust
organisations:
  - Dorset HealthCare University NHS Foundation Trust
  - NHS Dorset ICB
image: "il32v884.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project used Discrete Event Simulation to model the wait list for High Intensity Cognitive Behavioural Therapy. It found that changing an evening group to a face-to-face clinic could reduce wait times, especially for face-to-face or evening 1-1 appointments.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=KPmxGzSuN0s&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=4
    icon: fa-brands fa-youtube
---

The aim of the project was to use Discrete Event Simulation (DES) to model the current wait list for High Intensity Cognitive Behavioural Therapy (HI-CBT). The team wanted to see if changing the allocation of therapist resources by running an evening face-to-face clinic, instead of an evening group, would improve overall wait times for therapy.

Patients were created as entities within the model, and average % preferences for IESO (online therapy), group therapy, virtual or face-to-face 1-1 appointments were assigned. Along with whether the patient was a priority, preferred evening or face-to-face appointments, and average number of appointments offered. They used current and historic data of people waiting or seen for therapy, attendance rates, and meeting with the data lead and service managers within Steps 2 Wellbeing, in order to gain an accurate picture of the waiting and treatment pathway for patients.

The model does confirm that the longest wait times appear to be for people waiting for face-to-face or evening 1-1 appointments. The model shows improvements in waiting times when an evening group is changed to a 1-1 face-to-face evening clinic.

The team is making changes to the model based on stakeholder feedback and will present to senior management within the service.

{{< video https://www.youtube.com/watch?v=KPmxGzSuN0s&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=4 >}}


<!-- ===== hsma_4/h4_4005_des_delays_cancer_diagnosis_treatment/index.qmd ===== -->

---
title: "Use Of Discrete Event Simulation (DES) to reduce delays in Cancer Diagnosis & Treatment"
categories:
  - Discrete Event Simulation (DES)
  - Cancer
  - Colorectal
  - Identifying Bottlenecks in Pathways
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Cancer
  - Colorectal
  - Identifying Bottlenecks in Pathways
author:
  - name: Angel Masih
    affiliation: Gloucestershire Hospitals NHS Foundation Trust
  - name: James Page
    affiliation: University Hospitals of Morecambe Bay NHS Foundation Trust
  - name: Mahya Kaveh
    affiliation: Dartford and Gravesham NHS Trust
organisations:
  - Gloucestershire Hospitals NHS Foundation Trust
  - University Hospitals of Morecambe Bay NHS Foundation Trust
  - Dartford and Gravesham NHS Trust
image: "cuep9jku.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project developed a Discrete Event Simulation model for the Colorectal Cancer pathway identify key delays and solutions. Using three years of anonymised patient records, the model highlighted diagnostic delays during investigative stages.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=Wmpu4fpu0J4&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=2
    icon: fa-brands fa-youtube
---

The project aim was to develop a Discrete Event Simulation (DES) model based on Colorectal Cancer pathway at Gloucester Royal Hospital to identify the key delays within the pathway and identifying feasible solutions.

The team met with cancer service leads to discuss the scope of the project and discussed the patient pathway in detail. Three years of anonymised patient records were used to create the model. Delays for the pathway were split into patient & provider delays to focus only on provider delays.

They used SimPy to create a DES model using the current colorectal patient pathway. They ran the simulation for 100 runs to get the average waiting time for each stage of the pathway to identify the stages that took the longest amount of time. The DES model showed us the key delay, which is diagnostic delays caused during investigative stages.

The findings from the analysis will be presented to cancer leads to support reducing the waiting times for colorectal patients. The DES model helped to evidence key bottlenecks of the patient pathway and will help to discuss the prospect of how increased resource can help improve patient outcomes.

{{< video https://www.youtube.com/watch?v=Wmpu4fpu0J4&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=2 >}}


<!-- ===== hsma_4/h4_4006_des_flow_performance_utc/index.qmd ===== -->

---
title: "Discrete Event Simulation to Improve Flow and Performance in the Urgent Treatment Centre"
categories:
  - Discrete Event Simulation (DES)
  - Urgent Treatment Centres (UTC)
  - Emergency Departments
  - Identifying Bottlenecks in Pathways
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Urgent Treatment Centres (UTC)
  - Emergency Departments
  - Identifying Bottlenecks in Pathways
author:
  - name: Shilpa Patel
    affiliation: University College London Hospitals NHS Foundation Trust
organisations:
  - University College London Hospitals NHS Foundation Trust
image: "kfbt6ekn.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to improve Urgent Treatment Care by developing a model to help the Emergency Department allocate staff and rooms efficiently. The model tested alternative pathways and identified the need for additional rooms and better-aligned staffing rotas. These changes aimed to reduce bottlenecks and meet the target for patient flow.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=3JO8_70hHdA&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=11
    icon: fa-brands fa-youtube
  - name: News Story
    url: https://arc-swp.nihr.ac.uk/news/data-improves-urgent-care/
    icon: fa-solid fa-newspaper
---

The primary aim of the project was to improve Urgent Treatment Care (UTC) performance by developing a model which would help the Emergency Department (ED) team with the allocation of staff and rooms to match patient flow. The team wanted to understand what further staff and resources would be required for any variations in patient attendance. The ED team wanted to understand how changes in the patient pathway would reduce bottlenecks, for example, what would be the impact of front-loading diagnostics.

Initially, a discrete event simulation model was developed to show how patients currently flow through UTC. After an initial model had been developed, it was used to test the proposed alternative pathways for diagnostics. It was also used to model different numbers of staff and rooms. The model made it easy to understand the impact of changes to the existing provision and what would be most cost-effective.

The ED department was redesigned based on the model findings, which identified a need for additional rooms leading to reconfiguration of the space. It started a review of staffing rotas to see how they could be better aligned to findings from the analysis and future staffing rotas are designed to align with what the model identified was needed to meet the 95% target.

{{< video hthttps://www.youtube.com/watch?v=3JO8_70hHdA&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=11 >}}


<!-- ===== hsma_4/h4_4007_forecasting_los_ed/index.qmd ===== -->

---
title: "Forecasting Demand and Length of Stay in the Emergency Department"
categories:
  - Machine Learning
  - Forecasting
  - Streamlit
  - Paediatric
  - Length of Stay
  - Emergency Departments
  - Inpatients
  - Staffing Level Optimisation
  - NHS
techniques:
  - Machine Learning
  - Forecasting
  - Streamlit
areas:
  - Paediatric
  - Length of Stay
  - Emergency Departments
  - Inpatients
  - Staffing Level Optimisation
author:
  - name: Lisa Sabir
    affiliation: Sheffield Children's NHS Foundation Trust
organisations:
  - Sheffield Children's NHS Foundation Trust
image: "7eufiwyz.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to use forecasting and machine learning to predict Emergency Department arrivals and length of stay. A web-based app was designed to explore trends and suggest improvements. The app forecasts attendances and stay durations, helping plan workforce needs.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=a7MtCSbTg0I&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=7
    icon: fa-brands fa-youtube
---

The project aimed to use forecasting and machine learning methods to predict the length of stay and arrivals to the Emergency Department (ED) at different times of day, days of the week and months of the year. Understanding this would allow the team to examine trends and predict future demand so they better plan workforce.

They have designed a web-based app where they can input the Sheffield Children’s hospital data and use it to explore trends in attendances and length of stay. This allows them to see patterns and suggest improvements, such as when it would be better for extra staffing. The web-page produces a “Forecast” demonstrating the attendances by hour/day/month/year as well as length of stay via interactive buttons. It is then able to give an estimate for a selected time to predict future demand.

They have completed the forecasting methods for this project and are now developing the machine learning model. The team hope to gain permission for this to be used on a wider scale so individual trusts can input their own data.

{{< video https://www.youtube.com/watch?v=a7MtCSbTg0I&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=7 >}}


<!-- ===== hsma_4/h4_4008_meeting_demand_111/index.qmd ===== -->

---
title: "Meeting the demand of 111 for primary care services"
categories:
  - Discrete Event Simulation (DES)
  - Plotly Dash
  - Network Analysis
  - 111 Service
  - Primary Care (GP)
  - Emergency Departments
  - NHS
  - Telephone-based Services
techniques:
  - Discrete Event Simulation (DES)
  - Plotly Dash
  - Network Analysis
  - Telephone-based Services
areas:
  - 111 Service
  - Primary Care (GP)
  - Emergency Departments
author:
  - name: Richard Pilbery
    affiliation: Yorkshire Ambulance Service NHS Trust
  - name: Maddie Smith
    affiliation: NHS Devon ICB
  - name: Jon Green
    affiliation: University of Plymouth
organisations:
  - Yorkshire Ambulance Service NHS Trust
  - NHS Devon ICB
  - University of Plymouth
image: "Abby Dewhurst.jpg"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project modelled NHS 111 calls triaged to primary care. Simulations showed timely primary care contact could reduce 999 calls and ED attendances but would require nearly doubling primary care services.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=cg5Bp3O02io&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=1
    icon: fa-brands fa-youtube
  - name: Article
    url: https://arc-swp.nihr.ac.uk/publications/modelling-nhs-111-demand-for-primary-care-services-a-discrete-event-simulation/
    icon: fa-solid fa-newspaper
  - name: Paper
    url: https://bmjopen.bmj.com/content/13/9/e076203
    icon: fa-solid fa-file-contract
  - name: Code
    url: https://github.com/RichardPilbery/MOOOD-study
    icon: fa-brands fa-github
---

This was an attempt to model the impact of enforcing timely primary care interventions when 111 calls are undertaken.

{{< video https://www.youtube.com/watch?v=cg5Bp3O02io&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=1 >}}

More information: <https://arc-swp.nihr.ac.uk/publications/modelling-nhs-111-demand-for-primary-care-services-a-discrete-event-simulation/>


<!-- ===== hsma_4/h4_4009_ml_admissions_los_respiratory/index.qmd ===== -->

---
title: "Using Machine Learning to Predict Hospital Admissions and Length of Stay for Respiratory Conditions"
categories:
  - Machine Learning
  - Respiratory
  - NHS
  - Inpatient Admissions
techniques:
  - Machine Learning
areas:
  - Respiratory
  - Inpatient Admissions
author:
  - name: Andy McCann
    affiliation: NHS Midlands and Lancashire CSU
organisations:
  - NHS Midlands and Lancashire CSU
image: "ml9qqnl3.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to predict respiratory condition admissions and length of stay using patient history and demographics. Early-stage modelling showed promising preliminary findings. Further development will include more patient history to improve predictions and extend the model's capabilities.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=-0AGbib9Ig0&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=14
    icon: fa-brands fa-youtube
---

The aim of the project was to use available Primary and Secondary Care patient history and demographic information to better predict the chance of admission for respiratory conditions and subsequent length of stay, in order to better target interventions.

Due to time and data constraints, the modelling is currently at an early stage, but has demonstrated some interesting preliminary findings and put the structure in place for further development.

A Logistic Regression confirmed some expected factors but also revealed some surprises. An initial neural network with very little optimisation matches the Logistic Regression performance, with the potential to beat it when other features are included.

The model needs to take other features, particularly more patient history, into account to improve performance and be extended to predict length of stay as well as admission.

{{< video https://www.youtube.com/watch?v=-0AGbib9Ig0&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=14 >}}


<!-- ===== hsma_4/h4_4010_pifu_digital_outpatients_elective_recovery/index.qmd ===== -->

---
title: "The role of Patient Initiated Follow-up (PIFU) and ‘Digital Outpatients’ in Supporting the Elective Recovery - Can We Better Size Potential for Clearing the Backlog?"
categories:
  - Discrete Event Simulation (DES)
  - Patient Initiated Follow-Up (PIFU)
  - Digital Outpatients
  - Rheumatology
  - Reducing Backlogs
  - NHS
techniques:
  - Discrete Event Simulation (DES)
areas:
  - Patient Initiated Follow-Up (PIFU)
  - Digital Outpatients
  - Rheumatology
  - Reducing Backlogs
author:
  - name: Martina Fonseca
    affiliation: NHS England
  - name: Xiaochen Ge
    affiliation: NHS England
organisations:
  - NHS England
image: "wxsssb6m.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project aimed to explore the role of Patient Initiated Follow-up (PIFU) in addressing backlogs by mapping rheumatology outpatient pathways using discrete event simulation. The team modelled resource use and redeployment, focusing on PIFU's impact on referral-to-treatment waiting lists.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=TO5sKaW6BGk&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=12
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/nhsx/HSMA4-12-DES-rheum
    icon: fa-brands fa-github
---

The aim of the project is to find out what role Patient Initiated Follow-up (PIFU) can play in the redeployment of capacity to address the backlog. This will be done by mapping outpatient pathways for rheumatology sub-pathway using discrete event simulation (DES).

The team did what-if modelling of resource use based on the proportion of patients on a PIFU pathway, the rate of PIFU patient-initiated requests and the use of advice & guidance. They used this to understand how released resource is redeployed, and how the upstream referral-to-treatment (RTT) waiting list behaves (size and waiting time to first outpatient).

The focus was on rheumatology as a case study since it had well documented pathways and good clinical evidence base on PIFU, with PIFU actively endorsed by NHSE and GIRFT. It is mainly an outpatient specialty with many chronic patients on long-term follow-up, meaning that the effect of PIFU is in theory amplified.

Other opportunities include discussing a spin-off model that includes effect of other digital musculoskeletal peri-treatment interventions or creating a proof-of-concept generalised DES that can be used for other PIFU specialties (PIFU is being advocated across most elective specialties).

On the PIFU rheumatology model itself, the team aim to continue refining the model based on internal stakeholder feedback. A secondary aim is to create an end-user toy tool that could help demonstrate some of the what-if scenarios to operational managers, in collaboration with NHSE Digital Care Model colleagues.

{{< video https://www.youtube.com/watch?v=TO5sKaW6BGk&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=12 >}}


<!-- ===== hsma_4/h4_4011_predicting_non_elective_admissions/index.qmd ===== -->

---
title: "Predicting Non-Elective Admissions"
categories:
  - Machine Learning
  - Non-elective Admissions
  - Inpatient Admissions
  - Natural Language Processing (NLP)
  - NHS
  - "NHS 10-year plan shifts: Sickness to Prevention"
techniques:
  - Machine Learning
  - Natural Language Processing (NLP)
areas:
  - Non-elective Admissions
  - Inpatient Admissions
author:
  - name: Stephen Ashmead
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Karim Kamara
    affiliation: Royal Devon University Healthcare NHS Foundation Trust
  - name: Jahangir Alam
    affiliation: NHS North East London CSU
organisations:
  - Royal Devon University Healthcare NHS Foundation Trust
  - NHS North East London CSU
image: "lb926cjj.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to develop a predictive model to identify patients at high risk of admission and provide explanatory feedback. It combined structured and unstructured data models. The model helps predict non-elective admissions, enabling preventative care and better health outcomes, despite data limitations.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
---

The project aim was to develop a predictive model to identify patients at high risk of admission and to provide explanatory feedback as to why the patients were at risk. There were three elements of the project:

1. Using structured data to generate a predictive model

2. Use unstructured data from patient notes to generate a predictive model

3. To combine the two models to create an enhanced model

Three models were developed using structured data – logistic regression, random forest and neural network. Logistic regression performed best.

For the unstructured data, attempts to use more advanced Natural Language Processing techniques (such as neural networks and transformers) were unsuccessful due to limited computing power. However, a more basic model using a Term Frequency-Inverse Document Frequency matrix with a random forest showed some improvement on accuracy.

Electronic health record data can accurately be used to predict whether a patient is at risk of non-elective admission. Administrative events are often better indicators than clinical measures, however EHR data is prone to several limitations and biases which can lead to counter-intuitive correlations. For analysis of unstructured data, greater computing power than I have access to is required to analyse the large quantities of patient notes, even when focusing on relatively short time frames.

It will make a difference to patient care by allowing patients at risk of non-elective admission to receive preventative care, leading to better health outcomes for the individual patients and freeing up inpatient resources for other patients.


<!-- ===== hsma_4/h4_4012_predicting_violent_incidents_mh_inpatients/index.qmd ===== -->

---
title: "Predicting Violent Incidents on Mental Health Inpatient Units"
categories:
  - Machine Learning
  - Mental Health
  - Mental Health Inpatients
  - NHS
techniques:
  - Machine Learning
areas:
  - Mental Health
  - Mental Health Inpatients
author:
  - name: Iain Waring
    affiliation: Birmingham & Solihull Mental Health NHS Foundation Trust
organisations:
  - Birmingham & Solihull Mental Health NHS Foundation Trust
image: "6s86lwll.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    This project aimed to see if violent incidents could be reduced on hospital wards by predicting and preventing them, using machine learning. A dashboard would highlight high-risk wards to senior staff for intervention.
  links:
  - name: Video
    url:
    icon: fa-brands fa-youtube
  - name: Code
    url:
    icon: fa-brands fa-github
---

The aim of the project was to see if the occurrence of violent incidents on hospital wards could be reduced, if incidents could be pre-empted and interventions could be taken to try to prevent them from happening.

The trust has a wealth of electronic information about service users, staff, incidents, and what happens on inpatient units. The plan was to combine this information into a dataset and use machine learning techniques to predict which of our wards were most likely to suffer from an incident the following day. A dashboard would highlight these wards to senior nursing staff, who could experiment with actions to reduce incidents.

Discussions with key staff helped to identify which features from our systems would be the most helpful in predicting incidents.  A large dataset was constructed, and machine learning methods were used in an attempt to predict where incidents might happen. Unfortunately, the dataset did not prove to be informative enough to generate a working model – the predictions made were inaccurate and there was no way to apply them to the work environment.


<!-- ===== hsma_4/h4_4013_reducing_travel_times_cardiac_patients/index.qmd ===== -->

---
title: "Reducing Travel Times to Treatment for Cardiac Patients in the South East of England"
categories:
  - Mapping
  - Travel Times
  - Streamlit
  - Cardiology
  - Location Optimisation
  - NHS
techniques:
  - Mapping
  - Travel Times
  - Streamlit
  - Location Optimisation
areas:
  - Cardiology
author:
  - name: Glenn Ubly
    affiliation: NHS England Specialised Commissioning – South East Region
  - name: Atonia Drummond
    affiliation: NHS England
  - name: Janine James
    affiliation: NHS England
  - name: Victor Yu
    affiliation: The Strategy Unit
organisations:
  - NHS England Specialised Commissioning – South East Region
  - NHS England
  - The Strategy Unit
image: "7s1io79p.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project analysed travel times to understand the impact of flow of activity into London on patient travel. It identified a gap in cardiac surgery access for Kent & Medway patients, suggesting new sites could help. A Streamlit app visualised these impacts.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=28yXjieiMEM&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=6
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/GlennUbly/HSMA4_cardiac
    icon: fa-brands fa-github
  - name: Website
    url: https://glennubly-hsma4-cardiac-introduction-f1fq51.streamlitapp.com/
    icon: fa-solid fa-globe
---

The aim of the project was to employ geographical and statistical analysis of past and present travel times to understand the impact the flow of activity into London has on travel times for patients, whether referral pathways could be changed to minimise patient travel, and the extent to which additional sites would have a beneficial impact.

Initial analysis was undertaken on a sample of cardiac procedures within the hospital spell level data. The analysis identified a particular gap in the accessibility of cardiac surgery for patients in the Kent & Medway area, where there would be a significant benefit for the local population in the provision of a new cardiac surgery site or sites. The methods used gave a quantified and visual view of the impact of the options, and indicated the optimal configurations with 1 or 2 additional sites.

The team created a Streamlit application which allows a user to select from a list of possible new sites, and see the impact on travel times for Kent & Medway patients using maps, charts and a number of key travel time metrics.

The South East Cardiac Network have reviewed the findings, and this work will form part of the evidence base for service planning in the region. More generally, there has been interest in applying the methods and tools to other services.

{{< video https://www.youtube.com/watch?v=28yXjieiMEM&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=6 >}}


<!-- ===== hsma_4/h4_4014_service_planning_inequalities_carbon_output/index.qmd ===== -->

---
title: "Developing a Service Planning Decision Support Tool to Tackle Inequalities and Minimise Carbon Output"
categories:
  - Non-attendance Prediction
  - Machine Learning
  - Automation
  - Reproducible Analytical Pipelines (RAP)
  - Inequalities
  - Carbon Emissions
  - Health Equity Audits
  - NHS
techniques:
  - Machine Learning
  - Automation
  - Reproducible Analytical Pipelines (RAP)
areas:
  - Carbon Emissions
  - Health Equity Audits
  - Non-attendance Prediction
author:
  - name: Matt Eves
    affiliation: Derbyshire Community Health Services NHS Foundation Trust
  - name: Anya Gopfert
    affiliation: Torbay Council
  - name: Sally Brown
    affiliation: West Sussex County Council
organisations:
  - Derbyshire Community Health Services NHS Foundation Trust
  - Torbay Council
  - West Sussex County Council
image: "bef68gj9.png"
title-block-banner: ../../banner.png
repo: Y
pub-info:
  abstract: |
    The project explored the feasibility of considering inequalities and carbon emissions in new clinic locations. Achievements include automating a Health Equity Assessment, running logistic regression models to predict appointment no-shows, and estimating patient travel carbon emissions.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=zYWte2obxDs&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=8
    icon: fa-brands fa-youtube
  - name: Code
    url: https://github.com/hsma4-student/shine
    icon: fa-brands fa-github
---

There are three current significant health agendas to which this project broadly relates.

These are

1. The inequalities agenda
2. The digital and transformation agenda, and
3. The Net Zero agenda.

The aim of this project was to explore feasibility of considering the impact of a new clinic location on inequalities and carbon emissions, and any co-benefits or trade-offs between the two. Ultimately, the aim was to enable decision making to incorporate these two significant areas.

The team have achieved:

1. The automation of a Health Equity Assessment to compare the profile of patients in a service to the population at large

2. The running of a number of variations to a logistic regression model to identify features predictive of someone not attending their appointment

3. Quantifying an estimate for the patient travel carbon emissions associated with the current service design.

They are intending to continue working together as a team to finish the project’s initial scope (e.g. inc. possible new clinic sites and model impact on unmet need / emissions) – potentially supported by code from another project, emphasising the benefit of open source.

They have been successful in securing a funding from the Greener NHS Healthier Futures Action Fund joint bid.

{{< video https://www.youtube.com/watch?v=zYWte2obxDs&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=8 >}}


<!-- ===== hsma_4/h4_4015_spatial_modelling_crime/index.qmd ===== -->

---
title: "Spatial Modelling of Violent Crime to Support Strategic Analysis"
categories:
  - Mapping
  - Geostatistics
  - QGIS
  - Police
techniques:
  - Mapping
  - Geostatistics
  - QGIS
author:
  - name: Anupma Wadhera
    affiliation: TBC
  - name: Linda Wystemp
    affiliation: TBC
  - name: Andrea Casajuana Massanet
    affiliation: Counter Terrorism Policing
  - name: Helen Browne
    affiliation: Devon & Cornwall Police
  - name: Alessia Rose
    affiliation: Devon County Council
organisations:
  - Counter Terrorism Policing
  - Devon & Cornwall Police
  - Devon County Council
image: "m6ij2sto.png"
title-block-banner: ../../banner.png
pub-info:
  abstract: |
    The project aimed to use crime data and spatial analysis for intelligence reporting. Focusing on violent crime, the team used QGIS and Python libraries to analyse geographic offence data. The model identified hotspots, coldspots, and outliers, providing statistical confidence for intelligence reports.
  links:
  - name: Video
    url: https://www.youtube.com/watch?v=K0g2Iaw3blY&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=10
    icon: fa-brands fa-youtube
---

The aim of this project was to use various crime data variables and spatial analysis to turn them into useful insights for inclusion in assessed intelligence reporting.

The team chose to focus on violent crime offence data as they wanted to create our model using free and open source software.

They used QGIS and various Python libraries to explore the data. For the purpose of their model they obtained detailed geographic offence data uploaded by police forces in England and Wales.

The model was able to take a crime indicator (e.g. violent and sexual offences) for a region in the UK, prepare the data, apply and compare map classification schemes and run various analysis techniques to identify spatial autocorrelation, LISA , identify hotspots, coldspots and outliers. The statistical output provided a level of confidence in the findings that they can incorporate into intelligence confidence reporting levels.

The model will be shared with Commodity Threat Leads with the intention of using it internally to identify spatial trends in datasets that are restricted. Applying spatial analysis to these datasets will help identify regional variation and help quantify visual observations that will provide statistical certainty to any observed visual findings. The model will be proposed and applied to more restricted crime data in order to be used to draw out useful visualisations and insights to feed into intelligence reporting.

{{< video https://www.youtube.com/watch?v=K0g2Iaw3blY&list=PLgHO2TgIJXdn0k4y56xtM-VpcHU_5RJUN&index=10 >}}

