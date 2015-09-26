# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:12:03 2015

@author: stoimenoff
"""
def main():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(item) for item in input().split()]
        matrix.append(row)
    for i in range(n - 1, -1, -1):
        for j in range(n):    
            if i == n - 1:
                if j == 0:
                    continue
                matrix[i][j] += matrix[i][j - 1]
            if j == 0:
                matrix[i][j] += matrix[i + 1][j]
            if j > 0 and i < n - 1:
                matrix[i][j] += max(matrix[i + 1][j], matrix[i][j - 1])
    print(matrix[0][n - 1])
main()