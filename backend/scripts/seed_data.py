"""Seed the database with a minimal working dataset for local development/demo.

Creates: 2 users (admin + petugas), 3 ZNT zones (Jakarta Barat area, rough
sample polygons), 5 venues (spatial-joined against those zones automatically),
and a few months of tax_payment history for 2 venues so anomaly detection and
sustainability scoring both have something to work with.

Usage (from backend/):
    python -m scripts.seed_data
"""
import datetime
import uuid

from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon

from app.core.security import hash_password
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models.user import User, UserRole
from app.models.spatial_znt import SpatialZNT
from app.models.venue import Venue
from app.models.tax_payment import TaxPayment
from app.services.spatial_service import assign_znt_to_venue


def uid() -> str:
    return str(uuid.uuid4())


# Rough, illustrative bounding boxes around three West Jakarta sub-areas.
# Replace with real ZNT polygons once the actual dataset is available (Sprint 6).
ZNT_ZONES = [
    {"wilayah": "Kebon Jeruk", "znt_value": 25_000_000,
     "bbox": (106.760, -6.195, 106.780, -6.175)},   # premium
    {"wilayah": "Kembangan", "znt_value": 12_000_000,
     "bbox": (106.700, -6.190, 106.720, -6.170)},    # menengah
    {"wilayah": "Cengkareng", "znt_value": 6_000_000,
     "bbox": (106.730, -6.160, 106.750, -6.140)},     # reguler
]

VENUES = [
    {"nama": "Padel House Kebon Jeruk", "lokasi": "Jl. Panjang, Kebon Jeruk",
     "latitude": -6.185, "longitude": 106.770, "jumlah_court": 4,
     "harga_sewa": 250_000, "jam_operasi": "07:00-23:00", "hari_operasi": "Setiap hari"},
    {"nama": "Arena Padel Kembangan", "lokasi": "Jl. Puri Indah, Kembangan",
     "latitude": -6.180, "longitude": 106.710, "jumlah_court": 3,
     "harga_sewa": 200_000, "jam_operasi": "08:00-22:00", "hari_operasi": "Setiap hari"},
    {"nama": "Cengkareng Padel Club", "lokasi": "Jl. Daan Mogot, Cengkareng",
     "latitude": -6.150, "longitude": 106.740, "jumlah_court": 2,
     "harga_sewa": 150_000, "jam_operasi": "09:00-21:00", "hari_operasi": "Senin-Sabtu"},
    {"nama": "Elite Padel Kebon Jeruk 2", "lokasi": "Jl. Kelapa Dua, Kebon Jeruk",
     "latitude": -6.190, "longitude": 106.775, "jumlah_court": 5,
     "harga_sewa": 275_000, "jam_operasi": "06:00-23:00", "hari_operasi": "Setiap hari"},
    {"nama": "Venue di Luar Zona", "lokasi": "Lokasi belum terdata ZNT-nya",
     "latitude": -6.300, "longitude": 106.900, "jumlah_court": 2,
     "harga_sewa": 180_000, "jam_operasi": "08:00-22:00", "hari_operasi": "Setiap hari"},
]


def seed():
    Base.metadata.create_all(bind=engine)  # convenience for quick local demos; Alembic remains the source of truth
    db = SessionLocal()
    try:
        if db.query(User).count() > 0:
            print("Database already seeded — skipping. Delete rows manually to re-seed.")
            return

        # --- Users ---
        admin = User(
            user_id=uid(), full_name="Admin Bappenda", email="admin@bappenda.go.id",
            hashed_password=hash_password("admin123"), role=UserRole.ADMIN_BAPPENDA,
        )
        petugas = User(
            user_id=uid(), full_name="Petugas Pengawasan", email="petugas@bappenda.go.id",
            hashed_password=hash_password("petugas123"), role=UserRole.PETUGAS_PENGAWASAN,
        )
        db.add_all([admin, petugas])
        db.commit()
        print("Seeded users: admin@bappenda.go.id / admin123, petugas@bappenda.go.id / petugas123")

        # --- ZNT zones ---
        znt_records = []
        for zone in ZNT_ZONES:
            minx, miny, maxx, maxy = zone["bbox"]
            polygon = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy), (minx, miny)])
            znt = SpatialZNT(
                znt_id=uid(), wilayah=zone["wilayah"], znt_value=zone["znt_value"],
                polygon=from_shape(polygon, srid=4326),
            )
            db.add(znt)
            znt_records.append(znt)
        db.commit()
        print(f"Seeded {len(znt_records)} ZNT zones")

        # --- Venues (spatial join runs automatically via assign_znt_to_venue) ---
        venue_records = []
        for v in VENUES:
            venue = Venue(venue_id=uid(), is_deleted=False, **v)
            db.add(venue)
            db.commit()
            db.refresh(venue)
            assign_znt_to_venue(db, venue)
            venue_records.append(venue)
            print(f"  - {venue.nama}: znt_id={venue.znt_id or '(tidak masuk zona manapun)'}")

        # --- Tax payment history (for anomaly + sustainability demo) ---
        # Venue 0: healthy/compliant, growing. Venue 1: underreporting (anomaly demo).
        today = datetime.date.today().replace(day=1)
        for i in range(6):
            periode = (today - datetime.timedelta(days=30 * (5 - i))).replace(day=1)

            db.add(TaxPayment(
                payment_id=uid(), venue_id=venue_records[0].venue_id, periode=periode,
                omzet_laporan=40_000_000 + i * 2_000_000,
                pbjt_pembayaran=(40_000_000 + i * 2_000_000) * 0.10,
            ))
            db.add(TaxPayment(
                payment_id=uid(), venue_id=venue_records[1].venue_id, periode=periode,
                omzet_laporan=35_000_000 - i * 1_000_000,
                pbjt_pembayaran=(35_000_000 - i * 1_000_000) * 0.04,  # underreporting -> high_risk
            ))
        db.commit()
        print("Seeded 6 months of tax_payment history for 2 venues")

        print("\nSeed complete.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
