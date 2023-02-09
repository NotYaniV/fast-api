from pydantic import BaseModel, Field

class ItemsSchema(BaseModel):
    item_name : str = Field(...)
    description : str = None
    price : int = Field(...)
    quantity : int = Field(...)
    img : str = None
    tag : str = Field(...)
    type : str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "item_name": "Food",
                "description": "edible",
                "price": 100,
                "quantity": 1,
                "img": "",
                "tag": "brunch",
                "type": "Indian",
            }
        }