# decoding and encoding hexadecimal digits
import binascii
import base64

# initial byte string
s = b'hello'

# encode as hex
h = binascii.b2a_hex(s)
print(h)

# decode back to bytes
print(binascii.a2b_hex(h))

# using base64 module
print(format('Using base64 module', '*^30'))
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))

if __name__ == '__main__':
    pass
