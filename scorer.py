
RISK_RULES = {
    "No HTTPS": 30,
    "Login keyword detected": 20,
    "Long URL detected": 10
}

def calculate_score(findings):
    score = 0 #score starts from 0

    for finding in findings:
        if finding in RISK_RULES:
            score += RISK_RULES[finding]
    
    return score

def get_risk_level(score):
    if score <= 30:
        return "LOW"
    elif score <= 60:
        return "MEDIUM"
    else:
        return "HIGH"

