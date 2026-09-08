from pydantic import BaseModel, Field


class VenueBase(BaseModel):
    nama: str = Field(min_length=1, max_length=200)
    lokasi: str = Field(min_length=1, max_length=300)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    jumlah_court: int = Field(ge=1, le=100)
    harga_sewa: float = Field(ge=0)
    jam_operasi: str = Field(min_length=1, max_length=100)
    hari_operasi: str = Field(min_length=1, max_length=100)
    rating: float | None = Field(default=None, ge=0, le=5)


class VenueCreate(VenueBase):
    pass


class VenueUpdate(VenueBase):
    pass


class VenueOut(VenueBase):
    venue_id: str
    znt_id: str | None = None

    class Config:
        from_attributes = True
