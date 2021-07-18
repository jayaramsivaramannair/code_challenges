'''
Determine whether the height of the tree is balanced or not

You are given a binary tree and 
you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node 
differ in height by a maximum of 1.

Example 1:

Given the following tree [5,10,25,None,None,12,3]:

 5
   / \
 10  25
    /  \
   12   3

The above tree is balanced and thus will return 'True' because the difference between depth of right and left subtree
is not greater than 1

Example 2:

Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8

 The above tree is not balanced and thus the result will be 'False'

source: codesignal.com (Lambda Challenge)
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


root = BSTNode(5)
root.left = BSTNode(10)
root.right = BSTNode(25)
root.right.left = BSTNode(12)
root.right.right = BSTNode(3)



def checkBalanced(node):
    if node is None:
        return (0, True)
    
    # Values returned in a tuple are destructured
    left_depth, left_balance = checkBalanced(node.left)
    right_depth, right_balance = checkBalanced(node.right)
    
    # Returns a tuple consisting of an integer and a boolean value
    # integer contained within this tuple represents depth of the tree
    return (max(left_depth, right_depth) + 1, left_balance and right_balance and abs(left_depth - right_depth) <= 1)

def balancedBinaryTree(root):
    return checkBalanced(root)[-1]

print(balancedBinaryTree(root))