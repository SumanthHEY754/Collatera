# backend/models/user.py

from sqlalchemy import Column, String, Float
from backend.db.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String)
    email = Column(String)
    income = Column(Float)
    employment_status = Column(String)
