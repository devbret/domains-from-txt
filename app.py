import re
import sys

import tldextract

def clean_token(token):
    return token.strip().strip('.,);:=]>"\'""''<>[]{}')

def extract_domains_from_text(text):
    pattern = re.compile(
        r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b',
        re.IGNORECASE
    )

    matches = pattern.findall(text)
    domains = set()

    for match in matches:
        token = clean_token(match)

        extracted = tldextract.extract(token)

        if extracted.domain and extracted.suffix:
            domains.add(f"{extracted.domain}.{extracted.suffix}".lower())

    return sorted(domains)

def extract_unique_domains(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
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
        with open(output_file, 'w', encoding='utf-8') as f:
            for domain in domains:
                f.write(domain + '\n')
    except OSError as e:
        print(f"Error: could not write '{output_file}': {e.strerror}", file=sys.stderr)
        return 1

    print(f"Extracted {len(domains)} unique domains to {output_file}")
    return 0

if __name__ == "__main__":
    sys.exit(extract_unique_domains("input.txt", "domains_output.txt"))