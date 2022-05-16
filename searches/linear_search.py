#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : linear_search.py
@Time : 5/8/22 7:25 PM
@Desc:
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def linear_search(arr: List[int], x: int):
    """
    Liner Search
    :param arr:
    :param x:
    :return:
    """
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


def main():
    """
    Main function for drive the code.
    :return:
    """
    array = [2, 4, 0, 1, 9]
    x = 1
    result = linear_search(array, x)
    if result == -1:
        print("Element not found")
    else:
        print("Element found at index: ", result)


if __name__ == '__main__':
    main()
