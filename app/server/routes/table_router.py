from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.repository import table_repo
from server.models.order_model import TablesSchema
from server.models.error_model import ErrorResponseModel
from server.models.response_model import ResponseModel

router = APIRouter()

@router.post("/tables/", response_description="table data added into the database")
async def tables(table: TablesSchema = Body(...)):
    table = jsonable_encoder(table)
    new_table = await table_repo.add_tables(table)
    return ResponseModel(new_table, "table added successfully.")

# @router.get("/orders/{order_id}", response_description="order retrieved")
# async def orders(order_id):
#     items = await order_repo.get_order(order_id)
#     if items:
#         return ResponseModel(items, "items data retrieved successfully")
#     return ResponseModel(items,"Empty list returned")

# @router.get("/{item_name}", response_description="item data retrieved")
# async def items(item_name):
#     item = await order_repo.get_item_by_name(item_name)
#     if item:
#         return ResponseModel(item, "item data retrieved successfully")
#     return ErrorResponseModel("An error occurred.", 404, "item doesn't exist.")
