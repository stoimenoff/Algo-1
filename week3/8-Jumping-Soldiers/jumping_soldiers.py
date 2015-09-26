# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:35:21 2015

@author: stoimenoff
"""
items = [0] * 10001
def add(index, n):
    while index <= n:
        items[index] += 1
        index += (index & (-index))
def query(index, n):
    sum = 0
    while index > 0:
        sum += items[index]
        index -= (index & (-index))
    return sum
def newrow(n):
    for i in range(1, n + 1):
        items[i] = 0
def main():
    n_k = [int(item) for item in input().split()]
    n = n_k[0]
    k = n_k[1]
    max_s = -float("inf")
    result = None
    for i in range(1, k+1):
        newrow(n)
        row = [int(num) for num in input().split()]
        s = 0
        for j in range(1, n + 1):
            s += (j - 1 - query(row[j - 1], n))
            add(row[j - 1], n)
        if s > max_s:
            max_s = s
            result = i
    print(result)
main()
