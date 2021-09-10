# Best practice
# when reading or writing text to a binary-mode file,
# always encode or decode strings before processing it

with open('somefile2.bin', 'wb') as f:
    text2 = 'Hello World from ex_04b'  # normal strings
    f.write(text2.encode('utf-8'))  # encoding normal strings

with open('somefile2.bin', 'rb') as f:
    data = f.read(16)  # reading from binary-mode file
    text = data.decode('utf-8')  # decoding the file

if __name__ == '__main__':
    pass
