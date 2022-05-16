#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : first-bad-version.py
@Time : 5/16/22 3:40 PM
@Desc:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Input: n = 1, bad = 1
Output: 1

"""


def isBadVersion(version):
    pass


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def first_bad_dersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        start = 1
        end = n
        while start < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return int(start)


def main():
    """
    Main function for run the code.
    :return:
    """
    c = Solution()
    n = 5
    print(c.first_bad_dersion(n))


if __name__ == '__main__':
    main()
