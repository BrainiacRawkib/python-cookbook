# disassembling python byte code
import dis


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')


if __name__ == '__main__':
    dis.dis(countdown)
    print(countdown.__code__.co_code)
