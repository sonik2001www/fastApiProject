from pydantic import BaseModel


class BlogShort(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        from_attributes = True


class UserShort(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
