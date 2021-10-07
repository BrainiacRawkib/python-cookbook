# singleton pattern
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example Use
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


if __name__ == '__main__':
    a = Spam()
    a
    b = Spam()
    b
    c = Spam()
    c
    print(a == b)
    print(a is b)
