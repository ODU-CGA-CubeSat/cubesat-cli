#!/usr/bin/env python3

import argparse
import json
import sys
import requests
import toml
import traceback
import yaml
from os import path
from os import readlink
from subprocess import run


class CubeSatDB:
    """class used for validation and CRUD operations using the dof-cubesat schema"""

    def __init__(self):
        self.filepath = path.abspath(__file__)
        if path.islink(self.filepath):
            self.filepath = readlink(self.filepath)
        self.fullpath = path.dirname(self.filepath)
        self.dof_cubesat_path = path.join(self.fullpath, "dof-cubesat")
        self.dof_cubesat_schema_path = path.join(self.dof_cubesat_path, "dist/dof.yaml")

        with open(self.dof_cubesat_schema_path, "r") as file:
            self.dof_cubesat_schema_as_str = file.read()
            self.dof_cubesat_schema_as_dict = yaml.safe_load(
                self.dof_cubesat_schema_as_str
            )

    def setup_cli(self):
        # Setup parser
        self.parser = argparse.ArgumentParser(
            description="CLI tool for performing CRUD operations on bill of materials (BOM) data & assembly instructions data, using the dof-cubesat schema."
        )

        # Setup subparser for subcommands
        self.subparser = self.parser.add_subparsers(dest="command")
        self.parsers = {}

        # Iterate through classes specified in schema and create parsers for each class that is a root class
        for class_name in self.dof_cubesat_schema_as_dict["classes"]:
            if (
                "tree_root"
                in self.dof_cubesat_schema_as_dict["classes"][class_name].keys()
            ):
                self.parsers[class_name] = self.subparser.add_parser(
                    class_name.lower(),
                    description=self.dof_cubesat_schema_as_dict["classes"][class_name][
                        "description"
                    ],
                    help="Subcommand for {0} data".format(class_name),
                )
                self.parsers[class_name].add_argument(
                    "validate",
                    help="Validate a {0}".format(class_name),
                )


if __name__ == "__main__":

    # Setup cubesat database instance
    cubesat_db = CubeSatDB()
    cubesat_db.setup_cli()

    # Parse arguments
    args = cubesat_db.parser.parse_args()

    # Print help text if no arguments passed
    if len(sys.argv) == 1:
        cubesat_db.parser.print_help(sys.stderr)
        sys.exit(1)
