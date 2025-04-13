from sqlalchemy import Column, String, Float, ForeignKey
from backend.db.database import Base
import uuid
class Asset(Base):
    __tablename__ = "assets"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    asset_type = Column(String)
    details = Column(String)
    value = Column(Float)