from analyzer import analyze_url
from scorer import calculate_score, get_risk_level
from report import create_report
from whois_lookup import get_whois_info
from ssl_lookup import get_ssl_info
from dns_lookup import dns_lookup
from virustotal_lookup import virustotal_lookup
from abuseipdb_lookup import check_ip
from otx_lookup import check_ip_otx



def main():
    
    print("=" * 40)
    print("HARP-1283".center(40))
    print("=" * 40)

    url = input("\nEnter a URL: ").strip()  # Kullanıcıdan URL girişi alır ve başındaki/sonundaki boşlukları temizler
    if not url.startswith(("http://", "https://")):
        url = "http://" + url  # Eğer URL http veya https ile başlamıyorsa, başına http ekle
    
    print("\nAnalyzing...")

    findings = analyze_url(url)
    whois_info = get_whois_info(url)
    ssl_info =get_ssl_info(url)
    dns_info = dns_lookup(url)
    ip = dns_info["A"][0] if dns_info["A"] else None  # A kaydı varsa ilk IP adresini alır, yoksa None
    abuseipdb_info = check_ip(ip)
    otx_info = check_ip_otx(ip)
    virustotal_info = virustotal_lookup(url)


    score = calculate_score(
                    findings,
                    virustotal_info,
                    abuseipdb_info,
                    otx_info
                    )

    risk_level = get_risk_level(score)


    create_report(findings, 
        score, 
        risk_level, 
        whois_info, 
        ssl_info,
        dns_info,
        virustotal_info,
        abuseipdb_info,
        otx_info
        )


if __name__ == "__main__":
    main() #fonksiyon çalıştırıldı


