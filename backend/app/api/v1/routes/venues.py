import io

import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import UserRole, User
from app.api.deps import get_current_user, require_role
from app.schemas.venue import VenueCreate, VenueOut, VenueUpdate
from app.services import venue_service

router = APIRouter()
REQUIRED_IMPORT_COLUMNS = ["nama", "lokasi", "latitude", "longitude", "jumlah_court", "harga_sewa", "jam_operasi", "hari_operasi"]
MAX_IMPORT_BYTES = 5 * 1024 * 1024
MAX_IMPORT_ROWS = 10_000


@router.get("", response_model=list[VenueOut])
def list_venues(limit: int = Query(100, ge=1, le=200), offset: int = Query(0, ge=0), search: str | None = Query(None, max_length=200), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return venue_service.list_venues(db, limit=limit, offset=offset, search=search)


@router.post("/import")
async def import_venues(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA))):
    if not file.filename or not file.filename.lower().endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Hanya file .csv atau .xlsx yang didukung.")
    raw = await file.read()
    if len(raw) > MAX_IMPORT_BYTES:
        raise HTTPException(status_code=400, detail="File terlalu besar (max 5MB).")
    if len(raw) == 0:
        raise HTTPException(status_code=400, detail="File kosong.")
    try:
        df = pd.read_excel(io.BytesIO(raw)) if file.filename.lower().endswith(".xlsx") else pd.read_csv(io.BytesIO(raw))
    except Exception:
        raise HTTPException(status_code=400, detail="Gagal membaca file. Periksa format.")
    if len(df) > MAX_IMPORT_ROWS:
        raise HTTPException(status_code=400, detail="Terlalu banyak baris (max 10000).")
    df = df.where(pd.notnull(df), None)
    missing = [c for c in REQUIRED_IMPORT_COLUMNS if c not in df.columns]
    if missing:
        raise HTTPException(status_code=400, detail=f"Kolom wajib hilang: {', '.join(missing)}")
    created, errors = [], []
    for i, row in df.iterrows():
        try:
            venue = venue_service.create_venue(db, VenueCreate(**row.to_dict()))
            created.append(venue.venue_id)
        except ValidationError:
            errors.append({"row": int(i) + 2, "error": "Data baris tidak valid"})
        except SQLAlchemyError:
            db.rollback()
            errors.append({"row": int(i) + 2, "error": "Gagal menyimpan data"})
    return {"imported": len(created), "failed": len(errors), "errors": errors}


@router.post("", response_model=VenueOut)
def create_venue(payload: VenueCreate, db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA))):
    return venue_service.create_venue(db, payload)


@router.put("/{venue_id}", response_model=VenueOut)
def update_venue(venue_id: str, payload: VenueUpdate, db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA))):
    return venue_service.update_venue(db, venue_id, payload)


@router.delete("/{venue_id}")
def delete_venue(venue_id: str, db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN_BAPPENDA))):
    venue_service.delete_venue(db, venue_id)
    return {"status": "deleted", "venue_id": venue_id}
