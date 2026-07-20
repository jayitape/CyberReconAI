"""
CyberRecon AI v1.1.0

Enterprise Rich UI Module

Reusable UI components for CyberRecon AI
"""

from datetime import datetime
from typing import Any, Dict, List

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from pyfiglet import Figlet
from rich import box

console = Console()


# ==========================================
# UI Helper Functions
# ==========================================

def _risk_color(level: str) -> str:
    level = level.lower()

    if level in ("critical", "high"):
        return "red"
    elif level == "medium":
        return "yellow"
    elif level == "low":
        return "green"

    return "cyan"


def ui_title(title: str):
    console.print(Rule(title, style="cyan"))


def print_message(message: str, status: str = "INFO"):
    colors = {
        "INFO": "cyan",
        "SUCCESS": "green",
        "WARNING": "yellow",
        "ERROR": "red",
    }

    color = colors.get(status.upper(), "white")
    console.print(f"[{color}][{status}][/] {message}")


# ==========================================
# Premium Banner
# ==========================================

def show_banner():
    """Display CyberRecon AI enterprise banner."""

    banner = r"""
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗ ██████╗  █████╗  ███╗   ██╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝ ██╗  ██╗ ████╗  ██║
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██████╔╝█████╗  ██║      ██║  ██║ ██╔██╗ ██║
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██║      ██║  ██║ ██║╚██╗██║
╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║  ██║███████╗╚██████╗  █████╔╝ ██║ ╚████║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚════╝  ╚═╝  ╚═══╝

                               █████╗ ██╗
                              ██╔══██╗██║
                              ███████║██║
                              ██╔══██║██║
                              ██║  ██║██║
                              ╚═╝  ╚═╝╚═╝
"""

    subtitle = Text()
    subtitle.append("CyberRecon AI\n", style="bold bright_red")
    subtitle.append(
        "Authorized Defensive Security Assessment Toolkit\n",
        style="white",
    )
    subtitle.append("Enterprise Edition\n\n", style="bold red")
    subtitle.append("Version : v1.0.20\n", style="bright_white")
    subtitle.append("Python  : 3.12+\n", style="bright_white")
    subtitle.append("Platform: Windows\n", style="bright_white")
    subtitle.append("Developed by JAY ITAPE", style="bold yellow")

    console.print(
    Panel(
        Align.center(
            Text(banner, style="bold bright_red") + Text("\n") + subtitle
        ),
        title="[bold bright_red]CyberRecon AI[/bold bright_red]",
        subtitle="[bold white]Enterprise Security Framework[/bold white]",
        border_style="bright_red",
        padding=(1, 4),
    )
)

# ==========================================
# Section Header
# ==========================================

def show_section(title: str):
    console.print(
        Panel(
            f"[bold cyan]{title}[/bold cyan]",
            border_style="cyan",
        )
    )


# ==========================================
# Target Information
# ==========================================

def show_target_info(
    target: str,
    ip: str | None = None,
    technology: str | None = None,
):

    table = Table(title="Target Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value")

    table.add_row(
    "Target",
    str(target)
)

    if ip:
        table.add_row("IP Address", ip)

    if technology:
        table.add_row("Technology", technology)

    console.print(table)

# ==========================================
# WHOIS INFO
# ==========================================

def show_whois_info(whois_info: dict[str, object]) -> None:
    """
    Display WHOIS information using Rich table.

    Args:
        whois_info: Dictionary containing WHOIS lookup results.
    """

    from rich.table import Table

    table = Table(
        title="🌐 WHOIS Information",
        show_header=True,
        header_style="bold cyan",
        expand=True,
    )

    table.add_column("Field", style="bold green", width=25)
    table.add_column("Value", style="white")

    for key, value in whois_info.items():
        table.add_row(
            str(key).replace("_", " ").title(),
            str(value),
        )

    console.print(table)

# ==========================================
# DNS INFO
# ==========================================    

