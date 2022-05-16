#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : binary-search.py
@Time : 5/16/22 3:26 PM
@Desc:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search Operation.
        Time Complexity: O(log n)
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums)
        while start < end:
            mid = ((end - start) // 2) + start
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1

        return -1


def main():
    """
    Main function for run the code.
    :return:
    """
    c = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(c.search(nums, target))


if __name__ == '__main__':
    main()
