import collections

from mypy.plugins.enums import _T


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index: int, value: _T) -> None:
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


if __name__ == '__main__':
    a = Items([1, 2, 3, 4])
    print(len(a))
    a.append(5)
    print(a)
    print(a.count(2))
    a.remove(3)
    print(a)
