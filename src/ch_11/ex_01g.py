import requests


r = requests.get('http://httpbin.org/get?name=Brainy&n=37',
                 headers={'User-agent': 'goaway/1.0'})
resp = r.json()
print(resp['headers'])
print(resp['args'])

if __name__ == '__main__':
    pass
