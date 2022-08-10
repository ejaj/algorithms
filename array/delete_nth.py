from collections import defaultdict


def delete_nth_bruteforce(nums, n):
    """
    Time complexity O(n^2)
    Args:
        nums:
        n:

    Returns:

    """
    ans = []
    for num in nums:
        if ans.count(num) < n:
            ans.append(num)
    print(ans)


def delete_nth_has_map(nums, n):
    ans = []
    counts = defaultdict(int)
    for num in nums:
        if counts[num] < n:
            ans.append(num)
            counts[num] += 1
    print(counts)
    print(ans)


nums = [1, 2, 3, 1, 2, 1, 2, 3]
n = 2
delete_nth_has_map(nums, n)
