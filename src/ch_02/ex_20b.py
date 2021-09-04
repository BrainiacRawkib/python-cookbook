# byte string changes semantics of file operation
import os

with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# get a directory listing
path = os.listdir()
get_txt_txt = [n for n in path if n.endswith('.txt')]
print(get_txt_txt)

path = os.listdir(b'.')
print(path)

if __name__ == '__main__':
    pass
