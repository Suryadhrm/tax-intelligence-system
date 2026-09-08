"""initial schema — 7 tables from the PRD ERD (Section 11)

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-09-08

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # PostGIS extension must exist before any Geometry column is created.
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")

    op.create_table(
        "users",
        sa.Column("user_id", sa.String(36), primary_key=True),
        sa.Column("full_name", sa.String(150), nullable=False),
        sa.Column("email", sa.String(150), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column(
            "role",
            sa.Enum("admin_bappenda", "petugas_pengawasan", "viewer", name="userrole"),
            nullable=False,
            server_default="viewer",
        ),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default=sa.true()),
    )
    op.create_index("ix_users_email", "users", ["email"])

    op.create_table(
        "spatial_znt",
        sa.Column("znt_id", sa.String(36), primary_key=True),
        sa.Column("wilayah", sa.String(150), nullable=False),
        sa.Column("znt_value", sa.Float, nullable=False),
        sa.Column("polygon", Geometry(geometry_type="POLYGON", srid=4326), nullable=True),
    )

    op.create_index(
        "ix_spatial_znt_polygon_gist",
        "spatial_znt",
        ["polygon"],
        postgresql_using="gist",
    )

    op.create_table(
        "venues",
        sa.Column("venue_id", sa.String(36), primary_key=True),
        sa.Column("nama", sa.String(200), nullable=False),
        sa.Column("lokasi", sa.String(300), nullable=False),
        sa.Column("latitude", sa.Float, nullable=False),
        sa.Column("longitude", sa.Float, nullable=False),
        sa.Column("jumlah_court", sa.Integer, nullable=False),
        sa.Column("harga_sewa", sa.Float, nullable=False),
        sa.Column("jam_operasi", sa.String(100), nullable=False),
        sa.Column("hari_operasi", sa.String(100), nullable=False),
        sa.Column("rating", sa.Float, nullable=True),
        sa.Column("znt_id", sa.String(36), sa.ForeignKey("spatial_znt.znt_id"), nullable=True),
        sa.Column("is_deleted", sa.Boolean, nullable=False, server_default=sa.false()),
    )

    op.create_table(
        "revenue_prediction",
        sa.Column("prediction_id", sa.String(36), primary_key=True),
        sa.Column("venue_id", sa.String(36), sa.ForeignKey("venues.venue_id"), nullable=False),
        sa.Column("periode", sa.Date, nullable=False),
        sa.Column("estimasi_omzet", sa.Float, nullable=False),
        sa.Column("model_version", sa.String(50), nullable=False, server_default="v1"),
    )

    op.create_table(
        "tax_payment",
        sa.Column("payment_id", sa.String(36), primary_key=True),
        sa.Column("venue_id", sa.String(36), sa.ForeignKey("venues.venue_id"), nullable=False),
        sa.Column("periode", sa.Date, nullable=False),
        sa.Column("omzet_laporan", sa.Float, nullable=False),
        sa.Column("pbjt_pembayaran", sa.Float, nullable=False),
        sa.Column("status_usaha", sa.String(50), nullable=True),
        sa.Column("tanggal_mulai_usaha", sa.Date, nullable=True),
        sa.Column("tanggal_tutup_usaha", sa.Date, nullable=True),
    )

    op.create_table(
        "anomaly_result",
        sa.Column("anomaly_id", sa.String(36), primary_key=True),
        sa.Column("venue_id", sa.String(36), sa.ForeignKey("venues.venue_id"), nullable=False),
        sa.Column("payment_id", sa.String(36), sa.ForeignKey("tax_payment.payment_id"), nullable=False),
        sa.Column("anomaly_score", sa.Float, nullable=False),
        sa.Column(
            "risk_category",
            sa.Enum("normal", "monitoring", "high_risk", name="riskcategory"),
            nullable=False,
        ),
        sa.Column("rank", sa.Integer, nullable=True),
    )

    op.create_table(
        "sustainability_result",
        sa.Column("sustainability_id", sa.String(36), primary_key=True),
        sa.Column("venue_id", sa.String(36), sa.ForeignKey("venues.venue_id"), nullable=False),
        sa.Column("sustainability_score", sa.Float, nullable=False),
        sa.Column(
            "business_outlook",
            sa.Enum("positif", "stabil", "waspada", name="businessoutlook"),
            nullable=False,
        ),
        sa.Column("trend_direction", sa.String(20), nullable=False),
        sa.Column("confidence_level", sa.String(20), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("sustainability_result")
    op.drop_table("anomaly_result")
    op.drop_table("tax_payment")
    op.drop_table("revenue_prediction")
    op.drop_table("venues")
    op.drop_index("ix_spatial_znt_polygon_gist", table_name="spatial_znt")
    op.drop_table("spatial_znt")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
    op.execute("DROP TYPE IF EXISTS userrole")
    op.execute("DROP TYPE IF EXISTS riskcategory")
    op.execute("DROP TYPE IF EXISTS businessoutlook")
