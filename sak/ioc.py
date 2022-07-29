from re import compile, search, IGNORECASE

patterns = {
    'hash_md5': r'\b([a-f]|[0-9]){32}\b',
    'url': r'\b([a-z]{3,}://[\S]{3,})\b',
    'email': r'\b([a-z][_a-z0-9-.]+@[a-z0-9-]+\.[a-z]+)\b',
    'ipv4': r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b'
}

def extract(input_file):
    with input_file as f:
        for line in f:
            for pattern in patterns.values():
                p = compile(pattern, IGNORECASE)
                matches = search(p, line)
                if matches: print(matches)
