"""
CyberRecon AI
WHOIS Lookup Module

Retrieves WHOIS information for authorized reconnaissance purposes.
"""

from __future__ import annotations

import whois


def get_whois_info(domain: str) -> dict:
    """
    Retrieve WHOIS information for a domain.

    Args:
        domain: Target domain name.

    Returns:
        Dictionary containing WHOIS information.
    """

    try:
        data = whois.whois(domain)

        return {
            "domain": domain,
            "registrar": data.registrar,
            "creation_date": data.creation_date,
            "expiration_date": data.expiration_date,
            "updated_date": data.updated_date,
            "name_servers": data.name_servers,
        }

    except Exception as error:
        return {
            "domain": domain,
            "error": str(error),
        }