def show_dns_info(dns_info: dict[str, object]) -> None:
    """
    Display DNS enumeration results using Rich table.

    Args:
        dns_info: Dictionary containing DNS records.
    """

    from rich.table import Table

    table = Table(
        title="🔎 DNS Enumeration",
        show_header=True,
        header_style="bold cyan",
        expand=True,
    )

    table.add_column("Record", style="bold green", width=20)
    table.add_column("Value", style="white")

    for key, value in dns_info.items():
        table.add_row(
            str(key).upper(),
            str(value),
        )

    console.print(table)

#==========================================
# Http_headers Info
# ==========================================  

def show_http_headers(headers_info: dict[str, object]) -> None:
    """
    Display HTTP security header analysis using Rich table.

    Args:
        headers_info: Dictionary containing HTTP security header results.
    """

    from rich.table import Table

    table = Table(
        title="🛡️ HTTP Security Headers",
        show_header=True,
        header_style="bold cyan",
        expand=True,
    )

    table.add_column("Header", style="bold green", width=30)
    table.add_column("Value", style="white")

    for key, value in headers_info.items():
        table.add_row(
            str(key).replace("_", " ").title(),
            str(value),
        )

    console.print(table)

# =========================================
#   Technology info
# ==========================================


def show_technology_info(tech_info: dict[str, list[str]]) -> None:
    """
    Display detected technologies using Rich tables.

    Args:
        tech_info: Dictionary containing technology detection results.
    """

    from rich.table import Table

    table = Table(
        title="💻 Technology Detection",
        show_header=True,
        header_style="bold cyan",
        expand=True,
    )

    table.add_column("Category", style="bold green", width=25)
    table.add_column("Detected Technologies", style="white")

    categories = {
        "server": "Web Server",
        "cms": "CMS",
        "frameworks": "Frameworks",
        "javascript": "JavaScript Libraries",
    }

    for key, title in categories.items():
        values = tech_info.get(key, [])

        if values:
            table.add_row(
                title,
                "\n".join(values),
            )
        else:
            table.add_row(
                title,
                "None Detected",
            )

    console.print(table)

# ==========================================
# Subdomains Info
# ==========================================

def show_subdomains_info(subdomains: list[str]) -> None:
    """
    Display discovered subdomains in a professional table format.

    Args:
        subdomains: List of discovered subdomain names.
    """

    console.print("\n")

    table = Table(
        title="Subdomain Enumeration",
        box=box.ROUNDED
    )

    table.add_column(
        "No.",
        justify="center",
        style="cyan"
    )

    table.add_column(
        "Subdomain",
        style="green"
    )

    if not subdomains:
        table.add_row(
            "-",
            "No subdomains found"
        )

    else:
        for index, subdomain in enumerate(subdomains, start=1):

            table.add_row(
                str(index),
                subdomain
            )

    console.print(table)

    console.print(
        f"\n[bold]Total Subdomains Found:[/bold] {len(subdomains)}"
    )
# ==========================================
# Port Scan
# ==========================================

def show_port_scan_info(port_results: list[dict]) -> None:
    """
    Display port scan results in a professional Rich table.

    Args:
        port_results: List of detected open ports.
    """

    console.print()

    table = Table(
        title="Open Port Scan Results",
        box=box.ROUNDED,
    )

    table.add_column("Port", justify="center", style="cyan", no_wrap=True)
    table.add_column("Service", style="green")
    table.add_column("State", justify="center", style="yellow")
    table.add_column("Banner", style="white")

    if not port_results:
        table.add_row("-", "No open ports", "-", "-")
    else:
        for result in port_results:
            banner = result.get("banner") or "-"

            table.add_row(
                str(result.get("port", "-")),
                result.get("service", "-"),
                result.get("state", "-"),
                banner,
            )

    console.print(table)

    console.print(
        f"\n[bold]Open Ports Found:[/bold] {len(port_results)}"
    )

# ==========================================
# Service Detection Info
# ==========================================

