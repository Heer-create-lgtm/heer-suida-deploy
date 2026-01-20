"""
UIDAI ML Backend - FastAPI Application

Features:
- Enrollment Forecast: Time-series prediction for enrollment numbers
- Rush Period Analyzer: Predict busiest days and months for centers

PRIVACY SAFEGUARDS:
- Uses ONLY aggregated data from public government APIs
- No individual Aadhaar numbers processed
- All operations on state/district/age-group level
"""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from config import get_settings, OUTPUT_DIR, MODEL_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create output directories
for directory in [OUTPUT_DIR, MODEL_DIR]:
    os.makedirs(directory, exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown events."""
    # Startup
    logger.info("🚀 UIDAI ML Backend starting...")
    settings = get_settings()
    logger.info("📊 ML Backend configured and ready")
    yield
    # Shutdown
    logger.info("👋 UIDAI ML Backend shutting down...")


# Create FastAPI application
app = FastAPI(
    title="UIDAI ML Analytics API",
    description="""
    ML-powered system for Aadhaar enrollment analytics.
    
    ## Features
    - **Enrollment Forecast**: ARIMA-based time-series predictions for enrollment volumes
    - **Rush Period Analyzer**: Predict busiest days and months for enrollment centers
    
    ## Models Used
    - ARIMA/SARIMAX (time-series forecasting)
    - Statistical analysis for peak detection
    
    **Privacy:** Uses only aggregated, anonymized government data.
    """,
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8080",
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8080",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Mount static files for outputs
app.mount("/static", StaticFiles(directory=OUTPUT_DIR), name="static")

# Import and include routers for forecast and rush
from api.routes import forecast, rush

# Forecast API - Time-series enrollment forecasting
app.include_router(forecast.router, tags=["Enrollment Forecasting"])
# Rush Period API - Peak day prediction
app.include_router(rush.router, tags=["Rush Period Prediction"])


@app.get("/")
async def root():
    """Health check and API info"""
    return {
        "status": "healthy",
        "project": "UIDAI ML Analytics API",
        "version": "1.0.0",
        "endpoints": {
            "forecast_train": "/api/forecast/train",
            "forecast_predict": "/api/forecast/predict/{district}",
            "forecast_states": "/api/forecast/states",
            "rush_states": "/api/rush/states",
            "rush_districts": "/api/rush/districts/{state}",
            "rush_analyze": "/api/rush/analyze/{state}/{district}",
            "rush_predict": "/api/rush/predict/{state}/{district}"
        }
    }


@app.get("/health", tags=["System"])
async def health_check():
    """Check if the ML backend is running."""
    return {
        "status": "healthy",
        "service": "UIDAI ML Analytics Backend",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
