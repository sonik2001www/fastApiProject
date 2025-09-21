from pydantic import BaseModel
from typing import Optional
from .common import UserShort


class BlogBase(BaseModel):
    title: str
    body: str


class BlogCreate(BlogBase):
    user_id: int


class BlogUpdate(BlogBase):
    pass


class BlogPatch(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class BlogResponse(BlogBase):
    id: int
    user_id: int
    owner: UserShort

    class Config:
        from_attributes = True
