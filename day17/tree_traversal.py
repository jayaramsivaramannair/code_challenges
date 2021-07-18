'''

Implementation of Methods for Traversing a Tree

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

root = BSTNode(5)
root.left = BSTNode(10)
root.right = BSTNode(25)
root.right.left = BSTNode(12)
root.right.right = BSTNode(3)

#Pre-Order Traversal using Recursive Approach
'''
Pre-Order Traversal involves visiting the root, recursively traversing the left subtree and 
then finally traversing the right subtree

'''
def pre_order_traversal (root):
    print(root.value)
    if(root.left):
        pre_order_traversal(root.left)
    if(root.right):
        pre_order_traversal(root.right)

print("Below is pre-order traversal: ")
pre_order_traversal(root)


#Post-Order Traversal using Recursive Approach
'''
Post-Order Traversal involves recursively traversing the left subtree, then 
traversing the right subtree and finally visiting the root

'''

def post_order_traversal(root):
    if(root.left):
        post_order_traversal(root.left)
    if(root.right):
        post_order_traversal(root.right)
    print(root.value)

print("Below is post-order traversal")
post_order_traversal(root)

#In-Order Traversal - Recurisve Approach

'''
In-Order Traversal involves recursively traversing the left subtree, then 
visiting the root and then finally visiting the right subtree

'''

def in_order_traversal(root):
    if(root.left):
        in_order_traversal(root.left)
    
    print(root.value)

    if(root.right):
        in_order_traversal(root.right)

print("Below is in-order traversal")
in_order_traversal(root)


# Depth First Iterative Approach
def DFT_print(root):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node.value)

        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)

print("prints the node values using depth first approach")
DFT_print(root)

# Breadth First Iterative Approach
def BFT_print(root):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        current_node = queue.pop(0)
        print(current_node.value)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

print("prints the node values using breadth first approach")
BFT_print(root)

#Searching the tree for a specific value using iteration and queue
def search_iteratively(root, target):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node.value == target:
            return True

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return False

print(search_iteratively(root, 4))
print(search_iteratively(root, 3))

# Searching for a specific value using recursion

def search_recursion(root, target):
    if root.value == target:
        return True

    if root.left is None and root.right is None:
        return False

    found_left = False
    found_right = False

    if root.left:
        found_left =  search_recursion(root.left, target)

    if root.right:
        found_right = search_recursion(root.right, target)

    return found_left or found_right

print(search_recursion(root, 4))
print(search_recursion(root, 3))

def find_paths_dft(start_node):
    arr = []
    def dft_helper(root, path):
        path.append(root.value)

        if root.left is None and root.right is None:
            arr.append(path)

        if root.left:
            dft_helper(root.left, path.copy())

        if root.right:
            dft_helper(root.right, path.copy())

    dft_helper(start_node, [])
    return arr

print('Prints all the various paths used to traverse the tree')
print(find_paths_dft(root))

