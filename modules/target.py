"""
Target Intelligence Module

Performs basic target information gathering
for authorized security assessments only.

Features:
- URL normalization
- URL validation
- Domain extraction
- IP resolution
- Website connectivity check
"""


from typing import Dict
from urllib.parse import urlparse

import socket

import requests

from modules.logger import setup_logger


logger = setup_logger()



def normalize_url(url: str) -> str:
    """
    Normalize target URL.

    Args:
        url (str): User provided URL.

    Returns:
        str: Normalized URL.
    """

    if not url.startswith(
        ("http://", "https://")
    ):
        url = "https://" + url


    return url



def validate_url(url: str) -> bool:
    """
    Validate URL format.

    Args:
        url (str): Target URL.

    Returns:
        bool: True if valid else False.
    """

    try:

        parsed_url = urlparse(url)


        if parsed_url.netloc:
            return True


        return False


    except Exception as error:

        logger.error(
            "URL validation failed: %s",
            error
        )

        return False



def extract_domain(url: str) -> str:
    """
    Extract domain from URL.

    Args:
        url (str): Target URL.

    Returns:
        str: Domain name.
    """

    parsed_url = urlparse(url)


    return parsed_url.netloc



def resolve_ip(domain: str) -> str:
    """
    Resolve domain IP address.

    Args:
        domain (str): Target domain.

    Returns:
        str: IP address.
    """

    try:

        ip_address = socket.gethostbyname(
            domain
        )


        logger.info(
            "IP resolved for %s : %s",
            domain,
            ip_address
        )


        return ip_address



    except socket.gaierror:


        logger.warning(
            "Unable to resolve IP for %s",
            domain
        )


        return "Unknown"



def check_connectivity(url: str) -> bool:
    """
    Check website availability.

    Args:
        url (str): Target URL.

    Returns:
        bool: Reachability status.
    """

    try:

        headers = {

            "User-Agent":
            "Mozilla/5.0 CyberReconAI Security Assessment"

        }


        response = requests.get(

            url,

            headers=headers,

            timeout=10,

            allow_redirects=True

        )


        logger.info(
            "Target reachable: %s | Status Code: %s",
            url,
            response.status_code
        )


        return True



    except requests.exceptions.Timeout:


        logger.warning(
            "Connection timeout: %s",
            url
        )


        return False



    except requests.exceptions.ConnectionError:


        logger.warning(
            "Connection failed: %s",
            url
        )


        return False



    except requests.RequestException as error:


        logger.error(
            "Request error: %s",
            error
        )


        return False



def analyze_target(url: str) -> Dict[str, str]:
    """
    Perform complete target intelligence analysis.

    Args:
        url (str): Target URL.

    Returns:
        Dict[str, str]: Target information.
    """

    logger.info(
        "Starting target analysis"
    )


    normalized_url = normalize_url(
        url
    )


    if not validate_url(
        normalized_url
    ):

        raise ValueError(
            "Invalid URL provided"
        )



    domain = extract_domain(
        normalized_url
    )


    ip_address = resolve_ip(
        domain
    )


    reachable = check_connectivity(
        normalized_url
    )



    target_info = {

        "url":
        normalized_url,


        "domain":
        domain,


        "ip":
        ip_address,


        "scheme":
        urlparse(
            normalized_url
        ).scheme,


        "reachable":
        str(reachable)

    }



    logger.info(
        "Target analysis completed"
    )


    return target_info