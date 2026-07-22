"""
CyberRecon AI v1.1.0

Main Application Controller

Authorized Defensive Security Assessment Toolkit

Enterprise Edition
"""

from __future__ import annotations

import os
import sys

from modules import ui

from modules.cli import parse_arguments
from modules.concurrent import ConcurrentScanner

from modules.dns_lookup import get_dns_records
from modules.http_headers import get_security_headers
from modules.json_report import generate_json_report

from modules.logger import setup_logger

from modules.pdf_generator import generate_pdf_report
from modules.port_scanner import scan_ports

from modules.report_generator import generate_report

from modules.risk_engine import calculate_security_score

from modules.robots_analyzer import analyze_robots_txt

from modules.scan_id import generate_scan_id

from modules.scan_timer import (
    calculate_duration,
    end_timer,
    get_time,
    start_timer,
)

from modules.service_detector import detect_services

from modules.ssl_checker import get_ssl_info

from modules.subdomain_enum import get_subdomains

from modules.target import analyze_target

from modules.technology_detector import TechnologyDetector

from modules.vulnerability_intelligence import (
    VulnerabilityIntelligence,
)

from modules.whois_lookup import get_whois_info
from modules.version import VERSION



# ==================================================
# ENVIRONMENT INITIALIZATION
# ==================================================


def initialize_environment() -> None:
    """
    Initialize CyberRecon AI runtime environment.
    """

    os.makedirs(
        "reports",
        exist_ok=True,
    )



# ==================================================
# REPORT GENERATOR
# ==================================================


def generate_reports(
    domain: str,
    scan_data: dict,
) -> tuple[str, str, str]:
    """
    Generate HTML, PDF and JSON reports.

    Returns:
        HTML path,
        PDF path,
        JSON path
    """

    html_path = generate_report(
        domain,
        scan_data,
    )


    pdf_filename = (
        f"reports/{domain.replace('.', '_')}_report.pdf"
    )


    pdf_path = generate_pdf_report(
        html_path,
        pdf_filename,
    )


    json_filename = (
        domain.replace(".", "_")
        + "_report.json"
    )


    json_path = generate_json_report(
        scan_data,
        json_filename,
    )


    return (
        html_path,
        pdf_path,
        json_path,
    )



# ==================================================
# MAIN ENGINE
# ==================================================


