# interacting with HTTP services as a client

# For simple things, it’s usually easy enough to use the urllib.request module
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url+'?' + querystring)
resp = u.read()

if __name__ == '__main__':
    pass
