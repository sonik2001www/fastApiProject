from fastapi import FastAPI
from .routers import blog, user, auth
from .db.database import engine, Base

app = FastAPI(title="Blog API")

Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

