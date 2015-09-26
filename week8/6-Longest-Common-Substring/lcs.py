# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:03:28 2015

@author: stoimenoff
"""
class LCS:
    def calculate_lcs(self, string1, string2):
        n = len(string1)
        m = len(string2)
        max_i = None
        max_j = None
        matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if string1[j-1] == string2[i-1]:
                    matrix[i][j] += (matrix[i-1][j-1] + 1)
                    if max_i == None:
                        max_i = i
                        max_j = j
                    elif matrix[max_i][max_j] < matrix[i][j]:
                        max_i = i
                        max_j = j
        lcs = ""
        #for row in matrix:
        #    print(row)
        while max_i != None and matrix[max_i][max_j] > 0:
            lcs += string1[max_j - 1]
            max_i -= 1
            max_j -= 1
        return lcs[::-1]

def main():
    s1 = input()
    s2 = input()
    print( LCS().calculate_lcs(s1, s2) )
main()