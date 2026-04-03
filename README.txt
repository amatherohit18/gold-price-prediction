
# 🪙 Gold Price Prediction System

## 📌 Overview

This project predicts gold prices using **Machine Learning techniques** and visualizes the results through an interactive dashboard. It combines **data preprocessing, feature engineering, model training, and real-time data integration** to simulate a real-world financial prediction system.

---

## 🚀 Features

* 📊 Data Cleaning & Preprocessing
* 📈 Feature Engineering (Lag Features)
* 🤖 Machine Learning Models:

  * Linear Regression
  * Random Forest
* 📉 Model Evaluation using RMSE
* 📡 Live Gold Price using API
* 📊 Interactive Dashboard using Streamlit
* 📉 Candlestick Chart Visualization
* 🔮 Future Price Prediction

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Plotly
* Streamlit
* yfinance API

---

## 📁 Project Structure

```
gold-project/
│
├── gold.csv                # Dataset
├── preprocessing.py        # Data cleaning & feature engineering
├── model.py                # ML models and predictions
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd gold-project
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python -m streamlit run app.py
```

👉 The app will open in your browser.

---

## 📊 How It Works

1. **Data Loading**

   * Reads gold price dataset (CSV)

2. **Data Cleaning**

   * Handles missing values
   * Converts data types

3. **Feature Engineering**

   * Creates lag features (previous day prices)

4. **Model Training**

   * Trains Linear Regression and Random Forest

5. **Evaluation**

   * Uses RMSE to compare models

6. **Prediction**

   * Predicts future gold prices

7. **Visualization**

   * Displays trends, predictions, and candlestick charts

---

## 📉 Model Evaluation

The models are evaluated using:

* **RMSE (Root Mean Squared Error)**
  Lower RMSE indicates better performance.

---

## 📡 Live Data Integration

The project uses:

* `yfinance` API to fetch **real-time gold prices**

---

## 🖥️ Dashboard Features

* Gold price trend graph
* Candlestick chart
* Model comparison
* Prediction visualization
* Future forecasting

---

## ⚠️ Limitations

* Predictions depend on historical data
* Accuracy may vary with dataset quality
* External factors (inflation, global events) are not included

---

## 🔮 Future Improvements

* Add XGBoost model
* Improve accuracy using hyperparameter tuning
* Integrate more financial indicators
* Deploy on cloud (Streamlit Cloud / AWS)

---

## 👨‍💻 Author

**Rohit Amathe**

---

## ⭐ Conclusion

This project demonstrates how machine learning can be applied to financial time-series data, combining data processing, modeling, and visualization into a single system.

---




Features:
- Data Cleaning & Preprocessing
- Feature Engineering (MA, EMA, Lag)
- ML Models (LR, RF, GB)
- Live Gold Price API
- Candlestick Chart
- Model Comparison
- Future Prediction

Run:
pip install -r requirements.txt
streamlit run app.py
