from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.repository import item_repo
from server.models.item_model import ItemsSchema
from server.models.error_model import ErrorResponseModel
from server.models.response_model import ResponseModel

router = APIRouter()

@router.post("/item/", response_description="item data added into the database")
async def items(item: ItemsSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item = await item_repo.add_items(item)
    return ResponseModel(new_item, "item added successfully.")

@router.get("/item/", response_description="items retrieved")
async def items():
    items = await item_repo.get_all_items()
    if items:
        return ResponseModel(items, "items data retrieved successfully")
    return ResponseModel(items,"Empty list returned")

@router.get("/item/{item_name}", response_description="item data retrieved")
async def items(item_name):
    item = await item_repo.get_item_by_name(item_name)
    if item:
        return ResponseModel(item, "item data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "item doesn't exist.")
