#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : longest-substring-without-repeating-characters.py
@Time : 5/22/22 12:01 AM
@Desc:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start = 0
        max_len = 0
        for i, val in enumerate(s):
            if val in chars:
                start = max(start, chars[val] + 1)
            max_len = max(max_len, i - start + 1)
            chars[val] = i
        return max_len
