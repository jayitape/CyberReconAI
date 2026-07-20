"""
CyberRecon AI
Enterprise PDF Report Generator

Version:
v1.0.20

Converts HTML security reports into
professional PDF reports using Playwright Chromium.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

from playwright.sync_api import sync_playwright

from modules.logger import setup_logger


logger = setup_logger()


PDF_FORMAT: Final[str] = "A4"


def generate_pdf_report(
    html_path: str,
    pdf_path: str,
) -> str:
    """
    Generate PDF report from HTML report.

    Args:
        html_path:
            Path of generated HTML report.

        pdf_path:
            Output PDF file path.

    Returns:
        Generated PDF path.

    Raises:
        FileNotFoundError:
            If HTML report does not exist.
    """

    html_file = Path(html_path)
    output_file = Path(pdf_path)


    if not html_file.exists():

        logger.error(
            "HTML report not found: %s",
            html_path,
        )

        raise FileNotFoundError(
            html_path
        )


    try:

        logger.info(
            "Starting PDF generation..."
        )


        with sync_playwright() as playwright:

            browser = playwright.chromium.launch(
                headless=True
            )


            page = browser.new_page()


            page.goto(
                html_file.resolve().as_uri(),
                wait_until="networkidle",
            )


            page.pdf(
                path=str(output_file),
                format=PDF_FORMAT,
                print_background=True,
                margin={
                    "top": "20px",
                    "bottom": "20px",
                    "left": "20px",
                    "right": "20px",
                },
            )


            browser.close()


        logger.info(
            "PDF generated successfully: %s",
            pdf_path,
        )


        return str(output_file)


    except Exception as exc:

        logger.exception(
            "PDF generation failed: %s",
            exc,
        )

        raise