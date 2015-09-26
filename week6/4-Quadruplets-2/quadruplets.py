# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:55:53 2015

@author: stoimenoff
"""

class Quadruplets:
    def count_zeros(self, n, a, b, c, d):
        sum_count = {}
        for i in range(n):
            for j in range(n):
                cur_sum = a[i] + b[j]
                if cur_sum in sum_count:
                   sum_count[cur_sum] += 1
                else:
                    sum_count[cur_sum] = 1
        zeros = 0
        for i in range(n):
            for j in range(n):
                cur_sum = c[i] + d[j]
                if -cur_sum in sum_count:
                   zeros += sum_count[-cur_sum]
        return zeros                    
                    
def main():
    n = int(input())
    a = [int(item) for item in input().split()]
    b = [int(item) for item in input().split()]
    c = [int(item) for item in input().split()]
    d = [int(item) for item in input().split()]
    print(Quadruplets().count_zeros(n, a,b,c,d))
main()
        