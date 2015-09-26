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

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
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
            self.tail.next_node = new_node
            self.tail = new_node
    def add_head(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next_node = self.head
            self.head = new_node
    def pop(self):
        if self.head != None:
            value = self.head.value
            self.head = self.head.next_node
            if self.head == None:
                self.tail = None
            return value
    def peek(self):
        return self.head
    def __str__(self):
        to_str = ""
        node = self.head
        while node != None:
            to_str += str(node.value)
            to_str += " "
            node = node.next_node
        return to_str

class KLists:

    # Merge K sorted lists.
    # lists - [LinkedList]
    def merge(self, lists):
        merged = LinkedList()
        min_heap = Heap()  
        for i in range(len(lists)):
            min_heap.add(lists[i].peek())
        while not min_heap.is_empty():
            minimum = min_heap.pop()
            merged.add_tail(minimum)
            next_node = minimum.get_next()
            if next_node != None:
                min_heap.add(next_node)
        return merged
        
def main():
    k = int(input())
    lists = []
    for i in range(k):
        row = input().split()
        linked_list = LinkedList()
        for i in range(len(row)-1):
            linked_list.add_tail(int(row[i]))
        lists.append(linked_list)
    print (KLists().merge(lists))
            
        
main()
        