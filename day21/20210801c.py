'''
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. 
Your function should return a reference to the head of the updated linked list.

Example:

Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N

Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


source: codesignal.com (Final Lambda Sprint Challenge)
'''

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = ListNode(data)

        if self.head:
            current = self.head

            #This will bring you to the last node in the list
            while current.next:
                current = current.next

            current.next = new_node

        else:
            self.head = new_node
    
    def print_node_data(self):
        print_string = "Elements of the list are : "
        if self.head is None:
            return "There are no items in the list!"
        
        current_node = self.head
        while current_node:
            print_string += " -> " + str(current_node.value)
            current_node = current_node.next

        return print_string

root = ListNode(3)
list = LinkedList(root)
list.append(4)
list.append(3)
list.append(2)
list.append(6)
list.append(1)
list.append(2)
list.append(6)

print(list.print_node_data())

def condense_linked_list(node):
    current_node = node
            
    node_values = {}
    
    #Checks if the current_node is not None
    while current_node:
        node_values[current_node.value] = 1
        # Checks if the value for the next node is found in the hash table or not
        if current_node.next is not None and current_node.next.value in node_values:
            node_after_deleted_node = current_node.next.next
            current_node.next = node_after_deleted_node
        # If no duplicate value exists then simply move on to the next node
        else:
            current_node = current_node.next
            
    #return the original head node
    return node

print('After removal of duplicate values: ')
new_root = condense_linked_list(root)
new_list = LinkedList(new_root)
print(new_list.print_node_data())