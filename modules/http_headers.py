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

from typing import Dict, Any, List

import requests

from modules.logger import setup_logger


logger = setup_logger()



class SecurityHeaderAnalyzer:
    """
    Performs HTTP security header analysis.
    """


    SECURITY_HEADERS = {

        "Strict-Transport-Security":
        "HSTS",

        "Content-Security-Policy":
        "CSP",

        "X-Frame-Options":
        "Clickjacking Protection",

        "X-Content-Type-Options":
        "MIME Sniffing Protection",

        "Referrer-Policy":
        "Referrer Protection",

        "Permissions-Policy":
        "Browser Permissions Control"

    }



    def __init__(self, url: str):
        """
        Initialize analyzer.

        Args:
            url (str): Target URL.
        """

        self.url = url

        self.headers = {}

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

                timeout=10,

                headers={
                    "User-Agent":
                    "Mozilla/5.0 CyberReconAI"
                }

            )


            logger.info(
                "HTTP headers collected successfully"
            )


            self.headers = dict(
                response.headers
            )


            return self.headers



        except requests.RequestException as error:

            logger.error(
                "Header collection failed: %s",
                error
            )


            return {}



    def analyze_headers(self) -> Dict[str, Any]:
        """
        Analyze security headers.

        Returns:
            Dict[str, Any]: Security analysis result.
        """

        present_headers = {}

        missing_headers: List[str] = []


        for header, description in self.SECURITY_HEADERS.items():


            if header in self.headers:

                present_headers[description] = True


            else:

                present_headers[description] = False

                missing_headers.append(
                    header
                )


        total_headers = len(
            self.SECURITY_HEADERS
        )


        secure_headers = (
            total_headers -
            len(missing_headers)
        )


        score = f"{secure_headers}/{total_headers}"


        self.result = {

            "server":
            self.headers.get(
                "Server",
                "Unknown"
            ),


            "security_headers":
            present_headers,


            "missing_headers":
            missing_headers,


            "score":
            score

        }


        logger.info(
            "Security header analysis completed"
        )


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

    analyzer = SecurityHeaderAnalyzer(
        url
    )


    return analyzer.run()