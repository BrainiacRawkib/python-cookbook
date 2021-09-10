# reading binary data into a mutable buffer
import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


# write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)
print(buf[0:5])

with open('newsample.bin', 'wb') as f:
    print(f.write(buf))

record_size = 32

buf = bytearray(record_size)

# with open('bytearr.bin', 'rb') as f:
#     while True:
#         n = f.readinto(buf)
#         if n < record_size:
#             break
        # use content of buf

print(buf)

m1 = memoryview(buf)
print(m1)

if __name__ == '__main__':
    pass
