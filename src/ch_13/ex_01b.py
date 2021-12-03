import fileinput


with fileinput.input('text.txt') as f:
    for line in f:
        print(f.filename(), f.filelineno(), line, end='')

if __name__ == '__main__':
    pass
