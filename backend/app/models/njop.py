import uuid
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class NJOP(Base):
    __tablename__ = "njop"

    njop_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nop: Mapped[str] = mapped_column(String(100), index=True)
    venue_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("venues.venue_id"), nullable=True)
    nopd: Mapped[str | None] = mapped_column(String(100), nullable=True)
    tahun_pajak: Mapped[int] = mapped_column(Integer)
    alamat_objek: Mapped[str | None] = mapped_column(String(300), nullable=True)
    luas_bumi: Mapped[float | None] = mapped_column(Float, nullable=True)
    luas_bangunan: Mapped[float | None] = mapped_column(Float, nullable=True)
    njop_bumi_per_m2: Mapped[float | None] = mapped_column(Float, nullable=True)
    njop_bangunan_per_m2: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_njop_bumi: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_njop_bangunan: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_njop: Mapped[float | None] = mapped_column(Float, nullable=True)
    match_status: Mapped[str | None] = mapped_column(String(50), nullable=True)
    match_reason: Mapped[str | None] = mapped_column(String(300), nullable=True)
