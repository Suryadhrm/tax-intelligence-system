import uuid
from datetime import date, datetime, time
from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class BookingObservation(Base):
    __tablename__ = "booking_observation"

    observation_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    venue_id: Mapped[str] = mapped_column(String(36), ForeignKey("venues.venue_id"))
    observed_at: Mapped[datetime] = mapped_column(DateTime)
    tanggal_booking: Mapped[date] = mapped_column(Date)
    jam_mulai: Mapped[time] = mapped_column(Time)
    court: Mapped[str | None] = mapped_column(String(100), nullable=True)
    harga: Mapped[float] = mapped_column(Float)
    durasi: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status_slot: Mapped[str] = mapped_column(String(50))
    sumber: Mapped[str | None] = mapped_column(String(150), nullable=True)
