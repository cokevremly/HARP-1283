# 🛡️ HARP-1283

### Hybrid Analysis & Reconnaissance Platform v1.0

[Türkçe için](README-TR.md)

HARP-1283 is a Python-based cybersecurity analysis platform that combines **URL security analysis, risk scoring, SSL/TLS inspection, domain intelligence, DNS analysis, and external Threat Intelligence sources** into a unified workflow.

The project is designed to provide a practical and extensible platform for analyzing suspicious URLs and domains.

> The number **1283** is inspired by Mustafa Kemal Atatürk's student number at the Turkish Military Academy.

---

## ✨ Features

### 🔍 URL Security Analysis

HARP-1283 performs rule-based analysis of submitted URLs.

Current checks include:

* HTTPS availability
* Suspicious keyword detection
* Long URL detection
* Security findings generation
* Risk score calculation
* Risk level classification

Risk levels:

* 🟢 **LOW**
* 🟡 **MEDIUM**
* 🔴 **HIGH**

---

### 🔐 SSL/TLS Analysis

The platform analyzes the SSL/TLS certificate associated with a target domain.

Information may include:

* Certificate issuer
* Domain information
* Certificate validity
* Remaining validity period

---

### 🌐 WHOIS Lookup

HARP-1283 retrieves WHOIS information to provide additional domain intelligence.

---

### 📡 DNS Analysis

The platform supports querying common DNS record types:

* A
* AAAA
* MX
* NS
* CNAME
* TXT

This provides additional context about the target domain's DNS infrastructure.

---

### 🦠 VirusTotal Integration

HARP-1283 integrates with VirusTotal to enrich URL and IP analysis with external threat intelligence.

The integration can provide:

* Malicious detections
* Suspicious detections
* Harmless results
* Undetected results
* Reputation information

---

### 🚨 AbuseIPDB Integration

AbuseIPDB data can be used to investigate the IP address associated with a target.

Relevant information may include:

* Abuse confidence score
* Report count
* Country
* ISP / organization

---

### 🛰️ AlienVault OTX Integration

AlienVault Open Threat Exchange (OTX) is used as an additional threat intelligence source.

The integration can provide information such as:

* Reputation
* Pulse count
* Country
* ASN
* Organization

---

## 📊 Risk Scoring

HARP-1283 combines security findings and available threat intelligence results to calculate an overall risk score.

Example:

```text
Risk Score: 45/100
Risk Level: MEDIUM
```

The final score can vary depending on the URL characteristics and the available Threat Intelligence results.

---

## 📄 Security Reporting

Analysis results are consolidated into a security report containing:

* URL analysis findings
* Technical information
* Threat Intelligence results
* Risk score
* Risk level

The reporting layer is designed to provide a concise overview of the performed analysis.

---

## 🖥️ Web Interface

HARP-1283 includes a **Streamlit-based web interface**.

The interface allows users to:

1. Enter a URL
2. Start the analysis
3. Review security findings
4. Inspect SSL/TLS information
5. Review WHOIS and DNS data
6. View Threat Intelligence results
7. Evaluate the final risk score

---

## 🏗️ Project Structure

```text
HARP-1283/
│
├── app.py                    # Streamlit web interface
├── main.py                   # CLI entry point
│
├── analyzer.py               # URL security analysis
├── scorer.py                 # Risk score calculation
├── report.py                 # Security report generation
│
├── ssl_lookup.py             # SSL/TLS analysis
├── whois_lookup.py           # WHOIS lookup
├── dns_lookup.py             # DNS analysis
│
├── virustotal_lookup.py      # VirusTotal integration
├── abuseipdb_lookup.py       # AbuseIPDB integration
├── otx_lookup.py             # AlienVault OTX integration
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/cokevremly/HARP-1283.git
```

Enter the project directory:

```bash
cd HARP-1283
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running HARP-1283

### Streamlit Interface

Run:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

### CLI

The project can also be executed through the CLI entry point:

```bash
python main.py
```

---

## 🔑 API Configuration

Some Threat Intelligence integrations require API keys.

Currently supported external services include:

* VirusTotal
* AbuseIPDB
* AlienVault OTX

API keys should **never be hard-coded or committed to GitHub**.

Use environment variables or another secure configuration method.

---

## 🧪 Example

A URL can be analyzed through the Streamlit interface or CLI.

Example findings:

```text
Findings:
- No HTTPS
- Login keyword detected
- Long URL detected

Risk Score: 45/100
Risk Level: MEDIUM
```

Threat Intelligence results are incorporated when the corresponding services are available.

---

## 🛠️ Technologies

* Python
* Streamlit
* SSL/TLS
* WHOIS
* DNS
* VirusTotal API
* AbuseIPDB API
* AlienVault OTX API
* Git
* GitHub

---

## 🗺️ Roadmap

HARP-1283 is under active development.

### 🔎 OSINT Module

### 🦠 Malware Analysis

### 🤖 AI Analyst

### 📡 Additional Threat Intelligence

---

## ⚠️ Disclaimer

HARP-1283 is developed for **educational, research, and authorized security testing purposes**.

Only analyze URLs, domains, IP addresses, and systems that you own or have explicit permission to test.

The developer is not responsible for unauthorized or illegal use of this project.

---

## 👩‍💻 Author

**Merve KOÇ**

https://www.linkedin.com/in/merve-ko%C3%A7-167194177/

---
