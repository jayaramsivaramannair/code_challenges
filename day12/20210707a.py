'''
First Implementation of a Simple Singly Linked List in Python
'''

# Class for LinkedListNode - This represents each element in the linked list data structure


class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# class for the LinkedList Itself


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = LinkedListNode(data)

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


# Creating a new node for the linked list
a = LinkedListNode(1)

# Initializing an instance of the Linked List Class and providing a was a reference for head of the linked list
my_ll = LinkedList(a)
my_ll.append(2)
my_ll.append(3)

# Below will print the value of a which is '1' because it is the head in this Linked List Structure
print(my_ll.head.data)

# This will print 2 as my_ll.head.next is pointing to the next element in the list which is '2'
print(my_ll.head.next.data)

# This will print 3
print(my_ll.head.next.next.data)