def show_service_detection_info(
    services: list[dict],
) -> None:
    """
    Display detected services in a professional Rich table.

    Args:
        services: List of detected services.
    """

    console.print()

    table = Table(
        title="Service Detection",
        box=box.ROUNDED,
    )

    table.add_column(
        "Port",
        justify="center",
        style="cyan",
        no_wrap=True,
    )

    table.add_column(
        "Service",
        style="green",
    )

    table.add_column(
        "State",
        justify="center",
        style="yellow",
    )

    if not services:
        table.add_row(
            "-",
            "No services detected",
            "-",
        )
    else:
        for service in services:
            table.add_row(
                str(service.get("port", "-")),
                service.get("service", "-"),
                service.get("state", "-"),
            )

    console.print(table)

    console.print(
        f"\n[bold]Detected Services:[/bold] {len(services)}"
    )

# ==========================================
# Robots Info
# ==========================================

def show_robots_info(
    robots_info: Dict[str, Any],
) -> None:
    """
    Display robots.txt analysis in a professional Rich table.

    Args:
        robots_info: Dictionary containing robots.txt analysis results.
    """

    table = Table(
        title="Robots.txt Analyzer",
        box=box.ROUNDED,
    )

    table.add_column(
        "Property",
        style="bold cyan",
        width=30,
    )

    table.add_column(
        "Value",
        style="white",
    )

    if robots_info.get("status") != "Completed":
        table.add_row(
            "Status",
            str(robots_info.get("message", "Analysis failed")),
        )
        console.print(table)
        return

    summary = robots_info.get("summary", {})

    table.add_row(
        "Robots URL",
        str(robots_info.get("robots_url", "-")),
    )

    table.add_row(
        "User Agents",
        str(robots_info.get("user_agents", "-")),
    )

    table.add_row(
        "Disallowed Paths",
        str(summary.get("total_disallowed", 0)),
    )

    table.add_row(
        "Allowed Paths",
        str(summary.get("total_allowed", 0)),
    )

    table.add_row(
        "Sitemaps",
        str(summary.get("total_sitemaps", 0)),
    )

    table.add_row(
        "Sensitive Findings",
        str(summary.get("sensitive_findings", 0)),
    )

    console.print(table)

# ==========================================
# Risk Engine Info
# ==========================================

def show_risk_engine_info(
    risk_report: Dict[str, Any],
) -> None:
    """
    Display overall security score and findings using Rich UI.

    Args:
        risk_report: Dictionary returned by the Risk Engine.
    """

    score = risk_report.get("score", 0)
    risk_level = str(risk_report.get("risk_level", "UNKNOWN"))

    color = _risk_color(risk_level)

    console.print(
        Panel(
            (
                f"[bold]Overall Security Score:[/bold] {score}/100\n\n"
                f"[bold]Risk Level:[/bold] "
                f"[{color}]{risk_level}[/{color}]"
            ),
            title="Security Risk Assessment",
            border_style=color,
        )
    )

    findings = risk_report.get("findings", [])

    if findings:
        show_findings(findings)
    else:
        show_no_findings()



# ==========================================
# Vulnerability Intelligence Info
# ==========================================


def show_vulnerability_intelligence(
    vulnerability_report: dict[str, Any],
) -> None:
    """
    Display vulnerability intelligence results.

    Args:
        vulnerability_report: Vulnerability analysis report.
    """

    table = Table(
        title="Vulnerability Intelligence",
        box=box.ROUNDED,
        show_lines=True,
    )

    table.add_column(
        "Category",
        style="bold cyan",
    )

    table.add_column(
        "Details",
        style="white",
    )

    products = vulnerability_report.get("products", [])
    cves = vulnerability_report.get("cves", [])
    summary = vulnerability_report.get("summary", {})

    table.add_row(
        "Detected Products",
        ", ".join(products) if products else "None Detected",
    )

    table.add_row(
        "Detected CVEs",
        ", ".join(cves) if cves else "None Detected",
    )

    severity_summary = (
        f"Critical: {summary.get('critical', 0)} | "
        f"High: {summary.get('high', 0)} | "
        f"Medium: {summary.get('medium', 0)} | "
        f"Low: {summary.get('low', 0)}"
    )

    table.add_row(
        "Severity Summary",
        severity_summary,
    )

    console.print(table)
