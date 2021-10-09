# replacing raw byte code of any function
import types


def add(x, y):
    return x + y


c = add.__code__

if __name__ == '__main__':
    print(c)
    print(c.co_code)

    # Make a completely new code object with bogus byte code
    newbytecode = b'xxxxxxx'
    nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount,
                        c.co_nlocals, c.co_stacksize, c.co_flags, newbytecode,
                        c.co_consts, c.co_firstlineno, c.co_lnotab)
    print(nc)
    add.__code__ = nc
