#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : binary_search.py
@Time : 5/8/22 7:31 PM
@Desc:
Time Complexity:
    Best: O(1)
    Worst: O(log n)
    Average: O(log n)
Space Complexity: O(1)
"""


def binary_search(array, x, low, high):
    """
    Binary Search, Iteration Method
    :param array:
    :param x:
    :param low:
    :param high:
    :return:
    """
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(array, x, low, high):
    """
    Binary Search, Recursive Method
    :param array:
    :param x:
    :param low:
    :param high:
    :return:
    """

    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search_recursive(array, x, low, mid - 1)
        else:
            return binary_search_recursive(array, x, mid + 1, high)

    else:
        return -1


def main():
    """
    Main function for drive the code.
    :return:
    """
    array = [3, 4, 5, 6, 7, 8, 9]
    x = 4
    # result = binary_search(array, x, 0, len(array) - 1)
    result = binary_search_recursive(array, x, 0, len(array) - 1)
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")


if __name__ == '__main__':
    main()
