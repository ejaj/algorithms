#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : squares-of-a-sorted-array.py
@Time : 5/17/22 1:00 PM
@Desc:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        results = [x * x for x in nums]
        results.sort()
        return results


def main():
    """
    Main function run the code
    :return:
    """
    nums = [-4, -1, 0, 3, 10]
    s = Solution()
    print(s.sorted_squares(nums))


if __name__ == '__main__':
    main()
