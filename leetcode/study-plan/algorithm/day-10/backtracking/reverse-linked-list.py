#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : reverse-linked-list.py
@Time : 5/25/22 10:56 AM
@Desc:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        n = head.next
        h = self.reverseList(n)
        head.next = None
        n.next = head

        return h
