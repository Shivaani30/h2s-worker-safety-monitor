# H₂S Worker Safety Monitor

> An AI-powered IoT safety monitoring system designed to detect hazardous Hydrogen Sulfide (H₂S) exposure and provide timely alerts for workers in high-risk environments.

## Overview

Workers in industries such as sewage treatment, oil & gas, wastewater management, and confined-space operations can be exposed to Hydrogen Sulfide (H₂S), a highly hazardous gas that can become dangerous before workers are able to recognize the exposure themselves.

**H₂S Worker Safety Monitor** combines sensor-based environmental monitoring, machine learning, and a real-time web dashboard to identify potentially hazardous conditions and support faster safety intervention.

The system is designed around a simple principle:

> **Sense → Analyze → Assess Risk → Alert**

---

## Key Features

- **H₂S Hazard Monitoring**
  - Continuously monitors environmental H₂S readings.
  - Identifies potentially dangerous exposure conditions.

- **AI-Based Risk Assessment**
  - Uses machine-learning models to classify environmental conditions.
  - Combines sensor readings to estimate worker safety risk.

- **Real-Time Dashboard**
  - Displays incoming worker/environment data.
  - Provides an easy-to-understand safety status.

- 🚨 **Hazard Alerts**
  - Highlights dangerous conditions requiring attention.
  - Designed to support rapid response by supervisors.

- **IoT + Web Architecture**
  - Sensor/device data can be transmitted to the backend.
  - Backend processes and exposes the latest safety information through APIs.

- **Safety Analytics**
  - Enables monitoring of sensor readings and risk trends.
  - Provides a foundation for historical analysis and predictive safety systems.

---

## System Architecture

```text
        ┌───────────────────────┐
        │   Environmental       │
        │      Sensors          │
        │                       │
        │   H₂S / Temperature   │
        │   Humidity / Other    │
        └───────────┬───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   IoT / Edge Device   │
        │                       │
        │  Sensor Acquisition   │
        │  Data Transmission    │
        └───────────┬───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │       FastAPI         │
        │       Backend         │
        │                       │
        │  Data Processing      │
        │  API Endpoints        │
        │  Risk Assessment      │
        └───────────┬───────────┘
                    │
              ┌─────┴─────┐
              ▼           ▼
      ┌─────────────┐ ┌─────────────┐
      │ ML Risk     │ │ Safety Data │
      │ Model       │ │ Processing   │
      └──────┬──────┘ └──────┬──────┘
             │               │
             └───────┬───────┘
                     ▼
          ┌─────────────────────┐
          │   Web Dashboard     │
          │                     │
          │  Risk Status        │
          │  Sensor Readings    │
          │  Alerts             │
          │  Worker Safety      │
          └─────────────────────┘
