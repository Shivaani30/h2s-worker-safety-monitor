import numpy as np
import pandas as pd

np.random.seed(42)

rows = []

for _ in range(5000):

    # Simulated sensor values
    h2s = np.random.uniform(0, 100)
    nh3 = np.random.uniform(0, 50)

    temperature = np.random.uniform(20, 40)
    humidity = np.random.uniform(30, 80)

    cumulative_exposure = np.random.uniform(0, 10)

    # H2S trend: negative = falling, positive = rising
    h2s_trend = np.random.uniform(-10, 10)

    # Initial prototype risk logic
    risk_score = (
        0.55 * h2s +
        0.10 * nh3 +
        0.05 * cumulative_exposure +
        0.05 * abs(temperature - 25) +
        0.05 * abs(humidity - 50) +
        0.20 * max(h2s_trend, 0)
    )

    risk_score = min(100, max(0, risk_score))

    if risk_score < 30:
        status = "SAFE"
    elif risk_score < 60:
        status = "WARNING"
    else:
        status = "DANGER"

    rows.append([
        h2s,
        nh3,
        temperature,
        humidity,
        cumulative_exposure,
        h2s_trend,
        risk_score,
        status
    ])

df = pd.DataFrame(rows, columns=[
    "h2s",
    "nh3",
    "temperature",
    "humidity",
    "cumulative_exposure",
    "h2s_trend",
    "risk_score",
    "risk_status"
])

df.to_csv("h2s_training_data.csv", index=False)

print("Dataset generated successfully!")
print("Rows:", len(df))
print()
print(df.head())
print()
print("Status distribution:")
print(df["risk_status"].value_counts())