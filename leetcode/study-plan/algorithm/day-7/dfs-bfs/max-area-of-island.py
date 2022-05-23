#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : max-area-of-island.py
@Time : 5/23/22 12:42 PM
@Desc:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
"""

from typing import List


class Solution:
    def maxArea_of_island(self, grid: List[List[int]]) -> int:
        def dfs(i, j, size):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return size
            grid[i][j] = 0
            return 1 + dfs(i, j + 1, size) + dfs(i, j - 1, size) + dfs(i + 1, j, size) + dfs(i - 1, j, size)

        # Find the maximum size count
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i, j, 0))
        return max_size
