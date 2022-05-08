#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : shell_sort.py
@Time : 5/8/22 7:09 PM
@Desc:
Time Complexity:
    Best: O(nlog n)
    Worst: O(n^2)
    Average: O(nlog n)
Space Complexity: O(1)
"""

from typing import List


def shell_sort(arr: List[int]):
    gap = len(arr) // 2  # initialize the gap

    while gap > 0:
        i = 0
        j = gap

        # check the array in from left to right, till the last possible index of j
        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1

            # we look back from ith index to the left, we swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1

        gap //= 2


def main():
    """
    Main function for drive the code
    :return:
    """
    arr = [12, 34, 54, 2, 3]
    print("input array:", arr)

    shell_sort(arr)
    print("sorted array", arr)


if __name__ == '__main__':
    main()
