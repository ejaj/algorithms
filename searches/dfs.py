#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : dfs.py
@Time : 5/8/22 8:42 PM
@Desc:
Time Complexity: O(V+E)
Auxiliary Space: O(V)
Pros:
    1. Less Memory
    2. Does Path Exist?
Cons:
    1. Can Get Slow
"""
from collections import defaultdict


class Graph:
    """
    Graph class
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add edge to the graph
        :param u:
        :param v:
        :return:
        """
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        """
        Print all value of the graph
        :param v:
        :param visited:
        :return:
        """
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        """
        Depth First Search (DFS)
        :param v:
        :return:
        """
        visited = set()
        self.dfs_util(v, visited)


def dfs_function_based(graph, start, visited=None):
    """
    Depth First Search (DFS), function based.
    :param graph:
    :param start:
    :param visited:
    :return:
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs_function_based(graph, next, visited)
    return visited


def main():
    """
    Main function for drive code
    :return:
    """
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])
             }

    dfs_function_based(graph, '0')


if __name__ == '__main__':
    main()
