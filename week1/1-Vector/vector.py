class Vector:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.size = 0
    # Adds value at a specific index in the Vector.
    # Complexity: O(n)
    def insert(self, index, value):
        if self.size == self.capacity:
            self.items += self.capacity * [None]
            self.capacity *= 2
        for i in range(self.size - 1, index, -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = value
        self.size += 1
    # Adds value to the end of the Vector.
    # Complexity: O(1)
    def add(self, value):
        if self.size == self.capacity:
            self.items += self.capacity * [None]
            self.capacity *= 2
        self.items[self.size] = value
        self.size += 1
    # Returns value at a specific index in the Vector
    # Complexity: O(1)
    def get(index):
        return self.items[index]
    # Removes element at the specific index
    # Complexity: O(n)
    def remove(self, index):
        for i in range(index, self.size - 1):
            self.items[i] = self.items[i + 1]
        self.items[self.size - 1] = None
        self.size -= 1
    # Removes element at the last index
    # Complexity: O(1)
    def pop(self):
        self.items[self.size - 1] = None
        self.size -= 1
    # Returns the number of elements in the Vector.
    # Complexity: O(1)
    def size(self):
        return self.size

    # Returns the total capacity of the Vector.
    # Complexity: O(1)
    def capacity(self):
        return self.capacity
