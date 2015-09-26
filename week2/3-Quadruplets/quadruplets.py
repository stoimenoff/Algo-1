# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:32:57 2015

@author: stoimenoff
"""
def find_first_occurrence(items, value):
    low = 0
    high = len(items) - 1
    index = -1
    while low <= high:
        mid = int(low + (high - low)/2)
        if items[mid] < value:
            low = mid + 1
        elif items[mid] > value:
            high = mid - 1
        else:
            index = mid
            high = mid - 1
    return index

def find_last_occurrence(items, value):
    low = 0
    high = len(items) - 1
    index = -1
    while low <= high:
        mid = int(low + (high - low)/2)
        if items[mid] < value:
            low = mid + 1
        elif items[mid] > value:
            high = mid - 1
        else:
            index = mid
            low = mid + 1
    return index
            
class Quadruplets:

    # Returns the number of quadruplets that sum to zero.
    # a - [int]
    # b - [int]
    # c - [int]
    # d - [int]
    def zero_quadruplets_count(self, a, b, c, d):
        cd_pairs = []
        for c_value in c:
            for d_value in d:
                cd_pairs.append(c_value + d_value)
        quadruplets_number = 0
        cd_pairs.sort()
        for a_value in a:
            for b_value in b:
                first_occ = find_first_occurrence(cd_pairs, - a_value - b_value)
                if first_occ != -1:  
                    last_occ = find_last_occurrence(cd_pairs, - a_value - b_value)
                    quadruplets_number += (1 + last_occ - first_occ)
        return quadruplets_number
        
def main():
    n = int(input())
    l1 = [int(num) for num in input().split(" ")]
    l2 = [int(num) for num in input().split(" ")]
    l3 = [int(num) for num in input().split(" ")]
    l4 = [int(num) for num in input().split(" ")]
    print (Quadruplets().zero_quadruplets_count(l1, l2, l3, l4))
main()