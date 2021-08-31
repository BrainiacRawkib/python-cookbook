# combining multiple mappings into a single mapping
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

# del c['y']  # raises KeyError: "Key not found in the first mapping: 'y'"
c['z'] = 30  # it will affect the first mapping which is a
c['w'] = 34  # it will affect the first mapping which is a

values = ChainMap()
values['x'] = 1
# add a new mapping
values = values.new_child()
values['x'] = 2
# add a new mapping
values = values.new_child()
values['x'] = 3
print(values)  # prints ChainMap({'x': 3}, {'x': 2}, {'x': 1})

# discard last mapping
values = values.parents  # removes last map entry which is {'x': 3}
values = values.parents  # removes last map entry which is {'x': 2}

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)

merged2 = ChainMap(a, b)

if __name__ == '__main__':
    print(c)
    print(c['x'])  # Outputs 1 (from a)
    print(c['y'])  # Outputs 1 (from b)
    print(c['z'])  # Outputs 1 (from a)
    print(len(c))
    print(values)
    print(merged['x'])
    print(merged)
    print('merged2--->', merged2)
    print('merged2--->', merged2['x'])
    a['x'] = 56
    print('merged2--->', merged2['x'])
    print('merged2--->', merged2)
