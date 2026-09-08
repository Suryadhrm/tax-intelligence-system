import uuid
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from geoalchemy2 import Geometry as GeoGeometry
from app.db.base import Base


class SpatialZNT(Base):
    """PRD table: spatial_znt — Zona Nilai Tanah reference per polygon/wilayah (Module 3)."""
    __tablename__ = "spatial_znt"

    znt_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    wilayah: Mapped[str] = mapped_column(String(150))
    znt_value: Mapped[float] = mapped_column(Float)  # Rp / m^2
    polygon = mapped_column(GeoGeometry(geometry_type="POLYGON", srid=4326), nullable=True)
