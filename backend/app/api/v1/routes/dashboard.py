from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.services import dashboard_service
router = APIRouter()
@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return dashboard_service.get_summary(db)
@router.get("/trend/omzet")
def omzet_trend(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return dashboard_service.get_omzet_trend(db)
