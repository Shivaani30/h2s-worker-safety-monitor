from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
# STORE THE MOST RECENT SENSOR READING
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

    latest_data = data

    print()
    print("====================================")
    print("DATA RECEIVED FROM ESP32")
    print("====================================")

    print("Worker ID:", data.get("worker_id"))
    print("H2S:", data.get("h2s"))
    print("NH3:", data.get("nh3"))
    print("Temperature:", data.get("temperature"))
    print("Humidity:", data.get("humidity"))
    print(
        "Cumulative Exposure:",
        data.get("cumulative_exposure")
    )
    print("Risk Score:", data.get("risk_score"))
    print("Local Status:", data.get("local_status"))

    print("====================================")

    return {
        "status": "success",
        "message": "Sensor data received"
    }


# ==========================================
# GIVE LATEST DATA TO FRONTEND
# ==========================================

@app.get("/latest")
def get_latest_data():

    return latest_data