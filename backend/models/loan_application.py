from sqlalchemy import Column, String, Float, Integer
from backend.db.database import Base
import uuid

class LoanApplication(Base):
    __tablename__ = "loan_applications"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    income = Column(Float)
    loan_amount = Column(Float)
    term_months = Column(Integer)
    credit_score = Column(Integer)
    collateral_value = Column(Float)
    employment_status = Column(String)
    score = Column(Integer)
    tier = Column(String)
    decision = Column(String)