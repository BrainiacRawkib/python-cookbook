# adding or changing the encoding of an already open file
import io
import sys
import urllib.request

# if you want to add unicode encoding/decoding to an already existing file
# url = urllib.request.urlopen('https://www.python.org')
# f = io.TextIOWrapper(url, encoding='utf-8')
# text = f.read()

# if you want to change unicode encoding/decoding to an already existing file
print(sys.stdout.encoding)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
f = open('sample2.txt', 'w')
print(f)
print(f.buffer)
print(f.buffer.raw)
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
# print(f)
# f.write('Hello')
# print(f)
# b = f.detach()
# print(b)
# f = io.TextIOWrapper(b, encoding='latin-1')
# print(f)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('jalape\u00f1o')

if __name__ == '__main__':
    pass
