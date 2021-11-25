# RPC client.py
from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(s.keys())
print(s.get('foo'))
print(s.get('spam'))
s.delete('spam')
print(s.exists('spam'))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
s.set('foo', p)
print(s.get('foo'))

# Handling of Binary data is different
s.set('foo', b'Hello World')
print(s.get('foo'))


if __name__ == '__main__':
    pass
