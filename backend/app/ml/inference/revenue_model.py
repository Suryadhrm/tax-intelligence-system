"""Transparent September revenue baseline from booking observations."""
from sqlalchemy.orm import Session
from app.models.booking_observation import BookingObservation
from app.models.venue import Venue

SOLD_STATUSES = {"terindikasi_terjual", "sold", "booked"}


def aggregate_booking_revenue(observations) -> float:
    return float(sum(item.harga for item in observations if item.status_slot.lower() in SOLD_STATUSES))


def predict_revenue(db: Session, venue_id: str) -> float:
    if db.query(Venue).filter(Venue.venue_id == venue_id).first() is None:
        raise ValueError(f"Venue {venue_id} not found")
    observations = db.query(BookingObservation).filter(BookingObservation.venue_id == venue_id).all()
    return aggregate_booking_revenue(observations)
