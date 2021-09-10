# reading and writing binary data

# write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World from ex_04')

# read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()
    print(data)

if __name__ == '__main__':
    pass
