from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user, require_role
from app.models.user import User, UserRole
from app.ml.inference.anomaly_model import detect_anomaly
from app.models.venue import Venue
router = APIRouter()
@router.get("/ranking/high-risk")
def get_high_risk_ranking(limit: int = Query(20, ge=1, le=200), category: str | None = Query(None), db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA, UserRole.PETUGAS_PENGAWASAN))):
    results = []
    for venue in db.query(Venue).filter(Venue.is_deleted.is_(False)).all():
        result = detect_anomaly(db, venue.venue_id)
        if result.get("anomaly_score") is None or (category and result["risk_category"] != category):
            continue
        results.append({"nama": venue.nama, **result})
    results.sort(key=lambda r: r["anomaly_score"], reverse=True)
    for i, result in enumerate(results, 1):
        result["rank"] = i
    return results[:limit]
@router.get("/{venue_id}")
def get_anomaly_result(venue_id: str, db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA, UserRole.PETUGAS_PENGAWASAN))):
    return detect_anomaly(db, venue_id)
