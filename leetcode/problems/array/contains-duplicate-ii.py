#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : contains-duplicate-ii.py
@Time : 7/21/22 2:50 PM
@Desc:
Input: nums = [1,2,3,1], k = 3
Output: true
Input: nums = [1,0,1,1], k = 1
Output: true
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


def contains_near_by_duplicate(nums, k):
    hash_map = {}
    # for i in range(len(nums)):
    #     if nums[i] in hash_map and abs(i - hash_map[nums[i]]) <= k:
    #         return True
    #     hash_map[nums[i]] = i

    for index, value in enumerate(nums):
        if value in hash_map and abs(index - hash_map[value]) <= k:
            return True
        hash_map[value] = index
    return False


def main():
    """
    main function to drive code
    Returns:

    """
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(contains_near_by_duplicate(nums, k))


if __name__ == '__main__':
    main()
