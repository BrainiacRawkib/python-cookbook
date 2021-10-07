from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass


if __name__ == '__main__':
    pass
