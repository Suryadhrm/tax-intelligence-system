from sqlalchemy import String, Numeric, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import uuid
class TaxPayment(Base):
    __tablename__="tax_payment"
    id: Mapped[str]=mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str]=mapped_column(String, ForeignKey("venues.id"))
    periode: Mapped[str]=mapped_column(String)
    omzet_laporan: Mapped[float]=mapped_column(Numeric(14,2))
    pbjt_pembayaran: Mapped[float]=mapped_column(Numeric(14,2))
    status_usaha: Mapped[str | None]=mapped_column(String, nullable=True)
