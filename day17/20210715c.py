'''

Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. 
The strings should have the following format:
"root->node1->node2->...->noden", 
representing the path from root to noden, where root is the value stored in the root 
and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively 
(noden representing the leaf).

Example:

Given the following tree;

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}

The result would be - treePaths(t) = ["5->2->10", "5->2->4", "5->-3"]

The above tree looks like the following:

  5
   / \
  2  -3
 / \
10  4

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
root.left = BSTNode(2)
root.left.left = BSTNode(10)
root.left.right = BSTNode(4)
root.right = BSTNode(-3)

def treePaths(t):
    arr = []
    def dft_helper(root, path):
        if root is None:
            return []
        path.append(root.value)

        #This will occur only when we have reached the left
        string_representation = ""
        if root.left is None and root.right is None:
            for i in range(len(path) - 1):
                string_representation += str(path[i])
                string_representation += "->"
            
            string_representation += str(path[len(path) - 1])
            arr.append(string_representation)

        if root.left:
            dft_helper(root.left, path.copy())

        if root.right:
            dft_helper(root.right, path.copy())

    dft_helper(t, [])
    return arr

print(treePaths(root))