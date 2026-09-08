from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import require_role
from app.models.user import User, UserRole
from app.ml.inference.sustainability_model import score_sustainability
router = APIRouter()
@router.get("/{venue_id}")
def get_sustainability_result(venue_id: str, db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA, UserRole.PETUGAS_PENGAWASAN))):
    return score_sustainability(db, venue_id)
