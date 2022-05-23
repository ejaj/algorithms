#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : flood-fill-recursively.py
@Time : 5/23/22 11:34 AM
@Desc: 
"""
# Dimensions of a martix
M = 8
N = 8


def flood_fill_util(screen, x, y, prev_color, new_color):
    if x < 0 or x >= M or y < 0 or y >= N or screen[x][y] != prev_color or screen[x][y] == new_color:
        return
    screen[x][y] = new_color

    # Recur for north, east, south and west
    flood_fill_util(screen, x + 1, y, prev_color, new_color)
    flood_fill_util(screen, x - 1, y, prev_color, new_color)
    flood_fill_util(screen, x, y + 1, prev_color, new_color)
    flood_fill_util(screen, x, y - 1, prev_color, new_color)


def flood_fill(screen, x, y, new_color):
    prev_color = screen[x][y]
    if prev_color == new_color:
        return
    flood_fill_util(screen, x, y, prev_color, new_color)


def main():
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 0],
              [1, 0, 0, 1, 1, 0, 1, 1],
              [1, 2, 2, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 2, 2, 0],
              [1, 1, 1, 1, 1, 2, 1, 1],
              [1, 1, 1, 1, 1, 2, 2, 1]]

    x = 4
    y = 4
    new_color = 3
    flood_fill(screen, x, y, new_color)

    print("Updated screen after call to floodFill:")
    for i in range(M):
        for j in range(N):
            print(screen[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
