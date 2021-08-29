# 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100         .......513.25   ..........'

# cost = int(record[20:32]) * float(record[40:48])

SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4, 2)

s = 'HelloWorld'
b = slice(0, 50, 2)
c = [0, 1, 2, 3, 4, 5, 6]

if __name__ == '__main__':
    print(cost)
    print(items[a])
    print(a.step)
    print(items[2:4])
    print(b.indices(len(s)))
    print('unpacking--->', *b.indices(len(s)))
    for i in range(*b.indices(len(s))):
        print(s[i])
    print(*c)
