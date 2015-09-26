# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:24:56 2015

@author: stoimenoff
"""
import random
import sys

class Heap:
    def __init__(self):
        self.items = []
    def get_min_child_index(self, index):
        min_child_index = index #return same value as input = no child
        if 2*index + 1 < len(self.items):
            min_child_index = 2*index + 1
        if 2*index + 2 < len(self.items):
            if self.items[2*index + 2] < self.items[min_child_index]:
                min_child_index = 2*index + 2
        return min_child_index
    def add(self, item):
        self.items.append(item)
        index = len(self.items) - 1
        while self.items[index] < self.items[(index - 1) >> 1] and index != 0:
                swap = self.items[index]
                self.items[index] = self.items[(index - 1) >> 1]
                self.items[(index - 1) >> 1] = swap
                index = (index - 1) >> 1
    def pop(self):
        minimum = self.items[0]
        self.items[0] = self.items[-1]
        del self.items[-1]
        index = 0
        min_child_index = self.get_min_child_index(index)
        while self.items != [] and self.items[index] > self.items[min_child_index]:
            swap = self.items[index]
            self.items[index] = self.items[min_child_index]
            self.items[min_child_index] = swap
            index = min_child_index
            min_child_index = self.get_min_child_index(index)
        return minimum
    def get_root(self):
        return self.items[0]
    def is_empty(self):
        if self.items == []:
            return True
        return False
    def size(self):
        return len(self.items)
    def print_heap(self):
        for item in self.items:
            print (item)

def main():
    n_k = input().split()
    items = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    heap = Heap()
    for i in range(n):
        heap.add(int(items.pop()))
    for i in range(k-1):
        heap.pop()
    print(heap.pop())
main()
