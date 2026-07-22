"""
CyberRecon AI
NVD CVE Intelligence Client

Version: v1.1.0
"""

from __future__ import annotations

from typing import Any

import requests

from modules.cache_manager import CacheManager
from modules.logger import setup_logger

logger = setup_logger()


class NVDClient:
    """
    Client for the National Vulnerability Database (NVD) API.
    """

    BASE_URL = (
        "https://services.nvd.nist.gov/rest/json/"
        "cves/2.0"
    )

    def __init__(
        self,
        timeout: int = 10,
    ) -> None:
        """
        Initialize NVD client.
        """

        self.timeout = timeout
        self.cache = CacheManager("nvd_cache.json")

    @staticmethod
    def normalize_cpe(
        cpe: str,
    ) -> str:
        """
        Normalize a CPE string for NVD lookup.
        """

        parts = cpe.split(":")

        if len(parts) >= 5:
            return ":".join(parts[:5])

        return cpe

    def _extract_cvss(
        self,
        cve: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Extract highest available CVSS metrics.

        Priority:
            CVSS v3.1
            CVSS v3.0
            CVSS v2
        """

        metrics = cve.get("metrics", {})

        priority = [
            ("cvssMetricV31", "3.1"),
            ("cvssMetricV30", "3.0"),
            ("cvssMetricV2", "2.0"),
        ]

        for metric_name, version in priority:

            if metric_name not in metrics:
                continue

            metric = metrics[metric_name][0]

            data = metric.get("cvssData", {})

            return {
                "version": version,
                "base_score": data.get("baseScore"),
                "severity": (
                    data.get("baseSeverity")
                    or metric.get("baseSeverity")
                ),
                "attack_vector": data.get("attackVector"),
                "attack_complexity": data.get("attackComplexity"),
                "exploitability_score": metric.get(
                    "exploitabilityScore"
                ),
                "impact_score": metric.get(
                    "impactScore"
                ),
            }

        return {}

    def search_cves(
        self,
        cpe: str,
    ) -> list[dict[str, Any]]:
        """
        Search CVEs for a CPE.

        Returns:
            Normalized vulnerability list.
        """

        normalized_cpe = self.normalize_cpe(cpe)

        if self.cache.has(normalized_cpe):

            logger.info(
                "NVD cache hit: %s",
                normalized_cpe,
            )

            return self.cache.get(
                normalized_cpe,
                [],
            )

        logger.info(
            "NVD cache miss: %s",
            normalized_cpe,
        )

        params: dict[str, Any] = {
            "virtualMatchString": normalized_cpe,
            "resultsPerPage": 20,
        }

        try:

            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=self.timeout,
            )

            response.raise_for_status()

            data = response.json()

            raw_vulnerabilities = data.get(
                "vulnerabilities",
                [],
            )

            vulnerabilities: list[
                dict[str, Any]
            ] = []

            for item in raw_vulnerabilities:

                cve = item.get(
                    "cve",
                    {},
                )

                descriptions = cve.get(
                    "descriptions",
                    [],
                )

                description = ""

                for desc in descriptions:

                    if desc.get("lang") == "en":

                        description = desc.get(
                            "value",
                            "",
                        )

                        break

                cve_id = cve.get(
                    "id",
                    "Unknown",
                )

                vulnerabilities.append(
                    {
                        "cve": cve_id,
                        "description": description,
                        "cvss": self._extract_cvss(
                            cve
                        ),
                        "url": (
                            "https://nvd.nist.gov/vuln/detail/"
                            f"{cve_id}"
                        ),
                    }
                )

            self.cache.set(
                normalized_cpe,
                vulnerabilities,
            )

            logger.info(
                "Cached %d CVEs for %s",
                len(vulnerabilities),
                normalized_cpe,
            )

            return vulnerabilities

        except requests.RequestException as error:

            logger.error(
                "NVD request failed: %s",
                error,
            )

        except ValueError as error:

            logger.error(
                "Invalid NVD response: %s",
                error,
            )

        return []