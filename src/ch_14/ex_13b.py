# To time a block of statements, you can define a context manager
import time
from contextlib import contextmanager


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


if __name__ == '__main__':
    with timeblock('counting'):
        n = 1000000
        while n > 0:
            n -= 1
