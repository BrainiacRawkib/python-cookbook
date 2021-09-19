# an alternative technique using the direct manipulation of the __class__
# attribute instance
class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')

    def write(self):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed.')


class OpenConnection(Connection):
    def read(self):
        print('reading')

    def write(self):
        print('writing')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)


if __name__ == '__main__':
    c = Connection()
    print(c)
    c.open()
    print(c)
    c.read()
    c.close()
    print(c)
