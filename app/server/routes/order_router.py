from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.repository import order_repo
from server.models.order_model import OrdersSchema
from server.models.error_model import ErrorResponseModel
from server.models.response_model import ResponseModel

router = APIRouter()

@router.post("/orders/", response_description="order data added into the database")
async def orders(order: OrdersSchema = Body(...)):
    order = jsonable_encoder(order)
    new_order = await order_repo.add_orders(order)
    return ResponseModel(new_order, "order added successfully.")

@router.get("/orders/{order_id}", response_description="order retrieved")
async def orders(order_id):
    items = await order_repo.get_order(order_id)
    if items:
        return ResponseModel(items, "items data retrieved successfully")
    return ResponseModel(items,"Empty list returned")

# @router.get("/{item_name}", response_description="item data retrieved")
# async def items(item_name):
#     item = await order_repo.get_item_by_name(item_name)
#     if item:
#         return ResponseModel(item, "item data retrieved successfully")
#     return ErrorResponseModel("An error occurred.", 404, "item doesn't exist.")
