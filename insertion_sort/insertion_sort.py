"""
the insertion sort
"""

def insertion_sort(arr):
    """
    the insertion sort
    """
    for i in range(len(arr)):
        temp = arr[i]
        red = i - 1
        while red >= 0 and arr[red] > temp:
            arr[red + 1] = arr[red]
            red -= 1
        arr[red + 1] = temp


    return arr


a  = [6, 5, 4, 3, 2, 1, -100]
print(insertion_sort(a))
