from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user, require_role
from app.models.user import User, UserRole
from app.services import spatial_service
router = APIRouter()
@router.get("/znt/{venue_id}")
def get_znt_for_venue(venue_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return spatial_service.get_znt_for_venue(db, venue_id)
@router.post("/znt/rerun")
def rerun_spatial_join(db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA))):
    return {"status": "ok", "venues_updated": spatial_service.assign_znt_for_all_venues(db)}
