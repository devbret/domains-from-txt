import sys

from .extraction import extract_domains_from_text
from .file_io import read_text, write_domains

DEFAULT_INPUT_FILE = "input.txt"
DEFAULT_OUTPUT_FILE = "domains_output.txt"


def extract_unique_domains(input_file, output_file):
    try:
        text = read_text(input_file)
    except FileNotFoundError:
        print(
            f"Error: input file '{input_file}' not found. "
            f"Place your source text file in this directory and name it '{input_file}'.",
            file=sys.stderr,
        )
        return 1
    except OSError as e:
        print(f"Error: could not read '{input_file}': {e.strerror}", file=sys.stderr)
        return 1

    domains = extract_domains_from_text(text)

    try:
        write_domains(output_file, domains)
    except OSError as e:
        print(f"Error: could not write '{output_file}': {e.strerror}", file=sys.stderr)
        return 1

    print(f"Extracted {len(domains)} unique domains to {output_file}")
    return 0


def main():
    return extract_unique_domains(DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE)
