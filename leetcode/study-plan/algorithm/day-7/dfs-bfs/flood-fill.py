#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : flood-fill.py
@Time : 5/23/22 1:45 AM
@Desc:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
"""

from typing import List


class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        r_ls, c_ls = len(image), len(image[0])
        color = image[sr][sc]
        if color == new_color:
            return image
        queue = [(sr, sc)]
        while len(queue) > 0:
            r, c = queue.pop(0)
            if image[r][c] == color:
                image[r][c] = new_color
                if r - 1 >= 0: queue.append((r - 1, c))
                if r + 1 < r_ls: queue.append((r + 1, c))
                if c - 1 >= 0: queue.append((r, c - 1))
                if c + 1 < c_ls: queue.append((r, c + 1))
        return image
