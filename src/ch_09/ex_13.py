# using metaclass to control instance creation
class Spam:
    def __init__(self, name):
        self.name = name


a = Spam('Guido')
b = Spam('Diana')
