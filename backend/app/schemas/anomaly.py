from pydantic import BaseModel


class AnomalyResultOut(BaseModel):
    venue_id: str
    payment_id: str
    anomaly_score: float
    risk_category: str
    rank: int | None = None

    class Config:
        from_attributes = True
