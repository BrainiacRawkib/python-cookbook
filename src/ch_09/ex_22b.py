# advanced context manager
from contextlib import contextmanager


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


items = [1, 2, 3, 4]

with list_transaction(items) as working:
    working.append(5)
    working.append(6)
    working.append(7)

print(items)

if __name__ == '__main__':
    pass
