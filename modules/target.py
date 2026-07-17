"""
CyberRecon AI
Target Intelligence Module

Handles:
- URL normalization
- Domain extraction
- IP resolution
- Connectivity testing
"""

from __future__ import annotations

import socket
from urllib.parse import urlparse

import requests


def normalize_url(url: str) -> str:
    """
    Normalize target URL.

    Example:
        google.com -> https://google.com
    """

    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    return url


def extract_domain(url: str) -> str:
    """
    Extract domain from URL.
    """

    parsed = urlparse(url)
    return parsed.netloc


def resolve_ip(domain: str) -> str:
    """
    Resolve domain to IP address.
    """

    return socket.gethostbyname(domain)


def check_connectivity(url: str, timeout: int = 5) -> bool:
    """
    Check whether target is reachable.
    """

    try:
        response = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True,
        )

        return response.status_code < 500

    except requests.RequestException:
        return False


def get_target_info(url: str) -> dict:
    """
    Collect target information.
    """

    url = normalize_url(url)

    domain = extract_domain(url)

    ip_address = resolve_ip(domain)

    reachable = check_connectivity(url)

    return {
        "url": url,
        "domain": domain,
        "ip": ip_address,
        "reachable": reachable,
        "scheme": urlparse(url).scheme,
    }