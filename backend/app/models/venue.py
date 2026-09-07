from sqlalchemy import String, Integer, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import uuid
class Venue(Base):
    __tablename__="venues"
    id: Mapped[str]=mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nama: Mapped[str]=mapped_column(String)
    lokasi: Mapped[str]=mapped_column(String)
    latitude: Mapped[float]=mapped_column(Numeric(10,7))
    longitude: Mapped[float]=mapped_column(Numeric(10,7))
    jumlah_court: Mapped[int]=mapped_column(Integer)
    harga_sewa: Mapped[float]=mapped_column(Numeric(14,2))
    jam_operasi: Mapped[str]=mapped_column(String)
    hari_operasi: Mapped[str]=mapped_column(String)
    znt_id: Mapped[str | None]=mapped_column(String, nullable=True)
    deleted_at: Mapped[DateTime | None]=mapped_column(DateTime, nullable=True)
