# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:09:59 2015

@author: stoimenoff
"""
class BinaryIndexedMinTree:
    def __init__(self, items):
        self.n = 2**((len(items)-1).bit_length())
        self.size = 2*self.n - 1
        self.items = [0] * self.size
        for i in range(len(items)):
            self.items[self.n - 1 + i] = items[i]
        start = self.n - 2 + len(items)
        if start % 2 == 1:
            start += 1
        for i in range(start, 0, -2):
            if self.items[i] < self.items[i - 1]:
                self.items[(i - 1) >> 1] = self.items[i]
            else:
                self.items[(i - 1) >> 1] = self.items[i - 1]
    def get_min_child(self, tree_index):
        if 2*tree_index + 1 < len(self.items):
            tree_index = 2*tree_index + 1
            if tree_index + 1 < len(self.items):
                if self.items[tree_index + 1] < self.items[tree_index]:
                    tree_index += 1
        return tree_index
    def change(self, index, value):
        index_in_tree = self.n - 1 + index
        self.items[index_in_tree] = value
        i = (index_in_tree - 1) >> 1
        while i >= 0:
            min_ch = self.get_min_child(i)
            if self.items[i] == self.items[min_ch]:
                break
            self.items[i] = self.items[min_ch]
            if i == 0:
                break
            i = (i - 1) >> 1
    def query_range(self, start_index, end_index):
        current1 = self.n - 1 + start_index
        current2 = self.n - 1 + end_index
        if current1 == current2:
            return self.items[current1]
        min_el = self.items[current1]
        while current1 < current2:
            if current1 & 1 == 0: # If right child
                if min_el > self.items[current1]:
                    min_el = self.items[current1]
                current1 = current1 + 1
            
            if current2 & 1 == 1: # If left child
                if min_el > self.items[current2]:
                    min_el = self.items[current2]
                current2 = current2 - 1
            current2 = (current2 - 1) >> 1
            current1 = (current1 - 1) >> 1
        if min_el > self.items[2*current2 + 2]:
            min_el = self.items[2*current2 + 2]
        if min_el > self.items[2*current1 + 1]:
            min_el = self.items[2*current1 + 1]
        return min_el
def main():
    n_k = [int(num) for num in input().split()]
    n = n_k[0]
    k = n_k[1]
    items = [int(num) for num in input().split()]
    tree = BinaryIndexedMinTree(items)
    result = []
    for i in range(k):
        command = [item for item in input().split()]
        if command[0] == "min":
            result.append(tree.query_range(int(command[1]), int(command[2])))
            #print (result[-1])
        elif command[0] == "set":
            tree.change(int(command[1]), int(command[2]))
            #print (tree.items)
    for item in result:
        print (item)
main()
