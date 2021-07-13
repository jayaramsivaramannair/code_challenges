# Implementation of a binary tree in python

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Inserts a new value into the tree using the root as the starting point.
    def insert(self, value):
        if (value < self.value):
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Searches for a specific value within the tree
    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            #The value does not exist
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)

    # Goes through the tree and prints out each value
    def print_values(self):
        print(self.value)
        if self.left:
            self.left.print_values()
        if self.right:
            self.right.print_values()

    # Searches for the minimum value in the tree recursively
    def find_minimum(self):
        if self.left is None:
            return self.value
        return self.left.find_minimum()

tree_root = BSTNode(12)
tree_root.insert(2)
tree_root.insert(10)
tree_root.insert(16)
tree_root.insert(4)
tree_root.insert(30)

tree_root.print_values()
print("The Minimum Value in this tree is: ", tree_root.find_minimum())

