from selection_sort import selection_sort

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

def test_selection_sort():
    arr  = []
    assert is_array_equal( selection_sort(arr), [] )

    arr2  = [6, 5, 14, 3, 2, 1]
    assert is_array_equal( selection_sort(arr2), [1 , 2, 3, 5, 6, 14] )

    arr3  = [88, 1, 100, -200]
    assert is_array_equal( selection_sort(arr3), [-200, 1, 88, 100] )

