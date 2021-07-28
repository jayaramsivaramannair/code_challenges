'''
Binary Search Tree Implementation in Python
Print the values for each node in the tree using inorder, preorder and postorder traversal
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftNode = left
        self.rightNode = right

# This function will help us search for a target value within the tree
def search(searchValue, node):
    if node is None or node.value == searchValue:
        return node

    elif searchValue < node.value:
        return search(searchValue, node.leftNode)

    else:
        return search(searchValue, node.rightNode)

# This function will help us insert a new value into the tree
def insert(value, node):
    if value < node.value:
        if node.leftNode is None:
            node.leftNode = TreeNode(value)
        else:
            insert(value, node.leftNode)
    elif value > node.value:
        if node.rightNode is None:
            node.rightNode = TreeNode(value)
        else:
            insert(value, node.rightNode)

# This function prints the node values using inorder traversal
def traverse_and_print_inorder(node):
    if node is None:
        return
    traverse_and_print_inorder(node.leftNode)
    print(node.value)
    traverse_and_print_inorder(node.rightNode)

#This function prints the node values using preorder traversal
def traverse_and_print_preorder(node):
    if node is None:
        return
    print(node.value)
    traverse_and_print_preorder(node.leftNode)
    traverse_and_print_preorder(node.rightNode)

#This function prints the node values using postorder traversal
def traverse_and_print_postorder(node):
    if node is None:
        return
    traverse_and_print_postorder(node.leftNode)
    traverse_and_print_postorder(node.rightNode) 
    print(node.value)


rootNode = TreeNode('Moby Dick')
insert('Great Expectations', rootNode)
insert('Robinson Crusoe', rootNode)
insert('Alice in Wonderland', rootNode)
insert('Lord of the Flies', rootNode)
insert('Pride and Prejudice', rootNode)
insert('The Odyssey', rootNode)

print("Order for inorder traversal: ")
traverse_and_print_inorder(rootNode)
print('---------------------------')

print("Order for preorder traversal: ")
traverse_and_print_preorder(rootNode)
print('---------------------------')

print("Order for postorder traversal: ")
traverse_and_print_postorder(rootNode)
print('---------------------------')
