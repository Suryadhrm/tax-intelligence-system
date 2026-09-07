from fastapi import FastAPI
from app.api.v1.routes import auth, venues, spatial, revenue, tax, anomaly, sustainability, dashboard
app = FastAPI(title="Tax Intelligence System", version="0.1.0")
for r in [auth.router, venues.router, spatial.router, revenue.router, tax.router, anomaly.router, sustainability.router, dashboard.router]:
    app.include_router(r, prefix="/api/v1")
@app.get("/health")
def health(): return {"status":"ok"}
