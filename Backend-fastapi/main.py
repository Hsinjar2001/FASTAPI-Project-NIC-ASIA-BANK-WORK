from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import dashboard
# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Dashboard API",
    description="FastAPI Backend for Dashboard Application",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:3000",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register router
app.include_router(dashboard.router)


# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Dashboard API with FastAPI",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "metrics": "/api/dashboard/metrics",
            "sales": "/api/dashboard/sales",
            "traffic": "/api/dashboard/traffic"
        }
    }


# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {
        "status": "OK",
        "message": "Dashboard API is running"
    }