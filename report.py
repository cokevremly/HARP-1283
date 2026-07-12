def create_report(findings, score, risk_level):
    print("\nSecurity Report")
    print("---------------")

    for finding in findings:
        print(f"- {finding}")
    
    print(f"\nRisk Score: {score}/100")
    print(f"\nRisk Level: {risk_level}")

