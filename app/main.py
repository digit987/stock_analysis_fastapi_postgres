from fastapi import FastAPI
from app.database import database, create_tables
from app.routes.users import router as user_router
from app.routes.stocks import router as stock_router

app = FastAPI()

# Routes for user and stock-related endpoints
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(stock_router, prefix="/stocks", tags=["Stocks"])

@app.on_event("startup")
async def startup():
    await database.connect()  # Connecting to the database
    await create_tables()  # Creating the tables asynchronously (if not exists)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()  # Disconnecting from the database on shutdown
