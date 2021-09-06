# iterating in reverse
a = [1, 2, 3, 4, 5]

for x in reversed(a):  # reversed iteration only works if the object in question has a size that
    print(x)  # can be determined or if the object implements a __reversed_() special method.


# implementing __reversed__() method on a user-defined class
class CountDown:
    def __init__(self, start):
        self.start = start

    # forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


print(format('Custom Countdown', '*^20s'))

nums = CountDown(10)
for x in nums:
    print(x)

if __name__ == '__main__':
    pass
