from fastapi.routing import APIRouter
from ..services.prediction import run_prediction

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "Recommender system is operational."}


@router.get("/recommendations")
async def get_recommendations(user_id: int):
    # Placeholder logic for generating recommendations
    recommendations = await run_prediction()
    return {"user_id": user_id, "recommendations": recommendations}