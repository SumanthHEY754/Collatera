from sqlalchemy import Column, String, Integer, Float, ForeignKey
from backend.db.database import Base
import uuid
class Loan(Base):
    __tablename__ = "loans"
    loan_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    amount = Column(Float)
    term_months = Column(Integer)
    purpose = Column(String)