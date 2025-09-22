from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.config import settings
from ..core.security import verify_password, create_access_token
from ..db.database import get_db
from ..db.schemas.auth import LoginIn, Token
from ..db.crud.user import get_user_by_email

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login", response_model=Token, summary="Login and get JWT")
def login(form: LoginIn, db: Session = Depends(get_db)):
    user = get_user_by_email(db, form.email)
    if not user or not verify_password(form.password, user.hashed_password):

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": str(user.id), "email": user.email},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return Token(access_token=token)
