# iterating over fixed-sized records
from functools import partial

RECORD_SIZE = 32

with open('chunkfile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        pass
