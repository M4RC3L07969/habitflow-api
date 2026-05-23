from fastapi import APIRouter
from app.v1.models.user_model import User
from app.v1.schemas.user_schema import UserRequest
from app.v1.helpers.user_helpers import user_construction

router = APIRouter(prefix="/user")

USERS = [
    {
        "id": "d18f973f-1eac-403e-bb89-22e7aeb68379",
        "name": "Marcelo",
        "email": "marcelo@gmail.com",
        "password": "1234",
        "created_at":"2026-05-23"
    },
    {
        "id": "23cb88dd-99a4-4847-8a0f-f3219c69253e",
        "name": "John",
        "email": "john@gmail.com",
        "password": "1234",
        "created_at":"2026-05-23"
    }
]

@router.get("/")
async def get_all_users():
    return USERS

@router.post("/create")
async def create_user(user_request: UserRequest):
    new_user = user_construction(user_request)
    USERS.append(new_user)

    return {
        "message": "Usuário criado com sucesso",
        "user": new_user
    }