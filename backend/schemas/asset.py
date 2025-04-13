from pydantic import BaseModel

class AssetBase(BaseModel):
    user_id: str
    asset_type: str
    details: str
    value: float

class AssetCreate(AssetBase):
    id: str

class AssetResponse(AssetCreate):
    pass