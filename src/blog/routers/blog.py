from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..db import crud, schemas, database

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)


@router.post("/", response_model=schemas.BlogResponse, status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return crud.create_blog(db=db, blog=blog)


@router.get("/", response_model=list[schemas.BlogResponse])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_blogs(db, skip=skip, limit=limit)


@router.get("/{blog_id}", response_model=schemas.BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(database.get_db)):
    return crud.get_blog(db, blog_id=blog_id)


@router.put("/{blog_id}", response_model=schemas.BlogResponse)
def update_blog(blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(database.get_db)):
    return crud.update_blog(db, blog_id=blog_id, blog=blog)


@router.patch("/{blog_id}", response_model=schemas.BlogResponse)
def patch_blog(blog_id: int, blog: schemas.BlogPatch, db: Session = Depends(database.get_db)):
    return crud.patch_blog(db, blog_id=blog_id, blog=blog)


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(database.get_db)):
    crud.destroy_blog(db, blog_id=blog_id)
