from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import os

# ==========================================
# CREATE BACKEND
# ==========================================

app = FastAPI()

# ==========================================
# ALLOW FRONTEND CONNECTIONS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# LOAD ML MODEL
# ==========================================

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "ai",
    "h2s_risk_model.pkl"
)

model = joblib.load(MODEL_PATH)

print("ML model loaded successfully!")

# ==========================================
# STORE MOST RECENT SENSOR READING
# ==========================================

latest_data = {}


# ==========================================
# HOME PAGE
# ==========================================

@app.get("/")
def home():
    return {
        "message": "H2S Monitoring Backend is running"
    }


# ==========================================
# RECEIVE DATA FROM ESP32
# ==========================================

@app.post("/data")
def receive_data(data: dict):

    global latest_data

    # Get sensor values
    h2s = data.get("h2s", 0)
    nh3 = data.get("nh3", 0)
    temperature = data.get("temperature", 0)
    humidity = data.get("humidity", 0)
    cumulative_exposure = data.get("cumulative_exposure", 0)

    # ==========================================
    # ML PREDICTION
    # ==========================================

    features = [[
        h2s,
        nh3,
        temperature,
        humidity,
        cumulative_exposure
    ]]

    prediction = model.predict(features)[0]

    # Get prediction probabilities
    probabilities = model.predict_proba(features)[0]

    classes = model.classes_

    confidence = max(probabilities) * 100

    # ==========================================
    # STORE RESULT
    # ==========================================

    latest_data = {
        **data,
        "risk_status": prediction,
        "ml_confidence": round(confidence, 2)
    }

    # ==========================================
    # PRINT DATA
    # ==========================================

    print()
    print("====================================")
    print("DATA RECEIVED FROM ESP32")
    print("====================================")

    print("Worker ID:", data.get("worker_id"))
    print("H2S:", h2s)
    print("NH3:", nh3)
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Cumulative Exposure:", cumulative_exposure)

    print("------------------------------------")
    print("ML RISK:", prediction)
    print("ML CONFIDENCE:", f"{confidence:.2f}%")
    print("====================================")

    return {
        "status": "success",
        "risk_status": prediction,
        "confidence": round(confidence, 2),
        "message": "Sensor data processed successfully"
    }


# ==========================================
# GIVE LATEST DATA TO FRONTEND
# ==========================================

@app.get("/latest")
def get_latest_data():

    return latest_data