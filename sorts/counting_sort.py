#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : counting_sort.py
@Time : 4/26/22 5:12 PM
@Desc:
Time Complexity:
    Best: O(n+k)
    Worst: O(n+k)
    Average: O(n+k)
Space Complexity: O(max)
"""


def counting_sort(array):
    """
    Counting Sort
    :param array:
    :return:
    """
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1

    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


def main():
    arr = [4, 2, 2, 8, 3, 3, 1]
    counting_sort(arr)
    print("Sorted Array in Ascending Order: ")
    print(arr)


if __name__ == '__main__':
    main()
