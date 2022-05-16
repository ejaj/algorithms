#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : floyd_warshall.py
@Time : 5/9/22 12:42 AM
@Desc:
Time Complexity: O(n^3)
Space Complexity: O(n2^)
"""
# The number of vertices
nV = 4
INF = 999


def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_distance(distance)


def print_distance(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def main():
    G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
    floyd_warshall(G)


if __name__ == '__main__':
    main()
