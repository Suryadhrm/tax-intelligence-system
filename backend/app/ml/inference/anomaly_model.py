"""Transparent PBJT screening; indicative, not proof of a violation."""
from sqlalchemy.orm import Session
from app.models.tax_payment import TaxPayment
from app.core.config import settings
from app.ml.inference.revenue_model import predict_revenue


def screen_payment(estimated_pbjt: float, paid_pbjt: float) -> dict:
    gap = max(estimated_pbjt - paid_pbjt, 0)
    ratio = paid_pbjt / estimated_pbjt if estimated_pbjt else 1.0
    score = max(0.0, min(1.0, 1 - ratio))
    category = "normal" if ratio >= 0.8 else "monitoring" if ratio >= 0.5 else "high_risk"
    return {"gap": gap, "payment_ratio": round(ratio, 4), "anomaly_score": round(score, 4), "risk_category": category, "reason": f"PBJT dibayar {ratio:.1%} dari estimasi; gap Rp{gap:,.0f}."}


def detect_anomaly(db: Session, venue_id: str) -> dict:
    estimated_pbjt = predict_revenue(db, venue_id) * settings.PBJT_TAX_RATE
    record = db.query(TaxPayment).filter(TaxPayment.venue_id == venue_id).order_by(TaxPayment.periode.desc()).first()
    if record is None:
        return {"venue_id": venue_id, "anomaly_score": None, "risk_category": "tidak ada data pembayaran", "gap": None, "payment_ratio": None, "reason": "Data PBJT pembayaran belum tersedia."}
    paid = record.pbjt_dibayar
    return {"venue_id": venue_id, "estimasi_pbjt": estimated_pbjt, "pbjt_dibayar": paid, "pbjt_pembayaran": paid, **screen_payment(estimated_pbjt, paid)}
