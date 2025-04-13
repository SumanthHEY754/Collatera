# backend/create_tables.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.db.database import engine
from backend.models.user import User
from backend.models.loan import Loan
from backend.models.asset import Asset
from backend.models.credit_score import CreditScore
from backend.models.loan_application import LoanApplication

# Create all tables
User.metadata.create_all(bind=engine)
Loan.metadata.create_all(bind=engine)
Asset.metadata.create_all(bind=engine)
CreditScore.metadata.create_all(bind=engine)
LoanApplication.metadata.create_all(bind=engine)


print("✅ Tables created successfully!")
