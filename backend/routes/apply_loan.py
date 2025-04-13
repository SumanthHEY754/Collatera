from fastapi import APIRouter
from backend.rule_based_scoring import score_loan_application

router = APIRouter()

@router.post("/apply-loan")
def apply_for_loan(app: dict):
    result = score_loan_application(app)
    return {
        "message": f"Loan application evaluated: {result['decision']}",
        "score": result["score"],
        "tier": result["tier"],
        "decision": result["decision"]
    }