# ==========================================
# Live Progress
# ==========================================

def show_progress(
    task_name: str = "Scanning Target",
    total: int = 100,
):

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
    ) as progress:

        task = progress.add_task(task_name, total=total)

        while not progress.finished:
            progress.update(task, advance=5)


# ==========================================
# Scan Status
# ==========================================

def show_scan_status(module: str, status: str):

    colors = {
        "RUNNING": "yellow",
        "COMPLETED": "green",
        "FAILED": "red",
        "INFO": "cyan",
    }

    color = colors.get(status.upper(), "white")

    console.print(
        Panel(
            f"""
Module : {module}

Status : [{color}]{status}[/{color}]

Time : {datetime.now().strftime("%H:%M:%S")}
""",
            title="Scan Status",
            border_style=color,
        )
    )
    # ==========================================
# Port Scanning Dashboard
# ==========================================

def show_ports(ports: List[Dict[str, Any]]):

    table = Table(title="Open Ports Discovery", show_lines=True)

    table.add_column("Port", style="cyan")
    table.add_column("Protocol")
    table.add_column("Service")
    table.add_column("State")
    table.add_column("Version")

    for port in ports:
        table.add_row(
            str(port.get("port", "-")),
            str(port.get("protocol", "TCP")),
            str(port.get("service", "-")),
            str(port.get("state", "-")),
            str(port.get("version", "-")),
        )

    console.print(table)


# ==========================================
# Technology Detection Panel
# ==========================================

def show_technology(technologies: Dict[str, Any]):

    table = Table(title="Technology Fingerprint")

    table.add_column("Component", style="cyan")
    table.add_column("Detected Value")

    for key, value in technologies.items():

        if isinstance(value, list):
            value = ", ".join(str(v) for v in value) if value else "-"

        table.add_row(str(key).replace("_", " ").title(), str(value))

    console.print(table)


# ==========================================
# Vulnerability Findings Dashboard
# ==========================================

def show_findings(findings: List[Dict[str, Any]]):

    table = Table(
        title="Security Vulnerability Findings",
        show_lines=True,
    )

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Finding")
    table.add_column("Severity")
    table.add_column("CVSS")
    table.add_column("Description")

    for idx, finding in enumerate(findings, start=1):

        severity = str(
            finding.get(
                "severity",
                finding.get("risk", "Unknown"),
            )
        )

        color = _risk_color(severity)

        title = finding.get(
            "title",
            finding.get(
                "issue",
                "Unknown Issue",
            ),
        )

        description = finding.get(
            "description",
            finding.get(
                "details",
                "-",
            ),
        )

        table.add_row(
            str(idx),
            str(title),
            f"[{color}]{severity}[/{color}]",
            str(finding.get("cvss", "-")),
            str(description),
        )

    console.print(table)
    # ==========================================
# Risk Level Summary
# ==========================================

def show_risk_summary(findings: List[Dict[str, Any]]):

    risk_count = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
        "Info": 0,
    }

    for finding in findings:

        severity = str(
            finding.get(
                "severity",
                finding.get("risk", "Info"),
            )
        ).capitalize()

        if severity in risk_count:
            risk_count[severity] += 1
        else:
            risk_count["Info"] += 1

    table = Table(title="Risk Distribution")

    table.add_column("Severity", style="cyan")
    table.add_column("Count", justify="center")

    for level, count in risk_count.items():
        color = _risk_color(level)
        table.add_row(
            f"[{color}]{level}[/{color}]",
            str(count),
        )

    console.print(table)


# ==========================================
# Scan Statistics
# ==========================================

