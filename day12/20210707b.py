'''
Inserting a Value into an Already Sorted Linked List

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. 
Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: 
in real data you will be given a head node l of the linked list

Example: 

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];

For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];

For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].


source: codesignal.com (Lambda Challenge)
'''


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def insertValueIntoSortedLinkedList(l, value):
    current = l

    # If the linked list is currently empty then the new_node will be the first element in the list
    if current is None:
        new_node = ListNode(value)
        return new_node

    # if the new value is the lowest value and hence becomes the first element in the list
    if value < current.value:
        new_node = ListNode(value)
        new_node.next = current
        # We return the new_node because this has become the new head for the linked list
        return new_node

    # This will loop will be run in all other cases other than above
    while current.next is not None and current.next.value < value:
        current = current.next

    new_node = ListNode(value)
    new_node.next = current.next
    current.next = new_node

    return l


def listTraversal(head):
    while head is not None:
        print(head.value)
        head = head.next
    return


ll = ListNode(1)
insertValueIntoSortedLinkedList(ll, 20)
insertValueIntoSortedLinkedList(ll, 3)
insertValueIntoSortedLinkedList(ll, 4)
insertValueIntoSortedLinkedList(ll, 10)
insertValueIntoSortedLinkedList(ll, 5)
insertValueIntoSortedLinkedList(ll, 6)

head = ll

listTraversal(head)
