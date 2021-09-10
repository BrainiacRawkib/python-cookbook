# getting a directory listing
import os

dirs = os.listdir('../ch_05')

print(dirs)

# get all dirs
dirnames = [name for name in dirs
            if os.path.isfile(os.path.join('../ch_05', name))]

print(dirnames)

# getting python files only
pyfiles = [name for name in dirs if name.endswith('.py')]
print(pyfiles)

if __name__ == '__main__':
    pass
