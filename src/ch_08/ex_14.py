# Implementing custom containers
import collections


class A(collections.Iterable):

    def __iter__(self):
        pass


class B(collections.Sequence):
    def __getitem__(self, item):
        pass

    def __len__(self):
        pass


class C(collections.Mapping):

    def __getitem__(self, item):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass


x = ''
print(isinstance(x, collections.Sequence))
print(isinstance(x, collections.Iterable))

if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
