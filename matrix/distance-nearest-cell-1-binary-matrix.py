#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : distance-nearest-cell-1-binary-matrix.py
@Time : 5/24/22 5:32 PM
@Desc:

Input : N = 3, M = 4
        mat[][] = { 0, 0, 0, 1,
                    0, 0, 1, 1,
                    0, 1, 1, 0 }
Output : 3 2 1 0
         2 1 0 0
         1 0 0 1
Explanation:
For cell at (0, 0), nearest 1 is at (0, 3),
so distance = (0 - 0) + (3 - 0) = 3.
Similarly, all the distance can be calculated.

Input : N = 3, M = 3
        mat[][] = { 1, 0, 0,
            0, 0, 1,
            0, 1, 1 }
Output :
       0 1 1
       1 1 0
       1 0 0
Explanation:
For cell at (0, 1), nearest 1 is at (0, 0), so distance
is 1. Similarly, all the distance can be calculated.
"""


def print_distance_brute_force(mat):
    N = 3
    M = 4
    ans = [[None] * M for i in range(N)]

    for i in range(N):
        for j in range(M):
            ans[i][j] = 999999999999
    for i in range(N):
        for j in range(M):
            for k in range(N):
                for l in range(M):
                    if mat[k][l] == 1:
                        ans[i][j] = min(ans[i][j], abs(i - k) + abs(j - l))
    for i in range(N):
        for j in range(M):
            print(ans[i][j], end=" ")
        print()


def main():
    N = 3
    M = 4

    mat = [[0, 0, 0, 1],
           [0, 0, 1, 1],
           [0, 1, 1, 0]]

    print_distance_brute_force(mat)


if __name__ == '__main__':
    main()
