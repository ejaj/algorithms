#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : populating-next-right-pointers-in-each-node.py
@Time : 5/23/22 1:14 PM
@Desc: 
"""


class Solution:
    ##BFS
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = []
        queue.append(root)
        while (len(queue) > 0):
            temp = []
            while queue:
                cur_node = queue.pop(0)
                if cur_node.left:
                    temp.append(cur_node.left)
                if cur_node.right:
                    temp.append(cur_node.right)
            for i in range(len(temp) - 1):
                temp[i].next = temp[i + 1]
            queue.extend(temp)
        return root

    ## Recursion
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     if root is None or root.left is None:
    #         return root
    #     root.left.next = root.right
    #     if root.next:
    #         root.right.next = root.next.left
    #     self.connect(root.left)
    #     self.connect(root.right)
    #     return root
