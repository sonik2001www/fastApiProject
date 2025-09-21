from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..db import crud, schemas, database

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_user(db=db, user_id=user_id)


@router.patch("/{user_id}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK)
def patch_user(user: schemas.UserPatch, user_id: int, db: Session = Depends(database.get_db)):
    return crud.patch_user(db=db, user_id=user_id, user=user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    crud.destroy_user(db=db, user_id=user_id)
