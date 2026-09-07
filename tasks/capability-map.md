# Capability Map — Tax Intelligence System
| Module id | Responsibility | Depends on |
|---|---|---|
| identity | auth & RBAC, JWT | — |
| venue-mgmt | CRUD + import CSV/Excel + soft-delete | identity |
| gis-znt | spatial join PostGIS, Leaflet map | venue-mgmt |
| revenue-estimation | XGBoost Regression + baseline | gis-znt |
| pbjt-calc | tarif × omzet | revenue-estimation |
| anomaly-detection | IsolationForest score+kategori+ranking | pbjt-calc |
| sustainability | weighted score 0-100 + outlook (Should Have) | anomaly-detection |
| dashboard-analytics | KPI agregat, grafik, peta heat/choropleth | semua di atas |
Build order: identity → venue-mgmt → gis-znt → revenue-estimation → pbjt-calc → anomaly-detection → dashboard-analytics → sustainability (paralel setelah anomaly jika data historis cukup)
Spec files: tasks/specs/SPEC-<module-id>.md
