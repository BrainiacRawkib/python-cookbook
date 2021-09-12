# reading and writing binary arrays of structures
from struct import Struct
# Hint: for working with binary data using the struct module
# is actually common.


# write a list of tuples out to a binary file
def write_records(records, format, f):
    """
    Write a sequence of tuples to a binary file of structures.
    :param records:
    :param format:
    :param f:
    :return:
    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# reading file back into list of tuples
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# to read the entire file into a byte string with single read and convert it piece by piece
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in
            range(0, len(data), record_struct.size))


# example
if __name__ == '__main__':
    # writing
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open('data.bin', 'wb') as f:
        write_records(records, '<idd', f)

    # reading
    with open('data.bin', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)
            # process rec

    # read entire file into a byte string
    with open('data.bin', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        print(rec)
        # process rec
