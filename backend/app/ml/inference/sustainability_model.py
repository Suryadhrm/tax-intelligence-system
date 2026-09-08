"""Model 3 (PRD Section 8): Business Sustainability — Should Have / prototype.

MVP approach: transparent trend analysis + weighted scoring, not a black-box
forecast. Must never claim a deterministic survival period — see PRD Module 7.
"""
from sqlalchemy.orm import Session

from app.models.tax_payment import TaxPayment

MIN_PERIODS_FOR_SCORING = 3  # minimum historical periods before scoring is attempted


def score_sustainability(db: Session, venue_id: str) -> dict:
    history = (
        db.query(TaxPayment)
        .filter(TaxPayment.venue_id == venue_id)
        .order_by(TaxPayment.periode.asc())
        .all()
    )

    if len(history) < MIN_PERIODS_FOR_SCORING:
        return {
            "venue_id": venue_id,
            "sustainability_score": None,
            "business_outlook": None,
            "trend_direction": None,
            "confidence_level": "rendah",
            "note": "Data belum memadai untuk proyeksi.",
        }

    omzet_series = [h.omzet_laporan for h in history]
    trend = "naik" if omzet_series[-1] > omzet_series[0] else "turun" if omzet_series[-1] < omzet_series[0] else "stabil"

    # Placeholder weighted score — refine with the rule-based approach from PRD Model 3
    growth_ratio = (omzet_series[-1] - omzet_series[0]) / omzet_series[0] if omzet_series[0] else 0
    score = max(0, min(100, 50 + growth_ratio * 100))
    outlook = "positif" if score >= 65 else "stabil" if score >= 40 else "waspada"

    return {
        "venue_id": venue_id,
        "sustainability_score": round(score, 1),
        "business_outlook": outlook,
        "trend_direction": trend,
        "confidence_level": "sedang" if len(history) < 6 else "tinggi",
        "note": "Skor bersifat indikatif berdasarkan tren historis, bukan jaminan keberlangsungan usaha.",
    }
