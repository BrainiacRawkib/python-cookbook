# printing to a file

# redirect the output of print() function to a file
with open('hello.txt', 'at') as f:
    print('Hello World i append mode!', file=f)

if __name__ == '__main__':
    pass
