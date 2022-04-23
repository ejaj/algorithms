#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : quick_sort.py
@Time : 4/23/22 4:00 PM
@Desc:
"""


def partition(array, low, high):
    """
    Find the partition position
    :param array:
    :param low:
    :param high:
    :return:
    """
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    """
    Perform quicksort
    Time Complexity:
        Best: O(n*log n)
        Worst: O(n2)
        Average: O(n*log n)
    Space Complexity: O(log n)
    :param array:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)


def main():
    """
    Main function for run code
    :return:
    """
    data = [8, 7, 2, 1, 0, 9, 6]
    print("Unsorted Array")
    print(data)

    size = len(data)

    quick_sort(data, 0, size - 1)

    print('Sorted Array in Ascending Order:')
    print(data)


if __name__ == '__main__':
    main()
