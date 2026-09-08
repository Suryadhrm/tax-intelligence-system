from pydantic import BaseModel, ConfigDict


class AnomalyResultOut(BaseModel):
    venue_id: str
    payment_id: str
    anomaly_score: float
    risk_category: str
    rank: int | None = None
    model_config = ConfigDict(from_attributes=True)
