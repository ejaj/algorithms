"""
arr = [0, 1, 2, 4, 5, 7]
output = [(0, 2), (4, 5), (7, 7)].
"""


def summarize_ranges(arr):
    result = []

    if len(arr) == 1:
        return [str(arr[0])]
    i = 0

    while i < len(arr):
        number = arr[i]
        while i + 1 < len(arr) and arr[i + 1] - arr[i] == 1:
            i += 1
        if arr[i] != number:
            result.append((number, arr[i]))
        else:
            result.append((number, number))
        i += 1
    print(result)


arr = [0, 1, 2, 4, 5, 7]
summarize_ranges(arr)
