from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_blog(db: Session, blog: schemas.BlogCreate):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def destroy_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()


def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    old_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not old_blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    old_blog.title = blog.title
    old_blog.body = blog.body
    db.add(old_blog)
    db.commit()
    db.refresh(old_blog)
    return old_blog


def patch_blog(db: Session, blog_id: int, blog: schemas.BlogPatch):
    old_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not old_blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog.title is not None:
        old_blog.title = blog.title
    if blog.body is not None:
        old_blog.body = blog.body

    db.commit()
    db.refresh(old_blog)
    return old_blog

