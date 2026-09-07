from sqlalchemy import String, Numeric, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import uuid
class RevenuePrediction(Base):
    __tablename__="revenue_prediction"
    id: Mapped[str]=mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str]=mapped_column(String, ForeignKey("venues.id"))
    periode: Mapped[str]=mapped_column(String)
    omzet_estimasi: Mapped[float]=mapped_column(Numeric(14,2))
    ci_low: Mapped[float | None]=mapped_column(Numeric(14,2), nullable=True)
    ci_high: Mapped[float | None]=mapped_column(Numeric(14,2), nullable=True)
    created_at: Mapped[DateTime]=mapped_column(DateTime, server_default=func.now())
