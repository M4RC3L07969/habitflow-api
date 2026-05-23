from uuid import uuid4
from datetime import date
from app.v1.models.user_model import User
from app.v1.schemas.user_schema import UserRequest
from app.v1.helpers.password_helpers import hash_password


def user_construction(user_request: UserRequest):
    return User(
        id = str(uuid4()),
        name = user_request.name,
        email = user_request.email,
        password_hash = hash_password(user_request.password),
        created_at = date.today()
    )