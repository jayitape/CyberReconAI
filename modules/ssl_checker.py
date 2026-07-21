"""
SSL/TLS Certificate Analyzer Module

This module analyzes HTTPS certificates
for authorized security assessments only.

Features:
- Certificate issuer detection
- Subject detection
- Validity dates
- Expiry calculation
"""

import socket
import ssl
from datetime import datetime
from typing import Any, Dict

from modules.logger import setup_logger

logger = setup_logger()


def get_certificate(domain: str) -> Dict[str, Any]:
    """
    Retrieve SSL certificate information.

    Args:
        domain (str): Target domain.

    Returns:
        Dict[str, Any]: Certificate information.
    """

    certificate_info: Dict[str, Any] = {}

    try:

        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=15) as connection:

            with context.wrap_socket(connection, server_hostname=domain) as ssl_socket:

                certificate = ssl_socket.getpeercert()

                tls_version = ssl_socket.version()

                cipher = ssl_socket.cipher()
                
                cipher_suite = cipher[0] if cipher else "Unknown"
                
                if not certificate:
                    logger.warning(
                        
                        "No SSL certificate data received for %s",
                        domain,
                        )
                    return {}
                
                
                subject: tuple[Any, ...] = certificate.get(
                     "subject",
                     (),
                     
                     )
                
                subject_name = "Unknown"
                
                for group in subject:
                    for attribute in group:
                        key, value = attribute
                        if key == "commonName":
                            subject_name = value
                            
                            break

                issuer: tuple[Any, ...] = certificate.get(
                     "issuer",
                     (),
                     )
                     
                issuer_org = "Unknown"
                
                issuer_cn = ""
                for group in issuer:
                    for attribute in group:
                         key, value = attribute
                         
                         if key == "organizationName":
                            issuer_org = value
                         elif key == "commonName":
                            issuer_cn = value
                            
                issuer_name = issuer_org
                if issuer_cn:
                    
                    issuer_name = f"{issuer_org} ({issuer_cn})"

                valid_from: str = str(
                          certificate.get(
                               "notBefore",
                               "Unknown",
                               )
                               )
                
                valid_until: str = str(
                    certificate.get(
                        "notAfter",
                        "Unknown",
                        )
                        )

        days_remaining = None
        
        if valid_until != "Unknown":
            
            expiry_date = datetime.strptime(
                valid_until,
                "%b %d %H:%M:%S %Y %Z",
                )
            current_date = datetime.utcnow()
            
            days_remaining = (
                expiry_date - current_date
                ).days
            
        certificate_info = {
                "subject": subject_name,
                "issuer": issuer_name,
                "valid_from": valid_from,
                "valid_until": valid_until,
                "days_remaining": days_remaining,
                "tls_version": tls_version,
                "cipher_suite": cipher_suite,
                }
            
        logger.info("SSL certificate analysis completed for %s", domain)

    except ssl.SSLError as error:

        logger.error("SSL error: %s", error)

    except socket.timeout:

        logger.error("SSL connection timeout for %s", domain)

    except Exception as error:

        logger.exception("Certificate analysis failed: %s", error)

    return certificate_info


def get_ssl_info(domain: str) -> Dict[str, Any]:
    """
    Public function for SSL analysis.

    Args:
        domain (str): Target domain.

    Returns:
        Dict[str, Any]: SSL information.
    """

    return get_certificate(domain)
