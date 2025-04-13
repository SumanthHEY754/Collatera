from sqlalchemy import Column, String, Integer, ForeignKey
from backend.db.database import Base
import uuid
class CreditScore(Base):
    __tablename__ = "credit_scores"

    score_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    credit_score = Column(Integer)