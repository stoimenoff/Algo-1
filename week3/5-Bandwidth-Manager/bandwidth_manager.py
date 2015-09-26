# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:21:14 2015

@author: stoimenoff
"""
protocols = {"ICMP" : 1, "UDP" : 2, "RTM" : 3, "IGMP" : 4, "DNS" : 5, "TCP" : 6}
class Protocol:
    def __init__(self, protocol, payload, number_of_addition):
        self.priority = protocols[protocol]
        self.payload = payload
        self.time = number_of_addition
    def __gt__(self, prot):
        if self.priority == prot.priority:
            return self.time > prot.time
        return self.priority > prot.priority
    def __ge__(self, prot):
        if self.priority == prot.priority:
            return self.time >= prot.time
        return self.priority >= prot.priority        
    def __lt__(self, prot):
        if self.priority == prot.priority:
            return self.time < prot.time
        return self.priority < prot.priority
    def __le__(self, prot):
        if self.priority == prot.priority:
            return self.time <= prot.time
        return self.priority <= prot.priority
    def __str__(self):
        return str(self.payload)
        
class Heap:
    def __init__(self):
        self.items = []
    def get_min_child_index(self, index):
        min_child_index = index #return same value as input = no child
        if 2*index + 1 < len(self.items):
            min_child_index = 2*index + 1
        if 2*index + 2 < len(self.items):
            if self.items[2*index + 2] < self.items[min_child_index]:
                min_child_index = 2*index + 2
        return min_child_index
    def add(self, item):
        self.items.append(item)
        index = len(self.items) - 1
        while self.items[index] < self.items[(index - 1) >> 1] and index != 0:
                swap = self.items[index]
                self.items[index] = self.items[(index - 1) >> 1]
                self.items[(index - 1) >> 1] = swap
                index = (index - 1) >> 1
    def pop(self):
        minimum = self.items[0]
        self.items[0] = self.items[-1]
        del self.items[-1]
        index = 0
        min_child_index = self.get_min_child_index(index)
        while self.items != [] and self.items[index] > self.items[min_child_index]:
            swap = self.items[index]
            self.items[index] = self.items[min_child_index]
            self.items[min_child_index] = swap
            index = min_child_index
            min_child_index = self.get_min_child_index(index)
        return minimum
    def get_root(self):
        return self.items[0]
    def is_empty(self):
        if self.items == []:
            return True
        return False
    def size(self):
        return len(self.items)
    def print_heap(self):
        for item in self.items:
            print (item)
            
class BandwidthManager:
    def __init__(self):
        self.heap = Heap()
        self.additions = 0
#receives a packet with specified protocol and payload
    def rcv(self, protocol, payload):
        self.heap.add(Protocol(protocol, payload, self.additions))
        self.additions += 1
#returns the payload of the packet which should be sent
    def send(self):
        if not self.heap.is_empty():
            to_send = self.heap.pop()
            return to_send
        return "Nothing to send!"

def main():
    n = int(input())
    bm = BandwidthManager()
    for i in range(n):
        recieve = [item for item in input().split()]
        if recieve[0] == 'send':
            sent = bm.send()
            print(sent)
        elif recieve[0] == "rcv": 
            bm.rcv(recieve[1], recieve[2])
main()
