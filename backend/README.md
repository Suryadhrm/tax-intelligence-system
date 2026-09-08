# Backend — Tax Intelligence System API

FastAPI service that exposes venue management, GIS/ZNT integration, revenue
estimation, PBJT calculation, anomaly detection, and sustainability analytics
endpoints, per the PRD.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then fill in real values

# 1. Make sure PostgreSQL + PostGIS is running (see ../docker-compose.yml,
#    or `docker compose up db` from the repo root) and DATABASE_URL in .env
#    points to it.

# 2. Create the schema
alembic upgrade head

# 3. Seed demo data (2 users, 3 ZNT zones, 5 venues, 6 months of tax_payment)
python -m scripts.seed_data

# 4. Run the API
uvicorn app.main:app --reload
```

API docs available at http://localhost:8000/docs once running.

Demo login after seeding: `admin@bappenda.go.id` / `admin123` (Admin Bappenda)
or `petugas@bappenda.go.id` / `petugas123` (Petugas Pengawasan).

### Adding a new migration

After changing a model in `app/models/`, generate the next revision:

```bash
alembic revision --autogenerate -m "describe the change"
alembic upgrade head
```

## Structure

```
app/
  core/       # settings, security (JWT, password hashing)
  db/         # SQLAlchemy engine/session, declarative base
  models/     # ORM models (one file per table from the PRD ERD)
  schemas/    # Pydantic request/response schemas
  api/v1/     # versioned routers, one file per module
  services/   # business logic between routes and models/ML
             #   spatial_service.py runs the real PostGIS point-in-polygon
             #   join (ST_Contains) — auto-triggered on venue create/update
  ml/inference/  # loads trained models (from ../ml/training) and serves predictions
migrations/   # Alembic — schema versioning (see "Adding a new migration" below)
scripts/
  seed_data.py  # demo dataset: users, ZNT zones, venues, tax_payment history
tests/
```

### Endpoints beyond basic CRUD

- `POST /api/v1/venues/import` — bulk CSV import (validates each row, runs the
  ZNT spatial join automatically per row via the normal create_venue path).
- `POST /api/v1/spatial/znt/rerun` — re-runs the spatial join for every venue
  (Admin Bappenda only) — use after importing new/updated ZNT polygons.
- `GET /api/v1/anomaly/ranking/high-risk` — venues ranked by anomaly score,
  optional `?category=high_risk` filter and `?limit=` (Module 6).
- `GET /api/v1/dashboard/summary` / `GET /api/v1/dashboard/trend/omzet` —
  aggregate cards and the omzet trend chart (Module 8).

## Trained models

Training/experimentation lives in the top-level `../ml/` folder (notebooks +
scripts), kept separate from this serving code. Export trained artifacts
(`.joblib`/`.json`) into `app/ml/inference/artifacts/` for the API to load.
