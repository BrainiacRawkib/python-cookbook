# accessing variables defined inside a closure
def sample():
    n = 0

    # closure function
    def func():
        print('n = ', n)

    # accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


if __name__ == '__main__':
    f = sample()
    f()
    f.set_n(10)
    f()
    f.get_n()
