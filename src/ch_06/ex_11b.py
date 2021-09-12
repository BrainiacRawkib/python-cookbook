import struct
from struct import Struct

record_struct = Struct('<idd')
print(record_struct.size)
a = (1, 2.0, 3.0)
print(record_struct.pack(*a))
print(struct.pack('<idd', 1, 2.0, 3.0))
# print(struct.unpack('<idd', _))
# print(record_struct.unpack(_))

if __name__ == '__main__':
    pass
