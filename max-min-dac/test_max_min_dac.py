"""
A module to test max-min-dac func
"""

from max_min_dac import max_min_dac

def test_max_min_dac():
    """
    Function to test max_min_dac()
    """

    arr1 = []
    assert max_min_dac(arr1, 0, len(arr1) - 1) == ()

    arr2 = [1]
    assert max_min_dac(arr2, 0, len(arr2) - 1) == (1, 1)

    arr3 = [1, 2]
    assert max_min_dac(arr3, 0, len(arr3) - 1) == (2, 1)

    arr4 = [11, 55, 43, 89, -98, 15]
    assert max_min_dac(arr4, 0, len(arr4) - 1) == (89, -98)
