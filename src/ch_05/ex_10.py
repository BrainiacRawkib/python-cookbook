# memory mapping binary files
import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size = 1000000
with open('memory_map.bin', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('memory_map.bin')
print(len(m))
print(m[0:10])
print(m[0:11])
print(m[0], m[1])

# reassign a slice
m[0:11] = b'Hello World'
m.close()

# verify that changes were made
with open('memory_map.bin', 'rb') as f:
    print(f.read(11))

with memory_map('data.bin') as m:
    print(len(m))
    print(m[0:10])

m = memory_map('data.bin')

# memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x00\x00\x00'
print(v[0])

if __name__ == '__main__':
    pass
