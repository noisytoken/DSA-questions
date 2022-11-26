"""
A function to calcualte of an element using divide and conquer
"""

import math

def power_of_element_dac(base, exp):
    """
    A function to calcualte of an element using divide and conquer
    """


    if exp == 1:
        return base

    mid = math.floor( exp / 2)
    conquer = power_of_element_dac(base, mid)
    combine = conquer * conquer

    if exp % 2 == 0:
        return combine
    else:
        return combine * base

print(power_of_element_dac(2, 1))
print(power_of_element_dac(2, 5))
print(power_of_element_dac(2, 6))
print(power_of_element_dac(2, 7))

# print(power_of_element_dac(2, 64))
# print(power_of_element_dac(2, 2))
# print(power_of_element_dac(2, 4))
# print(power_of_element_dac(2, 1024))
