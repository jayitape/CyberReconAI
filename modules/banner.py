"""
CyberRecon AI

Banner Module

Displays professional CLI banner.
"""


from rich.console import Console
from rich.panel import Panel


console = Console()



def show_banner() -> None:
    """
    Display CyberRecon AI application banner.
    """


    banner = """

CyberRecon AI

Website Security Assessment Toolkit

Version : 1.0.13

For Authorized Security Assessments Only

"""


    console.print(

        Panel(

            banner,

            title="CyberRecon AI",

            border_style="cyan"

        )

    )