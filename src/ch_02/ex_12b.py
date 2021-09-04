import unicodedata
import sys

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}

print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'
x.translate(digitmap)
print(x)
print(x.translate(digitmap))

# I/O encoding and decoding
a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore'))
print(b.encode('ascii', 'ignore').decode('ascii'))

if __name__ == '__main__':
    pass
