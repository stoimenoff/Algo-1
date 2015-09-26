# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:43:04 2015

@author: stoimenoff
"""
class LIS:
    def get_lis_of(self, sequence):
        longest_i = 0
        longest_l = 1
        longest_ending_at = [[sequence[0]]]
        for i in range(1, len(sequence)):
            max_prev = []
            for j in range(0, i):
                if sequence[j] < sequence[i]:
                    if len(max_prev) < len(longest_ending_at[j]):
                        max_prev = longest_ending_at[j].copy()
            longest_ending_at.append(max_prev)
            longest_ending_at[i].append(sequence[i])
            if len(longest_ending_at[i]) > longest_l:
                longest_l = len(longest_ending_at[i])
                longest_i = i
        return longest_ending_at[longest_i]
def main():
    n = int(input())
    sequence = [int(item) for item in input().split()]
    lis = LIS().get_lis_of(sequence)
    print(len(lis))
    for item in lis:
        print(item, end = " ")
    print("")
main()