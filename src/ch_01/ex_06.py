from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

s = defaultdict(set)
s['a'].add(1)
s['a'].add(2)
s['b'].add(4)

# not cool
d = {}
for key, value in d:
    if key not in d:
        d[key] = []
    d[key].append(value)

# cool
l = defaultdict(list)
for k, v in l:
    l[k].append(v)

if __name__ == '__main__':
    print(d)
    print(s)
