#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : permutation-in-string.py
@Time : 5/22/22 12:03 AM
@Desc:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        s1_len = len(s1)

        for i in range(len(s2) - s1_len + 1):
            if Counter(s2[i:i + s1_len]) == s1_counter:
                return True

        return False
