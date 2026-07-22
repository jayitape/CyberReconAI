# 🛡️ CyberRecon AI

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Version](https://img.shields.io/badge/Version-v1.1.0-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Type Checked](https://img.shields.io/badge/mypy-100%25%20Clean-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

</p>

---

# 🚀 CyberRecon AI

**CyberRecon AI** is an enterprise-inspired **Website Security Assessment Toolkit** developed in Python for **authorized defensive security assessments**.

It automates reconnaissance, security intelligence collection, vulnerability correlation, risk analysis, and generates professional security assessment reports.

CyberRecon AI follows a clean modular architecture with:

- Enterprise logging
- Intelligent caching
- Concurrent processing
- Rich terminal dashboard
- Strong type safety using **mypy**

---

# ✨ Key Features

## 🌐 Target Intelligence

- Domain Analysis
- WHOIS Lookup
- DNS Enumeration
- Subdomain Discovery

---

## 🔒 Security Assessment

- SSL/TLS Certificate Analysis
- HTTP Security Header Analysis
- robots.txt Analysis
- TCP Port Scanning
- Service Detection
- Technology Fingerprinting

---

## 🧠 Vulnerability Intelligence

- National Vulnerability Database (NVD) Integration
- CPE Based Vulnerability Matching
- CVSS Information Extraction
- Vulnerability Intelligence Engine

---

## 📊 Risk Analysis

- Security Risk Score Calculation
- Risk Level Classification
- Security Findings Generation
- Vulnerability Summary

---

## 📄 Reporting System

CyberRecon AI generates:

- Professional HTML Reports
- JSON Security Reports
- Enterprise PDF Reports

Reports include:

- Scan Metadata
- Scan ID
- Duration
- Security Score
- Findings
- Technical Details
- Recommendations

---

## ⚙️ Enterprise Features

- Modular Python Architecture
- Enterprise Logging Framework
- JSON Cache Manager
- Concurrent Intelligence Collection
- Rich Terminal UI Dashboard
- Type Hints
- 100% mypy Clean Codebase

---

# 🏗️ Architecture

                User / CLI
                   |
                   v
            Target Analysis
                   |
    +--------------+--------------+
    |              |              |
    v              v              v
  WHOIS          DNS        SSL/TLS
    |              |              |
    +--------------+--------------+
                   |
                   v
          HTTP Security Headers
                   |
                   v
        Technology Detection
                   |
                   v
        Subdomain Enumeration
                   |
                   v
         Port & Service Scanner
                   |
                   v
      Vulnerability Intelligence
                   |
                   v
             Risk Engine
                   |
                   v
      HTML + JSON + PDF Reports

---

# 🎯 Project Objectives

CyberRecon AI is designed to:

- Automate website reconnaissance
- Identify common security weaknesses
- Collect security intelligence
- Perform vulnerability correlation
- Generate professional assessment reports
- Demonstrate enterprise Python development practices
- Provide an extensible cybersecurity research platform

---

# ⭐ Project Highlights

✅ Enterprise-inspired security workflow  
✅ Modular Python architecture  
✅ Professional logging system  
✅ Intelligent caching mechanism  
✅ Concurrent processing framework  
✅ Rich terminal dashboard  
✅ HTML, JSON & PDF reporting  
✅ 100% mypy clean codebase  
✅ Portfolio-ready cybersecurity project  

---

# ⚠️ Disclaimer

CyberRecon AI is intended **only for authorized defensive security assessments and educational purposes**.

Do not scan systems without explicit permission from the owner.

The author is not responsible for misuse of this software.

---

# 📂 Project Structure


CyberReconAI/

├── cache/
│ └── nvd_cache.json

├── modules/
│
│ ├── banner.py
│ ├── cache_manager.py
│ ├── cli.py
│ ├── concurrent.py
│ ├── dns_lookup.py
│ ├── http_headers.py
│ ├── json_report.py
│ ├── logger.py
│ ├── nvd_client.py
│ ├── pdf_generator.py
│ ├── port_scanner.py
│ ├── report_generator.py
│ ├── risk_engine.py
│ ├── robots_analyzer.py
│ ├── scan_id.py
│ ├── scan_timer.py
│ ├── service_detector.py
│ ├── ssl_checker.py
│ ├── subdomain_enum.py
│ ├── target.py
│ ├── technology_detector.py
│ ├── ui.py
│ ├── version.py
│ ├── vulnerability_intel.py
│ └── whois_lookup.py
│
├── reports/

├── tests/

├── main.py

├── requirements.txt

├── README.md

└── LICENSE


---

# ⚙️ Requirements

- Python 3.12+
- Internet Connection
- Windows / Linux

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/jayitape/CyberReconAI.git
Enter Directory
cd CyberReconAI
Create Virtual Environment
Windows
python -m venv venv

Activate:

venv\Scripts\activate
Linux
python3 -m venv venv

Activate:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
🚀 Running CyberRecon AI

Basic Scan:

python main.py --url google.com

Usage:

python main.py --url <target>

Example:

python main.py --url example.com
📊 Generated Reports

After every successful scan CyberRecon AI generates:

HTML Report

Includes:

Executive Summary
Target Information
WHOIS Data
DNS Records
SSL Analysis
HTTP Headers
Technologies
Ports
Services
Vulnerabilities
Risk Assessment
JSON Report

Contains:

Scan Metadata
Scan ID
Scan Duration
Target Details
Security Findings
Vulnerability Intelligence
Risk Score
PDF Report

Professional security assessment document containing:

Security Summary
Technical Findings
Risk Classification
Recommendations
Assessment Details
🔧 Logging

CyberRecon AI provides enterprise logging for:

Scan Start
Scan Completion
API Requests
Cache Events
Errors
Report Generation
🧩 Modules Overview
Module	Description
banner.py	Startup banner
cli.py	CLI argument handling
target.py	Target validation
whois_lookup.py	WHOIS intelligence
dns_lookup.py	DNS enumeration
ssl_checker.py	SSL/TLS analysis
http_headers.py	HTTP security headers
technology_detector.py	Technology detection
subdomain_enum.py	Subdomain discovery
port_scanner.py	TCP port scanning
service_detector.py	Service detection
robots_analyzer.py	robots.txt analysis
nvd_client.py	NVD integration
vulnerability_intel.py	Vulnerability correlation
risk_engine.py	Risk calculation
report_generator.py	HTML reports
json_report.py	JSON reports
pdf_generator.py	PDF reports
ui.py	Enterprise Rich dashboard
concurrent.py	Concurrent processing
cache_manager.py	Intelligence caching
version.py	Version management
logger.py	Logging framework
🛠️ Technologies Used
Language
Python 3.12+
Libraries
requests
rich
dnspython
python-whois
beautifulsoup4
Wappalyzer
jinja2
playwright
Development Tools
VS Code
Git
GitHub
mypy
pytest
📊 Security Coverage

CyberRecon AI currently performs:

✅ WHOIS Enumeration
✅ DNS Enumeration
✅ SSL/TLS Inspection
✅ HTTP Header Analysis
✅ Technology Detection
✅ Subdomain Discovery
✅ Port Scanning
✅ Service Detection
✅ robots.txt Analysis
✅ NVD CVE Intelligence
✅ Risk Assessment
✅ Professional Reporting

🚀 Roadmap
✅ Version 1.1.0

Completed:

Enterprise Rich UI Dashboard
Concurrent Processing Framework
Improved Risk Visualization
Enhanced Reporting Workflow
Type Hardening
Production-ready Architecture
🔜 Version 1.2.0

Planned:

EPSS Integration
CISA KEV Integration
ExploitDB Intelligence
AI Risk Analysis
Advanced Vulnerability Correlation
Additional Security Checks
⚡ Performance Features
Modular design
Intelligent caching
Concurrent execution
Reduced API requests
Clean error handling
Type-safe development
📈 Current Project Status
Component	Status
Target Analysis	✅ Complete
WHOIS Lookup	✅ Complete
DNS Enumeration	✅ Complete
SSL Analysis	✅ Complete
HTTP Headers	✅ Complete
Technology Detection	✅ Complete
Subdomain Enumeration	✅ Complete
Port Scanner	✅ Complete
Service Detection	✅ Complete
robots.txt Analyzer	✅ Complete
NVD Integration	✅ Complete
Vulnerability Intelligence	✅ Complete
Risk Engine	✅ Complete
HTML Report	✅ Complete
JSON Report	✅ Complete
PDF Report	✅ Complete
Enterprise UI	✅ Complete
Concurrent Processing	✅ Complete
mypy Type Hardening	✅ Complete
🤝 Contributing

Contributions are welcome.

Please ensure:

Type hints included
Code follows project architecture
mypy checks pass
Documentation updated
📜 License

MIT License

👨‍💻 Author

Jay Itape

Electronics & Telecommunication Engineering Student
Cybersecurity Enthusiast
CEH Candidate

GitHub:

https://github.com/jayitape

<p align="center">

CyberRecon AI v1.1.0

Enterprise Website Security Assessment Toolkit

Developed with ❤️ in Python

© 2026 Jay Itape

</p>