def main() -> None:
    """
    CyberRecon AI execution engine.
    """


    initialize_environment()


    ui.show_banner()


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

        # ==================================
        # TARGET ANALYSIS
        # ==================================


        target_info = analyze_target(
            target_url
        )


        domain = target_info["domain"]


        normalized_url = target_info["url"]



        ui.show_target_info(

            target=domain,

            ip=target_info["ip"],

        )



        # ==================================
        # INTELLIGENCE COLLECTION
        # ==================================


        scanner = ConcurrentScanner()


        results = scanner.run(

            {

                "whois":
                    lambda:
                    get_whois_info(domain),



                "dns":
                    lambda:
                    get_dns_records(domain),



                "ssl":
                    lambda:
                    get_ssl_info(domain),



                "headers":
                    lambda:
                    get_security_headers(
                        normalized_url
                    ),



                "technology":
                    lambda:
                    TechnologyDetector(
                        normalized_url
                    ).analyze(),



                "subdomains":
                    lambda:
                    get_subdomains(domain),



                "ports":
                    lambda:
                    scan_ports(domain),



                "robots":
                    lambda:
                    analyze_robots_txt(
                        normalized_url
                    ),

            }

        )
                # ==================================
        # COLLECT RESULTS
        # ==================================

        whois_info = results["whois"]

        dns_info = results["dns"]

        ssl_info = results["ssl"]

        headers_info = results["headers"]

        tech = results["technology"]

        subdomain_result = results["subdomains"]

        port_results = results["ports"]

        robots_info = results["robots"]



        # ==================================
        # DISPLAY INFORMATION
        # ==================================

        ui.show_whois_info(
            whois_info
        )


        ui.show_dns_info(
            dns_info
        )


        ui.show_section(
            "SSL/TLS CERTIFICATE"
        )


        ui.show_ssl_info(
            ssl_info
        )


        ui.show_http_headers(
            headers_info
        )


        ui.show_technology_info(
            tech
        )



        # ==================================
        # VULNERABILITY INTELLIGENCE
        # ==================================

        vulnerability_report = (
            VulnerabilityIntelligence(
                tech
            ).analyze()
        )


        ui.show_vulnerability_intelligence(
            vulnerability_report
        )



        # ==================================
        # SUBDOMAIN HANDLING
        # ==================================

        if isinstance(
            subdomain_result,
            dict
        ):

            subs = subdomain_result.get(
                "subdomains",
                []
            )

        else:

            subs = subdomain_result



        ui.show_subdomains_info(
            subs
        )


        ui.show_port_scan_info(
            port_results
        )


        ui.show_robots_info(
            robots_info
        )



        # ==================================
        # SECURITY RISK ENGINE
        # ==================================

        risk_report = calculate_security_score(

            headers=headers_info,

            ssl_info=ssl_info,

            robots_info=robots_info,

            ports=port_results,

            subdomains=subs,

        )


        ui.show_risk_engine_info(
            risk_report
        )



        # ==================================
        # SERVICE DETECTION
        # ==================================

        services = detect_services(
            port_results
        )


        ui.show_service_detection_info(
            services
        )



        # ==================================
        # TIMER STOP
        # ==================================

        scan_end = end_timer()


        scan_end_time = get_time()


        scan_duration = calculate_duration(

            scan_start,

            scan_end

        )



        print(
            "\n========== REPORT GENERATION =========="
        )



        # ==================================
        # SCAN DATA BUILD
        # ==================================

        scan_data = {


            "scan_metadata": {

                "version":
                    VERSION,


                "scan_id":
                    scan_id,


                "scan_start_time":
                    scan_start_time,


                "scan_end_time":
                    scan_end_time,


                "scan_duration":
                    scan_duration,

            },


            "target_information":
                target_info,


            "whois_information":
                whois_info,


            "dns_information":
                dns_info,


            "ssl_information":
                ssl_info,


            "headers_information":
                headers_info,


            "technology_information":
                tech,


            "vulnerability_information":
                vulnerability_report,


            "subdomains":
                subs,


            "ports":
                port_results,


            "robots_information":
                robots_info,


            "risk_score":
                risk_report["score"],


            "risk_level":
                risk_report["risk_level"],


            "findings":
                risk_report["findings"],


            "services":
                services,

        }



        # ==================================
        # REPORT GENERATION
        # ==================================

        html_path, pdf_path, json_path = generate_reports(

            domain,

            scan_data,

        )


        print(
            f"PDF Report Generated : {pdf_path}"
        )



        # ==================================
        # FINAL SUMMARY
        # ==================================

        summary = {


            "Target":
                domain,


            "Security Score":
                f"{risk_report['score']}/100",


            "Risk Level":
                risk_report["risk_level"],


            "Open Ports":
                len(port_results),


            "Services":
                len(services),


            "Subdomains":
                len(subs),


            "Findings":
                len(risk_report["findings"]),


            "Scan Duration":
                scan_duration,

        }



        ui.show_summary(
            summary
        )



        ui.show_report_info(

            "HTML Report",

            html_path,

        )


        ui.show_report_info(

            "JSON Report",

            json_path,

        )


        ui.show_completion()



        logger.info(

            "CyberRecon AI scan completed successfully"

        )



    except Exception as error:


        logger.exception(

            "CyberRecon AI scan failed: %s",

            error,

        )


        print(
            "\n[!] Scan failed. Check logs."
        )


        sys.exit(1)




if __name__ == "__main__":

    main()