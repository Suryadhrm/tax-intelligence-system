from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import uuid
# polygon geometry disimpan sebagai WKT/GeoJSON text untuk MVP; upgrade ke GeoAlchemy2+PostGIS setelah init
class SpatialZNT(Base):
    __tablename__="spatial_znt"
    id: Mapped[str]=mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    wilayah: Mapped[str]=mapped_column(String)
    znt_value: Mapped[float]=mapped_column(Numeric(14,2))
    polygon_wkt: Mapped[str | None]=mapped_column(String, nullable=True)
