# defining context managers the easy way
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# Example use
if __name__ == '__main__':
    with timethis('counting'):
        n = 10000000
        while n > 0:
            n -= 1
