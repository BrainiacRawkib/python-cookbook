# implementing multiple dispatch with function annotations
class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, i: str, n: int = 0):
        print('Bar 2:', i, n)


if __name__ == '__main__':
    s = Spam()
    s.bar(2, 3)
    s.bar('hello')
