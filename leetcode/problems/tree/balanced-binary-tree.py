#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : balanced-binary-tree.py
@Time : 6/6/22 4:57 PM
@Desc:
Input: root = [3,9,20,null,null,15,7]
Output: true
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Input: root = []
Output: true
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
