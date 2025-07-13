# 🔥 Calories Burn Prediction – Machine Learning Regression Project

Predict the number of calories burned using biometric and activity data, powered by ML!

---

## 🧠 Overview

This repository delivers an end-to-end **calories burn prediction system**, built using real-world health and activity data and trained with **supervised ML regression models** such as Random Forest and XGBoost. It’s ideal for fitness apps, personal wellness dashboards, or academic projects.

---

## 📊 Features

- ingested **7 key input features**:  
  `age`, `gender`, `height`, `weight`, `duration`, `heart_rate`, `body_temperature`  
- Extensive **Exploratory Data Analysis** (EDA): distributions, trends, and correlations  
- Applied **feature engineering** and preprocessing techniques  
- **Model training & comparison** using:
  - Linear Regression  
  - Decision Tree Regressor  
  - Random Forest Regressor  
  - XGBoost Regressor  
- Final model deployed using **pickle** for real-time predictions  
- Error metrics like **Mean Absolute Error (MAE)** evaluated on a test split

---

## ⚙️ Why This Project Matters

- Offers **high accuracy** in calorie-burn estimation using just 7 inputs  
- **Lightweight and interpretable** — suitable for mobile or web-based health applications  
- A **great learning resource** for regression modeling, model evaluation, and deployment in Python  
- Structured for adaptation to further use cases like wellness coaching or activity tracking

---

## 📁 Project Structure

```
Calories-Burn-Prediction/
│
├── data/
│ ├── calories.csv ← main dataset containing features and target
│ └── exercise.csv ← supplementary activity dataset (if used)
│
├── notebooks/
│ └── calories_prediction.ipynb ← Jupyter notebook with EDA, preprocessing, feature engineering, and model training
│
├── models/
│ └── rfr.pkl ← Trained Random Forest Regressor model (Pickle file)
│
├── app/
│ ├── calories.py ← Main application file (e.g., Flask or Streamlit)
│ └── requirements.txt ← Project dependencies
│
└── README.md ← This file: project overview, instructions, and results
```

---


### 🔍 Description of Key Folders & Files

- **`data/`**: Source datasets used for model training and testing.
- **`notebooks/`**: Interactive Jupyter notebook demonstrating:
  - Exploratory Data Analysis (EDA)
  - Feature engineering and preprocessing
  - Model building and evaluation
  - Comparison of multiple regression models (Linear, Decision Tree, Random Forest, XGBoost)
- **`models/`**: Stores the final trained machine learning model (`rfr.pkl`) used for predictions.
- **`calories/`**: Contains deployment code:
  - `app.py`: script to load the model and serve predictions (e.g., web UI or command‑line)
  - `requirements.txt`: lists Python packages required to run the app
- **`README.md`**: High-level overview, setup instructions, model performance, and usage examples.

---

### ✅ How to Use This Structure in README

Include a section in your README like this:

```markdown
## 🧾 Repository Structure

See the project organized into folders based on functionality:

- **data/** — raw input datasets (`.csv`)
- **notebooks/** — Jupyter notebook illustrating full workflow from EDA to model building
- **models/** — trained `.pkl` model used for predictions
- **calories/** — application code and dependencies 
- **README.md** — project overview and usage instructions

