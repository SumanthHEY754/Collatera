from pydantic import BaseModel

class LoanBase(BaseModel):
    user_id: str
    amount: float
    term_months: int
    purpose: str

class LoanCreate(LoanBase):
    loan_id: str

class LoanResponse(LoanCreate):
    pass