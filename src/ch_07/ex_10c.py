# using functools.partial method
class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))


if __name__ == '__main__':
    from functools import partial
    from ch_07.ex_10 import apply_async, add, print_result

    seq = SequenceNo()
    apply_async(add, (2, 3), callback=partial(handler, seq=seq))
    apply_async(add, ('hello', 'world!'), callback=partial(handler, seq=seq))

    # using lambda
    apply_async(add, ('hello', 'world!'), callback=lambda r: handler(r, seq))
