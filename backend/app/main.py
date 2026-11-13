from fastapi import FastAPI
from app.routes import general

# Create the FastAPI application
app = FastAPI(
    title="DevBridge API",
    description="Backend API for the DevBridge platform",
    version="1.0.0"
)

# Connect the general router
app.include_router(general.router)