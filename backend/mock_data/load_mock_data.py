import json
import os
import uuid
from backend.db.database import SessionLocal
from backend.models.user import User
from backend.models.loan import Loan
from backend.models.asset import Asset
from backend.models.credit_score import CreditScore

def load_data(model_class, filename, id_field=None):
    session = SessionLocal()
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path) as f:
        data = json.load(f)

    # Clear existing records
    session.query(model_class).delete()
    session.commit()

    for item in data:
        if id_field and id_field in item:
            item.pop(id_field)
        if model_class == Asset and "id" not in item:
            item["id"] = str(uuid.uuid4())
        session.add(model_class(**item))
    session.commit()
    session.close()

if __name__ == "__main__":
    load_data(User, "users.json", "user_id")
    load_data(Loan, "loans.json", "loan_id")
    load_data(CreditScore, "credit_scores.json", "score_id")
    load_data(Asset, "assets.json", "id")