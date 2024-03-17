import sys
from pathlib import Path
import argparse
from parkmylatex.converter import get_rephrased_doc


def main():
    parser = argparse.ArgumentParser(
        description="A script for data processing")
    parser.add_argument("input", help="Input file path")
    parser.add_argument("output", help="Output file path")
    parser.add_argument(
        "-d", "--degree", help="Degree of correction", default="correct-only")

    args = parser.parse_args()

    input_file = Path(args.input)
    output_file = Path(args.output)
    modification_degree = args.degree

    with open(input_file, "r") as f:
        text = f.read()
        output = get_rephrased_doc(text, modification_degree)

    with open(output_file, "w") as f:
        f.write(output)
