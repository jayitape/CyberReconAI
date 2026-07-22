"""
CyberRecon AI
CVE Response Parser

Version: v1.1.0
"""

from typing import Any


class CVEParser:
    """
    Parses NVD CVE JSON responses.
    """


    def parse_cve(
        self,
        cve_record: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Parse single CVE record.

        Args:
            cve_record:
                Raw NVD CVE object.

        Returns:
            Normalized vulnerability data.
        """

        cve_data = cve_record.get(
            "cve",
            {},
        )

        cve_id = str(
            cve_data.get(
                "id",
                "UNKNOWN",
            )
        )

        description = self._extract_description(
            cve_data
        )

        cvss_score, severity = (
            self._extract_cvss(
                cve_data
            )
        )

        return {
            "cve_id": cve_id,
            "severity": severity,
            "cvss_score": cvss_score,
            "description": description,
        }


    def parse_multiple(
        self,
        records: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Parse multiple CVE records.

        Args:
            records:
                List of NVD CVE responses.

        Returns:
            Parsed vulnerability list.
        """

        vulnerabilities: list[
            dict[str, Any]
        ] = []

        for record in records:

            vulnerabilities.append(
                self.parse_cve(
                    record
                )
            )

        return vulnerabilities


    def _extract_description(
        self,
        cve_data: dict[str, Any],
    ) -> str:
        """
        Extract English CVE description.
        """

        descriptions = cve_data.get(
            "descriptions",
            [],
        )

        for item in descriptions:

            if item.get("lang") == "en":

                return str(
                    item.get(
                        "value",
                        "",
                    )
                )

        return "No description available"


    def _extract_cvss(
        self,
        cve_data: dict[str, Any],
    ) -> tuple[float, str]:
        """
        Extract CVSS score and severity.
        """

        metrics = cve_data.get(
            "metrics",
            {},
        )

        cvss_data = {}

        if "cvssMetricV31" in metrics:

            cvss_data = (
                metrics["cvssMetricV31"][0]
                .get(
                    "cvssData",
                    {},
                )
            )

        elif "cvssMetricV30" in metrics:

            cvss_data = (
                metrics["cvssMetricV30"][0]
                .get(
                    "cvssData",
                    {},
                )
            )

        elif "cvssMetricV2" in metrics:

            cvss_data = (
                metrics["cvssMetricV2"][0]
                .get(
                    "cvssData",
                    {},
                )
            )

        score = float(
            cvss_data.get(
                "baseScore",
                0.0,
            )
        )

        severity = str(
            cvss_data.get(
                "baseSeverity",
                "UNKNOWN",
            )
        ).upper()

        return score, severity