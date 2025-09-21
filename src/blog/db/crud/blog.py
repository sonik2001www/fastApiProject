from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models


def create_blog(db: Session, blog: schemas.BlogCreate):
    user = db.query(models.User).filter(models.User.id == blog.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {blog.user_id} not found"
        )

    new_blog = models.Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def get_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    old_blog = get_blog(db, blog_id)
    old_blog.title = blog.title
    old_blog.body = blog.body
    db.commit()
    db.refresh(old_blog)
    return old_blog


def patch_blog(db: Session, blog_id: int, blog: schemas.BlogPatch):
    old_blog = get_blog(db, blog_id)
    if blog.title is not None:
        old_blog.title = blog.title
    if blog.body is not None:
        old_blog.body = blog.body
    db.commit()
    db.refresh(old_blog)
    return old_blog


def destroy_blog(db: Session, blog_id: int):
    old_blog = get_blog(db, blog_id)
    db.delete(old_blog)
    db.commit()
