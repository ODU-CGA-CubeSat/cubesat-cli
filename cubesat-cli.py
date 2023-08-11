#!/usr/bin/env python3

import argparse
import json
import sys
import requests
import toml
import traceback
from os import path
from subprocess import run


class CubeSatDB:
    """class used for validation and CRUD operations using the dof-cubesat schema"""

    def __init__(self):
        fullpath = path.dirname(path.abspath(__file__))
        self.dof_cubesat_path = path.join(fullpath, "../dof-cubesat")
        self.dof_cubesat_schema_path = path.join(self.dof_cubesat_path, "dist/dof.yaml")


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
    parser_component.add_argument("validate", type=str, help="Validate that a Component directory contains a valid package.json")

    parser_componentlist = subparsers.add_parser(
        "componentlist",
        help="Subcommand for ComponentList data (i.e., parts.yaml or tools.yaml)",
    )
    parser_componentlist.add_argument("validate", type=str, help="Validate that a ComponentList (i.e., parts.yaml or tools.yaml) contains a valid list of ComponentListItem items")

    parser_activitysteps = subparsers.add_parser(
        "activitysteps",
        help="Subcommand for ActivitySteps (i.e., assemblySteps or operatingSteps) data",
    )
    parser_activitysteps.add_argument("validate", type=str, help="Validate that an ActivitySteps (i.e., assemblySteps.yaml) contains a valid list of assemblyStep items")

    # Parse arguments
    args = parser.parse_args()

    # Setup sealion-cli instance
    cubesat_cli = CubeSatDB()

    # Print help text if no arguments passed
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # componentlist
    if args.command == "componentlist":
        if len(sys.argv) == 2:
            parser_componentlist.print_help(sys.stderr)
            sys.exit(1)
