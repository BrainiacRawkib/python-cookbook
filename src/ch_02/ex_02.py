# matching text at the start or end of a string
import os

filename = 'spam.txt'
url = 'https://www.python.org'

foldernames = os.listdir('..')
filenames = os.listdir('.')

check_file_ext = [name for name in filenames if name.endswith(('.c', '.h'))]

any_py_ext = any(name.endswith('.py') for name in filenames)

if __name__ == '__main__':
    print(filename.endswith('.txt'))
    print(filename.startswith('file'))
    print(url.startswith('http'))
    print(foldernames)
    print(filenames)
    print('checking file exts -->', check_file_ext)
    print(any_py_ext)
