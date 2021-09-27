'''

Given the pointer to the head node of a linked list and an integer to insert at a certain position, 
create a new node with the given integer as its data attribute, insert this node at the desired positioin and return the head node. 

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. 
The head pointer given may be null meaning that the initial list is empty.

Example:

head refers to the first node in the list 1 -> 2 -> 3
data = 4
position = 2

Insert a node at position 2 with data = 4. The new list is 1 -> 2 -> 4 -> 3

Function Description:
Complete the function insertNodeAtPosition. 
it must return a reference to the head node of your finished list. 

insertNodeAtPositioin has the following Parameters:
- head: a SinglyLinkedListNode pointer to the head of the list
- data: an integer value to insert as data in your new node
- position: an integer position to insert the new node, zero based indexing

Returns:

- SinglyLinkedListNode pointer: a reference to the head of the revised list



source: Interview Preparation on Hackerrank.com (Linked Lists)
'''

# class for SinglyLinkedListNode


class SinglyLinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# class for the LinkedList Itself


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = SinglyLinkedListNode(data)

        # Checks if a reference to a head was passed because reference to head is needed for traversal
        if self.head:
            current = self.head

            # while current.head is pointing to another element in the list
            while current.next:
                current = current.next

            current.next = new_node
        else:
            # If no reference to a head was passed. It means that the new node itself is the head.
            self.head = new_node

    # The below will enable us to iterate over element of the linked list using for _ in _ syntax
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # The below will enable us to call the print() method directly on the linked list
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.data))
        return " -> ".join(nodes)


# Creating a new node for the linked list
a = SinglyLinkedListNode(16)

# Initializing an instance of the Linked List Class and providing a was a reference for head of the linked list
my_ll = LinkedList(a)
my_ll.append(13)
my_ll.append(7)
print("Before Insertion of the New Node")
print(my_ll)


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist
        # Return the new head
        return new_node

    current_node = llist
    # Iterate through until the desired position
    for i in range(position - 1):
        current_node = current_node.next

    new_node = SinglyLinkedListNode(data)
    new_node.next = current_node.next
    current_node.next = new_node

    # The original head remains unchanged
    return llist


insertNodeAtPosition(a, 1, 2)

print("After Insertion of the New Node")
print(my_ll)
