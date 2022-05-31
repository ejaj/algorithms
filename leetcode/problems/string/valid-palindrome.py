#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : valid-palindrome.py
@Time : 6/1/22 12:19 AM
@Desc:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for char in s:
            if char.isalnum():
                new_str += char.lower()

        return new_str == new_str[::-1]