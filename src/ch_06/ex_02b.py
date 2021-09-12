import json
from collections import OrderedDict
from pprint import pprint
from urllib.request import urlopen

# u = urlopen('https://search.twitter.com/search.json?q=python&rpp=5')
# resp = json.loads(u.read().decode('utf-8'))


s = '{"name": "ACME", "shares": 100, "price": 542.23}'

data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# how to turn JSON dictionary into a Python object


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(json.dumps(s, indent=4, sort_keys=True))

if __name__ == '__main__':
    # pprint(resp)
    pass
