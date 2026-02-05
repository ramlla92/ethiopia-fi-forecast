# Ethiopia Financial Inclusion Analysis

## Project Overview

This project analyzes financial inclusion in Ethiopia using multiple data sources, including survey data, mobile money adoption metrics, and documented interventions. It spans five tasks:

1. **Data Cleaning & Exploration**
2. **Financial Inclusion Insights**
3. **Event Impact Modeling**
4. **Forecasting Access and Usage**
5. **Dashboard Development**

The objective is to provide insights on account ownership, mobile money usage, gender gaps, policy impacts, and forecast future trends, and present them interactively via a dashboard.



## Folder Structure
```
ethiopia-fi-forecast/
│
├─ data/
│ ├─ processed/
│ │ └─ ethiopia_fi_unified_data_enriched.xlsx
│
├─ notebooks/
│ ├─ Task1_Data_Cleaning.ipynb
│ ├─ Task2_Insights.ipynb
│ ├─ Task3_Event_Impact_Modeling.ipynb
│ ├─ Task4_Forecasting.ipynb
│ └─ Task5_Dashboard_Development.ipynb
│
├─ app.py # Streamlit dashboard
├─ requirements.txt
└─ README.md
```

## Setup Instructions

1. **Clone the repository**

```bash
git clone <repo_url>
cd ethiopia-fi-forecast
```
Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```
Run Jupyter notebooks for each task (optional)
```bash
jupyter notebook
```
Run the interactive dashboard
```bash
streamlit run app.py
```
---
Key Insights

Mobile money adoption is high, but traditional account ownership grows slowly.

Gender gaps persist in account ownership and mobile money usage.

Policy and product interventions (Telebirr, Fayda) have measurable effects.

Forecasts show continued growth under optimistic scenarios, but uncertainties remain due to sparse historical data.

---

References

World Bank Global Findex Data

Telebirr, Fayda, Safaricom product launch reports

National financial inclusion reports, Ethiopian financial sector publications

---
Notes

Ensure data/processed/ethiopia_fi_unified_data_enriched.xlsx exists before running notebooks or dashboard.

Dashboard requires Streamlit and Plotly/Matplotlib for interactive plots.

This repository is structured to allow incremental analysis from raw data to forecasts and interactive visualization.
