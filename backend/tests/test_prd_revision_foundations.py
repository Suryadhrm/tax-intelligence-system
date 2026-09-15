from datetime import date, datetime, time
from pathlib import Path

from app.ml.inference.anomaly_model import screen_payment
from app.ml.inference.revenue_model import aggregate_booking_revenue
from app.ml.inference.sustainability_model import score_snapshot_potential
from app.models.booking_observation import BookingObservation
from app.models.njop import NJOP
from app.models.tax_payment import TaxPayment
from app.models.venue import Venue
from app.schemas.tax import TaxPaymentCreate


ROOT = Path(__file__).resolve().parents[2]


def test_venue_has_nullable_tax_and_jakarta_admin_identity():
    nullable = {"nopd", "nop", "kota_administrasi", "kecamatan", "kelurahan"}
    assert nullable <= set(Venue.__table__.columns.keys())
    assert all(Venue.__table__.columns[name].nullable for name in nullable)


def test_njop_and_booking_observation_models_cover_format_independent_fields():
    assert {"nop", "venue_id", "tahun_pajak", "alamat_objek", "luas_bumi", "luas_bangunan", "njop_bumi_per_m2", "njop_bangunan_per_m2", "total_njop"} <= set(NJOP.__table__.columns.keys())
    assert {"venue_id", "observed_at", "tanggal_booking", "jam_mulai", "court", "harga", "durasi", "status_slot", "sumber"} <= set(BookingObservation.__table__.columns.keys())


def test_tax_schema_distinguishes_liability_payment_and_dates_with_legacy_names():
    record = TaxPaymentCreate(venue_id="v1", periode="2026-09", omzet_laporan=1_000_000, pbjt_pembayaran=80_000, dpp_pbjt=900_000, tarif_pbjt=0.1, pbjt_terutang=90_000, tanggal_lapor=date(2026, 10, 1), tanggal_bayar=date(2026, 10, 2), status_pembayaran="partial")
    assert record.dpp_pbjt == 900_000
    assert record.pbjt_terutang == 90_000
    assert record.pbjt_dibayar == 80_000
    assert {"dpp_pbjt", "tarif_pbjt", "pbjt_terutang", "pbjt_dibayar", "tanggal_lapor", "tanggal_bayar", "status_pembayaran"} <= set(TaxPayment.__table__.columns.keys())


def test_revenue_aggregates_only_indicated_sold_slots():
    observations = [
        BookingObservation(venue_id="v", observed_at=datetime(2026, 9, 1), tanggal_booking=date(2026, 9, 2), jam_mulai=time(9), harga=300_000, status_slot="terindikasi_terjual"),
        BookingObservation(venue_id="v", observed_at=datetime(2026, 9, 1), tanggal_booking=date(2026, 9, 2), jam_mulai=time(10), harga=250_000, status_slot="tersedia"),
    ]
    assert aggregate_booking_revenue(observations) == 300_000


def test_anomaly_screen_is_transparent():
    result = screen_payment(100_000, 40_000)
    assert result == {"gap": 60_000, "payment_ratio": 0.4, "anomaly_score": 0.6, "risk_category": "high_risk", "reason": "PBJT dibayar 40.0% dari estimasi; gap Rp60,000."}


def test_snapshot_index_uses_available_fields_and_low_confidence():
    result = score_snapshot_potential(estimasi_omzet=80_000_000, okupansi=None, pbjt_dibayar=7_000_000, znt_value=None, total_njop=None, jumlah_court=4)
    assert 0 <= result["potential_index"] <= 100
    assert result["potential_category"] in {"rendah", "sedang", "tinggi"}
    assert result["confidence_level"] == "rendah"
    assert result["trend_direction"] is None
    assert result["factors"]


def test_scope_map_and_forward_migration_are_present():
    map_source = (ROOT / "frontend/src/pages/MapPage.jsx").read_text(encoding="utf-8")
    migration = (ROOT / "backend/migrations/versions/0002_dki_snapshot_foundations.py").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "DKI_JAKARTA_CENTER" in map_source and "[-6.2088, 106.8456]" in map_source
    assert 'down_revision = "0001_initial_schema"' in migration
    assert "DKI Jakarta" in readme and "dataset" in readme and "belum tersedia" in readme
