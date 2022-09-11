def merge_intervals_brute_force(arr):
    arr.sort()
    stack = [arr[0]]
    for i in arr[1:]:

        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    print("The Merged Intervals are :", end=" ")
    for i in range(len(stack)):
        print(stack[i], end=" ")


def merge_intervals(arr):
    arr.sort(key=lambda x: x[0])
    print(arr)
    index = 0
    print(arr[index][1])
    print(arr[1][0])
    # for i in range(1, len(arr)):
    #     print(i)


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# merge_intervals_brute_force(arr)
merge_intervals(arr)
