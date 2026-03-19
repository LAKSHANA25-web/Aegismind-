from fastapi import FastAPI
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Create FastAPI app
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AegisMind API Running"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    transformed = vectorizer.transform([text])
    prediction = str(model.predict(transformed)[0])    
    return {"prediction": prediction}