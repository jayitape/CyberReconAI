"""
CyberRecon AI
Professional Rich Theme
"""

from rich.theme import Theme
from rich.console import Console


CYBER_THEME = Theme(
    {
        "title": "bold bright_cyan",
        "header": "bold cyan",
        "success": "bold green",
        "warning": "bold yellow",
        "danger": "bold red",
        "info": "bold blue",
        "label": "bold white",
        "value": "white",
        "panel": "cyan",
        "table_header": "bold bright_cyan",
        "scan": "bold bright_magenta",
        "risk_low": "green",
        "risk_medium": "yellow",
        "risk_high": "red",
        "risk_critical": "bold red",
        "footer": "bright_black"
    }
)


console = Console(
    theme=CYBER_THEME,
    soft_wrap=True
)