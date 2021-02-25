"""Sort by swapping values
Consumes more CPU power

Example [5, 3, 8, 6, 7, 2]:
When i = 5:
j = 0: [3, 5, 8, 6, 7, 2]
j = 1: "
j = 2: [3, 5, 6, 8, 7, 2]
j = 3: [3, 5, 6, 7, 8, 2
j = 4: [3, 5, 6, 7, 2, 8]

When i = 4:
j = 0: "
j = 1: "
j = 2: "
j = 3: [3, 5, 6, 2, 7, 8]

When i = 3:
j = 0: "
j = 1: "
j = 2: [3, 5, 2, 6, 7, 8]

When i = 2:
j = 0: "
j = 1: [3, 2, 5, 6, 7, 8]

When i = 1:
j = 0: [2, 3, 5, 6, 7, 8]
"""


def sort(arr):
    # Loop from back
    for i in range(len(arr) - 1, 0, -1):
        # Loop until i-1
        for j in range(i):
            # Swap if num is bigger than next num
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
