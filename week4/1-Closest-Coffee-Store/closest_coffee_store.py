# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:08:49 2015

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

class ClosestCoffeeStore:

    # Finds the closest coffee store to a point.
    # graph - [[bool]]
    # starting_point - int
    # is_coffee_store - [bool]
    def closestCoffeeStore(self, graph, is_coffee_store, starting_point):
        verts = Queue()
        verts.push(starting_point)
        verts.push(-1)
        visited = [0] * len(graph)
        visited[starting_point] = 1
        distance = 0
        while verts.size != 0:
            vert = verts.pop()
            if vert == -1:
                distance += 1
                if verts.size != 0:
                    verts.push(-1)
                continue
            if is_coffee_store[vert] == 1:
                return distance
            else:
                for i in range(len(graph)):
                    if graph[vert][i] == 1 and visited[i] == 0:
                        verts.push(i)
                        visited[i] = 1
        return -1
        
def main():
    n = int(input())
    graph = []
    for i in range(n):
        row = [int(num) for num in input().split()]
        graph.append(row)
    starting_point = int(input())
    is_coffee_store = [int(num) for num in input().split()]
    print(ClosestCoffeeStore().closestCoffeeStore(graph, is_coffee_store, starting_point))
main()
