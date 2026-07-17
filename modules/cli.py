from __future__ import annotations

import argparse
from urllib.parse import urlparse


def validate_target(target: str) -> str:
    target = target.strip()

    if not target:
        raise argparse.ArgumentTypeError("Target URL cannot be empty.")

    if not target.startswith(("http://", "https://")):
        target = f"https://{target}"

    parsed = urlparse(target)

    if not parsed.netloc:
        raise argparse.ArgumentTypeError("Invalid target supplied.")

    return target


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="CyberRecon AI",
        description="Professional Website Security Assessment Toolkit",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--url",
        required=True,
        type=validate_target,
        help="Target website URL or domain",
    )

    return parser


def get_target() -> str:
    parser = build_parser()
    args = parser.parse_args()
    return args.url