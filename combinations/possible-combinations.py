#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : possible-combinations.py
@Time : 5/26/22 12:00 PM
@Desc: 
"""


def print_combination(arr, n, r):
    data = [0] * r
    print(data)
    combination_util(arr, data, 0, n - 1, 0, r)


def combination_util(arr, data, start, end, index, r):
    """
    Args:
        arr: Input Array
        data: Temporary array to store current combination
        start: Starting indexes in arr[]
        end: Ending indexes in arr[]
        index: Current index in data[]
        r:Size of a combination to be printed

    Returns:

    """
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return
    i = start
    while i <= end and end - i + 1 >= r - index:
        data[index] = arr[i]
        combination_util(arr, data, i + 1, end, index + 1, r)

        i += 1


def combinationUtil(arr, n, r, index, data, i):
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return
    if i >= n:
        return

    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1)

    combinationUtil(arr, n, r, index,
                    data, i + 1)


arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
print_combination(arr, n, r)
