import uuid
from sqlalchemy import String, Float, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import enum


class RiskCategory(str, enum.Enum):
    NORMAL = "normal"
    MONITORING = "monitoring"
    HIGH_RISK = "high_risk"


class AnomalyResult(Base):
    """PRD table: anomaly_result — output of Module 6 (Anomaly Detection System)."""
    __tablename__ = "anomaly_result"

    anomaly_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str] = mapped_column(String(36), ForeignKey("venues.venue_id"))
    payment_id: Mapped[str] = mapped_column(String(36), ForeignKey("tax_payment.payment_id"))
    anomaly_score: Mapped[float] = mapped_column(Float)
    risk_category: Mapped[RiskCategory] = mapped_column(Enum(RiskCategory))
    rank: Mapped[int | None] = mapped_column(nullable=True)
