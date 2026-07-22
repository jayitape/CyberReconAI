"""
SSL/TLS Certificate Analyzer Module

This module analyzes HTTPS certificates
for authorized security assessments only.

Features:
- Certificate issuer detection
- Subject detection
- Validity dates
- Expiry calculation
- TLS version detection
- Cipher strength evaluation
"""

import socket
import ssl
from datetime import datetime
from typing import Any, Dict, Optional, cast

from modules.logger import setup_logger


logger = setup_logger()


def get_certificate_status(days_remaining: Optional[int]) -> str:
    """
    Determine certificate validity status.

    Args:
        days_remaining: Remaining certificate validity days.

    Returns:
        Certificate status.
    """

    if days_remaining is None:
        return "UNKNOWN"

    if days_remaining < 0:
        return "EXPIRED"

    if days_remaining < 30:
        return "CRITICAL"

    if days_remaining < 90:
        return "WARNING"

    return "VALID"


def evaluate_tls_security(tls_version: Optional[str]) -> str:
    """
    Evaluate TLS security strength.

    Args:
        tls_version: TLS protocol version.

    Returns:
        TLS security rating.
    """

    if tls_version == "TLSv1.3":
        return "STRONG"

    if tls_version == "TLSv1.2":
        return "GOOD"

    return "WEAK"


def evaluate_cipher_strength(cipher: str) -> str:
    """
    Evaluate cipher security strength.

    Args:
        cipher: Cipher suite name.

    Returns:
        Cipher strength rating.
    """

    weak_keywords = [
        "RC4",
        "DES",
        "3DES",
        "NULL",
        "MD5",
    ]

    cipher_name = cipher.upper()

    for keyword in weak_keywords:
        if keyword in cipher_name:
            return "WEAK"

    strong_keywords = [
        "AES256",
        "AES_256",
        "CHACHA20",
        "AESGCM",
    ]

    for keyword in strong_keywords:
        if keyword in cipher_name:
            return "STRONG"

    return "MODERATE"


def get_certificate(domain: str) -> Dict[str, Any]:
    """
    Retrieve SSL certificate information.

    Args:
        domain:
            Target domain.

    Returns:
        Certificate analysis dictionary.
    """

    certificate_info: Dict[str, Any] = {}

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain, 443),
            timeout=15,
        ) as connection:

            with context.wrap_socket(
                connection,
                server_hostname=domain,
            ) as ssl_socket:

                certificate = ssl_socket.getpeercert()

                tls_version = ssl_socket.version()

                cipher_data = ssl_socket.cipher()

                cipher_suite = (
                    cipher_data[0]
                    if cipher_data
                    else "Unknown"
                )


                if not certificate:

                    logger.warning(
                        "No SSL certificate data received for %s",
                        domain,
                    )

                    return {}


                subject_data = cast(
                    tuple[tuple[tuple[str, str], ...], ...],
                    certificate.get("subject", ()),
                    )
                    
                subject_name = "Unknown"
                
                for group in subject_data:
                    for attribute in group:
                        key, value = attribute
                        if key == "commonName":
                            
                            subject_name = value
                            break



                issuer_data = cast(
                    tuple[tuple[tuple[str, str], ...], ...],
                    certificate.get("issuer", ()),
                    )

                issuer_org = "Unknown"
                issuer_cn = ""


                for group in issuer_data:

                    for attribute in group:

                        key, value = attribute

                        if key == "organizationName":

                            issuer_org = value

                        elif key == "commonName":

                            issuer_cn = value



                issuer_name = issuer_org

                if issuer_cn:

                    issuer_name = (
                        f"{issuer_org} ({issuer_cn})"
                    )



                valid_from = str(
                    certificate.get(
                        "notBefore",
                        "Unknown",
                    )
                )

                valid_until = str(
                    certificate.get(
                        "notAfter",
                        "Unknown",
                    )
                )



        days_remaining: Optional[int] = None


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

            "certificate_status": get_certificate_status(
                days_remaining
            ),

            "tls_version": tls_version,

            "tls_security": evaluate_tls_security(
                tls_version
            ),

            "cipher_suite": cipher_suite,

            "cipher_strength": evaluate_cipher_strength(
                cipher_suite
            ),

        }


        logger.info(
            "SSL certificate analysis completed for %s",
            domain,
        )


    except ssl.SSLError as error:

        logger.error(
            "SSL error: %s",
            error,
        )


    except socket.timeout:

        logger.error(
            "SSL connection timeout for %s",
            domain,
        )


    except Exception as error:

        logger.exception(
            "Certificate analysis failed: %s",
            error,
        )


    return certificate_info



def get_ssl_info(domain: str) -> Dict[str, Any]:
    """
    Public SSL analysis function.

    Args:
        domain:
            Target domain.

    Returns:
        SSL information.
    """

    return get_certificate(domain)