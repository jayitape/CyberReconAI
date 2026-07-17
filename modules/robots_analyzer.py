"""
CyberRecon AI
robots.txt Analyzer Module
"""

from typing import Dict, List
import requests


def analyze_robots(url: str) -> Dict:
    """
    Analyze robots.txt file.
    """

    result = {
        "found": False,
        "disallow": [],
        "allow": [],
        "sitemap": []
    }

    try:

        robots_url = url.rstrip("/") + "/robots.txt"

        response = requests.get(
            robots_url,
            timeout=10
        )

        if response.status_code != 200:
            return result

        result["found"] = True

        for line in response.text.splitlines():

            line = line.strip()

            if line.startswith("Disallow:"):
                result["disallow"].append(
                    line.split(":", 1)[1].strip()
                )

            elif line.startswith("Allow:"):
                result["allow"].append(
                    line.split(":", 1)[1].strip()
                )

            elif line.startswith("Sitemap:"):
                result["sitemap"].append(
                    line.split(":", 1)[1].strip()
                )

    except Exception:
        pass

    return result