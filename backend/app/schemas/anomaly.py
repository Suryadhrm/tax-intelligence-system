from pydantic import BaseModel, ConfigDict


class AnomalyResultOut(BaseModel):
    venue_id: str
    payment_id: str
    anomaly_score: float
    risk_category: str
    gap: float | None = None
    payment_ratio: float | None = None
    reason: str | None = None
    rank: int | None = None
    model_config = ConfigDict(from_attributes=True)
