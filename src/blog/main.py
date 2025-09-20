from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette import status

from .db import models, schemas, crud
from .db.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blogs/", response_model=schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db=db, blog=blog)


@app.get("/blogs/", response_model=list[schemas.BlogResponse])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_blogs(db, skip=skip, limit=limit)


@app.delete("/blogs/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(blog_id: int, db: Session = Depends(get_db)):
    return crud.destroy_blog(db, blog_id=blog_id)


@app.put("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def update_blog(blog: schemas.BlogUpdate, blog_id: int, db: Session = Depends(get_db)):
    return crud.update_blog(db, blog_id=blog_id, blog=blog)


@app.patch("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def patch_blog(blog: schemas.BlogPatch, blog_id: int, db: Session = Depends(get_db)):
    return crud.patch_blog(db, blog_id=blog_id, blog=blog)