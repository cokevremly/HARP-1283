def create_report(findings, score, risk_level, whois_info):
    print("\nSecurity Report")
    print("---------------")

    for finding in findings:
        print(f"- {finding}")
    
    print(f"\nRisk Score: {score}/100")
    print(f"Risk Level: {risk_level}")

    print("\nWHOIS Information")
    print("-----------------")
    registrar = whois_info["registrar"] or "Unknown"
    print(f"Registrar: {registrar}")
    print(f"Creation Date: {whois_info['creation_date']}")
    print(f"Expiration Date: {whois_info['expiration_date']}")
    



