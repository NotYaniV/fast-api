from pydantic import BaseModel, Field
from datetime import datetime
from bson.objectid import ObjectId
class OrdersSchema(BaseModel):
    items: list = Field(...)
    price: int = Field(None, gt=0)
    status: str = Field(...)
    date: datetime = None

    class Config:
        schema_extra = {
            "example": {
                "items": ["food","yay"],
                "price": 100,
                "status": "prep",
                "date": "11-02-2023"
            }
        }