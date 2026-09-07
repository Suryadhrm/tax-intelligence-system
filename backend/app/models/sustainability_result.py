from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import uuid
class SustainabilityResult(Base):
    __tablename__="sustainability_result"
    id: Mapped[str]=mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str]=mapped_column(String, ForeignKey("venues.id"))
    periode: Mapped[str]=mapped_column(String)
    sustainability_score: Mapped[float]=mapped_column(Numeric(5,2))
    outlook: Mapped[str]=mapped_column(String)  # Positif|Stabil|Waspada
    confidence: Mapped[str]=mapped_column(String)  # tinggi|sedang|rendah
