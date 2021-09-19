# calling a method on a parent class
class A:
    def spam(self):
        return 'A.spam!'


class B(A):
    def spam(self):
        print('B.spam!!')
        return super(B, self).spam()  # Call parent spam()


class C:
    def __init__(self):
        self.x = 0

    def __str__(self):
        return str(self.x)


class D(C):
    def __init__(self):
        super().__init__()
        self.y = 1

    def __str__(self):
        return str((self.x, self.y))


if __name__ == '__main__':
    b = B()
    print(b.spam())
    d = D()
    print(d)
