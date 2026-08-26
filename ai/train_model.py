import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("ai/h2s_training_data.csv")

# Features
X = data[
    [
        "h2s",
        "nh3",
        "temperature",
        "humidity",
        "cumulative_exposure"
    ]
]

# Target
y = data["risk_status"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

# Train
model.fit(X_train, y_train)

# Test
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("================================")
print("MODEL TRAINING COMPLETE")
print("================================")
print(f"Accuracy: {accuracy * 100:.2f}%")
print()
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "ai/h2s_risk_model.pkl")

print("Model saved as:")
print("ai/h2s_risk_model.pkl")