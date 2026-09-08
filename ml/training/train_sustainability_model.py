"""Business Sustainability scoring (PRD Model 3 — Should Have / prototype).

MVP approach is deliberately transparent (trend analysis + weighted scoring),
not a black-box model — see PRD Module 7 for the constraints on this feature.
This script is a placeholder for exploring/calibrating the weights once
historical data (>= a few periods per venue) is available; it does not export
a serialized model, since app/ml/inference/sustainability_model.py already
implements the rule-based logic directly.
"""
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "processed" / "venue_omzet_timeseries.csv"


def main():
    df = pd.read_csv(DATA_PATH)
    # TODO once real historical data exists: calibrate score weights against
    # known outcomes (e.g. venues that visibly scaled down operations) instead
    # of the fixed 50 + growth_ratio*100 placeholder in the serving code.
    print(df.groupby("venue_id")["omzet_bulanan"].describe())


if __name__ == "__main__":
    main()
