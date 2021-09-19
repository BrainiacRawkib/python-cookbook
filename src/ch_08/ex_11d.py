# automatically initializing instance variable
def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items:
        if k != 'self':
            setattr(self, k, v)


class Stock:
    def __init__(self, name, shares, price):
        init_fromlocals(self)
