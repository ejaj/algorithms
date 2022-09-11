def max_ones_index(nums):
    result, prev, curr = 0, 0, 0
    for n in nums:
        if n == 0:
            result = max(result, prev + curr + 1)
            prev, curr = curr, 0
        else:
            curr += 1
    return min(max(result, prev + curr + 1), len(nums))


def max_ones_index_three_indexes(nums):
    max_count = 0
    count = 0
    max_index = -1
    previous_zero_index = -1

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = i - previous_zero_index
            previous_zero_index = i

        if count > max_count:
            max_count = count
            max_index = previous_zero_index
    return max_index


def max_ones_index_three_indexes_other(nums):
    n = len(arr)
    max_count = 0
    max_index = 0
    prev_zero = -1
    prev_prev_zero = -1
    for current in range(n):
        if nums[current] == 0:
            if current - prev_prev_zero > max_count:
                max_count = current - prev_prev_zero
                max_index = prev_zero

            prev_prev_zero = prev_zero
            prev_zero = current
        if n - prev_prev_zero > max_count:
            max_index = current
    return max_index


arr = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
print(max_ones_index_three_indexes(arr))
