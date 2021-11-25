# If your interaction with a service is more complicated than this, you should probably
# look at the requests library
import requests

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# Extra headers
headers = {
    'User-agent': 'admin',
    'Spam': 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text

# Raw binary content returned
content = resp.content

# Json data returned
json = resp.json()

if __name__ == '__main__':
    pass
