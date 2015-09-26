# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:50:32 2015

@author: stoimenoff
"""
class Node:
    
    def __init__(self, number, name, left = None, right = None, parent = None):
        self.number = number
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
    def is_left_child(self):
        if self.parent != None:
            if self.parent.left == self:
                return True
        return False
    def is_leaf(self):
        if self.left == None and self.right == None:
            return True
        return False
    def has_one_child(self):
        if self.left == None and self.right != None:
            return True
        if self.left != None and self.right == None:
            return True
        return False
    def has_two_children(self):
        if self.left != None and self.right != None:
            return True
        return False
    def replace_data(self, number, name, left, right):
        self.number = number
        self.name = name
        self.left = left
        self.right = right
        if self.left != None:
            self.left.parent = self
        if self.right != None:
            self.right.parent = self
#    def find_replacement(self):
#        replacement = None
#        if self.right != None:
#            replacement = self.right.find_min()
#        else:
#            pass
#        return replacement
    def find_min(self):
        current = self
        while current.left != None:
            current = current.left
        return current
            
class PhoneBook:
    
    def __init__(self):
        self.root = None
#inserts a new contact
    def insert(self, number, name):
        if self.root == None:
            self.root = Node(number, name)
        else:
            self.add(number, name, self.root)
    def add(self, number, name, to_node):
        if name < to_node.name:
            if to_node.left == None:
                to_node.left = Node(number, name, parent = to_node)
            else:
                self.add(number, name, to_node.left)
        elif name > to_node.name:
            if to_node.right == None:
                to_node.right = Node(number, name, parent = to_node)
            else:
                self.add(number, name, to_node.right)
        else:
            to_node.number = number
#lookup a name and print its phone number
    def lookup(self, name):
        node = self.get(name)
        if node == None:
            print("NOT FOUND!")
        else:
            print(node.number)
    def get(self, name):
        current = self.root
        while current != None:
            if current.name > name:
                current = current.left
            elif current.name < name:
                current = current.right
            else:
                return current
        return None
#list all records in an alphabetical order
    def list(self):
        self.print_tree(self.root)
    def print_tree(self, node):
        if node == None:
            return
        self.print_tree(node.left)
        print(node.name, node.number)
        self.print_tree(node.right)
#remove a record for a given name
    def remove(self, name):
        node_to_remove = self.get(name)
        if node_to_remove == None:
            return
        if node_to_remove.name == self.root.name and self.root.is_leaf():
            self.root = None
        else:
            if node_to_remove.is_leaf(): #Has no children
                if node_to_remove.is_left_child():
                    node_to_remove.parent.left = None
                else:
                    node_to_remove.parent.right = None
            elif node_to_remove.has_one_child(): #Has one child
                if node_to_remove.left != None: #Has only left child
                    if node_to_remove.is_left_child(): #Is left child
                        node_to_remove.left.parent= node_to_remove.parent
                        node_to_remove.parent.left = node_to_remove.left
                    elif node_to_remove.parent == None: #Is root
                        self.root = self.root.left
                        self.root.parent = None
                    else: #Is right child
                        node_to_remove.left.parent = node_to_remove.parent
                        node_to_remove.parent.right = node_to_remove.left
                else: #Has only right child
                    if node_to_remove.is_left_child(): #Is left child
                        node_to_remove.right.parent = node_to_remove.parent
                        node_to_remove.parent.left = node_to_remove.right
                    elif node_to_remove.parent == None: #Is root
                        self.root = self.root.right
                        self.root.parent = None
                    else: #Is right child
                        node_to_remove.right.parent = node_to_remove.parent
                        node_to_remove.parent.right = node_to_remove.right
            else: #Has two children
                replacement = node_to_remove.right.find_min()
                self.remove(replacement.name)
                node_to_remove.name = replacement.name
                node_to_remove.number = replacement.number
def main():
    phone_book = PhoneBook()
    n = int(input())
    for i in range(n):
        command = [item for item in input().split()]
        if command[0] == "insert":
            phone_book.insert(int(command[1]), command[2])
        elif command[0] == "lookup":
            phone_book.lookup(command[1])
        elif command[0] == "remove":
            phone_book.remove(command[1])
        elif command[0] == "list":
            phone_book.list()
main()
