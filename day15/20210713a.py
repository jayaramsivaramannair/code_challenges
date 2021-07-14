'''
Minimum Depth of a Binary Tree

You are given a binary tree and you are asked to write a function that finds its minimum depth. 
The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. 
As a reminder, a leaf node is a node with no children.

Example: 

Given the binary tree [5,7,22,None,None,17,9],

    5
   / \
  7  22
    /  \
   17   9

The function will return minimum depth as 2

'''

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

def minimumDepthBinaryTree(root):
    if root is None:
        return 0
    #if the root has neither left nor right subtree then simply return 1
    if root.left is None and root.right is None:
        return 1
    
    #If the root has no left subtree then the calculate the depth of all nodes on the right subtree  
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    
    #if the root has no right subtree then the calculate the depth of all nodes on the left subtree  
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
    
    #If the root has both left and right subtree then calculate the depth of all nodes on either subtree
    left_depth = minimumDepthBinaryTree(root.left)
    right_depth = minimumDepthBinaryTree(root.right)
    
    #Comparison is made to check for the least number of nodes from root to leaf on either subtree
    if left_depth <= right_depth:
        return left_depth + 1
    else:
        return right_depth + 1

root = BSTNode(5)
root.insert(7)
root.insert(22)
root.insert(None)
root.insert(None)
root.insert(17)
root.insert(9)
root.print_values()

print(minimumDepthBinaryTree(root))