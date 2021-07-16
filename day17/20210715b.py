'''

Important Note: ----  Use a stack plus iteration instead of recursion

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), 
ordered from the leftmost to the rightmost one;

The elements after that should be the values of the nodes at height 2 
(i.e. the children of the nodes at height 1) ordered in the same way;
Etc.

Example:

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}

The tree looks like below:

     1
   /   \
  2     4
   \   /
    3 5


Result would be: traverseTree(t) = [1, 2, 4, 3, 5]

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

root = BSTNode(1)
root.left = BSTNode(2)
root.left.right = BSTNode(3)
root.right = BSTNode(4)
root.right.left = BSTNode(5)

def traverseTree(t):
    if t is None:
        return []
    result = []
    # queue data structure is used for tracking the nodes which are to be processed
    queue = []
    queue.append(t)

    while len(queue) > 0:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return result

print(traverseTree(root))