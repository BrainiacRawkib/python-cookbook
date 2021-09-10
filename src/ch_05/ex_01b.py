# Newline translation enabled by default
f = open('hello.txt', 'rt')
print(f.read())

# Newline translation disabled
g = open('hello.txt', 'rt', newline='')
print(g.read())

# Always open file in proper encoding format like utf-8, utf-16, ascii
f = open('sample.txt', 'rt', encoding='ascii')
print(f.read())

if __name__ == '__main__':
    pass
