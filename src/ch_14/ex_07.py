# Catching All Exceptions
import logging

logger = logging.getLogger(__name__)

try:
    f = open('filename.txt')
except Exception as e:
    logger.error(e)  # Important

if __name__ == '__main__':
    print(FileExistsError.__mro__)
