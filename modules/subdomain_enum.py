"""
CyberRecon AI

Subdomain Enumeration Module

Discovers subdomains using Certificate Transparency logs
and validates them through DNS resolution.

Authorized security assessments only.
"""


from typing import Dict, List

import json
import socket

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

            url = (
                f"https://crt.sh/?q=%25.{self.domain}"
                "&output=json"
            )


            response = requests.get(

                url,

                timeout=20

            )


            response.raise_for_status()



            certificates = response.json()



            for certificate in certificates:


                names = certificate.get(
                    "name_value",
                    ""
                )


                for name in names.split("\n"):


                    name = name.strip()


                    if name.startswith(
                        "*."
                    ):

                        name = name[2:]



                    if (

                        name.endswith(
                            self.domain
                        )

                        and name not in discovered

                    ):

                        discovered.append(
                            name
                        )



            logger.info(
                "Certificate transparency lookup completed"
            )


        except requests.RequestException as error:


            logger.error(
                "crt.sh request failed: %s",
                error
            )


        except json.JSONDecodeError:


            logger.error(
                "Invalid JSON response from crt.sh"
            )


        except Exception as error:


            logger.exception(
                "Subdomain discovery error: %s",
                error
            )



        return discovered




    def resolve_subdomain(
        self,
        subdomain: str
    ) -> str:
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


            ip_address = socket.gethostbyname(
                subdomain
            )


            return ip_address



        except socket.gaierror:


            return "Unknown"



        except Exception as error:


            logger.error(
                "DNS resolution error %s: %s",
                subdomain,
                error
            )


            return "Unknown"




    def validate_subdomains(
        self,
        subdomains: List[str]
    ) -> Dict[str, str]:
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


            ip_address = self.resolve_subdomain(
                subdomain
            )



            if ip_address != "Unknown":


                active[subdomain] = ip_address



                logger.info(
                    "Active subdomain found: %s",
                    subdomain
                )



        return active




    def enumerate(self) -> Dict[str, object]:
        """
        Perform complete subdomain enumeration.

        Returns:
            Dict[str, object]:
                Enumeration results.
        """


        logger.info(
            "Starting subdomain enumeration for %s",
            self.domain
        )



        self.subdomains = (
            self.fetch_certificate_logs()
        )



        self.active_subdomains = (
            self.validate_subdomains(
                self.subdomains
            )
        )



        result = {


            "domain":
            self.domain,


            "total_found":
            len(
                self.subdomains
            ),


            "subdomains":
            self.subdomains,


            "active":
            self.active_subdomains

        }



        logger.info(
            "Subdomain enumeration completed"
        )



        return result




def get_subdomains(
    domain: str
) -> Dict[str, object]:
    """
    Public function for subdomain enumeration.

    Args:
        domain (str):
            Target domain.

    Returns:
        Dict[str, object]:
            Subdomain report.
    """


    enumerator = SubdomainEnumerator(
        domain
    )


    return enumerator.enumerate()