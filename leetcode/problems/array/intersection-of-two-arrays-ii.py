#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : intersection-of-two-arrays-ii.py
@Time : 7/26/22 11:06 AM
@Desc:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from collections import Counter
from typing import List


# def intersect(nums1, nums2):
#     return list(set(nums1) & set(nums2))
#     temp = set(nums2)
#     lst3 = [value for value in nums1 if value in temp]
#     llist = [value for value in nums1 if value in nums2]
#     return llist


def intersect_by_sort(nums1, nums2):
    nums1.sort()
    nums2.sort()
    ans = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
            j += 1
    return ans


def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

    cnt = Counter(nums1)
    ans = []
    for x in nums2:
        if cnt[x] > 0:
            ans.append(x)
            cnt[x] -= 1
    return ans


def main():
    """
    main function to drive code
    Returns:

    """
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    intersect(nums1, nums2)


if __name__ == '__main__':
    main()
