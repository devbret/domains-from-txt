import re

import tldextract

from .cleaning import clean_token

DOMAIN_PATTERN = re.compile(
    r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b',
    re.IGNORECASE
)


def extract_domains_from_text(text):
    matches = DOMAIN_PATTERN.findall(text)
    domains = set()

    for match in matches:
        token = clean_token(match)

        extracted = tldextract.extract(token)

        if extracted.domain and extracted.suffix:
            domains.add(f"{extracted.domain}.{extracted.suffix}".lower())

    return sorted(domains)
