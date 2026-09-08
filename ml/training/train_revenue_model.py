"""Train the Revenue Prediction model (PRD Model 1 — XGBoost Regression).

Expects a processed CSV at ../data/processed/venues_with_omzet.csv with columns:
jumlah_court, harga_sewa, jam_operasi_mingguan, znt_value, wilayah (categorical), omzet_bulanan (target)

Usage:
    python train_revenue_model.py
"""
import joblib
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

DATA_PATH = Path(__file__).parent.parent / "data" / "processed" / "venues_with_omzet.csv"
ARTIFACT_PATH = Path(__file__).parent.parent.parent / "backend" / "app" / "ml" / "inference" / "artifacts" / "revenue_model.joblib"

FEATURES = ["jumlah_court", "harga_sewa", "jam_operasi_mingguan", "znt_value"]
TARGET = "omzet_bulanan"


def main():
    df = pd.read_csv(DATA_PATH)
    X, y = df[FEATURES], df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = XGBRegressor(n_estimators=300, max_depth=4, learning_rate=0.05, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(f"MAE:  {mean_absolute_error(y_test, preds):,.0f}")
    print(f"RMSE: {mean_squared_error(y_test, preds, squared=False):,.0f}")
    print(f"R2:   {r2_score(y_test, preds):.3f}")

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, ARTIFACT_PATH)
    print(f"Saved model to {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
