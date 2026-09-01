
RISK_RULES = {
    "No HTTPS": 30,
    "Login keyword detected": 20,
    "Long URL detected": 10
}

def calculate_score(
    findings,
    virustotal_info=None,
    abuseipdb_info=None,
    otx_info=None
    ):
    score = 0 #score starts from 0

    #VirusTotal için
    if virustotal_info and "error" not in virustotal_info:
        malicious = virustotal_info.get("Malicious", 0)
        suspicious = virustotal_info.get("Suspicious", 0)

        if malicious > 0:
            score += 30  # Malicious detections add 50 points
        elif suspicious > 0:
            score += 15  # Suspicious detections add 30 points

    #AbuseIPDB için
    if abuseipdb_info:
        data = abuseipdb_info.get("data", {})
        abuse_score = data.get("abuseConfidenceScore", 0)

        if abuse_score >= 80:
            score += 25  # High abuse score adds 25 points
        elif abuse_score >= 50:
            score += 15  # Medium abuse score adds 15 points
        elif abuse_score >= 20:
            score += 5  # Low abuse score adds 5 points

    #OTX için
    if otx_info:
        reputation = otx_info.get("reputation", 0)
        pulse_count = otx_info.get("pulse_info", {}).get("count", 0)

        if reputation < 0:
            score += 15  # Very bad reputation adds 15 points
        if pulse_count >= 50:
            score += 15  # Presence of pulses adds 15 points
        elif pulse_count >= 10:
            score += 10  # Presence of pulses adds 10 points
        elif pulse_count > 0:
            score += 5  # Presence of pulses adds 5 points


    for finding in findings:
        if finding in RISK_RULES:
            score += RISK_RULES[finding]

    score = min(score, 100) #score 100 ü geçse bile max 100 olacak.
    
    return score

def get_risk_level(score):
    if score <= 20:
        return "LOW"
    elif score <= 50:
        return "MEDIUM"
    elif score <= 80:
        return "HIGH"
    else:
        return "CRITICAL"

