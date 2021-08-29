p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

s = 'hello'
a, b, c, d, e = s


if __name__ == "__main__":
    print(x)
    print(y)
    print(_, shares, price, _)
    print('*' * 10 + 'unpacking' + '*' * 10)
    print(a, b, c, d, e)
