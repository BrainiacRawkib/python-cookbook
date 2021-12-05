from timeit import timeit

if __name__ == '__main__':
    print(timeit('math.sqrt(2)', 'import math',
                 number=10))  # to add number of iterations
    print(timeit('sqrt(2)', 'from math import sqrt'))
