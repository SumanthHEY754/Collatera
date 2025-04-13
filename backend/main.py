from fastapi import FastAPI
from backend.routes import users, loans, assets, credit_scores,apply_loan
from backend.routes import loan_application
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import loan_application


app = FastAPI(
    title="Collatera Loan API",
    description="API backend for Collatera loan application and scoring engine.",
    version="0.1.0"
)

# ✅ Health Check
@app.get("/")
def read_root():
    return {"message": "Collatera backend is running 🚀"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only! Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(loan_application.router)

# ✅ Include API Routes
app.include_router(users.router)
app.include_router(loans.router)
app.include_router(assets.router)
app.include_router(credit_scores.router)
app.include_router(apply_loan.router)
app.include_router(loan_application.router)
