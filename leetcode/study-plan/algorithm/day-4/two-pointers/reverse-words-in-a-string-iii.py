#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : reverse-words-in-a-string-iii.py
@Time : 5/19/22 12:19 PM
@Desc:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc

Input: s = "God Ding"
Output: "doG gniD"

"""


class Solution:
    def reverse_words(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]


def main():
    """
    Main function run the code
    :return:
    """
    nums = "Let's take LeetCode contest"
    s = Solution()
    print(s.reverse_words(nums))


if __name__ == '__main__':
    main()
