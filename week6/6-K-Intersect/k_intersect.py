# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:43:19 2015

@author: stoimenoff
"""
class KIntersect:
    def count(self, lists, n):
        nums = {}
        for i in range(n - 1):
            for item in lists[i]:
                if item in nums:
                    nums[item] += 1
                else:
                    nums[item] = 1
        result = []
        for item in lists[n-1]:
            if item in nums:
                if nums[item] == n - 1:
                  result.append(item)
        return result
def main():
    n = int(input())
    lists = []
    for i in range(n):
        list_i = [int(item) for item in input().split()][1:]
        lists.append(list_i)
    res = KIntersect().count(lists, n)
    for item in res:
        print(item)
main()