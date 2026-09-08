# Tax Intelligence System

Sistem Analitik Potensi Pendapatan dan Deteksi Anomali Pajak PBJT Venue Padel
Jakarta Barat — proyek magang untuk Bappenda (1 Sep – 4 Des 2026).

Lihat `docs/` untuk PRD lengkap.

## Struktur Repo

```
backend/     FastAPI API — routes, models (ORM), schemas, services, ML inference (serving)
frontend/    React PWA — Login, Dashboard, Map, Venue Detail
ml/          Notebook & script eksperimen/training model (terpisah dari kode serving)
docs/        Dokumen perencanaan (PRD, dsb.)
```

Setiap folder (`backend/`, `frontend/`, `ml/`) punya README sendiri dengan
instruksi setup.

## Menjalankan Semua Layanan Sekaligus (Docker)

```bash
docker compose up --build
```

- Backend API: http://localhost:8000/docs
- Frontend: http://localhost:3000
- Database: PostgreSQL + PostGIS di port 5432

## Pemetaan Modul PRD -> Kode

| Modul PRD | Lokasi Kode |
|---|---|
| Module 1: Authentication & User Management | `backend/app/api/v1/routes/auth.py`, `app/core/security.py` |
| Module 2: Venue Data Management | `backend/app/api/v1/routes/venues.py`, `app/services/venue_service.py` |
| Module 3: GIS & ZNT Integration | `backend/app/api/v1/routes/spatial.py`, `app/services/spatial_service.py` |
| Module 4: Revenue Estimation Engine | `backend/app/ml/inference/revenue_model.py` |
| Module 5: PBJT Estimation Engine | `backend/app/api/v1/routes/revenue.py` |
| Module 6: Anomaly Detection System | `backend/app/ml/inference/anomaly_model.py` |
| Module 7: Business Sustainability Analytics | `backend/app/ml/inference/sustainability_model.py` |
| Module 8: Dashboard Analytics | `backend/app/api/v1/routes/dashboard.py`, `frontend/src/pages/DashboardPage.jsx` |
| Model training (Section 8) | `ml/training/*.py` |
