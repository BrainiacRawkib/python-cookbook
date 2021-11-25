# Using requests to make a HEAD request
import requests


resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']

# Here is a requests example that executes a login into the
# Python Package Index
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user', 'password'))

if __name__ == '__main__':
    pass
