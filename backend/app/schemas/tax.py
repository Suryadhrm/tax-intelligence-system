from datetime import date
import re
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_validator


class TaxPaymentCreate(BaseModel):
    venue_id: str = Field(min_length=1)
    nopd: str | None = None
    periode: date
    omzet_laporan: float = Field(ge=0)
    dpp_pbjt: float | None = Field(default=None, ge=0)
    tarif_pbjt: float | None = Field(default=None, ge=0, le=1)
    pbjt_terutang: float | None = Field(default=None, ge=0)
    pbjt_dibayar: float = Field(default=0, ge=0, validation_alias=AliasChoices("pbjt_dibayar", "pbjt_pembayaran"))
    tanggal_lapor: date | None = None
    tanggal_bayar: date | None = None
    status_pembayaran: str | None = None

    @property
    def pbjt_pembayaran(self) -> float:
        return self.pbjt_dibayar

    @field_validator("periode", mode="before")
    @classmethod
    def validate_periode(cls, v):
        if isinstance(v, date):
            return v
        if isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}", v):
            return date(int(v[:4]), int(v[5:7]), 1)
        return v


class TaxPaymentOut(TaxPaymentCreate):
    payment_id: str
    model_config = ConfigDict(from_attributes=True)
