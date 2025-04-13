from pydantic import BaseModel

class LoanApplicationRequest(BaseModel):
    user_id: str
    income: float
    loan_amount: float
    term_months: int
    credit_score: int
    collateral_value: float
    employment_status: str

class LoanApplicationResponse(LoanApplicationRequest):
    score: int
    tier: str
    decision: str