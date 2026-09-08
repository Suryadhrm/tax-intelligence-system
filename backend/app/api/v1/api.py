from fastapi import APIRouter

from app.api.v1.routes import (
    auth, venues, spatial, revenue, tax, anomaly, sustainability, dashboard,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(venues.router, prefix="/venues", tags=["Venue Data Management"])
api_router.include_router(spatial.router, prefix="/spatial", tags=["GIS & ZNT Integration"])
api_router.include_router(revenue.router, prefix="/revenue", tags=["Revenue & PBJT Estimation"])
api_router.include_router(tax.router, prefix="/tax", tags=["Tax Payment"])
api_router.include_router(anomaly.router, prefix="/anomaly", tags=["Anomaly Detection"])
api_router.include_router(sustainability.router, prefix="/sustainability", tags=["Business Sustainability"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard Analytics"])
