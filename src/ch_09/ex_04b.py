import logging
from ch_09.ex_04 import logged


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!!!')


if __name__ == '__main__':
    pass
