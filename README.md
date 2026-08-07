# Groundwater Level Analyzer and Predictor

Machine Learning-based Groundwater Level Forecasting System

An end-to-end Machine Learning project developed during the IIT Patna Internship Program to analyze historical groundwater data, perform exploratory data analysis, engineer temporal features, and predict future groundwater levels using multiple Machine Learning and Deep Learning models.

---

## Overview

Groundwater is one of the most important freshwater resources and plays a crucial role in agriculture, industry, and domestic consumption. Accurate prediction of groundwater levels enables better water resource planning, sustainable groundwater management, and informed policy decisions.

This project presents a comprehensive Machine Learning pipeline that analyzes historical groundwater observations collected from official Government of India datasets. The workflow includes data preprocessing, exploratory data analysis, feature engineering, model training, model evaluation, and groundwater level forecasting using multiple Machine Learning and Deep Learning algorithms.

The objective of this project is to compare different predictive models and identify the most accurate approach for groundwater level prediction.

---

## Objectives

- Analyze historical groundwater monitoring data.
- Perform Exploratory Data Analysis (EDA).
- Engineer temporal and geographical features.
- Train and compare multiple Machine Learning models.
- Evaluate model performance using standard regression metrics.
- Predict future groundwater levels with high accuracy.

---

## Project Workflow

```
Government Data Sources
        │
        ▼
Data Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Groundwater Level Prediction
```

---

## Dataset Description

The project utilizes historical groundwater monitoring data collected from official Government of India sources.

The dataset contains:

- Groundwater Level
- Observation Station
- State
- District
- Latitude
- Longitude
- Observation Date
- Rainfall Information
- Population Data
- Seasonal Features

Approximately two decades of historical observations were used for analysis and forecasting.

---

## Data Preprocessing

The preprocessing pipeline includes:

- Missing value handling
- Duplicate record removal
- Date-time processing
- Outlier analysis
- Feature scaling
- Train-test splitting
- Feature selection

---

## Exploratory Data Analysis

The following analyses were performed:

- Correlation Matrix
- Monthly Groundwater Distribution
- Latitude Distribution
- Longitude Distribution
- District-wise Groundwater Analysis
- Histograms
- Scatter Plots
- Boxplots

These analyses helped understand spatial, seasonal, and temporal groundwater patterns.

---

## Feature Engineering

The following engineered features were created:

- Lag Features
- Rolling Mean
- Rolling Standard Deviation
- Month
- Season
- Year
- Latitude
- Longitude
- Population-based Features

---

## Machine Learning Models

The following models were implemented and evaluated:

- Random Forest
- XGBoost
- LightGBM
- CatBoost
- LSTM
- Ensemble Model
- Persistence Baseline

---

## Performance Metrics

Models were evaluated using:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score
- Mean Absolute Percentage Error (MAPE)
- Training Time

---

## Results

| Model | RMSE | MAE | R² Score |
|--------|------|------|----------|
| XGBoost | **0.2729** | **0.0895** | **1.0000** |
| LightGBM | 0.2762 | 0.0905 | 1.0000 |
| CatBoost | 0.2766 | 0.0916 | 1.0000 |
| Ensemble | 0.2770 | 0.0883 | 1.0000 |
| Random Forest | 0.2865 | 0.0913 | 1.0000 |
| LSTM | 0.3100 | 0.1004 | 1.0000 |

**Best Performing Model:** XGBoost

---

## Technologies Used

- Python
- Jupyter Notebook
- Visual Studio Code
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- TensorFlow / Keras
- Matplotlib
- Seaborn

---

## Data Sources

The datasets used in this project were obtained from official Government of India portals.

### Central Ground Water Board (CGWB)

Groundwater monitoring reports and groundwater resource data.

https://cgwb.gov.in/

Dynamic Ground Water Resources Report

https://cgwb.gov.in/cgwbpnm/public/uploads/documents/1743584819841710360file.pdf

---

### National Water Informatics Centre (NWIC)

Groundwater telemetry observation data.

https://nwdp.nwic.gov.in/

---

### India Climate & Energy Dashboard (NITI Aayog ICED)

Climate and environmental datasets.

https://iced.niti.gov.in/

---

### Population Dataset

Population statistics collected from publicly available Government of India census data.

---

## Installation

Clone the repository

```bash
git clone https://github.com/ananyaprashasti15ui/Groundwater-Level-Analyser-and-Predictor---IITP-Internship-Project.git
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook

```bash
jupyter notebook
```

---

## Team Members

This project was developed collaboratively during the IIT Patna Internship Program.

| Name | Registration Number | Institution |
|------|---------------------|-------------|
| **Ananya Prashasti** | — | SRM Institute of Science and Technology |
| **Raj Vardhan Jha** | 24190503043 | Central University of Jharkhand |
| **Sawan Ade** | 24013 | Indian Institute of Science Education and Research (IISER), Bhopal |
| **Akshat Ojha** | 24EJCIT019 | Jaipur Engineering College & Research Centre (Foundation) |
| **Akshay Singh** | 24EJCIT021 | Jaipur Engineering College & Research Centre (Foundation) |

---

## Academic Guidance

This project was carried out under the guidance of

**Dr. Rahul Misra**  
Professor  
Indian Institute of Technology (IIT) Patna

---

## Future Scope

Possible future enhancements include:

- Integration of real-time groundwater monitoring data
- Weather and rainfall forecasting integration
- GIS-based groundwater visualization
- Web dashboard using Streamlit
- Mobile application deployment
- Transformer-based deep learning models
- Multi-state groundwater forecasting

---

## Acknowledgements

The team sincerely acknowledges the support and guidance provided by **Dr. Rahul Misra**, Professor, IIT Patna, throughout the internship.

We also thank the following organizations for providing valuable datasets and resources:

- Indian Institute of Technology Patna
- Central Ground Water Board (CGWB)
- National Water Informatics Centre (NWIC)
- NITI Aayog – India Climate & Energy Dashboard (ICED)
- Open Source Python Community

---

## License

This repository is intended for academic, educational, and research purposes.
