from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.models.user import User
from backend.schemas.user import UserResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()