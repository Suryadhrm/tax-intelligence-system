from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user, require_role
from app.models.user import UserRole, User
from app.models.tax_payment import TaxPayment
from app.schemas.tax import TaxPaymentCreate, TaxPaymentOut
router = APIRouter()
@router.post("", response_model=TaxPaymentOut)
def record_tax_payment(payload: TaxPaymentCreate, db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA))):
    record = TaxPayment(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
@router.get("/{venue_id}", response_model=list[TaxPaymentOut])
def list_tax_payments(venue_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(TaxPayment).filter(TaxPayment.venue_id == venue_id).all()
