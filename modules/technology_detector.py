"""
CyberRecon AI
Technology Detection Module

Detects web technologies used by target websites.

Authorized security assessment only.
"""


from typing import Dict, List

import requests

from bs4 import BeautifulSoup

from modules.logger import setup_logger


logger = setup_logger()



class TechnologyDetector:
    """
    Technology fingerprinting engine.
    """


    def __init__(self, url: str):
        """
        Initialize technology detector.

        Args:
            url (str):
                Target website URL.
        """

        self.url = url

        self.headers: Dict[str, str] = {}

        self.html_content: str = ""

        self.session = requests.Session()


        self.session.headers.update(
            {
                "User-Agent":
                "CyberReconAI-Security-Scanner/1.0"
            }
        )



    def fetch_target(self) -> bool:
        """
        Fetch target website content.

        Returns:
            bool:
                True if successful else False.
        """

        try:

            response = self.session.get(

                self.url,

                timeout=20,

                allow_redirects=True

            )


            response.raise_for_status()


            self.headers = dict(
                response.headers
            )


            self.html_content = response.text


            logger.info(
                "Technology scan completed for %s",
                self.url
            )


            return True



        except requests.RequestException as error:


            logger.error(
                "Technology detection failed: %s",
                error
            )


            return False




    def detect_server(self) -> List[str]:
        """
        Detect web server technology.

        Returns:
            List[str]:
                Detected servers.
        """

        servers = []


        server = self.headers.get(
            "Server"
        )


        powered_by = self.headers.get(
            "X-Powered-By"
        )


        if server:

            servers.append(
                server
            )


        if powered_by:

            servers.append(
                powered_by
            )


        return servers




    def detect_cms(self) -> List[str]:
        """
        Detect CMS platforms.

        Returns:
            List[str]:
                CMS technologies.
        """

        cms = []


        content = self.html_content.lower()



        signatures = {

            "WordPress":
            [
                "wp-content",
                "wp-includes"
            ],


            "Drupal":
            [
                "drupal"
            ],


            "Joomla":
            [
                "joomla"
            ]

        }



        for name, keywords in signatures.items():

            for keyword in keywords:

                if keyword in content:

                    cms.append(name)

                    break



        return cms




    def detect_frameworks(self) -> List[str]:
        """
        Detect frontend frameworks.

        Returns:
            List[str]:
                Framework names.
        """

        frameworks = []


        content = self.html_content.lower()



        signatures = {


            "React":
            [
                "react",
                "_react"
            ],


            "Angular":
            [
                "ng-version"
            ],


            "Vue.js":
            [
                "vue"
            ],


            "Next.js":
            [
                "_next"
            ]

        }



        for name, keywords in signatures.items():

            for keyword in keywords:


                if keyword in content:

                    frameworks.append(name)

                    break



        return frameworks




    def detect_javascript(self) -> List[str]:
        """
        Detect JavaScript libraries.

        Returns:
            List[str]:
                JavaScript libraries.
        """

        libraries = []


        try:

            soup = BeautifulSoup(

                self.html_content,

                "html.parser"

            )


            scripts = soup.find_all(
                "script"
            )



            signatures = {


                "jQuery":
                "jquery",


                "Bootstrap":
                "bootstrap",


                "Lodash":
                "lodash"

            }



            for script in scripts:


                src = script.get(
                    "src",
                    ""
                ).lower()



                for name, keyword in signatures.items():


                    if keyword in src:

                        libraries.append(
                            name
                        )



        except Exception as error:


            logger.error(
                "JavaScript detection error: %s",
                error
            )



        return list(
            set(libraries)
        )




    def analyze(self) -> Dict[str, List[str]]:
        """
        Perform complete technology analysis.

        Returns:
            Dict[str, List[str]]:
                Technology report.
        """


        result = {


            "server": [],

            "cms": [],

            "frameworks": [],

            "javascript": []

        }



        if not self.fetch_target():

            return result




        result["server"] = self.detect_server()


        result["cms"] = self.detect_cms()


        result["frameworks"] = self.detect_frameworks()


        result["javascript"] = self.detect_javascript()



        return result