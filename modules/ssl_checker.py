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

from datetime import datetime
from typing import Dict, Any
import socket
import ssl

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

    certificate_info = {}


    try:

        context = ssl.create_default_context()


        with socket.create_connection(
            (domain, 443),
            timeout=5
        ) as connection:


            with context.wrap_socket(
                connection,
                server_hostname=domain
            ) as ssl_socket:


                certificate = ssl_socket.getpeercert()



        subject = certificate.get(
            "subject",
            []
        )


        issuer = certificate.get(
            "issuer",
            []
        )


        valid_from = certificate.get(
            "notBefore",
            "Unknown"
        )


        valid_until = certificate.get(
            "notAfter",
            "Unknown"
        )


        expiry_date = datetime.strptime(
            valid_until,
            "%b %d %H:%M:%S %Y %Z"
        )


        current_date = datetime.utcnow()


        days_remaining = (
            expiry_date - current_date
        ).days



        certificate_info = {

            "subject": subject,

            "issuer": issuer,

            "valid_from": valid_from,

            "valid_until": valid_until,

            "days_remaining": days_remaining

        }


        logger.info(
            "SSL certificate analysis completed for %s",
            domain
        )


    except ssl.SSLError as error:

        logger.error(
            "SSL error: %s",
            error
        )


    except socket.timeout:

        logger.error(
            "SSL connection timeout for %s",
            domain
        )


    except Exception as error:

        logger.exception(
            "Certificate analysis failed: %s",
            error
        )


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