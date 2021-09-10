# for file name matching use glob module or fnmatch module
import os
import time
import glob
from fnmatch import fnmatch

pyfiles = glob.glob('*.py')

print(pyfiles)

pyfiles = [name for name in os.listdir('../ch_05') if fnmatch(name, '*.py')]
print(pyfiles)

# get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print('file name: ', name, 'file size: ', meta.st_size, 'modified date: ',
          time.ctime(meta.st_mtime), 'creation date: ', time.ctime(meta.st_ctime), sep='-->')

if __name__ == '__main__':
    pass
