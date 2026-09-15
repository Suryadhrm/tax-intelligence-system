"""Descriptive single-period potential index, not forecasting."""
from sqlalchemy.orm import Session
from app.models.tax_payment import TaxPayment
from app.models.venue import Venue
from app.ml.inference.revenue_model import predict_revenue


def score_snapshot_potential(**values) -> dict:
    components = {
        "estimasi_omzet": min((values.get("estimasi_omzet") or 0) / 100_000_000, 1),
        "okupansi": min(values.get("okupansi") or 0, 1),
        "kepatuhan_pbjt": min((values.get("pbjt_dibayar") or 0) / max((values.get("estimasi_omzet") or 0) * 0.1, 1), 1),
        "kapasitas": min((values.get("jumlah_court") or 0) / 10, 1),
        "znt": min((values.get("znt_value") or 0) / 20_000_000, 1),
        "njop": min((values.get("total_njop") or 0) / 20_000_000_000, 1),
    }
    available = [name for name in components if values.get(name) is not None or name in {"kepatuhan_pbjt", "kapasitas"}]
    score = round(sum(components[name] for name in available) / max(len(available), 1) * 100, 1)
    category = "tinggi" if score >= 67 else "sedang" if score >= 34 else "rendah"
    return {"potential_index": score, "sustainability_score": score, "potential_category": category, "business_outlook": category, "factors": components, "trend_direction": None, "confidence_level": "rendah", "note": "Indeks deskriptif snapshot; bukan prediksi keberlangsungan usaha."}


def score_sustainability(db: Session, venue_id: str) -> dict:
    venue = db.query(Venue).filter(Venue.venue_id == venue_id).first()
    if venue is None:
        raise ValueError(f"Venue {venue_id} not found")
    payment = db.query(TaxPayment).filter(TaxPayment.venue_id == venue_id).order_by(TaxPayment.periode.desc()).first()
    result = score_snapshot_potential(estimasi_omzet=predict_revenue(db, venue_id), okupansi=None, pbjt_dibayar=payment.pbjt_dibayar if payment else None, znt_value=None, total_njop=None, jumlah_court=venue.jumlah_court)
    return {"venue_id": venue_id, **result}
