import collections
import bisect


class SortedItems(collections.Sequence):

    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == '__main__':
    items = SortedItems([5, 2, 3])
    print(list(items))
    print(items[0])
    print(items[-1])
    items.add(90)
    items.add(34)
    items.add(-10)
    print(items[1:9])
    for item in items:
        print(item)
    # type checking
    print(isinstance(items, collections.Iterable))
    print(isinstance(items, collections.Sequence))
    print(isinstance(items, collections.Container))
    print(isinstance(items, collections.Sized))
    print(isinstance(items, collections.Reversible))
    print(isinstance(items, collections.Mapping))
    print(isinstance(items, collections.MutableMapping))
