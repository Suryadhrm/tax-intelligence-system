import uuid
from sqlalchemy import String, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class TaxPayment(Base):
    """PRD table: tax_payment — reported omzet and actual PBJT payment per period (Module 5)."""
    __tablename__ = "tax_payment"

    payment_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str] = mapped_column(String(36), ForeignKey("venues.venue_id"))
    periode: Mapped[str] = mapped_column(Date)
    omzet_laporan: Mapped[float] = mapped_column(Float)
    pbjt_pembayaran: Mapped[float] = mapped_column(Float)
    status_usaha: Mapped[str | None] = mapped_column(String(50), nullable=True)
    tanggal_mulai_usaha: Mapped[str | None] = mapped_column(Date, nullable=True)
    tanggal_tutup_usaha: Mapped[str | None] = mapped_column(Date, nullable=True)  # for future survival analysis
