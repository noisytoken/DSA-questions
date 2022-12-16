def partition(a, p, q):
    """ Function to partition array
    """
    x  = a[p]
    i = p
    j = p + 1
    # print(a)
    while j <= q:
        if x >= a[j]:
            i += 1
            a[i], a[j] = a[j], a[i]
        j += 1

    a[p], a[i] = a[i], a[p]
    return i


def quick_sort(a, p, q):
    if p < q:
        m = partition(a, p, q)
        quick_sort(a, p, m - 1)
        quick_sort(a, m + 1, q)

    return a
        

arr = [50, 120, 150, 70, 45, 90, 15, 23, 88, 16]

# print(partition(arr, 0, len(arr)- 1 ))
print(quick_sort(arr, 0, len(arr) - 1))