from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.models.loan import Loan
from backend.schemas.loan import LoanResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/loans", response_model=list[LoanResponse])
def get_loans(db: Session = Depends(get_db)):
    return db.query(Loan).all()