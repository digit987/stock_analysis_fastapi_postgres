from fastapi import APIRouter, HTTPException
from app.schemas import User, UserCreate
from app import services

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    return await services.create_user(user)

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await services.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=list[User])
async def get_users():
    return await services.get_users()

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    return await services.update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return await services.delete_user(user_id)
