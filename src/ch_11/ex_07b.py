# client.py
from multiprocessing.connection import Client

c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
print(c.recv())
c.send(42)
print(c.recv())
c.send([1, 2, 3, 4, 5])
print(c.recv())

if __name__ == '__main__':
    pass
