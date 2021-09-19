# a more elegant approach is to encode each operational state as a
# separate class and arrange for the Connection class to the delegate
# state class.
class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    # Delegate to the state class
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState:

    @staticmethod
    def read(conn):
        raise NotImplementedError

    @staticmethod
    def write(conn, data):
        raise NotImplementedError

    @staticmethod
    def open(conn):
        raise NotImplementedError

    @staticmethod
    def close(conn):
        raise NotImplementedError


# Implementation of different states
class ClosedConnectionState(ConnectionState):

    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState:

    @staticmethod
    def read(conn):
        print('reading...')

    @staticmethod
    def write(conn, data):
        print('writing...')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


if __name__ == '__main__':
    c = Connection()
    print(c._state)
    # print(c.read())
    c.open()
    print(c._state)
    c.read()
    c.write('hello')
    c.close()
    print(c._state)
