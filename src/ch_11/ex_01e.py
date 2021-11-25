# using requests to pass HTTP cookies from one request to the next
import requests


# first request
url = 'http://httpbin.org/post'
resp1 = requests.get(url=url)

# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)

# using requests to upload content
files = {'files': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)

if __name__ == '__main__':
    pass
