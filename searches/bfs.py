#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : bfs.py
@Time : 5/8/22 8:41 PM
@Desc:
Time Complexity: O(V+E)
Auxiliary Space: O(V)
Pros:
    1. Shortest Path
    2. Closer Nodes
Cons:
    1. More Memory
"""
from collections import defaultdict, deque


class Graph:
    """
    Graph class
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add edge to the grpah
        :param u:
        :param v:
        :return:
        """
        self.graph[u].append(v)

    def bfs(self, s):
        """
        Breadth first search (BFS)
        :param s:
        :return:
        """
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


def bfs_function_based(graph, root):
    """
    Breadth first search (BFS)
    :param graph:
    :param root:
    :return:
    """
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def recursive_bfs(graph, q, discovered):
    """
    Breadth first search (BFS) using recursive.
    :param graph:
    :param q:
    :param discovered:
    :return:
    """
    if not q:
        return
    v = q.popleft()
    print(v, end=' ')
    for u in graph.adjList[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
    recursive_bfs(graph, q, discovered)


def main():
    """
    Main function for drive the code
    :return:
    """
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)")
    g.bfs(2)
    print()
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs_function_based(graph, 0)


if __name__ == '__main__':
    main()
