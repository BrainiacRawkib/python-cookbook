# using os.path module for greatest portability on Unix and Windows
import os

filename = 'src/ch_13/text.txt'
print(os.path.basename(filename))
print(os.path.dirname(filename))
print(os.path.split(filename))
print(os.path.join('src/ch_13/new', filename))
print(os.path.expanduser('~/src/ch_13/expand_user/text.txt'))

if __name__ == '__main__':
    pass
