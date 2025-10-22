from fastapi import FastAPI
from recommenders.routers import routes

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Fluc Recommender System API!"}

app.include_router(routes.router, prefix="/api")