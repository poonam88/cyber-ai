
# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample training data
data = pd.DataFrame({
    'log': [
        "Failed login from 192.168.1.1",
        "Admin access granted to user",
        "Multiple failed logins detected",
        "Normal system operation log",
        "System scan complete"
    ],
    'label': [1, 1, 1, 0, 0]  # 1 = alert, 0 = normal
})

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['log'])
y = data['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save vectorizer and model
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("trained_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model and vectorizer saved.")
