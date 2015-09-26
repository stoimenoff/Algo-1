# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:46:47 2015

@author: stoimenoff
"""
import random
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
        return (self.value)
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def contains(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next_node
        return False
    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next_node
        else:
            current = self.head
            while current != None:
                if current.next_node.value == value:
                    if current.next_node == self.tail:
                        self.tail = current
                    current.next_node = current.next_node.next_node
                    break
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

class RandSet:
    def __init__(self, size = 11):
        self.items = [LinkedList() for i in range(size)]
        self.values = []
        self.last = None
        self.size = size
        self.items_count = 0
    def hash(self, number):
        return number % self.size
    def contains(self, number):
        item = self.items[self.hash(number)].head
        while item != None:
            if self.values[item.value] == number:
                return True
            item = item.next_node
        return False
    def insert(self, number):
        if not self.contains(number):
            self.items[self.hash(number)].add_tail(len(self.values))
            self.last = self.items[self.hash(number)].tail
            self.values.append(number)
            self.items_count += 1
        if self.items_count / self.size > 0.7:
            #TODO
            #Resize set
            pass
    def remove(self, number):
        item = self.items[self.hash(number)].head
        while item != None:
            if self.values[item.value] == number:
                self.last.value = item.value
                item.value = len(self.values) - 1
                swap = self.values[item.value]
                self.values[item.value] = self.values[self.last.value]
                self.values[self.last.value] = swap
                del self.values[-1]
                self.items_count -= 1
                self.items[self.hash(number)].remove(item.value)
                break
            item = item.next_node
        item = self.items[self.hash(self.values[-1])].head
        while item != None:
            if self.values[item.value] == number:
                self.last = item
                break
            item = item.next_node
    def get_random(self):
        r = random.randint(0, self.items_count - 1)
        return self.values[r]
        
def main():
    r_set = RandSet()
    n = int(input())
    result = []
    for i in range(n):
        cmd = [item for item in input().split()]
        if cmd[0] == "insert":
            r_set.insert(int(cmd[1]))
        elif cmd[0] == "remove":
            r_set.remove(int(cmd[1]))
        elif cmd[0] == "contains":
            result.append(str(r_set.contains(int(cmd[1]))))
        elif cmd[0] == "random":
            result.append(r_set.get_random())
    for item in result:
        print(item)
main()