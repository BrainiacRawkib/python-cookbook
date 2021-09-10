# testing for the existence of a file
import os
import time

dir_path = 'ch_05'
file_path = 'ex_12.py'
link_path = 'c:/Python/Python36/python.exe'

# does the file exists
print(os.path.exists(file_path))

# is a regular file
print(os.path.isfile(file_path))

# is a directory
print(os.path.isdir(dir_path))

# is a symbolic link
print(os.path.islink(link_path))

# get the file linked to
print(os.path.realpath(link_path))

# get the file size
print(os.path.getsize(file_path))

# get the modification date
print(os.path.getmtime(file_path))

# decode the modification date with the time module
print(time.ctime(os.path.getmtime(file_path)))  # value changes when the file is modified

# decode the creation date with the time module
print(time.ctime(os.path.getctime(file_path)))  # returns the value of the file when it was created

if __name__ == '__main__':
    pass
