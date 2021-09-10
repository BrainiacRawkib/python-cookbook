# writing to a file that doesn't already exist

with open('textfile.txt', 'wt') as f:
    f.write('Hello world\n')

# 'xt' mode checks if the file already exists on the filesystem
# if the file doesn't exist, it creates a new file but if it does
# exists it raises FileExistsError: [Errno 17] File exists:

with open('textfile.txt', 'xt') as f:
    f.write('Hello world\n')

if __name__ == '__main__':
    pass
