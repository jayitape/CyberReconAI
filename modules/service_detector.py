"""
CyberRecon AI
Service Detection Module

Detects the service running on open ports.

Author: CyberRecon AI
"""

from typing import Dict, List


# Common TCP services
COMMON_SERVICES = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT",
}


def detect_services(open_ports: List[Dict]) -> List[Dict]:
    """
    Detect services running on open ports.

    Args:
        open_ports: List returned from port_scanner module.

    Returns:
        List of detected services.
    """

    detected = []

    for port_info in open_ports:

        port = port_info.get("port")

        service = COMMON_SERVICES.get(port, "Unknown")

        detected.append(
            {
                "port": port,
                "service": service,
                "state": port_info.get("state", "OPEN"),
            }
        )

    return detected