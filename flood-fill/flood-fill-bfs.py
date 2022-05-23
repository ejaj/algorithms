#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : flood-fill-bfs.py
@Time : 5/23/22 12:14 PM
@Desc: 
"""


def valid_coord(x, y, n, m):
    if x < 0 or y < 0:
        return 0
    if x >= n or y >= m:
        return 0
    return 1


def bfs(n, m, data, X, Y, new_color):
    visiting = [[0 for i in range(101)] for j in range(101)]
    obj = []
    obj.append([X, Y])
    visiting[X][Y] = 1

    while len(obj) > 0:
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        prev_color = data[x][y]
        data[x][y] = new_color
        obj.pop(0)

        # For Upside Pixel or Cell
        if valid_coord(x + 1, y, n, m) == 1 and visiting[x + 1][y] == 0 and data[x + 1][y] == prev_color:
            obj.append([x + 1, y])
            visiting[x + 1][y] = 1

        # For Downside Pixel or Cell
        if valid_coord(x - 1, y, n, m) == 1 and visiting[x - 1][y] == 0 and data[x - 1][y] == prev_color:
            obj.append([x - 1, y])
            visiting[x - 1][y] = 1

        # For Right side Pixel or Cell
        if valid_coord(x, y + 1, n, m) == 1 and visiting[x][y + 1] == 0 and data[x][y + 1] == prev_color:
            obj.append([x, y + 1])
            visiting[x][y + 1] = 1

        # For Left side Pixel or Cell
        if valid_coord(x, y - 1, n, m) == 1 and visiting[x][y - 1] == 0 and data[x][y - 1] == prev_color:
            obj.append([x, y - 1])
            visiting[x][y - 1] = 1
        for i in range(n):
            for j in range(m):
                print(data[i][j], end=" ")
            print()
        print()


def main():
    n = 8
    m = 8

    data = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
    ]

    x, y, color = 4, 4, 3
    bfs(n, m, data, x, y, color)


if __name__ == '__main__':
    main()
