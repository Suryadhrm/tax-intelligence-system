from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.spatial_znt import SpatialZNT
from app.models.venue import Venue


def find_znt_for_coordinates(db: Session, latitude: float, longitude: float) -> SpatialZNT | None:
    """Module 3 — real spatial join: finds the ZNT polygon that contains the given point.

    Uses PostGIS's ST_Contains(polygon, point) — GeoAlchemy2 registers Geometry
    columns so these generic SQL functions can be called via SQLAlchemy's
    func.* namespace directly (no special GeoAlchemy2 wrapper needed here),
    matching the "Spatial Analysis" step described in the PRD.
    """
    point = func.ST_SetSRID(func.ST_MakePoint(longitude, latitude), 4326)
    return (
        db.query(SpatialZNT)
        .filter(func.ST_Contains(SpatialZNT.polygon, point))
        .first()
    )


def assign_znt_to_venue(db: Session, venue: Venue) -> Venue:
    """Runs the spatial join for one venue and persists the resulting znt_id.

    Called automatically on venue create/update (Module 2 <-> Module 3 integration),
    and reusable from the seed script / a bulk "re-run spatial join" admin action.
    """
    znt = find_znt_for_coordinates(db, venue.latitude, venue.longitude)
    venue.znt_id = znt.znt_id if znt else None
    db.commit()
    db.refresh(venue)
    return venue


def assign_znt_for_all_venues(db: Session) -> int:
    """Bulk re-run of the spatial join — e.g. after importing new ZNT polygons."""
    venues = db.query(Venue).filter(Venue.is_deleted.is_(False)).all()
    updated = 0
    for venue in venues:
        znt = find_znt_for_coordinates(db, venue.latitude, venue.longitude)
        new_znt_id = znt.znt_id if znt else None
        if venue.znt_id != new_znt_id:
            venue.znt_id = new_znt_id
            updated += 1
    db.commit()
    return updated


def get_znt_for_venue(db: Session, venue_id: str) -> dict:
    """Module 3 output: ZNT value, wilayah, and a simple derived economic-zone factor."""
    venue = db.query(Venue).filter(Venue.venue_id == venue_id).first()
    if venue is None:
        return {"venue_id": venue_id, "znt_value": None, "wilayah": None, "faktor_ekonomi": "venue tidak ditemukan"}

    znt = db.query(SpatialZNT).filter(SpatialZNT.znt_id == venue.znt_id).first() if venue.znt_id else None
    if not znt:
        return {"venue_id": venue_id, "znt_value": None, "wilayah": None, "faktor_ekonomi": "belum terpetakan"}

    faktor_ekonomi = (
        "premium" if znt.znt_value > 20_000_000 else "menengah" if znt.znt_value > 8_000_000 else "reguler"
    )
    return {
        "venue_id": venue_id,
        "znt_value": znt.znt_value,
        "wilayah": znt.wilayah,
        "faktor_ekonomi": faktor_ekonomi,
    }
