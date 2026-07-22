"""
HTTP Security Headers Analyzer Module

Analyzes HTTP response headers for
authorized security assessments only.

Features:
- Server detection
- Security header checking
- Missing header identification
- Security score calculation
"""

from typing import Any, Dict, List

import requests

from modules.logger import setup_logger

logger = setup_logger()


class SecurityHeaderAnalyzer:
    """
    Performs HTTP security header analysis.
    """
        
    def __init__(self, url: str):
        """
        Initialize analyzer.

        Args:
            url (str): Target URL.
        """

        self.url = url

        self.headers: Dict[str, str] = {}

        self.result: Dict[str, Any] = {}

    def fetch_headers(self) -> Dict[str, str]:
        """
        Fetch HTTP response headers.

        Returns:
            Dict[str, str]: Response headers.
        """
        
        try:
            response = requests.get(
                self.url,
                timeout=20,
                allow_redirects=True,
                headers={
                    "User-Agent": "Mozilla/5.0 CyberReconAI"
                    },
                verify=True,
                )
            
            self.headers = {
                 key.lower(): value
                 for key, value in response.headers.items()
                 }
            
            
            return self.headers
            
        except requests.exceptions.SSLError:
            logger.warning(
                "SSL verification failed, retrying without verification"
                )
            
            response = requests.get(
                self.url,
                timeout=20,
                allow_redirects=True,
                headers={
                    "User-Agent": "Mozilla/5.0 CyberReconAI"
                    },
                    verify=False,
                    )
            self.headers = {
                 key.lower(): value
                 for key, value in response.headers.items()
                 }
        
            
            return self.headers
            
        except requests.exceptions.RequestException as error:
            logger.error(
                f"Header collection failed: {error}"
                )
            
            return {}

    def analyze_headers(self) -> Dict[str, Any]:
        """
        Analyze security headers.

        Returns:
            Dict[str, Any]: Security analysis result.
        """
        
        security_headers = {
            "strict-transport-security": "HTTP Strict Transport Security (HSTS)",
            "content-security-policy": "Content Security Policy (CSP)",
            "x-frame-options": "X-Frame-Options",
            "x-content-type-options": "X-Content-Type-Options",
            "referrer-policy": "Referrer-Policy",
            "permissions-policy": "Permissions-Policy",
            }

        present_headers = {}

        missing_headers: List[str] = []

        for header, description in security_headers.items():
            header_name = header.lower()
            
            if header_name in self.headers:
                
                present_headers[description] = True
            
            elif (
                header_name == "content-security-policy"
                and "content-security-policy-report-only" in self.headers
                ):
                
                present_headers[description] = True
                
            else:
                present_headers[description] = False
                missing_headers.append(header)

        total_headers = len(security_headers)

        secure_headers = total_headers - len(missing_headers)

        score = f"{secure_headers}/{total_headers}"

        self.result = {
            "server": self.headers.get("server", "Unknown"),
            "security_headers": present_headers,
            "missing_headers": missing_headers,
            "score": score,
        }


        logger.info("Security header analysis completed")

        return self.result

    def run(self) -> Dict[str, Any]:
        """
        Execute complete analysis.

        Returns:
            Dict[str, Any]: Final result.
        """

        self.fetch_headers()

        return self.analyze_headers()


def get_security_headers(url: str) -> Dict[str, Any]:
    """
    Public function for HTTP header analysis.

    Args:
        url (str): Target URL.

    Returns:
        Dict[str, Any]: Security header report.
    """

    analyzer = SecurityHeaderAnalyzer(url)

    return analyzer.run()
