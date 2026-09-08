from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.venue import Venue
from app.schemas.venue import VenueCreate, VenueUpdate
from app.services import spatial_service


def list_venues(db: Session, limit: int = 100, offset: int = 0, search: str | None = None) -> list[Venue]:
    q = db.query(Venue).filter(Venue.is_deleted.is_(False))
    if search:
        q = q.filter(Venue.nama.ilike(f"%{search}%"))
    return q.order_by(Venue.nama.asc()).limit(limit).offset(offset).all()


def get_venue_or_404(db: Session, venue_id: str) -> Venue:
    venue = db.query(Venue).filter(Venue.venue_id == venue_id).first()
    if venue is None or venue.is_deleted:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue


def create_venue(db: Session, payload: VenueCreate) -> Venue:
    venue = Venue(**payload.model_dump())
    db.add(venue)
    db.commit()
    db.refresh(venue)
    return spatial_service.assign_znt_to_venue(db, venue)


def update_venue(db: Session, venue_id: str, payload: VenueUpdate) -> Venue:
    venue = get_venue_or_404(db, venue_id)
    old_lat, old_lng = venue.latitude, venue.longitude
    for field, value in payload.model_dump().items():
        setattr(venue, field, value)
    db.commit()
    db.refresh(venue)
    if (venue.latitude, venue.longitude) != (old_lat, old_lng):
        venue = spatial_service.assign_znt_to_venue(db, venue)
    return venue


def delete_venue(db: Session, venue_id: str) -> None:
    venue = get_venue_or_404(db, venue_id)
    venue.is_deleted = True
    db.commit()
