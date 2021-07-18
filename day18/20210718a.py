'''

Implementation of a reversed linked list in Python

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].

source: codesignal.com (sprint challenge)
'''

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

# Call this function on head of the list
def node_values(head):
    nodes = []
    while head is not None:
        nodes.append(head.data)
        head = head.next
    return nodes


# Creating a new node for the linked list
a = LinkedListNode(1)

# Initializing an instance of the Linked List Class and providing a was a reference for head of the linked list
my_ll = LinkedList(a)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)

def reverseLinkedList(l):
    #checks that the list is not empty
    if l is not None:
        previous = None
        current = l
        following = current.next
    else:
        return
    
    while current is not None:
        current.next = previous
        previous = current
        current = following
        
        if following is not None:
            following = following.next
            
    l = previous
    return l

# Print all the node values in the list
print("Original List:")
print(node_values(a))
# This will reverse the linked list
new_head = reverseLinkedList(a)

#Prints all the node values in reverse order as the list has been reversed
print("Reversed List:")
print(node_values(new_head))