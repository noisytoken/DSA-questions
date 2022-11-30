"""
a module
"""

import pytest
from power_of_element_iterative import power_of_element_iterative

def test_power_of_element_iterative():
    """
    Function to test power_of_element_iterative() func
    """

    assert power_of_element_iterative(2, 4) == 16
    assert power_of_element_iterative(2, 6) == 64
    assert power_of_element_iterative(2, 8) == 256
    assert power_of_element_iterative(2, 9) == 512
    assert power_of_element_iterative(2, 8) == 256
    assert power_of_element_iterative(3, 5) == 243
    assert power_of_element_iterative(4, 3) == 64
    assert power_of_element_iterative(11, 3) == 1331
    assert power_of_element_iterative(25, 3) == 625*25
