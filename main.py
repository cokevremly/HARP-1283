import ssl

from analyzer import analyze_url
from scorer import calculate_score, get_risk_level
from report import create_report
from whois_lookup import get_whois_info
from ssl_lookup import get_ssl_info


def main():
    
    print("=" * 40)
    print("URL Security Analyzer".center(40))
    print("=" * 40)

    url = input("\nEnter a URL: ").strip()  # Kullanıcıdan URL girişi alır ve başındaki/sonundaki boşlukları temizler
    if not url.startswith(("http://", "https://")):
        url = "http://" + url  # Eğer URL http veya https ile başlamıyorsa, başına http ekle
    
    print("\nAnalyzing...")

    findings = analyze_url(url)
    whois_info = get_whois_info(url)
    ssl_info =get_ssl_info(url)

    score = calculate_score(findings)

    risk_level = get_risk_level(score)


    create_report(findings, 
        score, 
        risk_level, 
        whois_info, 
        ssl_info)


if __name__ == "__main__":
    main() #fonksiyon çalıştırıldı


