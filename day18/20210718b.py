'''
A function returning the sum of values of all the nodes with a value between lower and upper bounds. 

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32


Example 2:

Input:
root = [10,5,15,3,7,13,18,1,null,6]
lower = 6
upper = 10

           10
          /  \
       5       15
     / \     /   \ 
    3   7  13   18
   /   /
  1   6

Output:
23

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
    def print_values(self):
        print(self.value)
        if self.left:
            self.left.print_values()
        if self.right:
            self.right.print_values()

# Performing a breadth first search to check if each node value is between the bounds
def csBSTRangeSum(root, lower, upper):
    sum = 0

    if root is None:
        return sum

    queue = []
    queue.append(root)

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.value >= lower and current_node.value <= upper:
            print(current_node.value)
            sum = sum + current_node.value

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return sum


root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)

root.right.right = BSTNode(18)

print(csBSTRangeSum(root, 7, 15))


