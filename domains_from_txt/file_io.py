def read_text(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()


def write_domains(path, domains):
    with open(path, 'w', encoding='utf-8') as f:
        for domain in domains:
            f.write(domain + '\n')
