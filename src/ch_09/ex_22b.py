# advanced context manager
from contextlib import contextmanager


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working
