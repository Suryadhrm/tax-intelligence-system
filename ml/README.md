# ML — Training & Experimentation

Data-science side of the project: exploratory notebooks and training scripts.
This is intentionally separate from `backend/app/ml/inference/`, which only
*serves* already-trained artifacts.

## Structure

```
data/
  raw/         # untouched source data (venue lists, ZNT exports, tax reports)
  processed/   # cleaned/joined datasets ready for modeling
notebooks/     # exploratory analysis (EDA), one notebook per question
training/      # scripts that train + evaluate + export model artifacts
```

## Workflow

1. Drop raw exports into `data/raw/` (never edit them in place).
2. Clean/join in a notebook, save the result to `data/processed/`.
3. Train with a script in `training/`, e.g.:
   ```bash
   python training/train_revenue_model.py
   ```
4. Copy the exported `.joblib` file into
   `../backend/app/ml/inference/artifacts/` so the API can load it.

## Models (per PRD Section 8)

| Script | Model | Algorithm |
|---|---|---|
| `train_revenue_model.py` | Revenue Prediction | XGBoost Regression |
| `train_anomaly_model.py` | Anomaly Detection | Isolation Forest |
| `train_sustainability_model.py` | Business Sustainability (Should Have) | Trend analysis + weighted scoring |
