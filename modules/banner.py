"""
CyberRecon AI Banner Module
Displays the application banner.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner() -> None:
    """Display the CyberRecon AI banner."""

    banner = """
[bold cyan]CyberRecon AI[/bold cyan]

Website Security Assessment Toolkit

Version : 1.0.7

For Authorized Security Assessments Only
"""

    console.print(
        Panel.fit(
            banner,
            title="CyberRecon AI",
            border_style="green"
        )
    )