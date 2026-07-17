"""
CyberRecon AI Logger Module

This module configures application-wide logging.
"""

from pathlib import Path
import logging


# Create output directory if it does not exist
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


# Log file path
LOG_FILE = OUTPUT_DIR / "cyberrecon.log"


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    logger = logging.getLogger("CyberReconAI")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger