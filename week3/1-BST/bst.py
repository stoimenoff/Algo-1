class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value) + " " + str(self.left) + " " +  str(self.right)

class BST:

    # Checks if a binary tree is a binary search tree.
    # root - node with `left`, `right` and `value` properties
    def isBST(self, root):
        return self.isValidBST(root, 0, float("inf"))
    def isValidBST(self, node, min_el, max_el):
        if node == None:
            return True
        #print(node.value, min_el, max_el)
        if node.value < min_el or node.value > max_el:
            return False
        if node.left != None:           
            new_max = max_el
            if new_max > node.value:
                new_max = node.value
            if not self.isValidBST(node.left, min_el, new_max):
                return False
        if node.right != None:
            new_min = min_el
            if new_min < node.value:
                new_min = node.value
            if not self.isValidBST(node.right, new_min, max_el):
                return False
        return True

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
    if BST().isBST(items[0]):
        print("YES")
    else:
        print("NO")
        
main()