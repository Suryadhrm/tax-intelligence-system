from pydantic import BaseModel


class RevenuePredictionOut(BaseModel):
    venue_id: str
    periode: str
    estimasi_omzet: float
    model_version: str

    class Config:
        from_attributes = True


class PBJTEstimationOut(BaseModel):
    venue_id: str
    estimasi_omzet: float
    tarif_pbjt: float
    estimasi_pbjt: float
