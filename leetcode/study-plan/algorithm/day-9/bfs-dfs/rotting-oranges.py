#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : rotting-oranges.py
@Time : 5/25/22 10:48 AM
@Desc:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fresh_set = set()
        rotten = collections.deque()
        step = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    fresh_set.add((x, y))
                elif grid[x][y] == 2:
                    rotten.append([x, y, step])
        while rotten:
            x, y, step = rotten.popleft()
            for dx, dy in dirs:
                if 0 <= x + dx < row and 0 <= y + dy < col and grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    fresh_set.remove((x + dx, y + dy))
                    rotten.append([x + dx, y + dy, step + 1])
        return step if not fresh_set else -1