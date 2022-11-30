import math

def power_of_element_iterative(base: int , exp):
    """
    An iterative function to calcualte of power an element
    """

    result = base
    counter = 1
    while counter <= math.log(exp, 2):
        result = result * result
        counter += 1

    # (base ** (exp - base ** (counter - 1)))
    return result * (base ** (exp - 2 ** (counter - 1)))

print(power_of_element_iterative(11, 3))

