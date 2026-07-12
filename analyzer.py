def analyze_url(url):
    findings = []

    if "https" in url:
        findings.append("HTTPS detected")
    else:
        findings.append("No HTTPS")

    if "login" in url:
        findings.append("Login keyword detected")

    if len(url) > 50:
        findings.append("Long URL detected")

    return findings
    