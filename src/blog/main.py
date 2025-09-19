from fastapi import FastAPI

from . import schemas
from .db import models
from .db.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/blog")
def index(request: schemas.BlogPost):
    return request
