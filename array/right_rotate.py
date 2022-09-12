def right_rotate(arr, k):
    n = len(arr)
    k = k % n
    for i in range(n):
        if i < k:
            print(arr[n + i - k], end=" ")
        else:
            print(arr[i - k], end=" ")


def right_rotate_reverse(arr, k):
    n = len(arr)
    array = arr[:]

    def reverse(arr, a, b):
        while a < b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1

    k = k % n
    reverse(array, 0, n - k - 1)
    reverse(array, n - k, n - 1)
    reverse(array, 0, n - 1)
    return arr


def right_rotate_slice(arr, k):
    if arr is None:
        return None
    length = len(arr)
    k = k % length
    print(arr[length - k:])
    return arr[length - k:] + arr[:length - k]


arr = [1, 2, 3, 4, 5]
k = 2
right_rotate_reverse(arr, k)
