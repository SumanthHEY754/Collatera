from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.models.loan_application import LoanApplication
from backend.schemas.loan_application import LoanApplicationRequest, LoanApplicationResponse
from backend.rule_based_scoring import score_loan_application

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/apply-loan", response_model=LoanApplicationResponse)
def apply_loan(request: LoanApplicationRequest, db: Session = Depends(get_db)):
    result = score_loan_application(request.dict())
    loan_app = LoanApplication(
        **request.dict(),
        score=result["score"],
        tier=result["tier"],
        decision=result["decision"]
    )
    db.add(loan_app)
    db.commit()
    db.refresh(loan_app)
    return loan_app

@router.get("/applications", response_model=list[LoanApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    return db.query(LoanApplication).all()