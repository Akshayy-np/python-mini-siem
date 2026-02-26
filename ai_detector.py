def risk_score(attempts):
    if attempts < 5:
        return "LOW"
    elif 5 <= attempts < 20:
        return "MEDIUM"
    else:
        return "HIGH"