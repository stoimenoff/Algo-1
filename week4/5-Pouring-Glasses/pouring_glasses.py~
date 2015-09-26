# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:25:12 2015

@author: stoimenoff
"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, next_node):
        self.next_node = next_node
    def __gt__(self, node):
        return self.value > node.value
    def __lt__(self, node):
        return self.value < node.value
    def __str__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def add_head(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.set_next(self.head)
            self.head = new_node
    def pop(self):
        if self.head != None:
            value = self.head.value
            self.head = self.head.get_next()
            if self.head == None:
                self.tail = None
            return value
    def __str__(self):
        out = ""
        current = self.head
        while current != None:
            out += (str(current.value.amount) + " ")
            current = current.next_node
        return out
class Queue:
    def __init__(self):
        self.items = LinkedList()
        self.size = 0
    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(self, value):
        self.items.add_tail(value)
        self.size += 1
    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        return None
    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek(self):
        if self.size > 0:
            return self.items.head.value
        return None
    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size(self):
        return self.size

class GlassesAmount:
    def __init__(self, amount, parent):
        self.parent = parent
        self.amount = amount
    def print_pours(self):
        pours = []
        current = self
        while current.parent != None:
            #print(current.amount, current.parent.amount)
            from_g = None
            to_g = None
            if int(current.amount/10000) > int(current.parent.amount/10000):
                to_g = 1
            elif int(current.amount/10000) < int(current.parent.amount/10000):
                from_g = 1
            if int(current.amount % 100) > int(current.parent.amount % 100):
                to_g = 3
            elif int(current.amount % 100) < int(current.parent.amount % 100):
                from_g = 3
            if from_g == None:
                from_g = 2
            if to_g == None:
                to_g = 2
            pours.append(to_g)
            pours.append(from_g)
            current = current.parent
        #print(pours, "###############")
        for i in range(len(pours) - 1, 0, -2):
            print(pours[i], pours[i-1])
class PouringGlasses:
    def __init__(self, capacities, initial):
        self.amounts = [0] * 999999
        self.initial = initial
        self.capacities = capacities
    def set_amount_targets(self, target):
        for i in range(10000):
            self.amounts[10000*target + i] = 2
            self.amounts[int(i/100)*10000 + target*100 + (i % 100)] = 2
            self.amounts[i*100 + target] = 2
    def min_num_pours(self, target):
        self.set_amount_targets(target)
        check = Queue()
        start = GlassesAmount(self.initial, None)
        self.amounts[start.amount] = 1
        check.push(start)
        check.push(GlassesAmount(-1, None))
        pours = 0
        target_pour = None
        c1 = self.capacities[0]
        c2 = self.capacities[1]
        c3 = self.capacities[2]
        while check.size > 1:
            #print(check.items)
            pour = check.pop()
            if pour.amount == -1:
                check.push(GlassesAmount(-1, None))
                pours += 1
                continue
            #print(pour.amount)
            if self.amounts[pour.amount] >= 2:
                target_pour = pour
                #print(target_pour.amount, "TARGET")
                break
            #Ugliest pour
            to_check = pour.amount
            a1 = int(to_check/10000)
            a3 = to_check % 100
            a2 = int((to_check - (a1*10000 + a3))/100)
            pour_to_push = None
            if a1 < c1:
                if a1 + a2 <= c1:
                    pour_to_push = GlassesAmount( (a1+a2)*10000 + a3 , pour)
                else:
                    pour_to_push = GlassesAmount(  c1*10000 + (a2 - c1 + a1)*100 + a3  , pour)
                if self.amounts[pour_to_push.amount] != 1:
                    self.amounts[pour_to_push.amount] += 1
                    check.push(pour_to_push)
                if a1 + a3 <= c1:
                    pour_to_push = GlassesAmount( (a1+a3)*10000 + a2*100 , pour) 
                else:
                    pour_to_push = GlassesAmount( c1*10000 + a2*100 + (a3 - c1 + a1) , pour) 
                if self.amounts[pour_to_push.amount] != 1:
                    self.amounts[pour_to_push.amount] += 1
                    check.push(pour_to_push)
            if a2 < c2:
                if a2 + a1 <= c2:
                    pour_to_push = GlassesAmount( (a1+a2)*100 + a3 , pour) 
                else:
                    pour_to_push = GlassesAmount( (a1 - c2 + a2)*10000 + c2*100 + a3, pour )
                if self.amounts[pour_to_push.amount] != 1:
                    self.amounts[pour_to_push.amount] += 1
                    check.push(pour_to_push)
                if a2 + a3 <= c2:
                    pour_to_push = GlassesAmount( a1*10000 + (a2+a3)*100, pour )
                else:
                    pour_to_push = GlassesAmount( a1*10000 + c2*100 + (a3 - c2 + a2) , pour)
                if self.amounts[pour_to_push.amount] != 1:
                    self.amounts[pour_to_push.amount] += 1
                    check.push(pour_to_push)
            if a3 < c3:
                if a3 + a1 <= c3:
                    pour_to_push = GlassesAmount( a2*100 + (a3 + a1) , pour)
                else:
                    pour_to_push = GlassesAmount( (a1 - c3 + a3)*10000 + a2*100 + c3, pour)
                if self.amounts[pour_to_push.amount] != 1:
                    self.amounts[pour_to_push.amount] += 1
                    check.push(pour_to_push)
                if a3 + a2 <= c3:
                    pour_to_push = GlassesAmount( a1*10000 + (a3 + a2) , pour)
                else:
                    pour_to_push = GlassesAmount( a1*10000 + (a2 - c3 + a3)*100 + c3 , pour)
                if self.amounts[pour_to_push.amount] != 1:
                    self.amounts[pour_to_push.amount] += 1
                    check.push(pour_to_push)
        return (pours, target_pour)
    
def main():
    capacities = [int(num) for num in input().split()]
    initial_amounts = [int(num) for num in input().split()]
    initial = int(initial_amounts[0] * 10000 + initial_amounts[1] * 100 + initial_amounts[2])
    g = int(input())
    glasses = PouringGlasses(capacities, initial)
    p = glasses.min_num_pours(g)
    if p[1] == None:
        print("IMPOSSIBLE")
    else:
        print(p[0])
        p = p[1]
        p.print_pours()
main()
