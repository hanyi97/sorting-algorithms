"""Get the minimum value of unsorted array and swap value to the front

Advantages:
- Performs well on small lists

Disadvantages:
- Poor efficiency when dealing with huge list of items

Time Complexity:
- Worst Case: O(n^2)
- Best Case: O(n^2)
- Average Case: O(n^2)

Example [5, 3, 8, 6, 7, 2]:
When i = 0, min_index = 0 (5):
j = 0: "
j = 1: min_index = 1 (3)
j = 2: "
j = 3: "
j = 4: "
j = 5: min_index = 5 (2)
Swap number 5 and 2: [2, 3, 8, 6, 7, 5]

When i = 1, min_index = 1 (3):
j = 1: "
j = 2: "
j = 3: "
j = 4: "
j = 5: "
No change: [2, 3, 8, 6, 7, 5]

When i = 2, min_index = 2 (8)
j = 2: "
j = 3: min_index = 3 (6)
j = 4: "
j = 5: min_index = 5 (5)
Swap number 8 and 5: [2, 3, 5, 6, 7, 8]

When i = 3, min_index = 3 (6)
j = 3: "
j = 4: "
j = 5: "
No change: [2, 3, 5, 6, 7, 8]

When i = 4, min_index = 4 (7)
j = 4: "
j = 5: "
No change: [2, 3, 5, 6, 7, 8]
"""


def sort(arr):
    n = len(arr)
    # Loop until second last item
    for i in range(n-1):
        min_index = i
        # Get min index starting from i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap i position with min_index
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

