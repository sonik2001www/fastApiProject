from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ...core.security import hash_password


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)

    new_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def patch_user(db: Session, user_id: int, user: schemas.UserPatch):
    old_user = get_user(db, user_id)

    if user.name is not None:
        old_user.name = user.name
    if user.email is not None:
        old_user.email = user.email
    if user.hashed_password is not None:
        old_user.hashed_password = user.hashed_password

    db.commit()
    db.refresh(old_user)
    return old_user


def destroy_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()
