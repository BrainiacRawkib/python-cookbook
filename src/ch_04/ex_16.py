# replacing infinite while loops with an iterator
import sys

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def process_data(data):
    pass


# reader function can also be replaced by this function


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data=chunk)


# reader and reader2 function can also be replaced by this
f = open('passwd.txt')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

if __name__ == '__main__':
    pass
