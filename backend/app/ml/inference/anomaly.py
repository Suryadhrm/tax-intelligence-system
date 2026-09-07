def score(ratio:float)->tuple[float,str]:
    # ratio = bayar/estimasi; ponytail: rule-based fallback; upgrade ke IsolationForest
    if ratio>=0.85: return 0.1, "Normal"
    if ratio>=0.6: return 0.5, "Monitoring"
    return 0.9, "High Risk"
