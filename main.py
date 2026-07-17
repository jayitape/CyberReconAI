"""
CyberRecon AI

Main Application Entry Point

Authorized Security Assessment Toolkit
"""


from modules.banner import show_banner
from modules.logger import setup_logger
from modules.cli import parse_arguments
from modules.target import analyze_target
from modules.whois_lookup import get_whois_info
from modules.dns_lookup import get_dns_records
from modules.ssl_checker import get_ssl_info
from modules.http_headers import get_security_headers



logger = setup_logger()



def display_target_info(target_info: dict) -> None:
    """
    Display target intelligence information.
    """

    print("\n========== Target Information ==========")

    print(
        f"URL         : {target_info['url']}"
    )

    print(
        f"Domain      : {target_info['domain']}"
    )

    print(
        f"IP Address  : {target_info['ip']}"
    )

    print(
        f"Scheme      : {target_info['scheme']}"
    )

    print(
        f"Reachable   : {target_info['reachable']}"
    )



def display_whois_info(whois_info: dict) -> None:
    """
    Display WHOIS information.
    """

    print("\n========== WHOIS Information ==========")


    for key, value in whois_info.items():

        print(
            f"{key:<15}: {value}"
        )



def display_dns_info(dns_info: dict) -> None:
    """
    Display DNS enumeration results.
    """

    print("\n========== DNS Enumeration ==========")


    for record, values in dns_info.items():

        print(
            f"\n{record} Records:"
        )


        if values:

            for value in values:

                print(
                    f"  - {value}"
                )

        else:

            print(
                "  None"
            )



def display_ssl_info(ssl_info: dict) -> None:
    """
    Display SSL certificate information.
    """

    print(
        "\n========== SSL Certificate Information =========="
    )


    if ssl_info:


        print(
            f"Valid From     : {ssl_info.get('valid_from')}"
        )

        print(
            f"Valid Until    : {ssl_info.get('valid_until')}"
        )

        print(
            f"Days Remaining : {ssl_info.get('days_remaining')} days"
        )

        print(
            f"Issuer         : {ssl_info.get('issuer')}"
        )

        print(
            f"Subject        : {ssl_info.get('subject')}"
        )


    else:

        print(
            "SSL information unavailable"
        )



def display_security_headers(header_info: dict) -> None:
    """
    Display HTTP security header analysis.
    """

    print(
        "\n========== HTTP Security Headers =========="
    )


    if not header_info:

        print(
            "Header analysis unavailable"
        )

        return



    print(
        f"Server : {header_info.get('server')}"
    )


    print(
        f"Security Score : {header_info.get('score')}"
    )


    print(
        "\nSecurity Headers:"
    )


    for header, status in header_info.get(
        "security_headers",
        {}
    ).items():

        symbol = "✓" if status else "✗"

        print(
            f"{symbol} {header}"
        )



    missing = header_info.get(
        "missing_headers",
        []
    )


    if missing:

        print(
            "\nMissing Headers:"
        )


        for item in missing:

            print(
                f" - {item}"
            )



def main():
    """
    Main application workflow.
    """


    show_banner()


    args = parse_arguments()



    #
    # Target Intelligence
    #

    target_info = analyze_target(
        args.url
    )


    display_target_info(
        target_info
    )



    #
    # WHOIS
    #

    whois_info = get_whois_info(
        target_info["domain"]
    )


    display_whois_info(
        whois_info
    )



    #
    # DNS Enumeration
    #

    dns_info = get_dns_records(
        target_info["domain"]
    )


    display_dns_info(
        dns_info
    )



    #
    # SSL Analysis
    #

    ssl_info = get_ssl_info(
        target_info["domain"]
    )


    display_ssl_info(
        ssl_info
    )



    #
    # HTTP Security Headers
    #

    header_info = get_security_headers(
        target_info["url"]
    )


    display_security_headers(
        header_info
    )



if __name__ == "__main__":

    main()