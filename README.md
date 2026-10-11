# Demand Forecasting Engine - Iowa Liquor Sales

A robust, end-to-end machine learning and data engineering pipeline built to forecast weekly product volumes using historical sales data (2.8M+ rows). 

## 🚀 Tech Stack
* **Language:** Python
* **Libraries:** CatBoost, XGBoost, Statsmodels, Scikit-learn, Pandas, NumPy
* **Deployment/Integration:** FastAPI
* **Version Control:** Git & GitHub

## 📊 Project Overview
This project models weekly product sales volumes to optimize inventory and demand planning. It features automated feature engineering, temporal modeling, and robust evaluation metrics to handle large-scale retail transaction data.

## ⚙️ Key Features
* **Advanced Modeling:** Utilized gradient boosting frameworks (**CatBoost** and **XGBoost**) alongside time-series stats models.
* **Feature Engineering:** Extracted temporal trends, lagged variables, and rolling aggregates from massive transactional datasets.
* **API Integration:** Exposed the trained forecasting pipeline via **FastAPI** for real-time predictions.

## 📂 Repository Structure
* `app.py` - FastAPI application entry point.
* `main.py` - Core execution and data pipeline script.
* `catboost_model.pkl` - Serialized winning model artifact.
* `notebooks/` - Exploratory data analysis and model training notebooks.
