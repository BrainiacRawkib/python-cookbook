import json
from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 4
d['grok'] = 3


if __name__ == '__main__':
    for k in d:
        print(k, d[k])
    print(json.dumps(d))
