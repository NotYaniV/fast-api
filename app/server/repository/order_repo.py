from ._client import get_collection
from datetime import datetime

def _order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "items": order["items"],
        "price": order["price"],
        "status": order["status"],
        "date": order["date"]
    }

order_collection = get_collection("order")

async def get_order(order_id) -> list:
    order = await order_collection.find_one({"_id": order_id})
    return _order_helper(order) 

# async def get_item_by_name(item_name: str) -> dict:
#     item =  await item_collection.find_one({"item_name": item_name})
#     if item:
#         return _item_helper(item)

async def add_orders(order: dict) -> dict:
    order["date"] = datetime.now()
    order = await order_collection.insert_one(order)
    order = await order_collection.find_one({"_id": order.inserted_id})
    return _order_helper(order)

# async def update_item_by_name(item_name: str) -> list:
#     pass