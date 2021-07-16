'''
In-Order Traversal of a Binary Tree

You are given a binary tree. Write a function that returns the binary tree's node 
values using an in-order traversal.

Example:

Input: [2,None,3,4]

 2
    \
     3
    /
   4

Result: [2,4,3]

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

root = BSTNode(5)
root.left = BSTNode(10)
root.right = BSTNode(25)
root.right.left = BSTNode(12)
root.right.right = BSTNode(3)

def binaryTreeInOrderTraversal(root):
    result = []
    
    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)
        res.append(root.value)
        helper(root.right, res)

    helper(root, result)
    return result

print(binaryTreeInOrderTraversal(root))