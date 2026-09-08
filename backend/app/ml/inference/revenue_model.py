"""Model 1 (PRD Section 8): Revenue Prediction — XGBoost Regression.

Loads a trained model artifact (exported from ../../../../ml/training/train_revenue_model.py)
and serves predictions. Falls back to a naive heuristic until a real artifact exists,
so the API stays runnable end-to-end from Sprint 1.
"""
from pathlib import Path
from sqlalchemy.orm import Session

from app.models.venue import Venue

ARTIFACT_PATH = Path(__file__).parent / "artifacts" / "revenue_model.joblib"
_model = None


def _load_model():
    global _model
    if _model is None and ARTIFACT_PATH.exists():
        import joblib
        _model = joblib.load(ARTIFACT_PATH)
    return _model


def predict_revenue(db: Session, venue_id: str) -> float:
    venue = db.query(Venue).filter(Venue.venue_id == venue_id).first()
    if venue is None:
        raise ValueError(f"Venue {venue_id} not found")

    model = _load_model()
    if model is not None:
        features = [[venue.jumlah_court, venue.harga_sewa]]  # extend with ZNT/location features once trained
        return float(model.predict(features)[0])

    # Naive placeholder heuristic (replace once Sprint 8 trains the real model)
    hours_per_week = 12 * 7  # assumed operating hours, refine with jam_operasi parsing
    return venue.jumlah_court * venue.harga_sewa * hours_per_week * 0.5
