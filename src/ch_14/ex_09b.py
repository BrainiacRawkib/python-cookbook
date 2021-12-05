from ch_14.ex_09 import example

try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)

if __name__ == '__main__':
    pass
