# Tax Intelligence System — Venue Padel Jakarta Barat

PWA untuk estimasi potensi PBJT, deteksi anomali, dan analitik sustainability venue padel Jakbar.
Stack: React PWA + FastAPI + PostgreSQL+PostGIS + XGBoost + Isolation Forest + Leaflet.

## Struktur → Modul PRD

| Modul PRD | Route | Service | Model/Table | ML |
|---|---|---|---|---|
| M1 Auth & User Mgmt | `backend/app/api/v1/routes/auth.py` | `services/auth_service.py` | `models/user.py` | — |
| M2 Venue Mgmt | `venues.py` | `venue_service.py` | `models/venue.py` | — |
| M3 GIS & ZNT | `spatial.py` | `spatial_service.py` | `models/spatial_znt.py` | GeoPandas/PostGIS |
| M4 Revenue Estimation | `revenue.py` | `services/revenue_service.py` | `models/revenue_prediction.py` | `ml/inference/revenue.py` + `ml/scripts/train_revenue_model.py` |
| M5 PBJT Estimation | `tax.py` | `tax_service.py` | `models/tax_payment.py` | `pbjt = omzet * tarif` |
| M6 Anomaly Detection | `anomaly.py` | `anomaly_service.py` | `models/anomaly_result.py` | `ml/inference/anomaly.py` (Isolation Forest) |
| M7 Sustainability | `sustainability.py` | `sustainability_service.py` | `models/sustainability_result.py` | `ml/inference/sustainability.py` (weighted score) |
| M8 Dashboard | `dashboard.py` | `dashboard_service.py` | agregat semua | — |

## Quickstart
```bash
cp .env.example .env
docker compose up --build
# backend http://localhost:8000/docs
# frontend http://localhost:5173
```

## Spec-driven workflow
Lihat `tasks/capability-map.md` → `tasks/specs/SPEC-*.md` → `tasks/plan.md` → `tasks/todo.md`.

## Prinsip ML
`backend/app/ml/inference/` = serving + fallback heuristik (API tetap jalan sebelum model dilatih).
`ml/` = training & artifacts; tidak jadi microservice terpisah di MVP.
