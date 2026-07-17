"""
CyberRecon AI

Main application entry point.
"""

from modules.banner import show_banner
from modules.cli import get_target
from modules.logger import setup_logger


def main() -> None:
    """
    Main entry point of the application.
    """

    # Display application banner
    show_banner()

    # Initialize logger
    logger = setup_logger()

    # Get validated target from CLI
    target = get_target()

    logger.info("Target selected: %s", target)

    print(f"\n[+] Validated Target: {target}")

    # Placeholder for future reconnaissance modules
    logger.info("Reconnaissance pipeline initialized.")


if __name__ == "__main__":
    main()