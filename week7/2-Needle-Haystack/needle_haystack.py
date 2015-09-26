# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:07:04 2015

@author: stoimenoff
"""
def hash(string):
    hash = 0 
    for i in range(len(string)):
        hash = hash*27 + (ord(string[i]) - 97)
    return hash
def main():
    haystack = input()
    needle = input()
    base = 27**(len(needle) - 1)
    target_hash = hash(needle)
    current_hash = hash(haystack[0:len(needle)])
    if current_hash == target_hash:
        print(0)
    for i in range(len(needle), len(haystack)):
        current_hash -= (ord(haystack[i - len(needle)]) - 97)*base
        current_hash = current_hash*27 + (ord(haystack[i]) - 97)
        if current_hash == target_hash:
            print(i + 1 - len(needle))
main()