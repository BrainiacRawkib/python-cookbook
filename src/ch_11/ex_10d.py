from xmlrpc.client import ServerProxy

s = ServerProxy('https://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(s.keys())

if __name__ == '__main__':
    pass
