def risk_score(attempts):
    if attempts > 20:
        return "HIGH"
    elif attempts > 10:
        return "MEDIUM"
    else:
        return "LOW"