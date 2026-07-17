"""
CyberRecon AI

Main Application Entry Point

Authorized Defensive Security Assessment Toolkit
"""


import sys


from modules.banner import show_banner

from modules.logger import setup_logger

from modules.cli import parse_arguments

from modules.target import analyze_target

from modules.whois_lookup import get_whois_info

from modules.dns_lookup import get_dns_records

from modules.ssl_checker import get_ssl_info

from modules.http_headers import get_security_headers

from modules.technology_detector import TechnologyDetector

from modules.subdomain_enum import get_subdomains

from modules.port_scanner import scan_ports




def main():
    """
    Execute complete CyberRecon AI workflow.
    """


    # ==============================
    # Banner
    # ==============================

    show_banner()



    # ==============================
    # Logger
    # ==============================

    logger = setup_logger()


    logger.info(
        "CyberRecon AI started"
    )



    # ==============================
    # CLI Input
    # ==============================

    args = parse_arguments()

    target_url = args.url



    print(
        f"\n[+] Target : {target_url}"
    )



    try:


        # ==============================
        # Target Intelligence
        # ==============================

        print(
            "\n========== TARGET INFORMATION =========="
        )


        target_info = analyze_target(
            target_url
        )


        for key, value in target_info.items():

            print(
                f"{key}: {value}"
            )


        domain = target_info["domain"]

        normalized_url = target_info["url"]




        # ==============================
        # WHOIS
        # ==============================

        print(
            "\n========== WHOIS INFORMATION =========="
        )


        whois_info = get_whois_info(
            domain
        )


        for key, value in whois_info.items():

            print(
                f"{key}: {value}"
            )




        # ==============================
        # DNS Enumeration
        # ==============================

        print(
            "\n========== DNS ENUMERATION =========="
        )


        dns_info = get_dns_records(
            domain
        )


        for record, values in dns_info.items():

            print(
                f"{record}: {values}"
            )




        # ==============================
        # SSL/TLS Analysis
        # ==============================

        print(
            "\n========== SSL/TLS ANALYSIS =========="
        )


        ssl_info = get_ssl_info(
            domain
        )


        for key, value in ssl_info.items():

            print(
                f"{key}: {value}"
            )




        # ==============================
        # HTTP Security Headers
        # ==============================

        print(
            "\n========== HTTP SECURITY HEADERS =========="
        )


        header_info = get_security_headers(
            normalized_url
        )


        for key, value in header_info.items():

            print(
                f"{key}: {value}"
            )




        # ==============================
        # Technology Detection
        # ==============================

        print(
            "\n========== TECHNOLOGY DETECTION =========="
        )


        detector = TechnologyDetector(
            normalized_url
        )


        technology_info = detector.analyze()



        print(
            "\nWeb Server:"
        )

        for item in technology_info["server"]:

            print(
                f"- {item}"
            )



        print(
            "\nCMS:"
        )

        for item in technology_info["cms"]:

            print(
                f"- {item}"
            )



        print(
            "\nFrameworks:"
        )

        for item in technology_info["frameworks"]:

            print(
                f"- {item}"
            )



        print(
            "\nJavaScript Libraries:"
        )

        for item in technology_info["javascript"]:

            print(
                f"- {item}"
            )




        # ==============================
        # Subdomain Enumeration
        # ==============================

        print(
            "\n========== SUBDOMAIN ENUMERATION =========="
        )


        subdomains = get_subdomains(
            domain
        )


        if subdomains:


            print(
                f"\nTotal Subdomains Found: {len(subdomains)}"
            )


            for subdomain in subdomains:

                print(
                    f"- {subdomain}"
                )


        else:

            print(
                "No subdomains discovered"
            )





        # ==============================
        # Port Scanner
        # ==============================

        print(
            "\n========== PORT SCANNING =========="
        )


        logger.info(
            "Starting port scanning"
        )



        port_results = scan_ports(
            domain
        )



        if port_results:


            print(
                f"\nOpen Ports Found: {len(port_results)}"
            )



            for port in port_results:


                print(
                    f"\nPort: {port['port']}"
                )

                print(
                    f"Service: {port['service']}"
                )

                print(
                    f"State: {port['state']}"
                )

                print(
                    f"Banner: {port['banner']}"
                )



        else:


            print(
                "No open common ports detected"
            )



        logger.info(
            "CyberRecon AI scan completed successfully"
        )



    except Exception as error:


        logger.exception(
            "Scan failed: %s",
            error
        )


        print(
            "\n[!] Scan failed. Check logs."
        )


        sys.exit(1)





if __name__ == "__main__":

    main()