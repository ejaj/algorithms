#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : dijkstras.py
@Time : 5/16/22 1:10 PM
@Desc:
Time Complexity: O(V^2)
Space complexity: O(V2)
"""
import sys


class Graph:
    def __init__(self, vertices):
        """
        :param vertices:
        """
        self.V = vertices
        self.graph = [
            [0 for column in range(vertices)]
            for row in range(vertices)
        ]

    def print_data(self, dist):
        """
        Print Vertex and Distance from Source.
        :param dist:
        :return:
        """
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minimum_distance(self, dist, visited):
        """
        Find the vertex with minimum distance value, from the set of vertices not yet included in visited
        :param dist:
        :param visited:
        :return:
        """
        min = sys.maxsize
        min_index = min
        for u in range(self.V):
            if dist[u] < min and not visited[u]:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        """
        Implements Dijkstra's single source, shortest path algorithm for a graph represented,
        using adjacency matrix representation.
        :param src:
        :return:
        """
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for count in range(self.V):
            current_vertex = self.minimum_distance(dist, visited)
            visited[current_vertex] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for neighbour in range(self.V):
                if self.graph[current_vertex][neighbour] > 0 and not visited[neighbour] and \
                        dist[neighbour] > dist[current_vertex] + self.graph[current_vertex][neighbour]:
                    dist[neighbour] = dist[current_vertex] + self.graph[current_vertex][neighbour]
        self.print_data(dist)


def main():
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    g.dijkstra(0)


if __name__ == '__main__':
    main()
