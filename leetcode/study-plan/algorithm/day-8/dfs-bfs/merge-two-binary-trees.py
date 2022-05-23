#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : merge-two-binary-trees.py
@Time : 5/23/22 1:06 PM
@Desc:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.merge_trees(root1.left, root2.left)
        root1.right = self.merge_trees(root1.right, root2.right)
        return root1
