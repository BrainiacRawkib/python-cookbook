# Creating Custom Exceptions
class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


if __name__ == '__main__':
    try:
        pass
    except TimeoutError as e:
        pass
    except ProtocolError as e:
        pass
