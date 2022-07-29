from hashlib import md5, sha1, sha256

block = 65536  # bytes

def calculate(input_file, algorithm):
    with input_file as f:
        if algorithm == 'sha256': h = sha256()
        elif algorithm == 'sha1': h = sha1()
        elif algorithm == 'md5':  h = md5()
        else:
            raise ValueError(f'Algorithm not supported: {algorithm}')
        
        while chunk := f.read(block):
            h.update(chunk)
        print(f'\n{h.hexdigest()}\n')
