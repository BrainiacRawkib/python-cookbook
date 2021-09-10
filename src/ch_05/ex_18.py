# wrapping an existing file descriptor as a file object
import os

# open a low-level file descriptor

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

# create a file object, but don't close the underlying fd when done
f = open(fd, 'wt', closefd=False)

if __name__ == '__main__':
    pass
