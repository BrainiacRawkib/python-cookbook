import numpy as np
from collections import namedtuple
from ch_06.ex_11 import read_records

Record = namedtuple('Record', ['kind', 'x', 'y'])

with open('data.bin', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

    for r in records:
        print(r.kind, r.x, r.y)

print('File closed: ', f.closed)

# using numpy
f = open('data.bin', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)
print(records[0])
print(records[1])
print(records[2])

if __name__ == '__main__':
    pass
