from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    income: float
    employment_status: str

class UserCreate(UserBase):
    user_id: str

class UserResponse(UserCreate):
    pass