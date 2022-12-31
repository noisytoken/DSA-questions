"""
the  bubble sort
"""

def bubble_sort(arr):
    """
    the bubble sort
    """
    for i in range(0, len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr

a = [6,5,4,3,2,1]

print(bubble_sort(a))
