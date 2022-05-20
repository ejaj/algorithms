#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : remove-nth-node-from-end-of-list.py
@Time : 5/20/22 2:55 PM
@Desc: 
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_Nth_from_end(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
