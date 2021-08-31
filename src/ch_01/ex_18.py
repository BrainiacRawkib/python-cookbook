# mapping names to sequence elements
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('brainy@admin.com', '2021-10-19')

# unpacking
addr, joined = sub


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def compute_cost2(records):
    total = 0.0
    for rec in records:
        print(rec)
        s = Stock(*rec)
        total += s.shares * s.price
    return total


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}

if __name__ == '__main__':
    print(sub)
    print(sub.addr)
    print(addr, joined)
    print(stock_prototype)
    # stock_prototype.shares = 129  # AttributeError: can't set attribute
    # stock_prototype._replace(shares=123)  # the way to set attribute of a namedtuple
    print(dict_to_stock(a))
    print(dict_to_stock(b))
