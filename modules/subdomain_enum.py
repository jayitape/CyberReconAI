"""
CyberRecon AI

Subdomain Enumeration Module

Discovers subdomains using Certificate Transparency logs
and validates them through DNS resolution.

Authorized security assessments only.
"""

import json
import socket
from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor

import requests

from modules.logger import setup_logger

logger = setup_logger()


class SubdomainEnumerator:
    """
    Performs subdomain enumeration.
    """

    def __init__(self, domain: str):
        """
        Initialize subdomain enumerator.

        Args:
            domain (str):
                Target domain.
        """

        self.domain = domain

        self.subdomains: List[str] = []

        self.active_subdomains: Dict[str, str] = {}

    def fetch_certificate_logs(self) -> List[str]:
        """
        Fetch subdomains from crt.sh Certificate Transparency logs.

        Returns:
            List[str]:
                Discovered subdomains.
        """

        discovered = []

        try:

            url = f"https://crt.sh/?q=%25.{self.domain}" "&output=json"

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 Chrome/138.0 Safari/537.36"
                        ),
                        },
                        )

            response.raise_for_status()

            certificates = response.json()

            for certificate in certificates:

                names = certificate.get("name_value", "")

                for name in names.split("\n"):
                    name = name.strip()
                    
                    if not name:
                        continue
                    # Skip email addresses
                    
                    if "@" in name:
                        logger.debug("Skipping email entry: %s", name)
                        continue
                    
                    if name.startswith("*."):
                        name = name[2:]
                        
                        
                    if name.endswith(self.domain) and name not in discovered:
                        discovered.append(name)

            logger.info("Certificate transparency lookup completed")

        except requests.RequestException as error:

            logger.warning("crt.sh request failed: %s", error)

        except json.JSONDecodeError:

            logger.warning("Invalid JSON response from crt.sh")

        except Exception as error:

            logger.exception("Subdomain discovery error: %s", error)

        return discovered

    def fetch_alienvault(self) -> List[str]:
        """
        Fetch subdomains from AlienVault OTX.
        """
        discovered: List[str] = []
        try:
            url = (
                f"https://otx.alienvault.com/api/v1/"
                f"indicators/domain/{self.domain}/passive_dns"
                )
                
            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 "
                        "(Windows NT 10.0; Win64; x64)"
                        )
                        },
                        )
            
            response.raise_for_status()
            
            data = response.json()
            
            for record in data.get("passive_dns", []):
                
                hostname = record.get("hostname", "").strip()
                
                if (
                    hostname.endswith(self.domain)
                    and hostname not in discovered
                    ):
                    
                    discovered.append(hostname)
                    
                    logger.info("AlienVault lookup completed")
                    
        except requests.RequestException as error:
            
            logger.warning("AlienVault request failed: %s", error)
            
        except json.JSONDecodeError:
            
            logger.warning("AlienVault returned invalid JSON")

        except Exception as error:
            
            logger.exception("AlienVault lookup error: %s", error)

        return discovered

    def resolve_subdomain(self, subdomain: str) -> str:
        """
        Resolve subdomain IP address.

        Args:
            subdomain (str):
                Subdomain name.

        Returns:
            str:
                IP address or Unknown.
        """

        try:

            ip_address = socket.gethostbyname(subdomain)

            return ip_address

        except socket.gaierror:

            return "Unknown"

        except Exception as error:

            logger.warning("DNS resolution error %s: %s", subdomain, error)

            return "Unknown"

    def validate_subdomains(self, subdomains: List[str]) -> Dict[str, str]:
        """
        Validate discovered subdomains.

        Args:
            subdomains (List[str]):
                List of subdomains.

        Returns:
            Dict[str, str]:
                Active subdomains with IP.
        """

        active = {}

        for subdomain in subdomains:

            ip_address = self.resolve_subdomain(subdomain)

            if ip_address != "Unknown":

                active[subdomain] = ip_address

                logger.info("Active subdomain found: %s", subdomain)

        return active

    def enumerate(self) -> Dict[str, object]:
        """
        Perform complete subdomain enumeration.

        Returns:
            Dict[str, object]:
                Enumeration results.
        """

        logger.info("Starting subdomain enumeration for %s", self.domain)

        crt_results = self.fetch_certificate_logs()
        
        otx_results = self.fetch_alienvault()
        
        self.subdomains = sorted(
            
            set(crt_results + otx_results)
            )

        self.active_subdomains = self.validate_subdomains(self.subdomains)

        result = {
            "domain": self.domain,
            "total_found": len(self.subdomains),
            "subdomains": self.subdomains,
            "active": self.active_subdomains,
        }

        logger.info("Subdomain enumeration completed")

        return result


def get_subdomains(domain: str) -> Dict[str, object]:
    """
    Public function for subdomain enumeration.

    Args:
        domain (str):
            Target domain.

    Returns:
        Dict[str, object]:
            Subdomain report.
    """

    enumerator = SubdomainEnumerator(domain)

    return enumerator.enumerate()
