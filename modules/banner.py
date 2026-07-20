"""
CyberRecon AI
Professional Banner
"""

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


VERSION = "1.0.17"


def show_banner():

    logo = r"""

   ██████╗██╗   ██╗██████╗ ███████╗██████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝

        ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
        ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
        ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
        ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
        ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
        ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝

                         █████╗ ██╗
                        ██╔══██╗██║
                        ███████║██║
                        ██╔══██║██║
                        ██║  ██║██║
                        ╚═╝  ╚═╝╚═╝

"""

    text = Text()

    text.append(logo, style="bold bright_cyan")

    text.append("\n")

    text.append("Website Security Assessment Toolkit\n", style="bold white")

    text.append("Professional Defensive Security Framework\n", style="bright_green")

    text.append("────────────────────────────────────────────\n", style="cyan")

    text.append(f"Version : {VERSION}\n", style="bold yellow")

    text.append("Authorized Security Testing Only\n", style="bold red")

    console.print(
        Panel(
            Align.center(text),
            border_style="bright_cyan",
            padding=(1, 4),
            title="[bold green]CyberRecon AI[/bold green]",
            subtitle="[cyan]Developed by Jay Itape[/cyan]",
        )
    )
