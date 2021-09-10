# manipulating pathnames
import os

path = 'src/ch_05/ex_11.py'

# get the last component of the path
print(os.path.basename(path))

# get the directory name
print(os.path.dirname(path))

# join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

# expand the user's home directory
path = '~/ch_05/ex_11.py'
print(os.path.expanduser(path))

# split the file extension
print(os.path.splitext(path))

if __name__ == '__main__':
    pass
