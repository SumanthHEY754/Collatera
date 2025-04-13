from pydantic import BaseModel

class CreditScoreBase(BaseModel):
    user_id: str
    credit_score: int

class CreditScoreCreate(CreditScoreBase):
    score_id: str

class CreditScoreResponse(CreditScoreCreate):
    pass