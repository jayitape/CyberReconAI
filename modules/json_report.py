"""
CyberRecon AI
Professional JSON Report Generator
Version: 1.1.0
"""

import json
import os
from datetime import datetime


def generate_json_report(scan_data, filename):
    """
    Generate SOC Analyst friendly JSON Report
    """

    os.makedirs("reports", exist_ok=True)

    report_path = os.path.join("reports", filename)

    json_report = {
        "cyberrecon_ai": {
            "tool_name": "CyberRecon AI",
            "version": "1.1.0",
            "generated_by": "CyberRecon AI - Authorized Defensive Security Assessment Toolkit",
            "scan_information": {
                "timestamp": datetime.utcnow().isoformat(),
                "scan_id": scan_data.get("scan_id", "N/A"),
                "target": scan_data.get("target", {}),
            },
            "reconnaissance": {
                "whois": scan_data.get("whois", {}),
                "dns": scan_data.get("dns", {}),
                "ssl_tls": scan_data.get("ssl", {}),
                "http_headers": scan_data.get("headers", {}),
                "technology_detection": scan_data.get("technology", {}),
                "subdomains": scan_data.get("subdomains", []),
                "robots_txt": scan_data.get("robots", {}),
            },
            "network_assessment": {
                "ports": scan_data.get("ports", []),
                "services": scan_data.get("services", []),
            },
            "security_assessment": {
                "risk_score": scan_data.get("risk_score", 0),
                "risk_level": scan_data.get("risk_level", "UNKNOWN"),
                "vulnerability_findings": scan_data.get("findings", []),
            },
            "status": "Scan completed successfully.",
        }
    }

    with open(report_path, "w", encoding="utf-8") as file:

        json.dump(json_report, file, indent=4, ensure_ascii=False)

    return report_path
