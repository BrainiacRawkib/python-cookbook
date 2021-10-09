# if you want to interpret the code in ex_25 manually,
# you'd need to use some of the constants defined in the opcode module
import opcode
from ch_09.ex_25 import countdown


c = countdown.__code__.co_code

if __name__ == '__main__':
    print(opcode.opname[c[0]])
    print(opcode.opname[c[2]])
