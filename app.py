import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from model import get_results, get_predictions, predict_future, get_live_gold_price
from preprocessing import load_data

st.title("Gold Price Prediction System")

# Load dataset
df = load_data()

# Preview
st.subheader("Dataset Preview")
st.write(df.tail())

# Live price
st.subheader("Live Gold Price")
if st.button("Get Live Price"):
    price = get_live_gold_price()
    st.success(f"Live Gold Price (USD): {price}")

# Trend graph
st.subheader("Gold Price Trend")
st.line_chart(df['Close'])

# Candlestick chart
if all(col in df.columns for col in ['Open','High','Low','Close']):
    st.subheader("Candlestick Chart")
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])
    st.plotly_chart(fig)

# Model comparison
st.subheader("Model Accuracy (RMSE)")
results = get_results()
st.bar_chart(pd.DataFrame(results, index=[0]).T)

# Prediction graph
st.subheader("Actual vs Predicted")
lr_pred, rf_pred, y_test = get_predictions()

plt.figure()
plt.plot(y_test.values, label="Actual")
plt.plot(rf_pred, label="Random Forest")
plt.legend()

st.pyplot(plt)

# Future prediction
st.subheader("Future Prediction")
days = st.slider("Select Days", 1, 30, 7)

if st.button("Predict Future"):
    future = predict_future(days)
    st.write(future)

    plt.figure()
    plt.plot(future, label="Future Prediction")
    plt.legend()
    st.pyplot(plt)