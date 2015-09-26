# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:54:23 2015

@author: stoimenoff
"""
class Kpaths:
    def get(self, matrix, v, start, end, k):
        table = [[0 for i in range(v)] for i in range(k + 1)]
        table[0][start] = 1
        for i in range(1, k + 1):
            for j in range(0, v):
                if j == start:
                    continue
                paths = 0
                for a in range(v):
                    if matrix[a][j] == 1:
                        paths += table[i-1][a]
                table[i][j] = paths
        return table[k][end]

def main():
    e = int(input())
    edges= []
    v = 0
    for i in range(e):
        edge = [int(item) for item in input().split()]
        edges.append(edge)
        if edge[0] + 1 > v:
            v = edge[0] + 1
        if edge[1] + 1 > v:
            v = edge[1] + 1
    matrix = [[0 for i in range(v)] for i in range(v)]
    for i in range(e):
        matrix[edges[i][0]][edges[i][1]] = 1
    sek = [int(item) for item in input().split()]
    print( Kpaths().get(matrix, v, sek[0], sek[1], sek[2]) )
main()
