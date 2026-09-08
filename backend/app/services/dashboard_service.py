from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.venue import Venue
from app.models.tax_payment import TaxPayment
from app.ml.inference.revenue_model import predict_revenue
from app.ml.inference.anomaly_model import detect_anomaly


def get_summary(db: Session) -> dict:
    """Module 8: aggregate cards for the main dashboard.

    total_venue, total_omzet_potensial and total_pbjt_potensial are computed
    from live estimates (predict_revenue) rather than a cached table, which is
    fine at MVP data volume; jumlah_anomali groups venues by risk category.
    """
    venues = db.query(Venue).filter(Venue.is_deleted.is_(False)).all()

    total_omzet_potensial = 0.0
    risk_counts = {"normal": 0, "monitoring": 0, "high_risk": 0}
    venues_with_payment_history = 0

    for venue in venues:
        estimasi_omzet = predict_revenue(db, venue.venue_id)
        total_omzet_potensial += estimasi_omzet

        anomaly = detect_anomaly(db, venue.venue_id)
        category = anomaly.get("risk_category")
        if category in risk_counts:
            risk_counts[category] += 1
            venues_with_payment_history += 1

    total_pbjt_potensial = total_omzet_potensial * settings.PBJT_TAX_RATE

    return {
        "total_venue": len(venues),
        "total_omzet_potensial": round(total_omzet_potensial, 2),
        "total_pbjt_potensial": round(total_pbjt_potensial, 2),
        "venues_with_payment_history": venues_with_payment_history,
        "distribusi_risiko": risk_counts,
        "jumlah_anomali": risk_counts["monitoring"] + risk_counts["high_risk"],
    }


def get_omzet_trend(db: Session) -> list[dict]:
    """Module 8 chart: total reported omzet per periode, across all venues."""
    rows = (
        db.query(TaxPayment.periode, func.sum(TaxPayment.omzet_laporan).label("total_omzet"))
        .group_by(TaxPayment.periode)
        .order_by(TaxPayment.periode)
        .all()
    )
    return [{"periode": str(periode), "total_omzet": float(total)} for periode, total in rows]
