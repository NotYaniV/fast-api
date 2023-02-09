from pydantic import BaseModel, Field
from datetime import datetime
class OrderSchema(BaseModel):
    items: list = Field(...)
    price: int = Field(None, gt=0)
    status: str = Field(...)
    date: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "items": ["food","yay"],
                "price": 100,
                "status": "prep",
                "date": datetime.now()
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}