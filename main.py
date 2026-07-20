"""
CyberRecon AI v1.0.20

Main Application Entry Point

Authorized Defensive Security Assessment Toolkit
"""

import os
import sys

VERSION = "1.0.20"


from modules.cli import parse_arguments
from modules.dns_lookup import get_dns_records
from modules.http_headers import get_security_headers
from modules.json_report import generate_json_report
from modules.logger import setup_logger
from modules.port_scanner import scan_ports
from modules.report_generator import generate_report
from modules.risk_engine import calculate_security_score
from modules.robots_analyzer import analyze_robots_txt
from modules.scan_id import generate_scan_id
from modules.scan_timer import calculate_duration, end_timer, get_time, start_timer
from modules.service_detector import detect_services
from modules.ssl_checker import get_ssl_info
from modules.subdomain_enum import get_subdomains
from modules.target import analyze_target
from modules.technology_detector import TechnologyDetector
from modules.vulnerability_intelligence import VulnerabilityIntelligence
from modules.pdf_generator import generate_pdf_report

from modules.ui import (
    print_message,
    show_banner,
    show_completion,
    show_findings,
    show_footer,
    show_no_findings,
    show_ports,
    show_progress,
    show_report_info,
    show_risk_summary,
    show_scan_status,
    show_ssl_info,
    show_section,
    show_statistics,
    show_summary,
    show_target_info,
    show_whois_info,
    show_dns_info,
    show_technology,
    show_http_headers,
    show_technology_info,
    show_subdomains_info,
    show_port_scan_info,
    show_service_detection_info,
    show_robots_info,
    show_risk_engine_info,
    show_vulnerability_intelligence,
    ui_title,
)
    
from modules.whois_lookup import get_whois_info


def main():

    os.makedirs("reports", exist_ok=True)

    show_banner()

    logger = setup_logger()

    logger.info(f"CyberRecon AI v{VERSION} started")

    args = parse_arguments()

    target_url = args.url

    scan_id = generate_scan_id()

    scan_start = start_timer()

    scan_start_time = get_time()

    print(f"\n[+] Target : {target_url}")

    print(f"[+] Scan ID : {scan_id}")

    try:

        target_info = analyze_target(target_url)
        
        show_target_info(
            
            target=target_info["domain"],
            
            ip=target_info["ip"],
            )
        
        domain = target_info["domain"]
        
        normalized_url = target_info["url"]
        
        whois_info = get_whois_info(domain)
        
        show_whois_info(whois_info)

        dns_info = get_dns_records(domain)
        
        show_dns_info(dns_info)
            
        show_section("SSL/TLS CERTIFICATE")
            
        ssl_info = get_ssl_info(domain)
            
        show_ssl_info(ssl_info)

        headers_info = get_security_headers(normalized_url)
        
        show_http_headers(headers_info)

        tech = TechnologyDetector(normalized_url).analyze()

        show_technology_info(tech)

        vulnerability_report = VulnerabilityIntelligence(tech).analyze()

        show_vulnerability_intelligence(vulnerability_report)

        result = get_subdomains(domain)
        
        if isinstance(result, dict):
            
            subs = result.get("subdomains", [])

        else:
            
            subs = result
            
        show_subdomains_info(subs)

        port_results = scan_ports(domain)
        
        show_port_scan_info(port_results)
        
        robots_info = analyze_robots_txt(normalized_url)
        
        show_robots_info(robots_info)
        
        risk_report = calculate_security_score(
            
            headers=headers_info,
            ssl_info=ssl_info,
            robots_info=robots_info,
            ports=port_results,
            subdomains=subs,
            )
        show_risk_engine_info(risk_report)
        
        services = detect_services(port_results)
        
        show_service_detection_info(services)
        
        # ===============================
        # STOP TIMER BEFORE REPORT CREATION
        # ===============================

        scan_end = end_timer()

        scan_end_time = get_time()

        scan_duration = calculate_duration(scan_start, scan_end)

        print("\n========== REPORT GENERATION ==========")
        
        scan_data = {
            "scan_metadata": {
                "version": VERSION,
                "scan_id": scan_id,
                "scan_start_time": scan_start_time,
                "scan_end_time": scan_end_time,
                "scan_duration": scan_duration,
                },
                
                "target_information": target_info,
                "whois_information": whois_info,
                "dns_information": dns_info,
                "ssl_information": ssl_info,
                "headers_information": headers_info,
                "technology_information": tech,
                "vulnerability_information": vulnerability_report,
                "subdomains": subs,
                "ports": port_results,
                "robots_information": robots_info,
                "risk_score": risk_report["score"],
                "risk_level": risk_report["risk_level"],
                "findings": risk_report["findings"],
                "services": services,
                }
        
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
        
        print(
            f"PDF Report Generated: {pdf_path}"
            )
        
        json_filename = domain.replace(".", "_") + "_report.json"
        
        json_path = generate_json_report(scan_data, json_filename)
        
        summary = {
            "Target": domain,
            "Security Score": f"{risk_report['score']}/100",
            "Risk Level": risk_report["risk_level"],
            "Open Ports": len(port_results),
            "Services": len(services),
            "Subdomains": len(subs),
            "Findings": len(risk_report["findings"]),
            "Scan Duration": scan_duration,
            }
        
        show_summary(summary)
        
        show_report_info("HTML Report", html_path)
        
        show_report_info("JSON Report", json_path)
        
        show_completion()
        
        logger.info("CyberRecon AI scan completed successfully")

    except Exception as e:

        logger.exception("Scan failed: %s", e)

        print("\n[!] Scan failed. Check logs.")

        sys.exit(1)


if __name__ == "__main__":

    main()
