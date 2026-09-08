from datetime import date
import re

from pydantic import BaseModel, Field, field_validator


class TaxPaymentCreate(BaseModel):
    venue_id: str = Field(min_length=1)
    periode: date
    omzet_laporan: float = Field(ge=0)
    pbjt_pembayaran: float = Field(ge=0)

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

    class Config:
        from_attributes = True
