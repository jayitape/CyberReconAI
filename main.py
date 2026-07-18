"""
CyberRecon AI v1.0.16

Main Application Entry Point

Authorized Defensive Security Assessment Toolkit
"""


import sys
import os


VERSION = "1.1.0"


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
from modules.risk_engine import calculate_security_score

from modules.report_generator import generate_report
from modules.json_report import generate_json_report
from modules.scan_id import generate_scan_id

from modules.scan_timer import (
    start_timer,
    end_timer,
    calculate_duration,
    get_time
)
from modules.ui import (
    show_banner,
    ui_title,
    print_message,
    show_target_info,
    show_progress,
    show_scan_status,
    show_ports,
    show_technology,
    show_section,
    show_findings,
    show_risk_summary,
    show_statistics,
    show_no_findings,
    show_summary,
    show_completion,
    show_report_info,
    show_footer
)



def main():


    os.makedirs(
        "reports",
        exist_ok=True
    )


    show_banner()


    logger = setup_logger()


    logger.info(
        f"CyberRecon AI v{VERSION} started"
    )


    args = parse_arguments()


    target_url = args.url


    scan_id = generate_scan_id()


    scan_start = start_timer()

    scan_start_time = get_time()



    print(
        f"\n[+] Target : {target_url}"
    )


    print(
        f"[+] Scan ID : {scan_id}"
    )



    try:


        print(
            "\n========== TARGET INFORMATION =========="
        )


        target_info = analyze_target(
            target_url
        )


        for k, v in target_info.items():

            print(
                f"{k}: {v}"
            )



        domain = target_info["domain"]


        normalized_url = target_info["url"]



        print(
            "\n========== WHOIS INFORMATION =========="
        )


        whois_info = get_whois_info(
            domain
        )


        for k, v in whois_info.items():

            print(
                f"{k}: {v}"
            )



        print(
            "\n========== DNS ENUMERATION =========="
        )


        dns_info = get_dns_records(
            domain
        )


        for k, v in dns_info.items():

            print(
                f"{k}: {v}"
            )



        print(
            "\n========== SSL/TLS ANALYSIS =========="
        )


        ssl_info = get_ssl_info(
            domain
        )


        for k, v in ssl_info.items():

            print(
                f"{k}: {v}"
            )



        print(
            "\n========== HTTP SECURITY HEADERS =========="
        )


        headers_info = get_security_headers(
            normalized_url
        )



        for k, v in headers_info.items():

            print(
                f"{k}: {v}"
            )



        print(
            "\n========== TECHNOLOGY DETECTION =========="
        )


        tech = TechnologyDetector(
            normalized_url
        ).analyze()



        print(
            "\nWeb Server:"
        )


        for x in tech["server"]:

            print(
                f"- {x}"
            )



        print(
            "\nCMS:"
        )


        for x in tech["cms"]:

            print(
                f"- {x}"
            )



        print(
            "\nFrameworks:"
        )


        for x in tech["frameworks"]:

            print(
                f"- {x}"
            )



        print(
            "\nJavaScript Libraries:"
        )


        for x in tech["javascript"]:

            print(
                f"- {x}"
            )



        print(
            "\n========== SUBDOMAIN ENUMERATION =========="
        )


        result = get_subdomains(
            domain
        )


        if isinstance(result, dict):

            subs = result.get(
                "subdomains",
                []
            )

        else:

            subs = result



        print(
            f"\nTotal Subdomains Found: {len(subs)}"
        )


        for sub in subs:

            print(
                f"- {sub}"
            )


        print(
            "\n========== PORT SCANNING =========="
        )


        port_results = scan_ports(
            domain
        )


        if port_results:


            print(
                f"\nOpen Ports Found: {len(port_results)}"
            )


            for p in port_results:


                print(
                    f"\nPort    : {p['port']}"
                )


                print(
                    f"Service : {p['service']}"
                )


                print(
                    f"State   : {p['state']}"
                )


                if p.get("banner"):

                    print(
                        f"Banner  : {p['banner']}"
                    )


        else:


            print(
                "No open common ports detected"
            )



        print(
            "\n========== ROBOTS.TXT ANALYZER =========="
        )


        robots_info = analyze_robots_txt(
            normalized_url
        )


        if robots_info["status"] == "Completed":


            print(
                f"Robots URL: {robots_info['robots_url']}"
            )


            print(
                f"User Agents: {robots_info['user_agents']}"
            )


            print(
                f"Disallowed Paths: {robots_info['summary']['total_disallowed']}"
            )


            print(
                f"Allowed Paths: {robots_info['summary']['total_allowed']}"
            )


            print(
                f"Sitemaps: {robots_info['summary']['total_sitemaps']}"
            )


            print(
                f"Sensitive Findings: {robots_info['summary']['sensitive_findings']}"
            )


        else:


            print(
                robots_info["message"]
            )
            print(
            "\n========== SECURITY RISK SCORE =========="
        )


        risk_report = calculate_security_score(

            headers=headers_info,

            ssl_info=ssl_info,

            robots_info=robots_info,

            ports=port_results,

            subdomains=subs

        )


        print(
            f"\nOverall Security Score : {risk_report['score']}/100"
        )


        print(
            f"Risk Level : {risk_report['risk_level']}"
        )


        print(
            "\nFindings:"
        )


        if risk_report["findings"]:


            for finding in risk_report["findings"]:


                print(
                    f"\n[{finding['risk']}] {finding['issue']}"
                )


        else:


            print(
                "No security issues detected"
            )



        print(
            "\n========== SERVICE DETECTION =========="
        )


        services = detect_services(
            port_results
        )


        for s in services:


            print(
                f"\nPort    : {s['port']}"
            )


            print(
                f"Service : {s['service']}"
            )


            print(
                f"State   : {s['state']}"
            )



        # ===============================
        # STOP TIMER BEFORE REPORT CREATION
        # ===============================


        scan_end = end_timer()


        scan_end_time = get_time()


        scan_duration = calculate_duration(
            scan_start,
            scan_end
        )



        print(
            "\n========== REPORT GENERATION =========="
        )



        scan_data = {


            "scan_metadata": {


                "version": VERSION,


                "scan_id": scan_id,


                "scan_start_time": scan_start_time,


                "scan_end_time": scan_end_time,


                "scan_duration": scan_duration


            },


            "target_information": target_info,


            "whois_information": whois_info,


            "dns_information": dns_info,


            "ssl_information": ssl_info,


            "headers_information": headers_info,


            "technology_information": tech,


            "subdomains": subs,


            "ports": port_results,


            "robots_information": robots_info,


            "risk_score": risk_report["score"],


            "risk_level": risk_report["risk_level"],


            "findings": risk_report["findings"],


            "services": services

        }



        # ===============================
        # HTML REPORT GENERATION
        # ===============================


        report_path = generate_report(

            domain,

            scan_data

        )


        print(
            "\nHTML Report Generated Successfully:"
        )


        print(
            report_path
        )



        # ===============================
        # JSON REPORT GENERATION
        # ===============================


        print(
            "\n========== JSON REPORT GENERATION =========="
        )



        json_filename = (

            domain.replace(".", "_")

            +

            "_report.json"

        )



        json_path = generate_json_report(

            scan_data,

            json_filename

        )


        print(
            "\nJSON Report Generated Successfully:"
        )


        print(
            json_path
        )



        logger.info(
            "CyberRecon AI scan completed successfully"
        )



        print(
            "\n===================================="
        )


        print(
            " CyberRecon AI Scan Completed "
        )


        print(
            "===================================="
        )



    except Exception as e:


        logger.exception(
            "Scan failed: %s",
            e
        )


        print(
            "\n[!] Scan failed. Check logs."
        )


        sys.exit(1)





if __name__ == "__main__":


    main()