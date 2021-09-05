import struct

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

hi, lo = struct.unpack('>QQ', data)

print(hi)
print(lo)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

x = 523 ** 23
print(x)
# print(x.to_bytes(16, 'little'))  # OverflowError: int too big to convert
print(x.bit_length())

nbytes, rem = divmod(x.bit_length(), 8)
print(nbytes)

if rem:
    nbytes += 1

print(format('nbytes', '*^20s'))
print(nbytes)
print(nbytes.to_bytes(nbytes, 'little'))

if __name__ == '__main__':
    pass
