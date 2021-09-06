# creating new iteration patterns with generators

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))

# countdown generator


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


# create the generator, notice no output appears
c = countdown(3)
print(c)

# run to first yield and emit a value
print(next(c))
print(next(c))
print(next(c))
print(next(c))


if __name__ == '__main__':
    pass
