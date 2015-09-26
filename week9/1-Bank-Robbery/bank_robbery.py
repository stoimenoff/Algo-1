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
        
class Route_node:
    def __init__(self, index, distance, prev = None):
        self.index = index
        self.distance = distance
        self.prev = prev
        
class BankRobbery:
    def rob(self, n, adj_lists, b, p, h):
        police_index = [float("inf")] * n
        distance = 0
        police_q = Queue()
        police_q.push(p)
        police_q.push("#")
        while police_q.size > 1:
            junk = police_q.pop()
            if junk == "#":
                distance += 1
                police_q.push("#")
                continue
            police_index[junk] = distance
            for junk in adj_lists[junk]:
                if police_index[junk] == float("inf"):
                    police_index[junk] = -1
                    police_q.push(junk)
        rob_q = Queue()
        rob_q.push(Route_node(b, 0))
        visited = [False] * n
        visited[b] = True
        node = None
        while rob_q.size > 0:
            node = rob_q.pop()
            if node.index == h:
                break
            for junk in adj_lists[node.index]:
                if visited[junk] == False:
                   visited[junk] = True
                   rob_q.push(Route_node(junk, node.distance + 1, node))
        
        min_diff = police_index[node.index] - node.distance
        while node != None:
            if police_index[node.index] - node.distance < min_diff:
                min_diff = police_index[node.index] - node.distance
            node = node.prev
        return min_diff - 1

def main():
    n_m = [int(item) for item in input().split()]
    adj_lists = [[] for i in range(n_m[0])]
    for i in range(n_m[1]):
        i_j = [int(item) for item in input().split()]
        adj_lists[i_j[0] - 1].append(i_j[1] - 1)
        adj_lists[i_j[1] - 1].append(i_j[0] - 1)
    b_p_h = [int(item) for item in input().split()]
    print(BankRobbery().rob(n_m[0], adj_lists, b_p_h[0] - 1, b_p_h[1] - 1, b_p_h[2] - 1))
main()  
