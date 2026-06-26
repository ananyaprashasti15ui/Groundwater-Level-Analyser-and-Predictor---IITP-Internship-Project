# Groundwater-Level-Analyser-and-Predictor-IITP-Internship Project


> An ML-powered system for analysing historical groundwater trends and forecasting future levels, developed as part of the IITP Internship Project.

---

## Overview

This project analyses 20 years of historical groundwater data and predicts groundwater levels for the next 20 years using multiple Machine Learning algorithms. It is designed to support water resource management, agricultural planning, and environmental policy decisions.

The system integrates data from real-world platforms and government datasets to ensure predictions are grounded in authentic measurements.

---

## Key Features

- **Historical Analysis** — Visualises and analyses groundwater trends over the past 20 years
- **Future Prediction** — Forecasts groundwater levels for the next 20 years
- **Multiple ML Algorithms** — Compares performance across several models to find the best fit
- **Real Dataset Integration** — Uses data sourced from authentic government and environmental platforms
- **Interactive Visualisations** — Plots and graphs for both historical and predicted data
- **Location-based Analysis** — Supports region and station-wise groundwater level tracking

---

## ML Algorithms Used

| Algorithm | Use Case |
|---|---|
| Linear Regression | Baseline trend prediction |
| Random Forest | Non-linear pattern detection |
| Support Vector Machine (SVM) | High-dimensional data handling |
| LSTM (Long Short-Term Memory) | Time-series sequential forecasting |
| XGBoost | High-accuracy ensemble prediction |
| ARIMA / SARIMA | Statistical time-series forecasting |

> Models are evaluated using metrics such as RMSE, MAE, and R-squared Score to select the best performer. 

---

## Dataset Sources

Data has been collected from the following real-world platforms:

- **Central Ground Water Board (CGWB)** — [cgwb.gov.in](https://cgwb.gov.in)
- **India-WRIS (Water Resources Information System)** — [indiawris.gov.in](https://indiawris.gov.in)
- **NASA GRACE Satellite Data** — Groundwater storage anomaly data
- **IMD (India Meteorological Department)** — Rainfall data for correlation
- **data.gov.in** — Open government datasets

> Dataset spans approximately 2004 to 2024 (20 years historical), with predictions extending to 2044.

---

## Tech Stack

- **Language:** Python 3.x
- **ML Libraries:** scikit-learn, TensorFlow / Keras, XGBoost, statsmodels
- **Data Processing:** Pandas, NumPy
- **Visualisation:** Matplotlib, Seaborn, Plotly
- **Notebook Environment:** Jupyter Notebook / Google Colab
- **Version Control:** Git and GitHub

---

## Project Structure

```
Groundwater-Level-Analyser-and-Predictor---IITP-Internship-Project/
|
|-- data/
|   |-- raw/                  # Original datasets from platforms
|   |-- processed/            # Cleaned and preprocessed data
|
|-- notebooks/
|   |-- 01_EDA.ipynb          # Exploratory Data Analysis
|   |-- 02_Preprocessing.ipynb
|   |-- 03_Model_Training.ipynb
|   |-- 04_Prediction_and_Visualisation.ipynb
|
|-- models/
|   |-- saved_models/         # Trained and serialised models
|
|-- outputs/
|   |-- plots/                # Generated charts and graphs
|   |-- predictions/          # Predicted groundwater level CSVs
|
|-- src/
|   |-- preprocess.py
|   |-- train.py
|   |-- predict.py
|
|-- requirements.txt
|-- README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Groundwater-Level-Analyser-and-Predictor---IITP-Internship-Project.git
cd Groundwater-Level-Analyser-and-Predictor---IITP-Internship-Project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Notebooks

Open Jupyter Notebook or upload to Google Colab and run notebooks in order from 01 to 04.

---

## Results

- Achieved strong prediction accuracy across multiple ML models
- LSTM showed the best performance for long-term time-series forecasting
- Historical trends revealed seasonal fluctuations and declining water table levels in several regions
- Predictions up to 2044 highlight potential water stress zones

---

## Internship Details

| Field | Details |
|---|---|
| **Institution** | IIT Patna (IITP) |
| **Project Type** | Internship Project |
| **Domain** | Machine Learning / Environmental Data Science |
| **Focus Area** | Groundwater Level Analysis and Prediction |

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is open-source and available under the [MIT License](LICENSE).


> "Water is the driving force of all nature." — Leonardo da Vinci
