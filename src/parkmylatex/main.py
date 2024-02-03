import sys
from parkmylatex.converter import rephrase
modification_degree = 'correct-only'


def main():
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    except:
        print("An input or output file is missing.\npdflatex path/to/input_file path/to/output_file")
        return

    with open(input_file, 'r') as f:
        text = f.read()
        output = rephrase(text, modification_degree)

    with open(output_file, 'w') as f:
        f.write(output)
