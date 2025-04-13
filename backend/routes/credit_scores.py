from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.models.credit_score import CreditScore
from backend.schemas.credit_score import CreditScoreResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/credit-scores", response_model=list[CreditScoreResponse])
def get_credit_scores(db: Session = Depends(get_db)):
    return db.query(CreditScore).all()