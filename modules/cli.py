"""
Command Line Interface Module

Handles user arguments for CyberRecon AI.
"""

import argparse


def parse_arguments():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """

    parser = argparse.ArgumentParser(
        description="CyberRecon AI - Website Security Assessment Toolkit"
    )


    parser.add_argument(
        "--url",
        required=True,
        help="Target website URL"
    )


    return parser.parse_args()