"""
CyberRecon AI

Main application entry point.
"""

from modules.banner import show_banner
from modules.cli import get_target
from modules.logger import setup_logger
from modules.target import get_target_info


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

    # Collect target information
    target_info = get_target_info(target)

    # Display target information
    print("\n========== Target Information ==========")
    print(f"URL        : {target_info['url']}")
    print(f"Domain     : {target_info['domain']}")
    print(f"IP Address : {target_info['ip']}")
    print(f"Scheme     : {target_info['scheme']}")
    print(f"Reachable  : {target_info['reachable']}")

    logger.info("Reconnaissance pipeline initialized.")


if __name__ == "__main__":
    main()