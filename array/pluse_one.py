def plus_one_using_convert_string(arr):
    nums_str = ''.join(map(str, arr))
    plus_one = int(nums_str) + 1
    ans = []
    for i in str(plus_one):
        ans.append(int(i))
    print(ans)


def plus_one_last_element(arr):
    n = len(arr) - 1
    while n >= 0 and arr[n] == 9:
        arr[n] = 0
        n -= 1
    if n < 0:
        arr.insert(0, 1)
    else:
        arr[n] += 1
    return arr


def plus_one_reversed(num_arr):
    for idx in reversed(list(enumerate(num_arr))):
        num_arr[idx[0]] = (num_arr[idx[0]] + 1) % 10
        if num_arr[idx[0]]:
            return num_arr
    return [1] + num_arr


arr = [9, 9, 9]
plus_one_last_element(arr)
