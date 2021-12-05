# Handling Multiple Exceptions
import errno
import logging

logger = logging.getLogger(__name__)

try:
    f = open('filename.txt')
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %s %d', e, e.errno)

if __name__ == '__main__':
    print(FileExistsError.__mro__)
