from ch_07.ex_10 import apply_async, add, print_result


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


# using closure to capture state
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


# using coroutine
def coroutine_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


if __name__ == '__main__':
    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)
    apply_async(add, ('hello', 'world!'), callback=r.handler)

    # using closures
    print(format('using closures', '*^20'))
    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ('hello', 'world!'), callback=handler)

    # using coroutines
    print(format('using coroutines', '*^20'))
    handler = coroutine_handler()
    next(handler)
    apply_async(add, (2, 3), callback=handler.send)
    apply_async(add, ('hello', 'world!'), callback=handler.send)
