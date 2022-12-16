"""
A module to test quick_sort func
"""

from quick_sort import quick_sort


def is_array_equal(arr1, arr2):
    """
    Function to determine whether the passed array are equal in terms of values
    """
    if len(arr1) != len(arr2):
        return False

    idx =  0
    while  idx < len(arr1):
        if arr1[idx] != arr2[idx]:
            return False
        idx += 1

    return True

def test_is_array_equal():
    """
    func to test is_array_equal() func
    """
    assert is_array_equal([], [])
    assert is_array_equal([1, 2], [1, 2])
    assert is_array_equal([1, 2, 3], [1, 2, 3])


def test_quick_sort():
    """
    Function to test quick_sort()
    """

    arr1 = []
    assert is_array_equal( quick_sort(arr1, 0, len(arr1) - 1), [] )

    arr2 = [1]
    assert is_array_equal( quick_sort(arr2, 0, len(arr2) - 1), [1] )

    arr3 = [1, 2]
    assert is_array_equal( quick_sort(arr3, 0, len(arr3) - 1), [1, 2] )

    arr4 = [11, 55, 43, 89, -98, 15]
    assert is_array_equal( quick_sort(arr4, 0, len(arr4) - 1), [-98, 11, 15,43, 55, 89 ] )
