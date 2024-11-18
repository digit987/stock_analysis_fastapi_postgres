from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Shared fields for User
class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str

# Model for creating a new user
class UserCreate(UserBase):
    pass

# Model for retrieving a user
class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
