class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok')


if __name__ == '__main__':
    Spam.grok(34)
    print(callable(Spam))
    s = Spam()
    s.grok(45)
