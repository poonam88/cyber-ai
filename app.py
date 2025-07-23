import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st
import os

# -----------------------------
# Section 1: Train & Save Model
# -----------------------------

# Only train if .pkl files don't exist
if not os.path.exists("vectorizer.pkl") or not os.path.exists("cyber_alert_model.pkl"):
    st.info("Training model since no .pkl found...")

    # Sample data
    data = {
        'log': [
            "Unauthorized login attempt from 192.168.0.1",
            "File accessed successfully",
            "Malware detected in download",
            "System rebooted normally",
            "Phishing email clicked by user"
        ],
        'alert': [1, 0, 1, 0, 1]
    }

    df = pd.DataFrame(data)

    # Vectorize
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['log'])

    # Model
    model = LogisticRegression()
    model.fit(X, df['alert'])

    # Save model & vectorizer
    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("cyber_alert_model.pkl", "wb") as f:
        pickle.dump(model, f)

# -----------------------------
# Section 2: Load Model Safely
# -----------------------------

try:
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("cyber_alert_model.pkl", "rb") as f:
        model = pickle.load(f)

    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"❌ Model loading failed: {e}")

# -----------------------------
# Section 3: Streamlit UI
# -----------------------------

st.set_page_config(page_title="Cyber Alert Predictor", page_icon="🛡️")

st.title("🛡️ Cyber Alert Log Classifier")

if model_loaded:
    st.success("✅ Model loaded successfully!")

    # User input
    user_log = st.text_area("Enter system log here:", "")

    if st.button("Predict Alert"):
        if user_log.strip() == "":
            st.warning("Please enter a log to classify.")
        else:
            input_vec = vectorizer.transform([user_log])
            prediction = model.predict(input_vec)[0]

            if prediction == 1:
                st.error("🔴 Alert: Suspicious activity detected!")
            else:
                st.success("🟢 Normal activity.")

else:
    st.error("🚫 Could not load model/vectorizer. Please retrain.")

