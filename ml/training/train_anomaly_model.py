"""Train the Anomaly Detection model (PRD Model 2 — Isolation Forest).

Expects a processed CSV at ../data/processed/tax_ratios.csv with columns:
venue_id, estimasi_pbjt, pbjt_pembayaran, payment_ratio (= pembayaran / estimasi)

Usage:
    python train_anomaly_model.py
"""
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest

DATA_PATH = Path(__file__).parent.parent / "data" / "processed" / "tax_ratios.csv"
ARTIFACT_PATH = Path(__file__).parent.parent.parent / "backend" / "app" / "ml" / "inference" / "artifacts" / "anomaly_model.joblib"

FEATURES = ["payment_ratio"]


def main():
    df = pd.read_csv(DATA_PATH)
    X = df[FEATURES]

    model = IsolationForest(n_estimators=200, contamination="auto", random_state=42)
    model.fit(X)

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, ARTIFACT_PATH)
    print(f"Saved model to {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
