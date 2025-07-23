# 🚨 Cyber Alert Detection AI

A simple Streamlit app to classify log entries as **Cyber Alert** or **Not Alert** using a trained machine learning model.

## 💡 Features

- Upload `.csv` or `.txt` log files
- Predict cyber alerts using a trained classifier
- Download results as CSV
- Visual summary (bar chart)
- Logging predictions for future audits
- Deployable via Hugging Face Spaces

## 📂 Input Format

- **CSV**: Should contain a column named `log`
- **TXT**: Each line should be a separate log

## 🛠️ How to Use

1. Upload a `.csv` or `.txt` log file
2. Wait for predictions
3. View & download the result
4. Visualize prediction summary

## 🚀 Built With

- Python
- Streamlit
- scikit-learn
- Hugging Face Spaces

---

👉 **Model Location**: `models/cyber_alert_model.pkl`  
👉 **Vectorizer**: `models/vectorizer.pkl`
