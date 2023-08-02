#!/usr/bin/env python3

import argparse
import json
import sys
import requests
import toml
import traceback


class CubeSatDB:
    """class used for validation and CRUD operations using the dof-cubesat schema"""

    def __init__(self):
        pass


if __name__ == "__main__":
    # Setup parser
    parser = argparse.ArgumentParser(
        description="CLI tool for performing CRUD operations on bill of materials (BOM) data & assembly instructions data, using the dof-cubesat schema."
    )

    # Setup subparser for subcommands
    subparsers = parser.add_subparsers(dest="command")

    parser_component = subparsers.add_parser(
        "component", help="Subcommand for Component data"
    )

    parser_componentlist = subparsers.add_parser(
        "componentlist",
        help="Subcommand for ComponentList data (i.e., parts.yaml or tools.yaml)",
    )

    parser_activitysteps = subparsers.add_parser(
        "activitysteps",
        help="Subcommand for ActivitySteps (i.e., assemblySteps or operatingSteps) data",
    )

    # Print help text if no arguments passed
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse arguments
    args = parser.parse_args()

    # Setup sealion-cli instance
    cubesat_cli = CubeSatDB()
