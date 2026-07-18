"""
CyberRecon AI v1.1.0

Enterprise Rich UI Module

Reusable UI components for CyberRecon AI
"""

from datetime import datetime
from typing import Dict, List, Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.rule import Rule
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TimeElapsedColumn
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

console = Console()


# ==========================================
# UI Helper Functions
# ==========================================

def _risk_color(level: str) -> str:

    level = level.lower()

    if level in ["critical", "high"]:
        return "red"

    elif level == "medium":
        return "yellow"

    elif level == "low":
        return "green"

    else:
        return "cyan"



def ui_title(title: str):

    console.print(
        Rule(
            title,
            style="cyan"
        )
    )



def print_message(
        message: str,
        status: str = "INFO"
):

    colors = {

        "INFO": "cyan",
        "SUCCESS": "green",
        "WARNING": "yellow",
        "ERROR": "red"

    }


    color = colors.get(
        status.upper(),
        "white"
    )


    console.print(
        f"[{color}][{status}][/] {message}"
    )



# ==========================================
# Premium Banner
# ==========================================

def show_banner():

    banner = """

 ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝


        CyberRecon AI

 Website Security Assessment Toolkit

        Version : 1.1.0
        Enterprise Edition

"""


    panel = Panel(

        Align.center(

            Text(
                banner,
                style="bold cyan"
            )

        ),

        border_style="cyan"

    )


    console.print(panel)



# ==========================================
# Target Information Panel
# ==========================================


def show_target_info(
        target: str,
        ip: str = None,
        technology: str = None
):


    table = Table(
        title="Target Information"
    )


    table.add_column(
        "Field",
        style="cyan"
    )


    table.add_column(
        "Value"
    )


    table.add_row(
        "Target",
        target
    )


    if ip:

        table.add_row(
            "IP Address",
            ip
        )


    if technology:

        table.add_row(
            "Technology",
            technology
        )


    console.print(table)
    # ==========================================
# Live Progress Scanner
# ==========================================


def show_progress(
        task_name: str = "Scanning Target",
        total: int = 100
):

    with Progress(

        SpinnerColumn(),

        TextColumn(
            "[progress.description]{task.description}"
        ),

        BarColumn(),

        TextColumn(
            "{task.percentage:>3.0f}%"
        ),

        TimeElapsedColumn()

    ) as progress:


        task = progress.add_task(
            task_name,
            total=total
        )


        while not progress.finished:

            progress.update(
                task,
                advance=5
            )



# ==========================================
# Animated Status Messages
# ==========================================


def show_scan_status(
        module: str,
        status: str
):


    status_color = {

        "RUNNING": "yellow",
        "COMPLETED": "green",
        "FAILED": "red",
        "INFO": "cyan"

    }


    color = status_color.get(
        status.upper(),
        "white"
    )


    console.print(

        Panel(

            f"""

Module :

[bold]{module}[/bold]


Status :

[{color}]{status}[/{color}]


Time :

{datetime.now().strftime("%H:%M:%S")}

""",

            title="Scan Status",

            border_style=color

        )

    )



# ==========================================
# Port Scanning Dashboard
# ==========================================


def show_ports(
        ports: List[Dict[str,Any]]
):


    table = Table(

        title="Open Ports Discovery",

        show_lines=True

    )


    table.add_column(

        "Port",

        style="cyan"

    )


    table.add_column(

        "Protocol"

    )


    table.add_column(

        "Service"

    )


    table.add_column(

        "State"

    )


    table.add_column(

        "Version"

    )



    for port in ports:


        table.add_row(

            str(
                port.get(
                    "port",
                    "-"
                )
            ),


            str(
                port.get(
                    "protocol",
                    "TCP"
                )
            ),


            str(
                port.get(
                    "service",
                    "-"
                )
            ),


            str(
                port.get(
                    "state",
                    "-"
                )
            ),


            str(
                port.get(
                    "version",
                    "-"
                )
            )

        )


    console.print(table)



# ==========================================
# Technology Detection Panel
# ==========================================


def show_technology(
        technologies: Dict[str,str]
):


    table = Table(

        title="Technology Fingerprint"

    )


    table.add_column(

        "Component",

        style="cyan"

    )


    table.add_column(

        "Detected Value"

    )


    for key,value in technologies.items():


        table.add_row(

            str(key),

            str(value)

        )


    console.print(table)



# ==========================================
# Generic Section Header
# ==========================================


def show_section(
        name:str
):

    console.print(

        Panel(

            f"[bold cyan]{name}[/bold cyan]",

            border_style="cyan"

        )

    )
    # ==========================================
# Vulnerability Findings Dashboard
# ==========================================


