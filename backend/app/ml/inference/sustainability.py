def score(trend:float)->tuple[float,str]:
    # trend = slope omzet; ponytail: weighted fallback
    s=max(0,min(100,50+trend*10))
    outlook="Positif" if s>65 else "Waspada" if s<45 else "Stabil"
    return s, outlook
