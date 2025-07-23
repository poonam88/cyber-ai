import streamlit as st
import pandas as pd
import pickle
import os

st.title("🚨 Cyber Alert Detection AI")

uploaded_file = st.file_uploader("Upload a CSV or TXT file", type=["csv", "txt"])

model_path = "models/cyber_alert_model.pkl"
vectorizer_path = "models/vectorizer.pkl"

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
else:
    st.error("Model files not found!")

def predict_alerts(texts):
    X = vectorizer.transform(texts)
    return model.predict(X)

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        logs = df["log"].dropna().astype(str)
    else:
        logs = pd.Series(uploaded_file.read().decode("utf-8").splitlines())

    predictions = predict_alerts(logs)
    results = pd.DataFrame({"log": logs, "prediction": predictions})

    st.dataframe(results)
    st.download_button("Download Predictions", results.to_csv(index=False), "predictions.csv")
