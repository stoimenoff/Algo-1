# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:58:34 2015

@author: stoimenoff
"""
class Node:
   def __init__(self, children = {}):
       self.children = children.copy()
       self.is_last = False
       
class Dictionary:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = Node()
            node = node.children[word[i]]
        node.is_last = True
    def contains(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.is_last
        
def main():
    dictionary = Dictionary()
    result = []
    n = int(input())
    for i in range(n):
        cmd = [item for item in input().split()]
        if cmd[0] == "insert":
            dictionary.insert(cmd[1])
        elif cmd[0] == "contains":
            result.append(dictionary.contains(cmd[1]))
    for item in result:
        print(str(item).lower())
main()