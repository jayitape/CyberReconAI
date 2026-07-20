"""
CyberRecon AI
Risk Scoring Engine Module

Version: 1.0.15

Purpose:
Generate overall security risk score
from reconnaissance findings
"""

import logging

logger = logging.getLogger("CyberReconAI")


def calculate_security_score(
    headers=None, ssl_info=None, robots_info=None, ports=None, subdomains=None
):
    """
    Calculate security score based on findings
    """

    score = 100
    findings = []

    # ==========================
    # HTTP Security Headers
    # ==========================

    if headers:

        missing = headers.get("missing_headers", [])

        for header in missing:

            score -= 5

            findings.append(
                {"risk": "LOW", "issue": f"Missing security header: {header}"}
            )

    # ==========================
    # SSL Certificate
    # ==========================

    if ssl_info:

        days = ssl_info.get("days_remaining", 0)

        if days < 30:

            score -= 15

            findings.append({"risk": "HIGH", "issue": "SSL certificate expires soon"})

        elif days < 90:

            score -= 5

            findings.append(
                {"risk": "LOW", "issue": "SSL certificate expiry within 90 days"}
            )

    # ==========================
    # Robots.txt Analysis
    # ==========================

    if robots_info:

        sensitive = robots_info.get("summary", {}).get("sensitive_findings", 0)

        if sensitive > 0:

            score -= 10

            findings.append(
                {
                    "risk": "MEDIUM",
                    "issue": f"{sensitive} sensitive path(s) exposed in robots.txt",
                }
            )

    # ==========================
    # Open Ports
    # ==========================

    if ports:

        if len(ports) > 5:

            score -= 10

            findings.append({"risk": "MEDIUM", "issue": "Multiple open ports detected"})

    # ==========================
    # Subdomains
    # ==========================

    if subdomains:

        if len(subdomains) > 100:

            score -= 5

            findings.append(
                {"risk": "LOW", "issue": "Large subdomain footprint detected"}
            )

    # Prevent negative score

    if score < 0:
        score = 0

    # Risk Level

    if score >= 80:

        risk_level = "LOW"

    elif score >= 50:

        risk_level = "MEDIUM"

    else:

        risk_level = "HIGH"

    logger.info("Security risk score generated")

    return {"score": score, "risk_level": risk_level, "findings": findings}
