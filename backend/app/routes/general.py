from fastapi import APIRouter

# Create a router for general API endpoints
router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to DevBridge API!",
        "status": "Backend is running"
    }
    