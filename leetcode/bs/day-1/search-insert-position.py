#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : search-insert-position.py
@Time : 5/16/22 3:46 PM
@Desc:
Input: nums = [1,3,5,6], target = 5
Output: 2
Input: nums = [1,3,5,6], target = 2
Output: 1
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Binary Search Operation, if target value found in list return that index,
        if not found return inserted place index
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        return start


def main():
    """
    Main function for run the code.
    :return:
    """
    c = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(c.search_insert(nums, target))


if __name__ == '__main__':
    main()
