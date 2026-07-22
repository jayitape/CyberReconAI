"""
CyberRecon AI
Enterprise PDF Report Generator

Version:
v1.1.0

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
    Generate enterprise PDF report from HTML report.
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



        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )



        with sync_playwright() as playwright:



            browser = playwright.chromium.launch(
                headless=True
            )



            page = browser.new_page(
                viewport={
                    "width":1280,
                    "height":1800,
                }
            )



            page.goto(
                html_file.resolve().as_uri(),
                wait_until="load",
            )



            # wait for rendering

            page.wait_for_timeout(
                3000
            )



            # force print rendering

            page.emulate_media(
                media="print"
            )



            page.pdf(

                path=str(output_file),

                format=PDF_FORMAT,

                print_background=True,

                prefer_css_page_size=True,

                margin={

                    "top":"15mm",

                    "bottom":"15mm",

                    "left":"15mm",

                    "right":"15mm",

                },

            )



            browser.close()




        logger.info(
            "PDF generated successfully: %s",
            output_file,
        )



        return str(output_file)




    except Exception as exc:


        logger.exception(
            "PDF generation failed: %s",
            exc,
        )


        raise