# performing text operations on byte strings
import re

# bytes
data = b'Hello world'
print(data[0:5])
print('decode --> ', data[0:5].decode())
print(data.startswith(b'hello'))
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Yello'))

# bytearray
data = bytearray(b'Hello World')
print(data)
print('decoded ascii -->', data.decode('ascii'))
print(data.startswith(b'Hello'))
print(data.replace(b'Hello', b'Yello'))

# applying regex to byte strings
data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))  # pattern must be byte strings

# indexing of bytestring produce integers
print(data[0])
print(data[1])

# string formatting operations are not supported on byte strings
# b = b'{} {}'.format(b'ACME', 89)
# print(b)

text = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(text)

if __name__ == '__main__':
    pass
