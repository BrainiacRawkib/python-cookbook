# printing bad filenames
import os
import sys

f = open('b\udce4d.txt', 'w')


def bad_filename(filename):
    return repr(filename)[1:-1]


def bad_filename_escape(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


files = os.listdir()

# for name in files:  # UnicodeEncodeError: 'utf-8' codec can't encode character '\udce4'
#     print(name)  # in position 1: surrogates not allowed

# Fixed!
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename_escape(name))


if __name__ == '__main__':
    pass
