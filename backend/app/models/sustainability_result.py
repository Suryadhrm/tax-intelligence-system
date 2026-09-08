import uuid
from sqlalchemy import String, Float, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import enum


class BusinessOutlook(str, enum.Enum):
    POSITIF = "positif"
    STABIL = "stabil"
    WASPADA = "waspada"


class SustainabilityResult(Base):
    """PRD table: sustainability_result — output of Module 7 (Should Have / prototype).
    Score is indicative only — never interpret as a deterministic survival estimate."""
    __tablename__ = "sustainability_result"

    sustainability_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str] = mapped_column(String(36), ForeignKey("venues.venue_id"))
    sustainability_score: Mapped[float] = mapped_column(Float)
    business_outlook: Mapped[BusinessOutlook] = mapped_column(Enum(BusinessOutlook))
    trend_direction: Mapped[str] = mapped_column(String(20))  # naik / stabil / turun
    confidence_level: Mapped[str] = mapped_column(String(20))  # tinggi / sedang / rendah
