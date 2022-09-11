arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]

count = 0
result = 0
n = len(arr)
for i in range(0, n):
    if arr[i] == 1:
        count = count + 1
        result = max(result, count)
    else:
        count = 0
print(result)


## II
