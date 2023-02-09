from ._client import get_collection
from bson.objectid import ObjectId

def _item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "item_name": item["item_name"],
        "description": item["description"],
        "price": item["price"],
        "quantity": item["quantity"],
        "img": item["img"],
        "tag": item["tag"],
        "type": item["type"],
    }

item_collection = get_collection("item")

async def get_all_items() -> list:
    return [_item_helper(item) async for item in  item_collection.find()]

async def get_item_by_name(item_name: str) -> list:
    item =  await item_collection.find_one({"item_name": item_name})
    if item:
        return _item_helper(item)

async def add_items(item: dict) -> dict:
    item = await item_collection.insert_one(item)
    item = await item_collection.find_one({"_id": item.inserted_id})
    return _item_helper(item)

async def update_item_by_name(item_name: str) -> list:
    pass