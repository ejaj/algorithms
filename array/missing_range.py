"""
arr = [3, 5]
lo=1
hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""


def missing_range(arr, low, high):
    result = []
    for num in arr:
        if num == low:
            low += 1
        elif num > low:
            result.append((low, num - 1))
            low = num + 1
            print(low)
    # append remainder to list
    if low <= high:
        result.append((low, high))
    return result


arr = [3, 5]
low = 1
high = 10
print(missing_range(arr, low, high))
