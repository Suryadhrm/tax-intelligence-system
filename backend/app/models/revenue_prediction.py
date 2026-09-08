import uuid
from sqlalchemy import String, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class RevenuePrediction(Base):
    """PRD table: revenue_prediction — ML output from Module 4 (Revenue Estimation Engine)."""
    __tablename__ = "revenue_prediction"

    prediction_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str] = mapped_column(String(36), ForeignKey("venues.venue_id"))
    periode: Mapped[str] = mapped_column(Date)
    estimasi_omzet: Mapped[float] = mapped_column(Float)
    model_version: Mapped[str] = mapped_column(String(50), default="v1")
