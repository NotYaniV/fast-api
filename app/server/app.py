from fastapi import FastAPI
from server.routes.item_router import router as item_router
from server.routes.order_router import router as order_router
from server.routes.table_router import router as table_router
app = FastAPI()

app.include_router(item_router, tags=["Item"], prefix="/item_router")
app.include_router(order_router, tags=["Order"], prefix="/order_router")
app.include_router(table_router, tags=["Table"], prefix="/table_router")