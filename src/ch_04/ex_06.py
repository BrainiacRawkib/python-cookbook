# defining generator functions with extra state
from collections import deque


class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    with open('somefile.txt') as f:
        lines = LineHistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}: {}'.format(lineno, line), end='')

    f = open('somefile.txt')
    lines = LineHistory(f)
    # next(lines)  # call iter() method first before next() method
    it = iter(lines)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

