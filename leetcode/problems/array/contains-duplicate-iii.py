#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : contains-duplicate-iii.py
@Time : 7/21/22 3:25 PM
@Desc:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


def contains_nearby_almost_duplicate(nums, k, t):
    bucket = {}
    width = t + 1

    for i, n in enumerate(nums):
        bucket_i = n // width

        if bucket_i in bucket:
            return True
        elif bucket_i + 1 in bucket and abs(n - bucket[bucket_i + 1]) < width:
            return True
        elif bucket_i - 1 in bucket and abs(n - bucket[bucket_i - 1]) < width:
            return True

        bucket[bucket_i] = n
        if i >= k: del bucket[nums[i - k] // width]

    return False


def main():
    """
    main function to drive code
    Returns:

    """
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(contains_nearby_almost_duplicate(nums, k, t))


if __name__ == '__main__':
    main()
