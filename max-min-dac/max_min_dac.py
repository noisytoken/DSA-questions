"""
A function to calcualte max min using divide and conquer
"""

import math

a = [25, 10, 15, 500, 5, 3, -10]

def max_min_dac(arr, i, j):
    """
    max min using dac
    """

    if len(arr) == 0:
        return ()

    if i == j:
        return (arr[i], arr[i])

    if i == j - 1:
        if arr[i] > arr[j]:
            return (arr[i], arr[j])
        return (arr[j], arr[i])

    mid = math.floor((i + j) / 2)
    max1, min1 = max_min_dac(arr, i, mid)
    max2, min2 = max_min_dac(arr, mid + 1, j)

    _max = max1 if max1 > max2 else  max2
    _min = min1 if min1 < min2 else  min2

    return (_max, _min)

# print(max_min_dac([], 0, 0))
print(max_min_dac(a, 0, len(a) - 1))
