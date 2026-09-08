from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings
from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.ml.inference.revenue_model import predict_revenue
from app.schemas.revenue import PBJTEstimationOut
router = APIRouter()
@router.get("/{venue_id}/estimate", response_model=PBJTEstimationOut)
def estimate_revenue_and_pbjt(venue_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        estimasi_omzet = predict_revenue(db, venue_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    tarif = settings.PBJT_TAX_RATE
    return PBJTEstimationOut(venue_id=venue_id, estimasi_omzet=estimasi_omzet, tarif_pbjt=tarif, estimasi_pbjt=estimasi_omzet * tarif)
