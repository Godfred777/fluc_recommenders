from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "Recommender system is operational."}


@router.get("/recommendations")
async def get_recommendations(user_id: int):
    # Placeholder logic for generating recommendations
    recommendations = [f"item_{i}" for i in range(5)]
    return {"user_id": user_id, "recommendations": recommendations}