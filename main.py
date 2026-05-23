from fastapi import FastAPI
from app.v1.routes.user_routes import router as user_router

app = FastAPI(
    title="HabitFlow API",
    version="1.0.0"
)

app.include_router(user_router, tags=["Users"])


@app.get("/")
def home():
    return {"message": "HabitFlow API está rodando!"}