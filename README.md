# 🌍 Global Fuel Affordability & Price Intelligence System

## 📌 Overview
This project analyzes global fuel prices with respect to income, subsidies, and environmental impact. It combines Data Science and DataOps to deliver automated insights and a live dashboard.

---

## 🎯 Objectives
- Analyze fuel price trends across countries
- Evaluate fuel affordability relative to income
- Study EV adoption and environmental impact
- Build an automated data pipeline (DataOps)

---

## 📊 Dataset
Source: Kaggle – World vs Asia Fuel Prices

Features include:
- Fuel prices (gasoline, diesel, LPG)
- Monthly income
- Fuel affordability index
- Oil dependency
- EV adoption
- CO₂ emissions

---

## 🧹 Data Preprocessing
- Missing value imputation
- Date conversion
- Feature engineering:
  - Fuel Burden
  - Energy Risk Index
  - Green Score
- Normalization

---

## 📈 Exploratory Data Analysis
- Correlation heatmaps
- Affordability vs income analysis
- Subsidy impact study
- EV adoption trends

---

## ⚙️ DataOps Pipeline
Automated pipeline includes:
- Preprocessing
- Feature engineering
- EDA
- Logging

⏱ Scheduled every 3 minutes using Cron

---

## 📊 Dashboard
Built using Streamlit:
- KPIs (Fuel Price, Affordability)
- Graphs
- Pipeline logs

---

## 🤖 Machine Learning
Model: Random Forest Regressor  
Target: Fuel Affordability Index

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn
- Streamlit
- Cron (Scheduling)

---

## 📂 Project Structure  
