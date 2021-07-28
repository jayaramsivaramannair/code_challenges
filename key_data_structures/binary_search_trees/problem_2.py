'''
Write an algorithm that finds the greatest value within a binary search tree

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftNode = left
        self.rightNode = right

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

def traverse_and_print_preorder(node):
    if node is None:
        return
    print(node.value)
    traverse_and_print_preorder(node.leftNode)
    traverse_and_print_preorder(node.rightNode)

def greatest_value(node):
    if node.rightNode:
        return greatest_value(node.rightNode)
    else:
        return node.value

rootNode = TreeNode(1)
insert(5, rootNode)
insert(9, rootNode)
insert(2000, rootNode)
insert(4, rootNode)
insert(10, rootNode)
insert(600, rootNode)
insert(3, rootNode)
insert(8, rootNode)
traverse_and_print_preorder(rootNode)
print('maximum value is: ')
print(greatest_value(rootNode))