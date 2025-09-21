from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str

    class Config:
        from_attributes = True


class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True