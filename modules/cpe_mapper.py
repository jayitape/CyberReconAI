"""
CyberRecon AI - Advanced CPE Product Mapping Engine

Maps detected technologies into CPE identifiers
for vulnerability intelligence lookup.

Version:
v1.1.0
"""

from typing import Dict, List


class CPEMapper:
    """
    Converts detected technologies into CPE identifiers.
    """

    def __init__(self) -> None:
        """
        Initialize CPE database and aliases.
        """

        self.cpe_database: Dict[str, Dict[str, str]] = {

            "nginx": {
                "vendor": "nginx",
                "product": "nginx",
                "cpe": (
                    "cpe:2.3:a:nginx:nginx:*:*:*:*:*:*:*:*"
                ),
            },

            "apache": {
                "vendor": "apache",
                "product": "http_server",
                "cpe": (
                    "cpe:2.3:a:apache:http_server:*:*:*:*:*:*:*:*"
                ),
            },

            "wordpress": {
                "vendor": "wordpress",
                "product": "wordpress",
                "cpe": (
                    "cpe:2.3:a:wordpress:wordpress:*:*:*:*:*:*:*:*"
                ),
            },

            "drupal": {
                "vendor": "drupal",
                "product": "drupal",
                "cpe": (
                    "cpe:2.3:a:drupal:drupal:*:*:*:*:*:*:*:*"
                ),
            },

            "php": {
                "vendor": "php",
                "product": "php",
                "cpe": (
                    "cpe:2.3:a:php:php:*:*:*:*:*:*:*:*"
                ),
            },

            "mysql": {
                "vendor": "mysql",
                "product": "mysql",
                "cpe": (
                    "cpe:2.3:a:mysql:mysql:*:*:*:*:*:*:*:*"
                ),
            },
        }


        self.alias_database: Dict[str, str] = {

            # Apache
            "httpd": "apache",
            "apache web server": "apache",
            "apache server": "apache",

            # WordPress
            "wp": "wordpress",
            "wordpress cms": "wordpress",
            "wordpress platform": "wordpress",

            # PHP
            "php runtime": "php",

            # MySQL
            "mysql server": "mysql",
            "mysql database": "mysql",
        }


    def normalize_technology(
        self,
        technology: str,
    ) -> str:
        """
        Normalize detected technology names.

        Args:
            technology:
                Raw technology name.

        Returns:
            Normalized technology name.
        """

        normalized = (
            technology
            .lower()
            .strip()
        )

        return self.alias_database.get(
            normalized,
            normalized,
        )


    def get_cpe(
        self,
        technology: str,
    ) -> List[str]:
        """
        Get CPE identifiers for technology.

        Args:
            technology:
                Detected technology name.

        Returns:
            List containing matching CPE.
        """

        technology_name = (
            self.normalize_technology(
                technology
            )
        )

        product = self.cpe_database.get(
            technology_name
        )

        if not product:
            return []

        return [
            product["cpe"]
        ]


    def get_product_details(
        self,
        technology: str,
    ) -> Dict[str, str]:
        """
        Return CPE product metadata.

        Args:
            technology:
                Technology name.

        Returns:
            Vendor, product and CPE details.
        """

        technology_name = (
            self.normalize_technology(
                technology
            )
        )

        return self.cpe_database.get(
            technology_name,
            {},
        )


    def remove_duplicates(
        self,
        values: List[str],
    ) -> List[str]:
        """
        Remove duplicate values.

        Args:
            values:
                List of CPE strings.

        Returns:
            Unique CPE list.
        """

        return list(
            dict.fromkeys(values)
        )


    def map_technologies(
        self,
        technologies: List[str],
    ) -> List[str]:
        """
        Map technologies into CPE identifiers.

        Args:
            technologies:
                Detected technology list.

        Returns:
            Unique CPE identifiers.
        """

        cpes: List[str] = []

        for technology in technologies:

            cpes.extend(
                self.get_cpe(
                    technology
                )
            )

        return self.remove_duplicates(
            cpes
        )