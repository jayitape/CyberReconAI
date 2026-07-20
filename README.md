# 🛡️ CyberRecon AI

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Version](https://img.shields.io/badge/Version-v1.0.20-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Type Checked](https://img.shields.io/badge/mypy-100%25%20Clean-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

</p>

---

# 🚀 CyberRecon AI

**CyberRecon AI** is a modular, enterprise-inspired **Website Security Assessment Toolkit** developed in Python for **authorized defensive security assessments**.

It automates reconnaissance, collects security intelligence from multiple sources, performs vulnerability analysis, calculates a security risk score, and generates professional HTML, JSON, and PDF reports.

The project follows a clean modular architecture with enterprise logging, intelligent caching, and strong type safety using **mypy**.

---

# ✨ Key Features

## 🌐 Target Intelligence

- Domain Analysis
- WHOIS Lookup
- DNS Enumeration
- Subdomain Enumeration

## 🔒 Security Assessment

- SSL/TLS Certificate Analysis
- HTTP Security Header Analysis
- robots.txt Analysis
- Open Port Scanning
- Service Detection

## 🧠 Vulnerability Intelligence

- National Vulnerability Database (NVD) Integration
- CPE-based Vulnerability Lookup
- CVSS Information Extraction
- Vulnerability Intelligence Engine

## 📊 Risk Analysis

- Security Risk Score Calculation
- Risk Level Classification
- Findings Summary
- Security Recommendations

## 📄 Reporting

- Professional HTML Report
- JSON Report Export
- Scan Metadata
- Scan Duration
- Scan ID Generation
- Enterprise PDF Report Generation

## ⚙️ Enterprise Features

- Modular Project Architecture
- Enterprise Logging
- JSON Cache Manager
- Type Hints
- mypy Type Safety
- Production-ready Code

---

# 🏗️ Architecture

```
                    +----------------------+
                    |      User / CLI      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Target Analysis    |
                    +----------+-----------+
                               |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
+---------------+      +---------------+      +---------------+
| WHOIS Lookup  |      | DNS Analysis  |      | SSL Analysis  |
+---------------+      +---------------+      +---------------+
        |                      |                      |
        +----------------------+----------------------+
                               |
                               v
                    +----------------------+
                    | HTTP Header Analysis |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Technology Detection |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Subdomain Discovery  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Port & Service Scan  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | NVD Intelligence     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Risk Engine          |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |HTML+JSON+PDF Reports |
                    +----------------------+
```

---

# 🎯 Project Objectives

CyberRecon AI is designed to:

- Automate website reconnaissance
- Collect security intelligence from multiple sources
- Detect common security weaknesses
- Analyze publicly available vulnerability information
- Generate professional assessment reports
- Demonstrate enterprise Python development practices
- Provide a modular foundation for future security intelligence integrations

---

# ⭐ Project Highlights

- Enterprise-inspired modular architecture
- Professional logging system
- Intelligent caching mechanism
- Strong type safety (100% mypy clean)
- - Professional HTML, JSON & PDF reports
- Easy to extend with future intelligence modules
- Clean and maintainable Python code
- Production-ready project structure

---

## ⚠️ Disclaimer

CyberRecon AI is intended **only for authorized defensive security assessments and educational purposes**.

Do **not** use this tool against systems, networks, or applications without explicit permission from the owner.

The author is not responsible for any misuse of this software.
# 📂 Project Structure

```
CyberReconAI/
│
├── cache/
│   ├── nvd_cache.json
│   └── ...
│
├── modules/
│   ├── banner.py
│   ├── cache_manager.py
│   ├── cli.py
│   ├── dns_lookup.py
│   ├── http_headers.py
│   ├── json_report.py
│   ├── logger.py
│   ├── nvd_client.py
│   ├── port_scanner.py
│   ├── report_generator.py
│   ├── risk_engine.py
│   ├── robots_analyzer.py
│   ├── scan_id.py
│   ├── scan_timer.py
│   ├── service_detector.py
│   ├── ssl_checker.py
│   ├── subdomain_enum.py
│   ├── target.py
│   ├── technology_detector.py
│   ├── vulnerability_intel.py
│   └── whois_lookup.py
│
├── reports/
│
├── screenshots/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Requirements

- Python 3.12+
- Internet Connection
- Windows or Linux

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/jayitape/CyberReconAI.git
```

## 2. Navigate to the Project

```bash
cd CyberReconAI
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running CyberRecon AI

Basic Scan

```bash
python main.py --url google.com
```

Example

```bash
python main.py --url example.com
```

---

# 💻 Command Line Usage

```
python main.py --url <target>
```

Example

```
python main.py --url google.com
```

---

# 📋 Example Console Output

```
Target              : google.com

Security Score      : 91/100

Risk Level          : LOW

Open Ports          : 2

Detected Services

• HTTPS
• HTTP

Technologies

• Nginx
• HTTP/2
• TLS 1.3

Reports Generated

reports/google_com_report.html

reports/google_com_report.json

reports/google_com_report.pdf

```

---

# 📊 Generated Reports

CyberRecon AI automatically generates professional reports after every successful scan.

### HTML Report

Includes:

- Executive Summary
- Security Score
- SSL Information
- HTTP Security Headers
- DNS Records
- WHOIS Information
- Technologies
- Open Ports
- Services
- Vulnerabilities
- Risk Assessment

---

### JSON Report

Machine-readable report containing:

- Scan Metadata
- Target Information
- DNS
- WHOIS
- SSL
- HTTP Headers
- Technologies
- Subdomains
- Open Ports
- Services
- Vulnerability Intelligence
- Security Score
- Findings

### PDF Report

Professional PDF security assessment reports generated using the Playwright PDF engine.

Includes:

- Executive Summary
- Target Information
- Security Score
- Risk Level Classification
- Vulnerability Findings
- Technical Assessment Details
- Security Recommendations
- Scan Metadata

---

# 📁 Cache

External intelligence responses are cached to reduce API requests and improve performance.

Current cache sources:

- NVD

Future releases:

- EPSS
- CISA KEV
- ExploitDB

---

# 🔧 Logging

CyberRecon AI provides enterprise-style logging for:

- Scan Start
- Scan Completion
- Cache Hits
- Cache Misses
- API Requests
- Errors
- Report Generation
---

# 🧩 Modules Overview

CyberRecon AI follows a modular architecture where each module has a single responsibility.

| Module | Description |
|---------|-------------|
| `banner.py` | Displays the CyberRecon AI startup banner |
| `cli.py` | Parses command-line arguments |
| `target.py` | Validates and normalizes target URLs/domains |
| `whois_lookup.py` | Retrieves WHOIS information |
| `dns_lookup.py` | Performs DNS enumeration |
| `ssl_checker.py` | Analyzes SSL/TLS certificates |
| `http_headers.py` | Checks HTTP security headers |
| `technology_detector.py` | Detects web technologies |
| `subdomain_enum.py` | Enumerates subdomains |
| `port_scanner.py` | Performs TCP port scanning |
| `service_detector.py` | Identifies running services |
| `robots_analyzer.py` | Analyzes robots.txt |
| `nvd_client.py` | Queries the National Vulnerability Database (NVD) |
| `vulnerability_intel.py` | Correlates vulnerability intelligence |
| `risk_engine.py` | Calculates security score and risk level |
| `report_generator.py` | Generates HTML reports |
| `json_report.py` | Generates JSON reports |
| `pdf_generator.py` | Generates PDF reports using Playwright |
| `scan_id.py` | Creates unique scan IDs |
| `scan_timer.py` | Measures scan duration |
| `cache_manager.py` | Caches external intelligence |
| `logger.py` | Centralized enterprise logging |

---

# 🔄 Scan Workflow

```
User Input
     │
     ▼
Target Validation
     │
     ▼
WHOIS Lookup
     │
     ▼
DNS Enumeration
     │
     ▼
SSL/TLS Analysis
     │
     ▼
HTTP Header Analysis
     │
     ▼
Technology Detection
     │
     ▼
Subdomain Enumeration
     │
     ▼
Port Scanning
     │
     ▼
Service Detection
     │
     ▼
NVD Vulnerability Intelligence
     │
     ▼
Risk Engine
     │
     ▼
HTML + JSON Reports
```

---

# 🛠️ Technologies Used

### Programming Language

- Python 3.12+

### Python Libraries

- requests
- rich
- dnspython
- python-whois
- beautifulsoup4
- Wappalyzer
- colorama
- jinja2
- playwright

### Development Tools

- Visual Studio Code
- Git
- GitHub
- mypy
- pip
- virtualenv

---

# 📊 Security Assessment Coverage

CyberRecon AI currently performs:

- Domain Intelligence
- WHOIS Enumeration
- DNS Enumeration
- SSL/TLS Inspection
- HTTP Security Header Analysis
- Technology Fingerprinting
- Subdomain Discovery
- TCP Port Scanning
- Service Fingerprinting
- robots.txt Analysis
- NVD CVE Intelligence
- Security Risk Assessment
- Professional Report Generation

---

# 🚀 Roadmap

## ✅ Version 1.0.20

- Modular Architecture
- Professional Logging
- JSON Cache Manager
- NVD Integration
- Vulnerability Intelligence Engine
- HTML Reports
- JSON Reports
- Security Risk Engine
- mypy Type Safety
- Playwright PDF Engine
- Enterprise PDF Report Generation

---

## 🔜 Version 1.1.0

Planned improvements:

- EPSS Integration
- CISA Known Exploited Vulnerabilities (KEV)
- ExploitDB Integration
- Rich Terminal Dashboard
- Improved Technology Detection
- Concurrent Intelligence Collection
- Performance Optimizations

---

# ⚡ Performance Features

- Modular architecture
- Reusable components
- JSON-based caching
- Reduced external API requests
- Enterprise logging
- Type-safe codebase
- Clean error handling
- Maintainable project structure

---

# 🎯 Design Goals

CyberRecon AI is designed to be:

- Easy to use
- Easy to extend
- Modular
- Maintainable
- Type-safe
- Beginner-friendly
- Suitable for learning defensive cybersecurity concepts
- Portfolio-ready

---

# 📈 Current Project Status

| Component | Status |
|-----------|--------|
| Target Analysis | ✅ Complete |
| WHOIS Lookup | ✅ Complete |
| DNS Enumeration | ✅ Complete |
| SSL/TLS Analysis | ✅ Complete |
| HTTP Security Headers | ✅ Complete |
| Technology Detection | ✅ Complete |
| Subdomain Enumeration | ✅ Complete |
| Port Scanner | ✅ Complete |
| Service Detection | ✅ Complete |
| robots.txt Analysis | ✅ Complete |
| NVD Integration | ✅ Complete |
| Vulnerability Intelligence | ✅ Complete |
| Risk Engine | ✅ Complete |
| HTML Report | ✅ Complete |
| JSON Report | ✅ Complete |
| PDF Report | ✅ Complete |
| Playwright PDF Engine | ✅ Complete |
| Enterprise Logging | ✅ Complete |
| Cache Manager | ✅ Complete |
| mypy Type Hardening | ✅ Complete |
---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve CyberRecon AI:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

Please ensure your code:
- Follows the existing project structure
- Includes appropriate type hints
- Passes `mypy` checks
- Maintains code readability and documentation

---

# 🛡️ Responsible Usage

CyberRecon AI is intended for:

- Security learning
- Authorized penetration testing
- Internal security assessments
- Research
- Educational demonstrations

Always obtain explicit permission before scanning any system that you do not own or administer.

---

# 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 🙏 Acknowledgements

CyberRecon AI makes use of publicly available security data and open-source libraries.

Special thanks to:

- National Vulnerability Database (NVD)
- FIRST.org
- Python Software Foundation
- Open-source cybersecurity community

---

# 👨‍💻 Author

**Jay Itape**

- Electronics & Telecommunication Engineering Student
- Cybersecurity Enthusiast
- CEH Candidate
- Pune, Maharashtra, India

### GitHub

https://github.com/jayitape

---

# 📬 Contact

For suggestions, improvements, or collaboration, feel free to open an Issue or Pull Request on GitHub.

---

# ⭐ Support the Project

If you found this project useful:

⭐ Star this repository

🍴 Fork the project

🐛 Report bugs

💡 Suggest new features

Your support helps improve CyberRecon AI and encourages future development.

---

# 🗺️ Future Vision

CyberRecon AI will continue evolving with additional security intelligence capabilities, including:

- EPSS Integration
- CISA KEV Integration
- ExploitDB Intelligence
- Rich Terminal Dashboard
- Concurrent Intelligence Collection
- Additional Security Checks
- Expanded Reporting Features

---

# ⚠️ Disclaimer

CyberRecon AI is provided **for educational purposes and authorized defensive security assessments only**.

The author is **not responsible** for any misuse, unauthorized scanning, or illegal activities performed using this software.

Users are solely responsible for ensuring compliance with all applicable laws, regulations, and organizational policies before using this tool.

---

<p align="center">

**CyberRecon AI v1.0.20**

Enterprise-Inspired Website Security Assessment Toolkit

Developed with ❤️ in Python

© 2026 Jay Itape

</p>