class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    # Added special methods to support certain list operations like indexing,
    # len(), e.t.c
    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, key):
        del self._items[key]


if __name__ == '__main__':
    a = ListLike()
    a.append(23)
    print(a)
    a.insert(0, 3)
    print(len(a))  # if special methods were not add --> TypeError: object of type 'ListLike' has no len()
    print(a[1])  # if special methods were not add --> TypeError: 'ListLike' object does not support indexing
