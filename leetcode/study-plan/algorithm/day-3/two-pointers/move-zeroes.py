#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : move-zeroes.py
@Time : 5/18/22 11:30 AM
@Desc:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Input: nums = [0]
Output: [0]
"""

from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Movie all zeros to last of the list.
        Args:
            nums:

        Returns:

        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1


def main():
    """
    Main function run the code
    :return:
    """
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    print(s.move_zeroes(nums))


if __name__ == '__main__':
    main()
