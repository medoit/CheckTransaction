with open("SNLS.txt") as f:
    for line in f:
        print(line)
        skip = False
        result = list()
        for i in range(0, len(line)):
            if skip:
                skip = False
                continue
            if i + 1 < len(line):
                if line[i + 1] == '\0':
                    result.append('0')
                    result.append(line[i])
                    skip = True
                    continue
            result.append(line[i])
        print(''.join(result))