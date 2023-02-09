import motor.motor_asyncio

def _get_client():
    MONGO_DETAILS = "mongodb://localhost:27017"
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    return client.restaurant

def get_collection(collection: str):
    client = _get_client()
    return client.get_collection(collection)