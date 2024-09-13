#!/usr/bin/env python3

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Run WireViz with configurable options"
    )
    parser.add_argument("-f", "--files", required=True, help="Input file(s) to process")
    parser.add_argument(
        "-m", "--format", help="Output formats (g: GV, h: HTML, p: PNG, s: SVG, t: TSV)"
    )
    parser.add_argument(
        "-p", "--prepend", help="YAML file to prepend to the input file"
    )
    parser.add_argument("-o", "--output-dir", help="Directory to use for output files")
    parser.add_argument(
        "-n",
        "--output-name",
        help="File name (without extension) to use for output files",
    )

    args = parser.parse_args()

    command = ["wireviz"]

    if args.format:
        command.extend(["-f", args.format])
    if args.prepend:
        command.extend(["-p", args.prepend])
    if args.output_dir:
        command.extend(["-o", args.output_dir])
    if args.output_name:
        command.extend(["-O", args.output_name])

    command.extend(args.files.split())

    print(f"Running command: {' '.join(command)}")

    try:
        os.execvp("wireviz", command)
    except OSError as e:
        print(f"Error executing WireViz: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
