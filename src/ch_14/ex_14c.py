# Slower
class SomeClass:
    s = ''

    def op(self, value):
        pass

    def method(self):
        for x in self.s:
            self.op(self.s)


# Faster
class SomeClass2:
    s = ''

    def op(self, value):
        pass

    def method(self):
        value = self.s
        for x in value:
            self.op(value)
