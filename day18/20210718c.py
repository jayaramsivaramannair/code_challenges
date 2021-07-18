'''
Implementation for inverting a binary tree

Given a binary tree, write a function that inverts the tree

Input:
     6
   /   \
  4     8
 / \   / \
2   5 7   9

Output:
     6
   /   \
  8     4
 / \   / \
9   7 5   2

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
    # Goes through the tree and prints out each value
    def node_values(self):
        nodes = []
        queue = []

        if self is None:
            return []

        queue.append(self)

        while len(queue) > 0:
            current_node = queue.pop(0)
            nodes.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return nodes


root = BSTNode(6)
root.left = BSTNode(4)
root.right = BSTNode(8)
root.left.left = BSTNode(2)
root.left.right = BSTNode(5)
root.right.left = BSTNode(7)
root.right.right = BSTNode(9)

#Using Breadth First Search to Visit Each nodes in the tree
def csBinaryTreeInvert(root):
    queue = []

    if root is None:
        return

    queue.append(root)

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node is not None:
            # swap the left and right subtrees
            current_node.left, current_node.right = current_node.right, current_node.left
            # Add the left and right subtree of the visited node to the queue
            queue.append(current_node.left)
            queue.append(current_node.right)



# Before Inversion
print(root.node_values())
csBinaryTreeInvert(root)
# After Inversion
print(root.node_values())
