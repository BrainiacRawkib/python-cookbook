# making temporary files and directories
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory

# on unix systems, the file created ny TemporaryFile() is unnamed ans won't even have
# a directory entry. To relax this issue, use NamedTemporaryFile()
with TemporaryFile('w+t') as f:
    # read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # seek back to beginning and read the data
    f.seek(0)
    data = f.read()

# The files created by TemporaryFile() and NamedTemporaryFile() are deleted automatically when it's closed.
# If you don't want this supply a delete=False keyword argument.

with NamedTemporaryFile('w+t', delete=False) as f:
    # read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # seek back to beginning and read the data
    f.seek(0)
    named_data = f.read()

# Temporary file destroyed

# or
f = TemporaryFile('w+t')

# use temporary file

# file is destroyed
f.close()

# create a temporary directory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # use the directory

# Directory and all contents destroyed

if __name__ == '__main__':
    pass
