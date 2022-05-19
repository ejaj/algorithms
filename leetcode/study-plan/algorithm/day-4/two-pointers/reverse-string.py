#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : reverse-string.py
@Time : 5/19/22 12:11 PM
@Desc:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
