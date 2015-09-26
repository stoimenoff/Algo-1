# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:59:20 2015

@author: stoimenoff
"""
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    def __lt__(self, item):
        return self.weight < item.weight
    def __gt__(self, item):
        return self.weight > item.weight
    def __str__(self):
        return str(self.weight) + " " + str(self.value)

class Robbery:
    def get_max_value(self, n, capacity, items):
        matrix = [[0 for i in range(capacity + 1)] for i in range(n + 1)]
        max_value = 0
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                take = 0
                if j - items[i-1].weight >= 0:
                    take = items[i-1].value + matrix[i-1][j - items[i-1].weight]
                matrix[i][j] = max(take, matrix[i-1][j])
                if matrix[i][j] > max_value:
                    max_value = matrix[i][j]          
        return max_value

def main():
    n_w = [int(item) for item in input().split()]
    n = n_w[0]
    w = n_w[1]
    items = []
    for i in range(n):
        item = [int(item) for item in input().split()]
        item = Item(item[1], item[0])
        items.append(item)
    items.sort()
    print( Robbery().get_max_value(n, w, items) )
main()    