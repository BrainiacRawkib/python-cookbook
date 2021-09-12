# decoding and encoding base64
import base64

# some byte data
s = b'hello'

# encode as base64
a = base64.b64encode(s)

print(a)

# decode from base64
print(base64.b64decode(a))

if __name__ == '__main__':
    pass
