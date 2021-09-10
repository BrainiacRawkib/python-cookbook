# bypassing filename encoding
import os

# write a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# directory listing (decoded)
print(os.listdir('.'))

# directory listing (raw)
print(os.listdir(b'.'))

# open file with decoded filename
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())

# open file with raw filename
with open('jalapeño.txt') as f:
    print(f.read())

if __name__ == '__main__':
    pass
