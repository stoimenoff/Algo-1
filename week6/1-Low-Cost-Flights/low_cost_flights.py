# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:43:39 2015

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

class Airport:
    def __init__(self, id):
        self.id = id
        self.distance = float("inf")
    def __gt__(self, airport):
        return self.distance > airport.distance
    def __lt__(self, airport):
        return self.distance < airport.distance
    def __str__(self):
        return str(self.id) + " " + str(self.distance)
class AirportMap:
    def __init__(self, matrix, n):
        self.n = n
        self.matrix = matrix
        self.lowest = []
    def calculate_all_lowest_distances(self):
        for i in range(self.n):
            self.lowest.append(self.calculate_lowest_distances(i))
    def calculate_lowest_distances(self, airport_id):
        distances = [float("inf")] * self.n
        heap = Heap()
        for i in range(self.n):
            heap.add( Airport(i) )
        heap.items[airport_id].distance = 0
        heap.bubble_up(airport_id)
        while heap.size() > 0:
            current_airport = heap.pop()
            #heap.print_heap()
            distances[current_airport.id] = current_airport.distance
            for i in range(heap.size()):
                cur_to_i = self.matrix[current_airport.id][heap.items[i].id]
                if cur_to_i > 0:
                    if current_airport.distance + cur_to_i < heap.items[i].distance:
                        heap.items[i].distance = current_airport.distance + cur_to_i
                        heap.bubble_up(i)
        return distances
        
def main():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(item) for item in input().split()]
        matrix.append(row)
    a_map = AirportMap(matrix, n)
#    print( a_map.calculate_lowest_distances(3) )
    a_map.calculate_all_lowest_distances()
    m = int(input())
    result = []
    for i in range(m):
        i_j = [int(num) for num in input().split()]
        result.append( a_map.lowest[i_j[0]][i_j[1]] )
    for item in result:
        if item != float("inf"):
            print(item)
        else:
            print("NO WAY")
main()
    