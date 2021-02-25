"""Break list into halves and merge the smaller halves, and merge them back together
Efficient for large data sets
Recursive function

Example: [5, 3, 8, 6, 7, 2]
Split: [5, 3, 8] [6, 7, 2]
Split: [5] [3, 8] [6] [7, 2]
Split: [5] [3] [8] [6] [7] [2]

Merge & Sort: [3, 5] [6, 8] [2, 7]
Merge & Sort: [3, 5, 6, 8] [2, 7]
Merge & Sort: [2, 3, 5, 6, 7, 8]
"""


def merge_sort(arr, a, b):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    # Sort array
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # Sort if got remaining items left
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


def sort(arr):
    if len(arr) <= 1:
        return arr

    # Find mid point
    mid = len(arr) // 2
    # Split into two
    left = arr[:mid]
    right = arr[mid:]
    # Split into two again
    sort(left)
    sort(right)

    merge_sort(arr, left, right)
