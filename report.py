def create_report(findings, score, risk_level, whois_info, ssl_info):
    print("\nSecurity Report")
    print("---------------")

    for finding in findings:
        print(f"- {finding}")
    
    print(f"\nRisk Score: {score}/100")
    print(f"Risk Level: {risk_level}")

    print("\nWHOIS Information")
    print("-----------------")
    
    registrar = whois_info.get("registrar") or "Unknown"
    creation_date = whois_info.get("creation_date") or "Unknown"
    updated_date = whois_info.get("updated_date") or "Unknown"
    expiration_date = whois_info.get("expiration_date") or "Unknown"
    name_servers = whois_info.get("name_servers") or "Unknown"
    status = whois_info.get("status") or "Unknown"
    dnssec = whois_info.get("dnssec") or "Unknown"
    # .get() kullanmamızın sebebi eğer dictionaryde key yoksa None dönmesini engellemek ve "Unknown" olarak göstermek.
    #aksi takdirde dictionaryde key yoksa KeyError hatası alırız.
    
    print(f"Registrar: {registrar}")
    print(f"Creation Date: {creation_date}")
    print(f"Updated Date: {updated_date}")
    print(f"Expiration Date: {expiration_date}")
    print(f"Name Servers: {name_servers}")
    print(f"Status: {status}")
        
    if dnssec in ("unsigned", "no", "inactive", None):
        print("DNSSEC: Not enabled")
    else:
        print(f"DNSSEC: {dnssec}")

    print("\nSSL Information")
    print("-----------------")
    issuer = ssl_info.get("issuer") or "Unknown"
    issued_to = ssl_info.get("issued_to") or "Unknown"
    valid_from = ssl_info.get("valid_from") or "Unknown"
    valid_until = ssl_info.get("valid_until") or "Unknown"
    days_remaining = ssl_info.get("days_remaining")


    print(f"Issuer: {issuer}")
    print(f"Issued To: {issued_to}")
    print(f"Valid From: {valid_from}")
    print(f"Valid Until: {valid_until}")
    print(f"Days Remaining: {days_remaining}")


    print("\nReport generated successfully.")
    print("=" * 40)
    print("End of Report".center(40))
    print("=" * 40)
    print("\nThank you for using the URL Security Analyzer!")
    print("Stay safe online!")
    print("=" * 40)



