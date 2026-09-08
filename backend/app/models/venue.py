import uuid
from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Venue(Base):
    """PRD table: venues — master data venue padel (Module 2)."""
    __tablename__ = "venues"

    venue_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nama: Mapped[str] = mapped_column(String(200))
    lokasi: Mapped[str] = mapped_column(String(300))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    jumlah_court: Mapped[int] = mapped_column(Integer)
    harga_sewa: Mapped[float] = mapped_column(Float)
    jam_operasi: Mapped[str] = mapped_column(String(100))
    hari_operasi: Mapped[str] = mapped_column(String(100))
    rating: Mapped[float | None] = mapped_column(Float, nullable=True)
    znt_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("spatial_znt.znt_id"), nullable=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)  # soft-delete for audit trail
