# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:24:56 2015

@author: stoimenoff
"""
class Heap:
    def __init__(self):
        self.items = []
        self.heap_size = 0
    def add(self, item):
        self.items.append(item)
        i = self.heap_size
        while (i-1)>>1 >= 0 and self.items[i] < self.items[(i-1)>>1]:
            swap = self.items[i]
            self.items[i] = self.items[(i-1)>>1]
            self.items[(i-1)>>1] = swap
            i = (i-1)>>1
        self.heap_size = self.heap_size + 1
    def min_child(self, i):
        if 2 * i + 1 < self.heap_size:
            i = 2 * i + 1
            if i + 1 < self.heap_size and self.items[i] > self.items[i+1]:
                i += 1
        return i
    def pop(self):
        min_el = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.heap_size -= 1
        i = 0
        min_ch = self.min_child(i)
        while self.heap_size > 0 and self.items[min_ch] < self.items[i]:
            swap = self.items[min_ch]
            self.items[min_ch] = self.items[i]
            self.items[i] = swap
            i = min_ch
            min_ch = self.min_child(i)
        return min_el

def main():
    n = int(input())
    items = [int(num) for num in input().split()]
    heap = Heap()
    for i in range(n):
        heap.add(items[i])
    for i in range(n):
        items[i] = heap.pop()
    for item in items:
        print(item, end = " ")
main()
