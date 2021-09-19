# defining an interface or abstract base class
import io
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


if __name__ == '__main__':
    # a = IStream()
    s = SocketStream()
    f = open('foo.txt', 'w')
    print(isinstance(f, IStream))
