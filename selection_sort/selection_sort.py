"""
the selection sort
"""

def selection_sort(arr):
    """
    selection sort
    """
    i = 0
    for i in range(0, len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if  arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

a  = [6, 5, 4, 3, 2, 1]

print(selection_sort(a))