def show_statistics(stats: Dict[str, Any]):

    table = Table(title="Scan Statistics")

    table.add_column("Metric", style="cyan")
    table.add_column("Value")

    for key, value in stats.items():
        table.add_row(
            str(key).replace("_", " ").title(),
            str(value),
        )

    console.print(table)


# ==========================================
# Finding Detail
# ==========================================

def show_finding_detail(finding: Dict[str, Any]):

    severity = str(
        finding.get(
            "severity",
            finding.get("risk", "Unknown"),
        )
    )

    color = _risk_color(severity)

    panel = f"""
[bold cyan]Title[/bold cyan]
{finding.get("title", finding.get("issue", "-"))}

[bold cyan]Severity[/bold cyan]
[{color}]{severity}[/{color}]

[bold cyan]CVSS[/bold cyan]
{finding.get("cvss", "-")}

[bold cyan]Description[/bold cyan]
{finding.get("description", finding.get("details", "-"))}

[bold cyan]Recommendation[/bold cyan]
{finding.get("recommendation", "-")}
"""

    console.print(
        Panel(
            panel,
            title="Finding Details",
            border_style=color,
        )
    )


# ==========================================
# No Findings
# ==========================================

def show_no_findings():

    console.print(
        Panel(
            "[bold green]✓ No security issues detected.[/bold green]\n\n"
            "Target appears secure based on the completed assessment modules.",
            title="Security Result",
            border_style="green",
        )
    )
    # ==========================================
# Final Assessment Summary
# ==========================================

def show_summary(summary: Dict[str, Any]):

    console.print(
        Panel(
            Align.center(
                Text(
                    "CYBERRECON AI\nFINAL SECURITY ASSESSMENT",
                    style="bold cyan",
                )
            ),
            border_style="cyan",
        )
    )

    table = Table(title="Assessment Summary", show_lines=True)

    table.add_column("Metric", style="cyan")
    table.add_column("Result")

    for key, value in summary.items():
        table.add_row(
            str(key).replace("_", " ").title(),
            str(value),
        )

    table.add_row(
        "Generated Time",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    console.print(table)


# ==========================================
# Completion Banner
# ==========================================

def show_completion(
    message: str = "Security Assessment Completed Successfully",
):

    console.print(
        Panel(
            f"""
[bold green]
✓ {message}
[/bold green]

CyberRecon AI Enterprise Engine

Reports generated successfully.
""",
            title="Completed",
            border_style="green",
        )
    )


# ==========================================
# Report Information
# ==========================================

def show_report_info(report_type: str, path: str):

    console.print(
        Panel(
            f"""
Report Type : {report_type}

Location : {path}

Generated : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
""",
            title="Report Information",
            border_style="cyan",
        )
    )


# ==========================================
# Footer
# ==========================================

def show_footer():

    console.print(
        Rule(
            "CyberRecon AI | Authorized Defensive Security Assessment",
            style="cyan",
        )
    )

    console.print(
        Align.center(
            Text(
                "Built for SOC Analysts & Security Professionals",
                style="bold cyan",
            )
        )
    )


# ==========================================
# Complete Dashboard
# ==========================================

def show_dashboard(
    target: str,
    findings: List[Dict[str, Any]],
    summary: Dict[str, Any],
):

    show_banner()

    show_target_info(target)

    if findings:
        show_findings(findings)
        show_risk_summary(findings)
    else:
        show_no_findings()

    show_summary(summary)

    show_completion()

    # ==========================================
# SSL/TLS Certificate Information
# ==========================================

def show_ssl_info(ssl_info: Dict[str, Any]) -> None:
    """
    Display SSL/TLS certificate information in a Rich table.
    """

    table = Table(
        title="SSL/TLS Certificate",
        show_lines=True,
    )

    table.add_column(
        "Field",
        style="bold cyan",
        no_wrap=True,
    )

    table.add_column(
        "Value",
        style="white",
    )

    for key, value in ssl_info.items():

        if isinstance(value, list):
            value = str(value)

        table.add_row(
            str(key).replace("_", " ").title(),
            str(value),
        )

    console.print(table)

    show_footer()