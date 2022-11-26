import math

def power_of_element_iterative(base, exp):
    """
    An iterative function to calcualte of power an element
    """

    result = base
    counter = 1
    while counter <= math.log(exp, 2):
        result = result * result
        counter += 1

    return result

print(power_of_element_iterative(2, 16))