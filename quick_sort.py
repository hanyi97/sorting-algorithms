"""Uses a partition and pivot points
Divide and conquer with recursive function

1. Take last/first item as pivot point
2. Partition list by placing items smaller than pivot to the left and larger items to the right

Advantages:
- Regarded as best sorting algorithm
- Significant efficiency advantage on large lists
- No additional storage required

Disadvantages:
- Worst case similar to average performances of the bubble, insertion or selections sorts.

Time Complexity:
Worst Case: O(n^2)
Best Case: O(nlog(n))
Average Case: O(nlog(n))

Solve worst case by choosing:
1. A random index for pivot
2. Middle index of partition for the pivot
3. Median of first, middle and last partition for the pivot

Example [5, 3, 8, 6, 7, 2]
Pivot = 2:
[2, 3, 8, 6, 7, 5]

Pivot = 5:
[2, 3, 5, 6, 7, 8]

Pivot = 8
[2, 3, 5, 6, 7, 8]
"""


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            # Swap places
            arr[i], arr[j] = arr[j], arr[i]
    # Swap pivot
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    # Left pointer and right pointer is the same
    if left >= right:
        return
    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)


def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
