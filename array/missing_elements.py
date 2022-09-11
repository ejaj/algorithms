from bisect import bisect_left


def print_missing_elements(arr, n, low, high):
    arr.sort()
    binary_search = bisect_left(arr, low)
    index = binary_search
    x = low
    while index < n and x <= high:
        if arr[index] != x:
            print(x, end=" ")
        else:
            index += 1
        x += 1
    while x < high:
        print(x, end=" ")
        x = x + 1


def print_missing_elements_set(arr, n, low, high):
    s = set(arr)
    for x in range(low, high + 1):
        if x not in s:
            print(x, end=' ')


def print_missing_elements_using_arr(arr, n, low, high):
    points_of_range = [False] * (high - low + 1)
    for i in range(n):
        if low <= arr[i] <= high:
            points_of_range[arr[i] - low] = True
    print(points_of_range)
    for x in range(high - low + 1):
        if not points_of_range[x]:
            print(low + x, end=" ")


arr = [1, 3, 5, 4]
n = len(arr)
low = 1
high = 10
print_missing_elements_using_arr(arr, n, low, high)
