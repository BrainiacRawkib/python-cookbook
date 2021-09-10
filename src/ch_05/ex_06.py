# performing I/O operations on a string
from io import StringIO, BytesIO

s = StringIO()
string_text = 'this is a string text!'
s.write(string_text)
string_file = open('stringio.txt', 'wt')
print(s.getvalue(), file=string_file)  # redirect the data written so far to string_file
print(s.getvalue())  # get all of the data written so far


b = BytesIO()
bytes_text = b'this is a bytes text!'
b.write(bytes_text)
print(b.getvalue())

if __name__ == '__main__':
    pass
