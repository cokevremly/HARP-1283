from analyzer import analyze_url
from scorer import calculate_score, get_risk_level
from report import create_report
from whois_lookup import get_whois_info


def main():
    
    print("=" * 40)
    print("URL Security Analyzer".center(40))
    print("=" * 40)

    url = input("\nEnter a URL: ")
    
    print("\nAnalyzing...")

    findings = analyze_url(url)
    whois_info = get_whois_info(url)

   
    #print(whois_info)

    score = calculate_score(findings)

    risk_level = get_risk_level(score)

    create_report(findings, score, risk_level, whois_info)
    

if __name__ == "__main__":
    main() #fonksiyon çalıştırıldı


