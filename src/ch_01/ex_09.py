a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

c = a.keys() & b.keys()
d = a.keys() - b.keys()
e = a.items() & b.items()
filtered_dict = {key: a[key] for key in a.keys() - ['z', 'w']}

if __name__ == '__main__':
    print(c)
    print(d)
    print(e)
    print(filtered_dict)
