"""
CyberRecon AI
Robots.txt Analyzer Module

Version: 1.0.14
Purpose:
Authorized Defensive Security Assessment Toolkit
"""

import logging
from urllib.parse import urljoin
from typing import Any, Dict, List

import requests
import urllib3

logger = logging.getLogger("CyberReconAI")


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Common sensitive paths
SENSITIVE_PATHS = [
    "/admin",
    "/administrator",
    "/login",
    "/backup",
    "/backups",
    "/config",
    "/configuration",
    "/database",
    "/db",
    "/private",
    "/secret",
    "/test",
    "/dev",
    "/old",
    "/tmp",
    "/uploads",
]


def normalize_url(target: str) -> str:
    """
    Normalize target URL
    """

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    return target.rstrip("/")


def get_robots_url(target: str) -> str:
    """
    Generate robots.txt URL
    """

    return urljoin(normalize_url(target), "/robots.txt")


def fetch_robots_txt(target: str) -> str:
    """
    Fetch robots.txt content
    """

    robots_url = get_robots_url(target)

    try:

        response = requests.get(
            robots_url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 CyberRecon-AI"},
            verify=False,
        )

        if response.status_code == 200:

            logger.info("robots.txt found")

            return response.text

        logger.warning("robots.txt not found")

        return ""

    except requests.RequestException as error:

        logger.error(f"robots request failed: {error}")

        return ""


def parse_robots_content(content: str) -> Dict[str, Any]:
    """
    Parse robots.txt content
    """

    result: Dict[str, Any] = {
    "user_agents": [],
    "allow": [],
    "disallow": [],
    "sitemaps": [],
    "crawl_delay": None,
    "raw": content,
    }

    for line in content.splitlines():

        line = line.strip()

        if not line or line.startswith("#"):

            continue

        if ":" not in line:

            continue

        key, value = line.split(":", 1)

        key = key.lower().strip()

        value = value.strip()

        if key == "user-agent":

            result["user_agents"].append(value)

        elif key == "allow":

            result["allow"].append(value)

        elif key == "disallow":

            result["disallow"].append(value)

        elif key == "sitemap":

            result["sitemaps"].append(value)

        elif key == "crawl-delay":

            result["crawl_delay"] = value

    return result


def detect_sensitive_paths(disallowed_paths: List[str]) -> List[Dict]:
    """
    Detect sensitive paths exposed
    through robots.txt
    """

    findings = []

    for path in disallowed_paths:

        path_lower = path.lower()

        for sensitive in SENSITIVE_PATHS:

            if sensitive in path_lower:

                findings.append(
                    {
                        "path": path,
                        "risk": "Medium",
                        "reason": f"Sensitive path exposed: {path}",
                    }
                )

                break

    return findings


def analyze_sitemaps(sitemaps: List[str]) -> Dict:
    """
    Analyze sitemap information
    """

    return {"count": len(sitemaps), "sitemaps": sitemaps}


def generate_summary(data: Dict) -> Dict:
    """
    Generate analysis summary
    """

    return {
        "total_disallowed": len(data.get("disallow", [])),
        "total_allowed": len(data.get("allow", [])),
        "total_sitemaps": len(data.get("sitemaps", [])),
        "sensitive_findings": len(data.get("sensitive_paths", [])),
    }


def analyze_robots_txt(target: str) -> Dict:
    """
    Main robots.txt analyzer

    Compatible with CyberRecon AI main.py
    """

    logger.info(f"Starting robots.txt analysis for {target}")

    robots_content = fetch_robots_txt(target)

    if not robots_content:

        return {
            "status": "Not Found",
            "target": target,
            "robots_url": get_robots_url(target),
            "message": "robots.txt unavailable",
        }

    parsed_data = parse_robots_content(robots_content)

    parsed_data["sensitive_paths"] = detect_sensitive_paths(parsed_data["disallow"])

    parsed_data["sitemap_analysis"] = analyze_sitemaps(parsed_data["sitemaps"])

    parsed_data["summary"] = generate_summary(parsed_data)

    parsed_data["status"] = "Completed"

    parsed_data["target"] = target

    parsed_data["robots_url"] = get_robots_url(target)

    logger.info("robots.txt analysis completed")

    return parsed_data
