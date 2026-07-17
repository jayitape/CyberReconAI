"""
CyberRecon AI

Main Application Entry Point
"""


from modules.banner import show_banner
from modules.logger import setup_logger
from modules.cli import parse_arguments
from modules.target import analyze_target
from modules.whois_lookup import get_whois_info
from modules.dns_lookup import get_dns_records



def main() -> None:
    """
    Main execution function.
    """

    show_banner()

    logger = setup_logger()

    args = parse_arguments()

    target_info = analyze_target(args.url)

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


    # WHOIS Module

    whois_info = get_whois_info(
        target_info["domain"]
    )


    print("\n========== WHOIS Information ==========")


    for key, value in whois_info.items():

        print(
            f"{key:<12}: {value}"
        )


    # DNS Enumeration Module

    dns_info = get_dns_records(
        target_info["domain"]
    )


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


if __name__ == "__main__":
    main()