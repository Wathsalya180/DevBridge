
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.session import get_db

# Create a router for general API endpoints
router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to DevBridge API!",
        "status": "Backend is running"
    }


# Check whether the application can communicate with PostgreSQL
@router.get("/health/database")
def database_health(db: Session = Depends(get_db)):
    try:
        # Execute a simple database query
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
            "message": "PostgreSQL connection successful"
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
                "message": "Database connection failed"
            }
        )
