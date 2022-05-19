#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : two-sum-ii-input-array-is-sorted.py
@Time : 5/18/22 11:34 AM
@Desc: 
"""
from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in values:
                return [values[diff]+1, i+1]
            values[numbers[i]] = i


def main():
    """
    Main function for drive code
    Returns:

    """
    nums = [2,7,11,15]
    target = 9
    s = Solution()
    print(s.two_sum(nums, target))


if __name__ == '__main__':
    main()
