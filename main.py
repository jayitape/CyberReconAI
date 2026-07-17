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
from modules.service_detector import detect_services
from modules.robots_analyzer import analyze_robots_txt


def main():
    show_banner()
    logger = setup_logger()
    logger.info("CyberRecon AI started")

    args = parse_arguments()
    target_url = args.url

    print(f"\n[+] Target : {target_url}")

    try:
        print("\n========== TARGET INFORMATION ==========")
        target_info = analyze_target(target_url)

        for k, v in target_info.items():
            print(f"{k}: {v}")

        domain = target_info["domain"]
        normalized_url = target_info["url"]

        print("\n========== WHOIS INFORMATION ==========")
        for k, v in get_whois_info(domain).items():
            print(f"{k}: {v}")

        print("\n========== DNS ENUMERATION ==========")
        for k, v in get_dns_records(domain).items():
            print(f"{k}: {v}")

        print("\n========== SSL/TLS ANALYSIS ==========")
        for k, v in get_ssl_info(domain).items():
            print(f"{k}: {v}")

        print("\n========== HTTP SECURITY HEADERS ==========")
        for k, v in get_security_headers(normalized_url).items():
            print(f"{k}: {v}")

        print("\n========== TECHNOLOGY DETECTION ==========")
        tech = TechnologyDetector(normalized_url).analyze()

        print("\nWeb Server:")
        for x in tech["server"]:
            print(f"- {x}")

        print("\nCMS:")
        for x in tech["cms"]:
            print(f"- {x}")

        print("\nFrameworks:")
        for x in tech["frameworks"]:
            print(f"- {x}")

        print("\nJavaScript Libraries:")
        for x in tech["javascript"]:
            print(f"- {x}")

        print("\n========== SUBDOMAIN ENUMERATION ==========")
        result = get_subdomains(domain)

        if isinstance(result, dict):
            subs = result.get("subdomains", [])
        else:
            subs = result

        print(f"\nTotal Subdomains Found: {len(subs)}")
        for sub in subs:
            print(f"- {sub}")

        print("\n========== PORT SCANNING ==========")
        port_results = scan_ports(domain)

        if port_results:
            print(f"\nOpen Ports Found: {len(port_results)}")
            for p in port_results:
                print(f"\nPort    : {p['port']}")
                print(f"Service : {p['service']}")
                print(f"State   : {p['state']}")
                if p.get("banner"):
                    print(f"Banner  : {p['banner']}")
        else:
            print("No open common ports detected")

        print("\n========== SERVICE DETECTION ==========")
        for s in detect_services(port_results):
            print(f"\nPort    : {s['port']}")
            print(f"Service : {s['service']}")
            print(f"State   : {s['state']}")

        logger.info("CyberRecon AI scan completed successfully")

    except Exception as e:
        logger.exception("Scan failed: %s", e)
        print("\n[!] Scan failed. Check logs.")
        sys.exit(1)


if __name__ == "__main__":
    main()
