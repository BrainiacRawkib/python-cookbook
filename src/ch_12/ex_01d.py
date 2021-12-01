import time
import multiprocessing
from threading import Thread


class CountdownThread(Thread):
    def __init__(self, n):
        super(CountdownThread, self).__init__()
        self.n = 0

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


if __name__ == '__main__':
    c = CountdownThread(5)
    p = multiprocessing.Process(target=c.run)
    p.start()
