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
          
class Stack:
    def __init__(self):
        self.items = LinkedList()
        self.size = 0
    # Adds value to the end of the Stack.
    # Complexity: O(1)
    def push(self, value):
        self.items.add_head(value)
        self.size += 1
    # Returns value from the end of the Stack and removes it.
    # Complexity: O(1)
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        return None
    # Returns value from the end of the Stack without removing it.
    # Complexity: O(1)
    def peek(self):
        if self.size > 0:
            return self.items.head.value
        return None
    # Returns the number of elements in the Stack.
    # Complexity: O(1)
    def size(self):
        return self.size

def main():
    n = int(input())
    names = [item for item in input().split()]
    ids = {}
    name_to_build = [item for item in input().split()][0]
    for i in range(n):
        ids[names[i]] = i
    #print(ids)
    id_to_build = ids[name_to_build]
    dependences = []
    for i in range(n):
        i_dependences_nums = [ids[item] for item in input().split()[1:]]
        dependences.append(i_dependences_nums)
    #print(dependences)
    
    status = [0] * n
    status[id_to_build] = 1
    build_order = Queue()
    dep_stack = Stack()
    dep_stack.push(id_to_build)
    no_build_error = True
    while dep_stack.size > 0 and no_build_error == True:
        current = dep_stack.peek()
        if status[current] == -1:
            dep_stack.pop()
            continue
        to_add = []
        for dep in dependences[current]:
            if status[dep] == 1:
                no_build_error = False
                break
            if status[dep] == 0:
                to_add.append(dep)
        if len(to_add) == 0:
            status[current] = -1
            dep_stack.pop()
            build_order.push(current)
            for i in range(len(status)):
                if status[i] == 1:
                    status[i] = 0
        else:
            status[current] = 1
            for item in to_add:
                dep_stack.push(item)
    
    if no_build_error == True:
        for i in range(build_order.size):
            print(names[build_order.pop()], end = " ")
        print("")
    else:
        print("BUILD ERROR")
main()
