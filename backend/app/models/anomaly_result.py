from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import uuid
class AnomalyResult(Base):
    __tablename__="anomaly_result"
    id: Mapped[str]=mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str]=mapped_column(String, ForeignKey("venues.id"))
    payment_id: Mapped[str]=mapped_column(String, ForeignKey("tax_payment.id"))
    anomaly_score: Mapped[float]=mapped_column(Numeric(10,4))
    kategori: Mapped[str]=mapped_column(String)  # Normal|Monitoring|High Risk
    ranking: Mapped[int | None]=mapped_column(Numeric, nullable=True)
