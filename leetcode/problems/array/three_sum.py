#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : three_sum.py
@Time : 4/23/22 12:20 PM
@Desc:
nums = [1, 4, 45, 6, 10, 8]
target = 22

output = [1,4,5], index of value
"""
from typing import List


def three_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    Brute Force Approach
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    Args:
        nums:
        target:

    Returns:

    """
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]


def three_sum_sorting_pointers(nums, target):
    """
    Sorting and Two-Pointers technique.
    Args:
        nums:
        target:

    Returns:

    """
    arr_size = len(nums)
    nums.sort()
    for i in range(0, arr_size - 2):
        l = i + 1
        r = arr_size - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == target:
                return [i, l, r]
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return []


def three_sum_has_map(nums, target):
    """
    Hash Map / Set Method
    Time complexity: O(N^2)
    Auxiliary Space: O(N)
    Args:
        nums:
        target:

    Returns:

    """
    arr_size = len(nums)
    for i in range(0, arr_size - 1):
        s = {}
        curr_sum = target - nums[i]
        for j in range(i + 1, arr_size):
            triple_current_sum = curr_sum - nums[j]
            if triple_current_sum in s:
                return [i, j, s[triple_current_sum]]
            s[nums[j]] = j
    return []


def l_3sum_leet_code(nums):
    length = len(nums)
    result = []
    # for i in range(length):
    #     for j in range(i + 1, length):
    #         for k in range(j + 1, length):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 sorted_result = sorted([nums[i], nums[j], nums[k]])
    #                 if sorted_result not in result:
    #                     result.append(sorted_result)
    # return result
    # Input: nums = [-1, 0, 1, 2, -1, -4]
    # Output: [[-1, -1, 2], [-1, 0, 1]]
    nums.sort()

    # sorted_array = [-4, -1, -1, 0, 1, 2]

    for i in range(length):
        left, right = i + 1, length - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                sorted_result = sorted([nums[i], nums[left], nums[right]])
                if sorted_result not in result:
                    result.append([nums[i], nums[left], nums[right]])
                left += 1
                # Avoid duplicates for left
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result


def main():
    # nums = [1, 4, 45, 6, 10, 8]
    # target = 22
    # print(three_sum_brute(nums, target))
    # print(three_sum_sorting_pointers(nums, target))
    # print(three_sum_has_map(nums, target))

    nums = [-1, 0, 1, 2, -1, -4]
    print(l_3sum_leet_code(nums))


if __name__ == '__main__':
    main()
