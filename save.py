def save_in_file(filepath, data):
    with open(filepath, 'w+') as f:
        for el in data:
            f.write(str(el) + '\n')