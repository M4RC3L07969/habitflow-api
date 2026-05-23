from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
    
class UserRequest(BaseModel):
    id: Optional[str] = None
    name: str = Field(min_length=3, max_length=30)
    email: str = Field(min_length=13)
    password: str
    created_at: Optional[date] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Peter",
                "email": "peter@gmail.com",
                "password": "1234"
            }
        }
    }

class UserResponse:
    id: str
    name: str
    email: str
    created_at: date