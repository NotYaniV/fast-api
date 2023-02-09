from fastapi import FastAPI
from server.routes.item_router import router as item_router
app = FastAPI()

app.include_router(item_router, tags=["Student"], prefix="/item_router")