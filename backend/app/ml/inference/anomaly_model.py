"""Model 2 (PRD Section 8): Anomaly Detection — Isolation Forest.

Compares estimated PBJT vs actual payment. Falls back to a simple ratio-threshold
rule until the trained Isolation Forest artifact is available (Sprint 9).
"""
from pathlib import Path
from sqlalchemy.orm import Session

from app.models.tax_payment import TaxPayment
from app.core.config import settings
from app.ml.inference.revenue_model import predict_revenue

ARTIFACT_PATH = Path(__file__).parent / "artifacts" / "anomaly_model.joblib"
_model = None


def _load_model():
    global _model
    if _model is None and ARTIFACT_PATH.exists():
        import joblib
        _model = joblib.load(ARTIFACT_PATH)
    return _model


def detect_anomaly(db: Session, venue_id: str) -> dict:
    estimasi_omzet = predict_revenue(db, venue_id)
    estimasi_pbjt = estimasi_omzet * settings.PBJT_TAX_RATE

    latest_payment = (
        db.query(TaxPayment)
        .filter(TaxPayment.venue_id == venue_id)
        .order_by(TaxPayment.periode.desc())
        .first()
    )
    if latest_payment is None:
        return {"venue_id": venue_id, "anomaly_score": None, "risk_category": "tidak ada data pembayaran"}

    ratio = latest_payment.pbjt_pembayaran / estimasi_pbjt if estimasi_pbjt else 0
    # Placeholder rule-based scoring — replace with Isolation Forest output (Sprint 9)
    if ratio >= 0.8:
        category = "normal"
    elif ratio >= 0.5:
        category = "monitoring"
    else:
        category = "high_risk"

    return {
        "venue_id": venue_id,
        "estimasi_pbjt": estimasi_pbjt,
        "pbjt_pembayaran": latest_payment.pbjt_pembayaran,
        "anomaly_score": round(1 - ratio, 4),
        "risk_category": category,
    }
