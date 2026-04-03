import numpy as np
import yfinance as yf

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

from preprocessing import load_data, feature_engineering

# Load data
df = load_data()
df = feature_engineering(df)

print("Final dataset:", df.shape)

# 🔥 SAFETY CHECK
if len(df) < 10:
    raise ValueError("Dataset too small after cleaning. Use better dataset.")

# Features
X = df[['Close', 'Lag1', 'Lag2']]
y = df['Close']

# Split
split = int(len(df) * 0.8)

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Model
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Predictions
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

results = {
    "Linear Regression": rmse(y_test, lr_pred),
    "Random Forest": rmse(y_test, rf_pred)
}

def get_results():
    return results

def get_predictions():
    return lr_pred, rf_pred, y_test

def predict_future(days=7):
    last = X.iloc[-1:].copy()
    preds = []

    for _ in range(days):
        pred = rf.predict(last)[0]
        preds.append(pred)
        last['Close'] = pred

    return preds

def get_live_gold_price():
    gold = yf.Ticker("GC=F")
    data = gold.history(period="1d")
    return data['Close'].iloc[-1]