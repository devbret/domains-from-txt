import re
import tldextract

def extract_urls(text):
    url_pattern = re.compile(
        r'(https?://[^\s]+|www\.[^\s]+)',
        re.IGNORECASE
    )
    return url_pattern.findall(text)

def clean_url(url):
    return url.rstrip('.,);:=]>"\'')

def extract_domain(url):
    cleaned = clean_url(url)

    if not cleaned.startswith(('http://', 'https://')):
        cleaned = 'http://' + cleaned

    extracted = tldextract.extract(cleaned)

    if extracted.domain and extracted.suffix:
        return f"{extracted.domain}.{extracted.suffix}"

    return None

def extract_unique_domains(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    urls = extract_urls(text)

    domains = set()

    for url in urls:
        domain = extract_domain(url)
        if domain:
            domains.add(domain.lower())

    sorted_domains = sorted(domains)

    with open(output_file, 'w', encoding='utf-8') as f:
        for d in sorted_domains:
            f.write(f"{d}\n")

    print(f"Extracted {len(sorted_domains)} unique domains to {output_file}")

if __name__ == "__main__":
    extract_unique_domains("input.txt", "domains_output.txt")