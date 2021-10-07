# alternatively
class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super(LoggedGetattribute, self).__getattribute__(name)


# Example
class A(LoggedGetattribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass
