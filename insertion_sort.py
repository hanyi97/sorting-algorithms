"""Divide into 2 sub lists. Sorted and unsorted
A little faster than bubble and selection sort

1. Sorted list will start with 1 item
2. Take first item of unsorted list and insert into sorted list
3. Compare inserted item to the immediate left item
4. Swap position if smaller than left item

Example [5, 3, 8, 6, 7, 2]:
When i = 1:
[5, 3 | 8, 6, 7, 2]
Swap: [3, 5 | 8, 6, 7, 2]

When i = 2:
[3, 5, 8 | 6, 7, 2]
No need swap

When i = 3:
[3, 5, 8, 6 | 7, 2]
Swap: [3, 5, 6, 8 | 7, 2]

When i = 4:
[3, 5, 6, 8, 7 | 2]
Swap: [3, 5, 6, 7, 8 | 2]

When i = 5:
[3, 5, 6, 7, 8, 2]
Swap: [3, 5, 6, 7, 2, 8]
Swap: [3, 5, 6, 2, 7, 8]
Swap: [3, 5, 2, 6, 7, 8]
Swap: [3, 2, 5, 6, 7, 8]
Swap: [2, 3, 5, 6, 7, 8]
"""


def sort(arr):
    # Start looping from second item
    for i in range(1, len(arr)):
        val_to_sort = arr[i]
        # Keep swapping item on the left until it is sorted
        while arr[i - 1] > val_to_sort and i > 0:
            temp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = temp
            i -= 1
