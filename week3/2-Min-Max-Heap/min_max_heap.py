class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class MinMaxHeap:

    # Checks if a binary tree is a min/max heap.
    # root - node with `left`, `right` and `value` properties
    def isMinMax(self, root):
        return self.validate(root, 0, float("inf"), 1)
    def validate(self, node, min_el, max_el, level): #level: 0 - even, 1 - odd
        if node == None:
            return True
        if node.value >= min_el and node.value <= max_el:
            if level == 1: #odd
                if self.validate(node.left, node.value, max_el, 0):
                    if self.validate(node.right, node.value, max_el, 0):
                        return True
            if level == 0: #even
                if self.validate(node.left, min_el, node.value, 1):
                    if self.validate(node.right, min_el, node.value, 1):
                        return True
        return False
        
def main():
    n = int(input())
    items = [Node(int(num)) for num in input().split()]
    for i in range(n):
        if 2 * i + 1 >= len(items):
            break
        if items[2*i + 1].value != 0:
            items[i].left = items[2 * i + 1]
        if 2 * i + 2 < len(items):
            if items[2*i + 2].value != 0:            
                items[i].right = items[2 * i + 2]
    if MinMaxHeap().isMinMax(items[0]):
        print("YES")
    else:
        print("NO")
        
main()
        

