from pydantic import BaseModel


class SustainabilityResultOut(BaseModel):
    venue_id: str
    sustainability_score: float | None = None
    business_outlook: str | None = None
    trend_direction: str | None = None
    confidence_level: str
    note: str = "Skor bersifat indikatif, bukan jaminan keberlangsungan usaha."

    class Config:
        from_attributes = True
