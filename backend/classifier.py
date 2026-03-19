import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample dataset
data = {
    "text": [
        "learn python programming",
        "math lecture algebra",
        "science tutorial",
        "physics class",
        "funny prank video",
        "movie trailer",
        "comedy show",
        "minecraft gameplay",
        "pubg live stream",
        "instagram reels"
    ],
    "category": [
        "education",
        "education",
        "education",
        "education",
        "entertainment",
        "entertainment",
        "entertainment",
        "gaming",
        "gaming",
        "entertainment"
    ]
}

df = pd.DataFrame(data)

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# Train model
model = LogisticRegression()
model.fit(X, df["category"])

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained successfully!")