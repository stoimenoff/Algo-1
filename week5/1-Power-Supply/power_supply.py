# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:08:46 2015

@author: stoimenoff
"""
import heapq
class Heap:    
    def __init__(self):
        self.items = []
        self.size = 0
    def push(self, item):
        heapq.heappush(self.items, item)
        self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return heapq.heappop(self.items)
        return None
    def __str__(self):
        o = ""
        for item in self.items:
            o += (str(item.to) + " " + str(item.distance))
class Edge:
    def __init__(self, to, distance):
        self.to = to
        self.distance = distance
    def __gt__(self, edge):
        return self.distance > edge.distance
    def __lt__(self, edge):
        return self.distance < edge.distance

class PowerSupply:
    def calculate_cable_amount(self, graph, vertexes):
        heap = Heap()
        n = vertexes
        added = [0 for i in range(n)]
        added[0] = 1
        additons = 1
        for i in range(n):
            if graph[0][i] > 0:
                heap.push(Edge(i, graph[0][i]))
        distance = 0
        while additons != vertexes:
            to_add = heap.pop()
            added[to_add.to] = 1
            additons += 1
            distance += to_add.distance
            for i in range(n):
                if graph[to_add.to][i] > 0 and added[i] == 0:
                    heap.push(Edge(i, graph[to_add.to][i]))
        return distance
        
def main():
    n = int(input())
    graph = [[0 for i in range(1000)] for i in range(1000)]
    vertexes = 0
    for i in range(n):
        junction = [int(item) for item in input().split()]
        if junction[0] > vertexes:
            vertexes = junction[0]
        if junction[1] > vertexes:
            vertexes = junction[1]
        graph[junction[0]-1][junction[1]-1] = junction[2]
        graph[junction[1]-1][junction[0]-1] = junction[2]
    print( PowerSupply().calculate_cable_amount(graph, vertexes) )
main()