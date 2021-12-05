import math
from math import sqrt


# runs slower
def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result


# runs faster
def compute_roots2(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


# fastest
def compute_roots3(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


if __name__ == '__main__':
    nums = range(1000000)
    for n in range(100):
        r = compute_roots(nums)
