# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:58:34 2015

@author: stoimenoff
"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, next_node):
        self.next_node = next_node
    def __gt__(self, node):
        return self.value > node.value
    def __lt__(self, node):
        return self.value < node.value
    def __str__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def add_head(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.set_next(self.head)
            self.head = new_node
    def pop(self):
        if self.head != None:
            value = self.head.value
            self.head = self.head.get_next()
            if self.head == None:
                self.tail = None
            return value

class Queue:
    def __init__(self):
        self.items = LinkedList()
        self.size = 0
    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(self, value):
        self.items.add_tail(value)
        self.size += 1
    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        return None
    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek(self):
        if self.size > 0:
            return self.items.head.value
        return None
    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size(self):
        return self.size

class Stack:
    def __init__(self):
        self.items = LinkedList()
        self.size = 0
    # Adds value to the end of the Stack.
    # Complexity: O(1)
    def push(self, value):
        self.items.add_head(value)
        self.size += 1
    # Returns value from the end of the Stack and removes it.
    # Complexity: O(1)
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        return None
    # Returns value from the end of the Stack without removing it.
    # Complexity: O(1)
    def peek(self):
        if self.size > 0:
            return self.items.head.value
        return None
    # Returns the number of elements in the Stack.
    # Complexity: O(1)
    def size(self):
        return self.size

class Route_node:
    def __init__(self, index, prev = None, distance_from_prev = None):
        self.index = index
        self.prev = prev
        self.distance_from_prev = distance_from_prev        
        
class Edge:
    def __init__(self, v1, v2, weight, prev = None):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    def contains(self, vertex):
        if self.v1 == vertex or self.v2 == vertex:
            return True
        return False
    def copy(self):
        return Edge(self.v1, self.v2, self.weight)
    def swap(self):
        return Edge(self.v2, self.v1, self.weight)
    def __lt__(self, edge):
        return self.weight < edge.weight
    def __gt__(self, edge):
        return self.weight > edge.weight
    def __eq__(self, edge):
        return (self.v1 == edge.v1 and self.v2 == edge.v2 and self.weight == edge.weight)
    def __str__(self):
        return str(self.v1) + " --> " + str(self.v2) + " : " + str(self.weight)

class SpanningTree:
    def __init__(self, edges, n):
        self.adj = [[] for i in range(n)]
        self.n = n
        for edge in edges:
            self.adj[edge.v1].append(edge)
            self.adj[edge.v2].append(edge.swap())
        self.msum = float("inf")
        self.mst = self.MST()
        
    def MST(self):
        mst = [[] for i in range(self.n)]
        gotten = [0]
        free = [True] * self.n
        free[0] = False
        msum = 0
        for k in range(self.n-1):
            min_edge = Edge(-1,-1,float("inf"))
            for vertex in gotten:
                for edge in self.adj[vertex]:
                    if free[edge.v2] == True and edge < min_edge:
                        min_edge = edge
            gotten.append(min_edge.v2)
            free[min_edge.v2] = False
            msum += min_edge.weight
            mst[min_edge.v1].append(min_edge)
            mst[min_edge.v2].append(min_edge.swap())
            self.adj[min_edge.v1].remove(min_edge)
            self.adj[min_edge.v2].remove(min_edge.swap())
        self.msum = msum
        return mst
    def calculate_min_sum_if_edge_in_spanning_tree(self, added_edge):
        visited = [False] * self.n
        visited[added_edge.v1] = True
        vertexes = Stack()
        vertexes.push(Route_node(added_edge.v1))
        vert = None
        while vertexes.size > 0:
            vert = vertexes.pop()
            if vert.index == added_edge.v2:
                break
            for edge in self.mst[vert.index]:
                if visited[edge.v2] == False:
                    vertexes.push(Route_node(edge.v2, vert, edge.weight))
                    visited[edge.v2] = True
        max_distance = vert.distance_from_prev
        while vert.distance_from_prev != None:
            if vert.distance_from_prev > max_distance:
                max_distance = vert.distance_from_prev
            vert = vert.prev
        return self.msum - max_distance + added_edge.weight
            
    def SBST(self):
        sbst_sum = float("inf")
        for row in self.adj:
            for edge in row:
                cmsieist = self.calculate_min_sum_if_edge_in_spanning_tree(edge)
                if cmsieist < sbst_sum:
                    sbst_sum = cmsieist
        return sbst_sum

def main():
    n = int(input())
    edges = []
    v = 0
    for i in range(n):
        edge = [int(item) for item in input().split()]
        i = edge[0] - 1
        j = edge[1] - 1
        w = edge[2]
        edges.append( Edge(i, j, w) )
        if i > v:
            v = i
        if j > v:
            v = j
    v += 1
    print(SpanningTree(edges, v).SBST())
main()  
