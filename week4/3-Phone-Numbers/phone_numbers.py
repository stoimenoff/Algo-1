# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:15:12 2015

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

class PhoneNumbers:
    def min_phone_calls(self, graph):
        min_phone_calls = 0
        visited = [0] * len(graph)
        visited_num = 0
        to_visit = Queue()
        #visit 0
        to_visit.push(0)
        visited[0] = 1
        while visited_num != len(graph):
            visiting = to_visit.pop()
            visited_num += 1
            for i in range(len(graph)):
                if graph[visiting][i] == 1 and visited[i] == 0:
                    to_visit.push(i)
                    visited[i] = 1
            if to_visit.size == 0:
                min_phone_calls += 1
                for i in range(len(visited)):
                    if visited[i] == 0:
                        to_visit.push(i)
                        visited[i] = 1
                        break
        return min_phone_calls


def main():
    phone_book = {}
    graph = []
    k = int(input())
    phones = [int(n) for n in input().split()]
    i = 0
    for phone in phones:
        phone_book[phone] = i
        i += 1
    for i in range(k):
        line = [int(n) for n in input().split()]
        phones_of_i = [0] * k
        for phone in line[1:]:
            phones_of_i[phone_book[phone]] = 1
        graph.append(phones_of_i)
    print (PhoneNumbers().min_phone_calls(graph))
main()
    