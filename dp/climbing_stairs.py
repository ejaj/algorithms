#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : climbing_stairs.py
@Time : 5/9/22 11:14 AM
@Desc:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


def climb_stairs(n: int) -> int:
    """
    Climb stairs recursive.
    :param n:
    :return:
    """
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one


def climb_stairs_recursive(n):
    """
    Climb stairs recursive, using recursive method
    Time Complexity: O(2^n)
    Space Complexity: O(1)
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


def count_ways(s):
    """
    Count the ways.
    :param s:
    :return:
    """
    return climb_stairs_recursive(s + 1)


def climb_stairs_dp(n, dp):
    """
    Climb stairs recursive, using dp method
    Time Complexity: O(n)
    Auxiliary Space: O(n)
    :param n:
    :param dp:
    :return:
    """
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = climb_stairs_dp(n - 1, dp) + climb_stairs_dp(n - 2, dp)
    return dp[n]


def count_ways_dp(n):
    """
    Count the ways.
    :param n:
    :return:
    """
    dp = [-1 for i in range(n + 1)]
    climb_stairs_dp(n, dp)
    return dp[n]


def main():
    """
    Main function for drive the code.
    :return:
    """
    print(climb_stairs(3))
    print(count_ways(3))
    print(count_ways_dp(3))


if __name__ == '__main__':
    main()
