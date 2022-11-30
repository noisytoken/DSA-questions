"""
power_of_element_dac() testing module
"""

import pytest
from power_of_element_dac import power_of_element_dac

def test__power_of_element_dac():
    """
    Function to test power_of_element_dac()
    """
    assert power_of_element_dac(2, 0) == 1
    assert power_of_element_dac(2, 1) == 2
    assert power_of_element_dac(2, 2) == 4
    assert power_of_element_dac(2, 3) == 8
    assert power_of_element_dac(2, 4) == 16
    assert power_of_element_dac(2, 5) == 32
    assert power_of_element_dac(2, 10) == 1024

def test_wrong_arguments_passed():
    with pytest.raises(TypeError):
        power_of_element_dac("2", "0")
