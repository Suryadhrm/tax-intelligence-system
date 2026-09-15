# Tax Intelligence System

Sistem analitik potensi pendapatan dan penyaringan anomali PBJT venue padel di DKI Jakarta — proyek magang Bappenda (1 Sep–4 Des 2026).

## Status data

Fondasi skema bersifat independen dari format sumber. dataset PBJT September 2026, ZNT, NJOP, dan observasi booking aktual belum tersedia/disetujui; parser impor spesifik sumber sengaja belum dibuat. Cakupan analisis kelak mengikuti venue DKI Jakarta yang dapat direkonsiliasi, bukan klaim seluruh populasi.

## Struktur repo

```
backend/     FastAPI, SQLAlchemy/PostGIS, Alembic, analytics transparan
frontend/    React PWA: Login, Dashboard, Map, Venue Detail
ml/          Eksperimen training opsional; bukan baseline MVP
```

## Menjalankan layanan

```bash
docker compose up --build
```

- Backend API: http://localhost:8000/docs
- Frontend: http://localhost:3000
- Database: PostgreSQL + PostGIS pada port 5432

## Pemetaan PRD ke kode

| Modul | Lokasi |
|---|---|
| Venue DKI dan hierarki administrasi | `backend/app/models/venue.py`, `frontend/src/pages/MapPage.jsx` |
| GIS, ZNT, NJOP | `backend/app/models/spatial_znt.py`, `backend/app/models/njop.py` |
| Observasi booking dan estimasi omzet | `backend/app/models/booking_observation.py`, `backend/app/ml/inference/revenue_model.py` |
| PBJT periodik | `backend/app/models/tax_payment.py`, `backend/app/schemas/tax.py` |
| Penyaringan anomali | `backend/app/ml/inference/anomaly_model.py` |
| Indeks potensi snapshot | `backend/app/ml/inference/sustainability_model.py` |
| Perubahan database | `backend/migrations/versions/0002_dki_snapshot_foundations.py` |

## Batasan analitik

- Omzet: agregasi slot `terindikasi_terjual` × harga; tanpa heuristik kapasitas.
- Anomali: gap, rasio pembayaran, kategori, alasan; indikasi untuk verifikasi, bukan bukti pelanggaran.
- Indeks potensi: snapshot bidang yang tersedia, confidence rendah; bukan tren, forecasting, atau prediksi keberlangsungan.
