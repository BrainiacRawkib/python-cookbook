# countdown.py
import time
import pickle
import threading


class CountDown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus ', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, state):
        self.__init__(state)


if __name__ == '__main__':
    c = CountDown(30)

    # after a few moments
    # f = open('cstate.p', 'wb')
    # pickle.dump(c, f)
    # f.close()

    # open the file
    f = open('cstate.p', 'rb')
    print(pickle.load(f))