def show_findings(
        findings: List[Dict[str, Any]]
):


    table = Table(

        title="Security Vulnerability Findings",

        show_lines=True

    )


    table.add_column(

        "ID",

        style="cyan"

    )


    table.add_column(

        "Finding"

    )


    table.add_column(

        "Severity"

    )


    table.add_column(

        "CVSS"

    )


    table.add_column(

        "Description"

    )



    counter = 1


    for finding in findings:


        severity = str(

            finding.get(
                "severity",
                "Unknown"
            )

        )


        color = _risk_color(
            severity
        )


        table.add_row(

            str(counter),


            str(
                finding.get(
                    "title",
                    "Unknown Issue"
                )
            ),


            f"[{color}]{severity}[/{color}]",


            str(
                finding.get(
                    "cvss",
                    "-"
                )
            ),


            str(
                finding.get(
                    "description",
                    "-"
                )
            )

        )


        counter += 1



    console.print(table)




# ==========================================
# Risk Level Summary
# ==========================================


def show_risk_summary(
        findings: List[Dict[str,Any]]
):


    risk_count = {


        "Critical":0,

        "High":0,

        "Medium":0,

        "Low":0,

        "Info":0

    }



    for item in findings:


        level = str(

            item.get(
                "severity",
                "Info"
            )

        ).capitalize()



        if level in risk_count:

            risk_count[level] += 1



    table = Table(

        title="Risk Distribution"

    )


    table.add_column(

        "Severity"

    )


    table.add_column(

        "Count"

    )


    for level,count in risk_count.items():


        color = _risk_color(level)



        table.add_row(

            f"[{color}]{level}[/{color}]",

            str(count)

        )


    console.print(table)




# ==========================================
# Scan Statistics Panel
# ==========================================


def show_statistics(
        stats: Dict[str,Any]
):


    panel_text = ""


    for key,value in stats.items():


        panel_text += (

            f"\n[cyan]{key}[/cyan] : {value}"

        )



    console.print(

        Panel(

            panel_text,

            title="Scan Statistics",

            border_style="green"

        )

    )




# ==========================================
# Vulnerability Detail View
# ==========================================


def show_finding_detail(
        finding: Dict[str,Any]
):


    severity = str(

        finding.get(
            "severity",
            "Unknown"
        )

    )


    color = _risk_color(
        severity
    )



    details = f"""

[cyan]Title:[/cyan]

{finding.get('title','-')}


[cyan]Severity:[/cyan]

[{color}]{severity}[/{color}]


[cyan]CVSS Score:[/cyan]

{finding.get('cvss','-')}


[cyan]Description:[/cyan]

{finding.get('description','-')}


[cyan]Recommendation:[/cyan]

{finding.get('recommendation','-')}

"""



    console.print(

        Panel(

            details,

            title="Finding Details",

            border_style=color

        )

    )



# ==========================================
# Empty Result Handler
# ==========================================


def show_no_findings():

    console.print(

        Panel(

            """
No security issues detected.

Target appears secure based on
performed assessment modules.

""",

            title="Security Result",

            border_style="green"

        )

    )
    # ==========================================
# Final Enterprise Dashboard
# ==========================================


def show_summary(
        summary: Dict[str, Any]
):


    console.print(

        Panel(

            Align.center(

                Text(

                    "CYBERRECON AI\nFINAL SECURITY ASSESSMENT",

                    style="bold cyan"

                )

            ),

            border_style="cyan"

        )

    )



    table = Table(

        title="Assessment Summary",

        show_lines=True

    )


    table.add_column(

        "Metric",

        style="cyan"

    )


    table.add_column(

        "Result"

    )



    for key,value in summary.items():


        table.add_row(

            str(key).replace("_"," ").title(),

            str(value)

        )



    table.add_row(

        "Generated Time",

        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    )


    console.print(table)




# ==========================================
# Scan Completion Banner
# ==========================================


def show_completion(
        message: str = "Security Assessment Completed"
):


    console.print(

        Panel(

            f"""

[bold green]
✓ {message}
[/bold green]


CyberRecon AI Enterprise Engine


Report generation ready.

""",

            title="Completed",

            border_style="green"

        )

    )




# ==========================================
# Report Information Panel
# ==========================================


def show_report_info(
        report_type: str,
        path: str
):


    console.print(

        Panel(

            f"""

Report Type :

{report_type}


Location :

{path}


Generated :

{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

""",

            title="Report Information",

            border_style="cyan"

        )

    )




# ==========================================
# Footer Branding
# ==========================================


def show_footer():


    console.print(

        Rule(

            "CyberRecon AI | Authorized Defensive Security Assessment",

            style="cyan"

        )

    )



    console.print(

        Align.center(

            Text(

                "Built for SOC Analysts & Security Professionals",

                style="bold cyan"

            )

        )

    )



# ==========================================
# Quick Dashboard Wrapper
# ==========================================


def show_dashboard(
        target: str,
        findings: List[Dict[str,Any]],
        summary: Dict[str,Any]
):


    show_banner()


    show_target_info(
        target
    )


    if findings:

        show_findings(
            findings
        )


        show_risk_summary(
            findings
        )

    else:

        show_no_findings()



    show_summary(

        summary

    )


    show_completion()


    show_footer()