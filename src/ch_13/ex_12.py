import logging


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


# Example function (for testing)
def func():
    log.critical('A Critical Error')
    log.debug('A Debug message')


if __name__ == '__main__':
    func()  # doesn't print logs
    logging.basicConfig()
    func()  # print logs
