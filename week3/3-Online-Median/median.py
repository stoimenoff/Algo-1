# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:27:48 2015

@author: stoimenoff
"""
import heapq
class Heap:    
    def __init__(self):
        self.items = []
        self.size = 0
    def push(self, item):
        heapq.heappush(self.items, item)
        self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return heapq.heappop(self.items)
        return None
    def peek(self):
        if self.size > 0:
            return self.items[0]
        return None

class Median:
    def __init__(self):
        self.first_half = Heap() #max heap
        self.second_half = Heap() #min heap
        self.items = 0
#inserts the number and returns the median
    def insert(self, number):
        if self.items == 0:
            self.second_half.push(number)
        else:
            if self.second_half.peek() > number:
                self.first_half.push(-number)
            else:
                self.second_half.push(number)
            if self.first_half.size > self.second_half.size:
                self.second_half.push(- self.first_half.pop())
            if self.second_half.size - self.first_half.size == 2:
                self.first_half.push(- self.second_half.pop())
        self.items += 1
        return self.second_half.peek()

def main():
    k = int(input())
    nums = [int(num) for num in input().split()]
    median = Median()
    for i in range(k):
        print(median.insert(nums[i]))
main()
