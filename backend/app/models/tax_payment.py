import uuid
from datetime import date
from sqlalchemy import Date, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, synonym
from app.db.base import Base


class TaxPayment(Base):
    """PBJT period record; legacy table/attribute names remain API-compatible."""
    __tablename__ = "tax_payment"

    payment_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str] = mapped_column(String(36), ForeignKey("venues.venue_id"))
    nopd: Mapped[str | None] = mapped_column(String(100), nullable=True)
    periode: Mapped[date] = mapped_column(Date)
    omzet_laporan: Mapped[float] = mapped_column(Float)
    dpp_pbjt: Mapped[float | None] = mapped_column(Float, nullable=True)
    tarif_pbjt: Mapped[float | None] = mapped_column(Float, nullable=True)
    pbjt_terutang: Mapped[float | None] = mapped_column(Float, nullable=True)
    pbjt_dibayar: Mapped[float] = mapped_column("pbjt_dibayar", Float, default=0)
    pbjt_pembayaran = synonym("pbjt_dibayar")
    tanggal_lapor: Mapped[date | None] = mapped_column(Date, nullable=True)
    tanggal_bayar: Mapped[date | None] = mapped_column(Date, nullable=True)
    status_pembayaran: Mapped[str | None] = mapped_column(String(50), nullable=True)
    status_usaha: Mapped[str | None] = mapped_column(String(50), nullable=True)
    tanggal_mulai_usaha: Mapped[date | None] = mapped_column(Date, nullable=True)
    tanggal_tutup_usaha: Mapped[date | None] = mapped_column(Date, nullable=True)
