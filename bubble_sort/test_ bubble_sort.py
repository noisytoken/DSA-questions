from bubble_sort import bubble_sort

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


def test_bubble_sort():

    arr1 = []
    assert is_array_equal(bubble_sort([]), [])
    
    arr1 = [6,5,4,3,2,1]
    assert is_array_equal(bubble_sort(arr1), [1, 2, 3, 4, 5, 6])

    arr3 = [200, -100, 66, 10, -600]
    assert is_array_equal(bubble_sort(arr3), [-600, -100, 10, 66, 200 ])

    