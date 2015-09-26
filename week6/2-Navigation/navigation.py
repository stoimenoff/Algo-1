# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 00:14:11 2015

@author: stoimenoff
"""
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
        self.bubble_up(len(self.items) - 1)
    def bubble_up(self, index):
        while self.items[index] < self.items[ (index-1) >> 1 ] and index != 0:
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
            print (item, end = " ")
        print("")

class Junction:
    def __init__(self, id, prev = None, distance = float("inf")):
        self.id = id
        self.prev = prev
        self.distance = distance
    def __gt__(self, junction):
        return self.distance > junction.distance
    def __lt__(self, junction):
        return self.distance < junction.distance

class Navigation:
    def __init__(self, matrix, n):
        self.matrix = matrix
        self.n = n
    def navigate(self, start, end):
        heap = Heap()
        for i in range(self.n):
            heap.add( Junction(i) )
        heap.items[start].distance = 0
        heap.bubble_up(start)
        while heap.size() > 0:
            current = heap.pop()
            if current.id == end:
                return current
            for i in range(heap.size()):
                cur_to_i = self.matrix[current.id][heap.items[i].id]
                if cur_to_i > 0:
                    if current.distance + cur_to_i < heap.items[i].distance:
                        heap.items[i].distance = current.distance + cur_to_i
                        heap.items[i].prev = current
                        heap.bubble_up(i)
        return "NO WAY"

def main():
    init = [int(item) for item in input().split()]
    n = init[0]
    m = init[1]
    start = init[2]
    end = init[3]
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(m):
        edge = [int(item) for item in input().split()]
        matrix[edge[0] - 1][edge[1] - 1] = edge[2]
        matrix[edge[1] - 1][edge[0] - 1] = edge[2]
    nav = Navigation(matrix, n)
    result = []
    ending = nav.navigate(start - 1, end - 1)
    print(ending.distance)
    while ending != None:
        result.append(ending.id + 1)
        ending = ending.prev
    for i in range(len(result)-1, -1, -1):
        print(result[i], end = " ")
    print("")
main()