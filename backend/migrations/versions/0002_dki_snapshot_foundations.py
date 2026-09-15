"""DKI Jakarta snapshot-analysis foundations.

Revision ID: 0002_dki_snapshot_foundations
Revises: 0001_initial_schema
"""
from alembic import op
import sqlalchemy as sa

revision = "0002_dki_snapshot_foundations"
down_revision = "0001_initial_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    for name in ("nopd", "nop", "kota_administrasi", "kecamatan", "kelurahan"):
        op.add_column("venues", sa.Column(name, sa.String(100), nullable=True))

    op.alter_column("tax_payment", "pbjt_pembayaran", new_column_name="pbjt_dibayar")
    op.add_column("tax_payment", sa.Column("nopd", sa.String(100), nullable=True))
    op.add_column("tax_payment", sa.Column("dpp_pbjt", sa.Float(), nullable=True))
    op.add_column("tax_payment", sa.Column("tarif_pbjt", sa.Float(), nullable=True))
    op.add_column("tax_payment", sa.Column("pbjt_terutang", sa.Float(), nullable=True))
    op.add_column("tax_payment", sa.Column("tanggal_lapor", sa.Date(), nullable=True))
    op.add_column("tax_payment", sa.Column("tanggal_bayar", sa.Date(), nullable=True))
    op.add_column("tax_payment", sa.Column("status_pembayaran", sa.String(50), nullable=True))

    op.add_column("anomaly_result", sa.Column("gap", sa.Float(), nullable=True))
    op.add_column("anomaly_result", sa.Column("payment_ratio", sa.Float(), nullable=True))
    op.add_column("anomaly_result", sa.Column("reason", sa.String(300), nullable=True))

    op.create_table("njop",
        sa.Column("njop_id", sa.String(36), primary_key=True), sa.Column("nop", sa.String(100), nullable=False),
        sa.Column("venue_id", sa.String(36), sa.ForeignKey("venues.venue_id"), nullable=True), sa.Column("nopd", sa.String(100), nullable=True),
        sa.Column("tahun_pajak", sa.Integer(), nullable=False), sa.Column("alamat_objek", sa.String(300), nullable=True),
        sa.Column("luas_bumi", sa.Float(), nullable=True), sa.Column("luas_bangunan", sa.Float(), nullable=True),
        sa.Column("njop_bumi_per_m2", sa.Float(), nullable=True), sa.Column("njop_bangunan_per_m2", sa.Float(), nullable=True),
        sa.Column("total_njop_bumi", sa.Float(), nullable=True), sa.Column("total_njop_bangunan", sa.Float(), nullable=True),
        sa.Column("total_njop", sa.Float(), nullable=True), sa.Column("match_status", sa.String(50), nullable=True), sa.Column("match_reason", sa.String(300), nullable=True))
    op.create_index("ix_njop_nop", "njop", ["nop"])
    op.create_table("booking_observation",
        sa.Column("observation_id", sa.String(36), primary_key=True), sa.Column("venue_id", sa.String(36), sa.ForeignKey("venues.venue_id"), nullable=False),
        sa.Column("observed_at", sa.DateTime(), nullable=False), sa.Column("tanggal_booking", sa.Date(), nullable=False),
        sa.Column("jam_mulai", sa.Time(), nullable=False), sa.Column("court", sa.String(100), nullable=True),
        sa.Column("harga", sa.Float(), nullable=False), sa.Column("durasi", sa.Integer(), nullable=True),
        sa.Column("status_slot", sa.String(50), nullable=False), sa.Column("sumber", sa.String(150), nullable=True))


def downgrade() -> None:
    op.drop_table("booking_observation")
    op.drop_index("ix_njop_nop", table_name="njop")
    op.drop_table("njop")
    for name in ("reason", "payment_ratio", "gap"):
        op.drop_column("anomaly_result", name)
    for name in ("status_pembayaran", "tanggal_bayar", "tanggal_lapor", "pbjt_terutang", "tarif_pbjt", "dpp_pbjt", "nopd"):
        op.drop_column("tax_payment", name)
    op.alter_column("tax_payment", "pbjt_dibayar", new_column_name="pbjt_pembayaran")
    for name in ("kelurahan", "kecamatan", "kota_administrasi", "nop", "nopd"):
        op.drop_column("venues", name)
