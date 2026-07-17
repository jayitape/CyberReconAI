"""
DNS Enumeration Module

Performs DNS record enumeration for
authorized security assessments.

Supported Records:
- A
- AAAA
- MX
- NS
- TXT
- CNAME
"""

from typing import Dict, List

import dns.resolver

from modules.logger import setup_logger


logger = setup_logger()



class DNSEnumerator:
    """
    Handles DNS record enumeration.
    """

    def __init__(self, domain: str):
        """
        Initialize DNS Enumerator.

        Args:
            domain (str): Target domain.
        """

        self.domain = domain

        self.records: Dict[str, List[str]] = {

            "A": [],
            "AAAA": [],
            "MX": [],
            "NS": [],
            "TXT": [],
            "CNAME": []

        }



    def query_record(self, record_type: str) -> List[str]:
        """
        Query DNS record.

        Args:
            record_type (str): DNS record type.

        Returns:
            List[str]: DNS values.
        """

        results = []


        try:

            answers = dns.resolver.resolve(
                self.domain,
                record_type
            )


            for answer in answers:

                results.append(
                    answer.to_text()
                )


            logger.info(
                "%s record lookup successful",
                record_type
            )


        except dns.resolver.NoAnswer:

            logger.warning(
                "No %s record found",
                record_type
            )


        except dns.resolver.NXDOMAIN:

            logger.error(
                "Domain does not exist: %s",
                self.domain
            )


        except dns.resolver.Timeout:

            logger.error(
                "DNS timeout for %s",
                self.domain
            )


        except Exception as error:

            logger.exception(
                "DNS lookup error: %s",
                error
            )


        return results



    def enumerate_dns(self) -> Dict[str, List[str]]:
        """
        Perform complete DNS enumeration.

        Returns:
            Dict[str, List[str]]: DNS records.
        """

        logger.info(
            "Starting DNS enumeration for %s",
            self.domain
        )


        record_types = [

            "A",
            "AAAA",
            "MX",
            "NS",
            "TXT",
            "CNAME"

        ]


        for record in record_types:

            self.records[record] = (
                self.query_record(record)
            )


        logger.info(
            "DNS enumeration completed"
        )


        return self.records




def get_dns_records(domain: str) -> Dict[str, List[str]]:
    """
    Public DNS lookup function.

    Args:
        domain (str): Target domain.

    Returns:
        Dict[str, List[str]]: DNS information.
    """

    dns_enum = DNSEnumerator(
        domain
    )

    return dns_enum.enumerate_dns()