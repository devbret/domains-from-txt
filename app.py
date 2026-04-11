import re
import tldextract

def clean_token(token):
    return token.strip().strip('.,);:=]>"\'“”‘’<>[]{}')

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
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    domains = extract_domains_from_text(text)

    with open(output_file, 'w', encoding='utf-8') as f:
        for domain in domains:
            f.write(domain + '\n')

    print(f"Extracted {len(domains)} unique domains to {output_file}")

if __name__ == "__main__":
    extract_unique_domains("input.txt", "domains_output.txt")