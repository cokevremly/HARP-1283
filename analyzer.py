def analyze_url(url):
    findings = []

    if url.startswith("https://"):
        findings.append("HTTPS detected")
    else:
        findings.append("No HTTPS") #URL'in HTTPS ile başlayıp başlamadığını kontrol eder. Başlamıyorsa "No HTTPS" uyarısı ekler.

    if "login" in url.lower():  # URL'de "login" kelimesi geçiyorsa uyarı ekler. küçük harf duyarlılığı için .lower() kullanılır.   
        findings.append("Login keyword detected")

    if len(url) > 50:
        findings.append("Long URL detected")

    return findings
    