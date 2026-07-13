# 🔒 URL Security Analyzer

A Python-based URL security analysis tool that detects suspicious patterns, calculates a risk score, and classifies the security level of a given URL.

---

## ✨ Features

- ✅ HTTPS detection
- ✅ Suspicious keyword detection (`login`)
- ✅ Long URL detection
- ✅ Rule-based risk scoring
- ✅ Risk level classification (LOW / MEDIUM / HIGH)

---

## 📁 Project Structure

```
URL-Security-Analyzer/
│
├── analyzer.py      # URL analysis logic
├── scorer.py        # Risk score calculation
├── report.py        # Report generation
├── main.py          # Application entry point
└── .gitignore
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/cokevremly/URL-Security-Analyzer.git
```

Go to the project directory:

```bash
cd URL-Security-Analyzer
```

Run the application:

```bash
python main.py
```

---

## 💻 Example

Input:

```
http://example.com/login/account/security/check
```

Output:

```
Security Report
---------------
- No HTTPS
- Login keyword detected

Risk Score: 50/100
Risk Level: MEDIUM
```

---

## 🛠 Technologies

- Python 3
- Git
- GitHub

---

## 🚧 Planned Improvements

- AI-powered URL analysis
- WHOIS lookup
- DNS analysis
- SSL certificate inspection
- Threat Intelligence integration
- VirusTotal API support

---

## 👩‍💻 Author

Developed by Merve Koc.