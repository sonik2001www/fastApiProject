from pydantic import BaseModel
from typing import Optional


class BlogBase(BaseModel):
    title: str
    body: str


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogPatch(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class BlogResponse(BlogBase):
    id: int

    class Config:
        orm_mode = True


