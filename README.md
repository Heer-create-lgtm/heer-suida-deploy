# 🇮🇳 UIDAI Aadhaar Analytics Platform

> **A comprehensive ML-powered analytics platform for Aadhaar enrollment data analysis, fraud detection, and demand forecasting**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3-61DAFB.svg)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6.svg)](https://www.typescriptlang.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.4-38B2AC.svg)](https://tailwindcss.com/)

---


## 🧩 Problem Statement

### The Challenge

India's Aadhaar system processes **millions of enrollments daily** across 600+ districts. UIDAI faces critical challenges:

| Challenge | Impact |
|-----------|--------|
| **Unpredictable Demand** | Enrollment centers face overcrowding on certain days while remaining idle on others |
| **Resource Misallocation** | Staff and equipment not optimally distributed across districts |
| **Fraud Detection Gaps** | Manual identification of anomalous enrollment patterns is time-consuming |
| **Reactive Planning** | Decisions based on historical reports rather than predictive insights |
| **Geographic Blind Spots** | Lack of spatial analysis to identify underserved or overburdened regions |

### Our Solution

We built an **AI-powered analytics platform** that transforms raw enrollment data into actionable intelligence:

```
Raw Data → Feature Engineering → ML Models → Predictions → Policy Recommendations
```

**Key Value Propositions:**
- 📅 **Predict rush periods** before they happen (not after)
- 🎯 **Allocate resources** to districts that need them most
- 🚨 **Detect anomalies** automatically using ensemble ML
- 📊 **Visualize trends** through interactive dashboards
- 📋 **Generate policy recommendations** backed by data

---

## 💡 Key Innovations

### 1. Multi-Model Ensemble Architecture
Unlike single-model solutions, we combine **6 different ML algorithms** for robust predictions:
- ARIMA for time-series forecasting
- XGBoost for regression tasks
- Isolation Forest + Autoencoder for anomaly detection
- HDBSCAN for spatial clustering
- Random Forest for risk scoring

### 2. Real-Time Government API Integration
Directly fetches live data from **data.gov.in** - no static datasets. The system stays current automatically.

### 3. Explainable AI (XAI)
Every prediction comes with **SHAP-based explanations** so officials understand *why* the model made a decision.

### 4. Spatial Intelligence with Getis-Ord Gi*
Statistical hotspot detection that identifies **statistically significant clusters** - not just visual heatmaps.

### 5. Festival-Aware Predictions
The Rush Predictor incorporates **Indian festival calendars** to anticipate enrollment spikes during Diwali, Holi, and financial year-end.

### 6. Privacy-First Design
Zero PII processing. Only aggregated, publicly available government data is used.

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Key Innovations](#-key-innovations)
- [Overview](#-overview)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [ML Models](#-ml-models)
- [API Documentation](#-api-documentation)
- [Frontend Features](#-frontend-features)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [Data Sources](#-data-sources)
- [Privacy & Security](#-privacy--security)




---

## 🎯 Overview

This platform is built for the **UIDAI Data Hackathon** to provide intelligent analytics capabilities for Aadhaar enrollment data. The system offers:

- **📊 Enrollment Demand Forecasting** - ARIMA-based time-series predictions for future enrollment demand
- **🚨 Rush Period Prediction** - XGBoost-powered prediction of busiest days and months
- **🔍 Anomaly Detection** - Isolation Forest and Autoencoder-based fraud detection
- **🗺️ Spatial Intelligence** - Hotspot analysis with Getis-Ord Gi* statistics
- **📈 Risk Assessment** - Biometric re-enrollment risk scoring
- **📑 Policy Recommendations** - AI-generated actionable insights for government officials

### Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Model Ensemble** | Combines Random Forest, XGBoost, Isolation Forest, and Autoencoders |
| **Real-Time API Integration** | Live data from data.gov.in government APIs |
| **Interactive Dashboards** | React-based visualizations with Recharts and Leaflet maps |
| **SHAP Explainability** | Human-readable ML model explanations |
| **Geospatial Analysis** | District-level heatmaps and spatial clustering |

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           FRONTEND (React + Vite)                        │
│  ┌─────────────┐ ┌──────────────┐ ┌────────────┐ ┌───────────────────┐   │
│  │  Dashboard  │ │   Hotspots   │ │ Monitoring │ │ Spatial Intel     │   │
│  └─────────────┘ └──────────────┘ └────────────┘ └───────────────────┘   │
│  ┌─────────────┐ ┌──────────────┐ ┌────────────┐ ┌───────────────────┐   │
│  │ Risk Pred.  │ │Gender Tracker│ │  Anomalies │ │ Forecast Dashboard│   │
│  └─────────────┘ └──────────────┘ └────────────┘ └───────────────────┘   │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ HTTP/REST
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      NODE.JS API GATEWAY (Express)                       │
│              Port 3001 - Proxy & Routing Layer                           │
│  ┌────────────────┐  ┌───────────────┐  ┌────────────────────────────┐  │
│  │ /api/enrolment │  │ /api/hotspots │  │ /api/ml → Python Backend   │  │
│  │ /api/forecast  │  │ /api/rush     │  │ /api/biometric             │  │
│  └────────────────┘  └───────────────┘  └────────────────────────────┘  │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ HTTP Proxy
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    PYTHON ML BACKEND (FastAPI)                           │
│                       Port 8000 - ML Engine                              │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                         ML MODELS                                │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐ │    │
│  │  │ ARIMA        │  │ XGBoost      │  │ Isolation Forest       │ │    │
│  │  │ (Forecast)   │  │ (Rush Pred.) │  │ (Anomaly Detection)    │ │    │
│  │  └──────────────┘  └──────────────┘  └────────────────────────┘ │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐ │    │
│  │  │ Autoencoder  │  │ HDBSCAN      │  │ Random Forest/XGBoost  │ │    │
│  │  │ (PyTorch)    │  │ (Clustering) │  │ (Risk Scoring)         │ │    │
│  │  └──────────────┘  └──────────────┘  └────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                        SERVICES                                  │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐ │    │
│  │  │ DataGovClient│  │ FeatureEng.  │  │ ModelSelector          │ │    │
│  │  │ (API Client) │  │ (Pipeline)   │  │ (AutoML)               │ │    │
│  │  └──────────────┘  └──────────────┘  └────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────────────────┘    │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ HTTPS
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        DATA.GOV.IN APIs                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌─────────────────────────┐    │
│  │ Enrolment Data │  │ Demographic    │  │ Biometric Failure Stats │    │
│  │ (by District)  │  │ Statistics     │  │ (by Age Group)          │    │
│  └────────────────┘  └────────────────┘  └─────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠 Technology Stack

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.3 | UI Framework |
| **TypeScript** | 5.8 | Type Safety |
| **Vite** | 5.4 | Build Tool & Dev Server |
| **TailwindCSS** | 3.4 | Styling |
| **Shadcn/UI** | Latest | Component Library |
| **React Router** | 6.30 | Client-side Routing |
| **Recharts** | 2.15 | Data Visualization |
| **Leaflet** | 1.9 | Interactive Maps |
| **React Query** | 5.83 | Server State Management |

### Backend (Node.js Gateway)
| Technology | Version | Purpose |
|------------|---------|---------|
| **Express.js** | Latest | HTTP Server & Routing |
| **Axios** | Latest | HTTP Client (ML Proxy) |
| **CORS** | Latest | Cross-Origin Resource Sharing |
| **dotenv** | Latest | Environment Configuration |

### ML Backend (Python)
| Technology | Version | Purpose |
|------------|---------|---------|
| **FastAPI** | 0.109 | REST API Framework |
| **Uvicorn** | 0.27 | ASGI Server |
| **Pandas** | 2.2 | Data Processing |
| **NumPy** | 1.26 | Numerical Computing |
| **Scikit-learn** | 1.4 | ML Algorithms |
| **XGBoost** | 2.0 | Gradient Boosting |
| **PyTorch** | 2.2 | Deep Learning |
| **Statsmodels** | Latest | ARIMA Time Series |
| **SHAP** | 0.44 | Model Explainability |
| **HDBSCAN** | 0.8 | Density Clustering |
| **GeoPandas** | 0.14 | Geospatial Analysis |
| **Plotly** | 5.18 | Interactive Visualizations |
| **Folium** | 0.15 | Choropleth Maps |

---

## 📁 Project Structure

```
heer-suidai/
├── 📂 src/                          # Frontend React Application
│   ├── 📂 components/               # Reusable UI Components (55 files)
│   │   ├── ui/                      # Shadcn UI primitives
│   │   ├── dashboard/               # Dashboard-specific components
│   │   └── ...
│   ├── 📂 pages/                    # Main Application Pages
│   │   ├── Dashboard.tsx            # Main analytics dashboard
│   │   ├── Hotspots.tsx             # Enrollment hotspot analysis
│   │   ├── Monitoring.tsx           # Real-time monitoring
│   │   ├── RiskPredictor.tsx        # Risk prediction interface
│   │   ├── SpatialIntelligence.tsx  # Geospatial analysis
│   │   ├── GenderTracker.tsx        # Gender distribution tracking
│   │   └── Anomalies.tsx            # Anomaly detection dashboard
│   ├── 📂 hooks/                    # Custom React Hooks
│   ├── 📂 services/                 # API Client Services
│   ├── App.tsx                      # Main Application Component
│   └── main.tsx                     # Application Entry Point
│
├── 📂 server/                       # Node.js API Gateway
│   ├── index.js                     # Express server entry
│   ├── 📂 routes/                   # API Route Handlers
│   │   ├── enrolment.js             # Enrollment data routes
│   │   ├── demographic.js           # Demographic statistics
│   │   ├── biometric.js             # Biometric failure routes
│   │   ├── hotspots.js              # Spatial analysis endpoints
│   │   ├── ai.js                    # AI/ML integration routes
│   │   └── dashboard.js             # Dashboard data aggregation
│   ├── 📂 services/                 # Business Logic Services
│   └── 📂 public/                   # Static Files
│       ├── forecast-dashboard.html  # ARIMA forecast UI
│       └── rush-dashboard.html      # Rush period prediction UI
│
├── 📂 ml_backend/                   # Python ML Engine
│   ├── main.py                      # FastAPI application entry
│   ├── config.py                    # Configuration & constants
│   ├── requirements.txt             # Python dependencies
│   │
│   ├── 📂 models/                   # ML Model Implementations
│   │   ├── forecast.py              # ARIMA enrollment forecaster
│   │   ├── rush_predictor.py        # XGBoost rush period predictor
│   │   ├── isolation_forest.py      # Anomaly detection model
│   │   ├── autoencoder.py           # PyTorch autoencoder
│   │   ├── autoencoder_detector.py  # Full autoencoder pipeline
│   │   ├── ensemble.py              # Model ensemble manager
│   │   ├── clustering.py            # HDBSCAN spatial clustering
│   │   ├── supervised.py            # Supervised classifiers
│   │   └── unsupervised.py          # Unsupervised learners
│   │
│   ├── 📂 api/                      # API Layer
│   │   ├── schemas.py               # Pydantic data models
│   │   └── 📂 routes/               # FastAPI Routers
│   │       ├── forecast.py          # /api/forecast endpoints
│   │       ├── rush.py              # /api/rush endpoints
│   │       ├── analysis.py          # /api/analyze endpoints
│   │       ├── monitor.py           # Monitoring APIs
│   │       ├── policy_api.py        # Policy engine APIs
│   │       └── xai_endpoints.py     # Explainability APIs
│   │
│   ├── 📂 services/                 # Core Services
│   │   ├── data_gov_client.py       # data.gov.in API client
│   │   ├── feature_engineering.py   # Feature extraction pipeline
│   │   └── model_selector.py        # AutoML model selection
│   │
│   ├── 📂 visualization/            # Chart Generation
│   ├── 📂 explainability/           # SHAP & XAI modules
│   ├── 📂 policy/                   # Policy recommendation engine
│   ├── 📂 outputs/                  # Generated visualizations
│   └── 📂 data/                     # Data processing utilities
│
├── 📂 public/                       # Static Assets
├── package.json                     # Frontend dependencies
├── vite.config.ts                   # Vite configuration
├── tailwind.config.ts               # Tailwind configuration
└── tsconfig.json                    # TypeScript configuration
```

---

## 🤖 ML Models

### 1. ARIMA Enrollment Forecaster

**File:** `ml_backend/models/forecast.py`

**Purpose:** Predicts future enrollment demand at district and state levels using time-series analysis.

**Algorithm:** ARIMA (AutoRegressive Integrated Moving Average)

```python
class EnrollmentForecaster:
    """
    ARIMA-based time-series forecaster for district-level enrollment predictions.
    """
    def prepare_time_series(df: pd.DataFrame) -> Dict[str, pd.Series]
    def train_arima(district_series, order=(1,1,1), max_districts=50)
    def forecast(district: str, periods: int = 6, confidence_level: float = 0.95)
    def train_state_models(state_series, order=(1,1,1))
    def forecast_all_states(periods: int = 6, confidence_level: float = 0.95)
```

**Key Features:**
- Automatic stationarity testing using ADF (Augmented Dickey-Fuller) test
- Configurable ARIMA order (p, d, q) with intelligent defaults
- Confidence intervals for predictions
- State-level aggregation from district data
- Model versioning and backtesting metrics

---

### 2. Rush Period Predictor

**File:** `ml_backend/models/rush_predictor.py`

**Purpose:** Predicts the busiest days and months for enrollment centers to optimize resource allocation.

**Algorithm:** XGBoost Regression with temporal feature engineering

```python
class RushPredictor:
    """
    Predicts busiest days and months for enrollment centers by district.
    """
    FESTIVAL_MONTHS = {1: 0.1, 3: 0.15, 4: 0.1, ...}  # Holiday weights
    
    def extract_temporal_features(df: pd.DataFrame) -> pd.DataFrame
    def add_lag_features(df: pd.DataFrame, district: str) -> pd.DataFrame
    def train_district_model(df, state: str, district: str)
    def analyze_patterns(df, state: str, district: str)
    def predict_peak_days(state: str, district: str, days_ahead: int = 30)
```

**Features Extracted:**
- **Day of Week** (0-6) with cyclical encoding
- **Month** (1-12) with cyclical encoding
- **Quarter** (1-4)
- **Week of Year** (1-52)
- **Is Weekend** (binary)
- **Is Month Start/End** (binary)
- **Festival Period Weights**
- **Lag Features** (7-day, 14-day, 30-day)
- **Rolling Statistics** (7-day mean, variance)

---

### 3. Isolation Forest Anomaly Detector

**File:** `ml_backend/models/isolation_forest.py`

**Purpose:** Detects fraudulent or anomalous enrollment patterns using unsupervised learning.

**Algorithm:** Isolation Forest

**Key Parameters:**
- `n_estimators`: 100
- `contamination`: 0.05 (expected fraud rate)
- `random_state`: 42

**Features Used:**
- Enrollment counts by age group
- Geographic concentration metrics
- Temporal patterns (time of day, day of week)
- Deviation from historical averages

---

### 4. PyTorch Autoencoder

**File:** `ml_backend/models/autoencoder.py` & `autoencoder_detector.py`

**Purpose:** Deep learning-based anomaly detection using reconstruction error.

**Architecture:**
```
Input → Encoder → Latent Space → Decoder → Reconstruction
  ↓         ↓           ↓            ↓           ↓
 N dims  Dense(64)  Dense(32)   Dense(64)     N dims
```

**Training:**
- Loss Function: MSE (Mean Squared Error)
- Optimizer: Adam
- Anomaly Threshold: Mean + 2*Std of reconstruction error

---

### 5. HDBSCAN Spatial Clustering

**File:** `ml_backend/models/clustering.py`

**Purpose:** Identifies geographic clusters of high/low enrollment activity.

**Algorithm:** HDBSCAN (Hierarchical Density-Based Spatial Clustering)

**Advantages:**
- No need to specify number of clusters
- Handles noise/outliers automatically
- Works well with spatial data

---

### 6. Ensemble Detector

**File:** `ml_backend/models/ensemble.py` & `ensemble_detector.py`

**Purpose:** Combines multiple models for robust fraud detection.

**Ensemble Strategy:**
1. Isolation Forest Score (weight: 0.3)
2. Autoencoder Reconstruction Error (weight: 0.3)
3. XGBoost Classifier Score (weight: 0.4)

**Final Score:** Weighted average with configurable thresholds

---

## 🔌 API Documentation

### Node.js Gateway Endpoints (Port 3001)

#### Health Check
```http
GET /api/health
```

#### Enrollment Data
```http
GET /api/enrolment
GET /api/enrolment?state=Maharashtra&district=Mumbai
```

#### Demographic Statistics
```http
GET /api/demographic
GET /api/demographic?state=Delhi
```

#### Biometric Failure Data
```http
GET /api/biometric
```

#### Hotspots & Spatial Analysis
```http
GET /api/hotspots/spatial
GET /api/hotspots/districts/{state}
```

#### Forecast Endpoints (Proxied to ML Backend)
```http
GET  /api/forecast/districts          # List available districts
GET  /api/forecast/predict/{district} # Get forecast for district
POST /api/forecast/train              # Train models
GET  /api/forecast/states             # List available states
GET  /api/forecast/predict/state/{state}
GET  /api/forecast/predict-all-states
```

#### Rush Period Endpoints
```http
GET /api/rush/states
GET /api/rush/districts/{state}
GET /api/rush/analyze/{state}/{district}
GET /api/rush/predict/{state}/{district}?days=30
```

---

### Python ML Backend Endpoints (Port 8000)

#### Root & Health
```http
GET /                                 # API info
GET /health                           # Health check
```

#### Dataset APIs
```http
GET  /api/ml/datasets                 # List available datasets
POST /api/ml/select-dataset           # Select dataset for analysis
GET  /api/ml/datasets/{dataset_key}   # Fetch specific dataset
```

#### Analysis APIs
```http
POST /api/ml/analyze                  # Run analysis on selected data
POST /api/ml/train-model              # Train ML model
GET  /api/ml/risk-summary             # Get risk assessment summary
```

#### Model APIs
```http
GET  /api/ml/explain-model            # SHAP explanations
GET  /api/ml/visualizations           # Generated charts
```

#### Forecast APIs
```http
POST /api/forecast/train              # Train ARIMA models
GET  /api/forecast/districts          # Available districts
GET  /api/forecast/predict/{district} # District forecast
POST /api/forecast/train/states       # Train state models
GET  /api/forecast/states             # Available states
GET  /api/forecast/predict/state/{state}
GET  /api/forecast/predict-all-states
```

#### Rush Period APIs
```http
GET /api/rush/states
GET /api/rush/districts/{state}
GET /api/rush/analyze/{state}/{district}
GET /api/rush/predict/{state}/{district}
```

#### Monitoring & Policy APIs
```http
GET  /api/monitor/status              # System status
GET  /api/policy/recommendations      # AI policy recommendations
POST /api/policy/thresholds           # Update alert thresholds
```

---

## 💻 Frontend Features

### 1. Dashboard (`/`)
- **Overview Statistics:** Total enrollments, processing rates, success metrics
- **Real-time Charts:** Enrollment trends, age-group distributions
- **Quick Actions:** Navigate to detailed analysis views

### 2. Hotspots (`/hotspots`)
- **Interactive Map:** Leaflet-based choropleth of India
- **Getis-Ord Gi* Statistics:** Statistically significant hotspots
- **District Drill-down:** Click for detailed statistics

### 3. Spatial Intelligence (`/spatial-intelligence`)
- **Advanced Geospatial Analysis**
- **Temporal Heatmaps:** Time-based enrollment patterns
- **Cluster Visualization:** HDBSCAN results on map

### 4. Risk Predictor (`/risk-predictor`)
- **Biometric Failure Risk Scoring**
- **Feature Importance Visualization**
- **SHAP Explanations:** Per-prediction explanations

### 5. Monitoring (`/monitoring`)
- **Real-time System Health**
- **API Response Times**
- **Model Performance Metrics**

### 6. Anomalies (`/anomalies`)
- **Fraud Detection Dashboard**
- **Anomaly Timelines**
- **Alert Management**

### 7. Gender Tracker (`/gender-tracker`)
- **Gender Distribution Analysis**
- **State-wise Comparisons**
- **Trend Analysis**

### 8. Forecast Dashboard (`/forecast-dashboard`)
- **ARIMA Predictions Visualization**
- **Confidence Intervals**
- **Historical vs Predicted Comparison**

### 9. Rush Dashboard (`/rush-dashboard`)
- **Peak Day Predictions**
- **Monthly Rush Patterns**
- **Staff Allocation Recommendations**

---

## 🚀 Installation & Setup

### Prerequisites
- **Node.js** (v18+ recommended)
- **Python** (3.10+)
- **npm** or **bun** package manager

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/heer-suidai.git
cd heer-suidai
```

### 2. Frontend Setup
```bash
# Install dependencies
npm install

# Or using bun
bun install
```

### 3. Node.js Backend Setup
```bash
cd server
npm install

# Create environment file
cp .env.example .env
# Edit .env with your configuration
```

### 4. Python ML Backend Setup
```bash
cd ml_backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your DATA_GOV_API_KEY
```

### Environment Variables

#### `server/.env`
```env
PORT=3001
ML_BACKEND_URL=http://localhost:8000
DATA_GOV_API_KEY=your_api_key_here
```

#### `ml_backend/.env`
```env
HOST=0.0.0.0
PORT=8000
DEBUG=true
DATA_GOV_API_KEY=your_api_key_here
DATA_GOV_BASE_URL=https://api.data.gov.in/resource
```

---

## ▶️ Running the Application

### Option 1: Run All Services Manually

**Terminal 1 - Frontend (Vite Dev Server)**
```bash
npm run dev
# Frontend runs at http://localhost:5173
```

**Terminal 2 - Node.js Backend**
```bash
cd server
node index.js
# Backend runs at http://localhost:3001
```

**Terminal 3 - Python ML Backend**
```bash
cd ml_backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
# ML Backend runs at http://localhost:8000
```

### Option 2: Using Makefile (ML Backend)
```bash
cd ml_backend
make run        # Start server
make test       # Run tests
make lint       # Code linting
```

### Access Points

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | React Application |
| Node.js Gateway | http://localhost:3001 | API Gateway |
| ML Backend | http://localhost:8000 | FastAPI ML Engine |
| API Docs | http://localhost:8000/docs | Swagger UI |
| Forecast Dashboard | http://localhost:3001/forecast-dashboard | ARIMA Predictions |
| Rush Dashboard | http://localhost:3001/rush-dashboard | Peak Day Analysis |

---

## 📊 Data Sources

The platform fetches data from official **data.gov.in** APIs:

| Dataset | Resource ID | Description |
|---------|-------------|-------------|
| **Enrolment Data** | `83bc24dc-7e4e-4c30-b3e1-b5a0f0f37d3c` | District-wise enrollment statistics by age group |
| **Demographic Stats** | `9b946eb3-0a58-4d1c-be0c-f14db7b7bb51` | State-wise demographic distribution |
| **Biometric Failures** | `a1b5da68-ec50-4ac8-b48d-c15df82e5c2c` | Authentication failure rates by category |

**Data Fields Available:**
- `state`, `district`
- `age_0_5`, `age_5_17`, `age_18_greater`
- `date` (temporal grouping)
- `total_enrolment`
- `biometric_failure_rate`

---

## 🔒 Privacy & Security

> **IMPORTANT:** This platform is designed with privacy as a core principle.

### Privacy Safeguards

1. **No PII Processing**
   - Never processes individual Aadhaar numbers
   - All data is aggregated at state/district level
   - Only uses publicly available government statistics

2. **Aggregated Data Only**
   - Minimum aggregation: District + Age Group + Month
   - No individual-level records are stored or processed

3. **Data Source Transparency**
   - All data comes from official data.gov.in APIs
   - API keys are securely managed via environment variables

4. **No Data Persistence**
   - Raw data is fetched on-demand
   - Only trained models are persisted (no training data)

---