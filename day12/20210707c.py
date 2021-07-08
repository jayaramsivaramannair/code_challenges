'''
Merging Two Linked Lists however ensuring the elements in the final list still occur in a non-decreasing order

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. 
In other words, return a singly linked list, also sorted in non-decreasing order, 
that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];

For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].

source: codewars.com (Lambda Challenge)
'''

# This creates a new node in the list


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

# Appends a new element to tail of the list


def appendToTail(head, value):
    current = head

    while(current.next is not None):
        current = current.next

    new_node = ListNode(value)
    new_node.next = current.next
    current.next = new_node

# This prints out each element of the list


def printList(head):
    nodes = []
    while(head is not None):
        nodes.append(head.value)
        head = head.next
    return nodes


a = ListNode(1)
appendToTail(a, 3)
appendToTail(a, 5)
appendToTail(a, 11)
appendToTail(a, 13)
appendToTail(a, 16)

print(printList(a))


b = ListNode(1)
appendToTail(b, 2)
appendToTail(b, 3)
appendToTail(b, 10)
appendToTail(b, 12)
appendToTail(b, 14)
appendToTail(b, 15)

print(printList(b))


def mergeTwoLinkedLists(l1, l2):
    # Checks if either of the list is empty or not
    # If either list is empty then it returns the not empty list
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Initializing the merged list with the first value
    if l1.value <= l2.value:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    # copy the reference to head in order to traverse both the lists for comparison
    current = head

    while l1 is not None or l2 is not None:
        # If the either of the lists end prematurely
        if l1 is None:
            current.next = l2
            break
        if l2 is None:
            current.next = l1
            break

        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        # Move the head in order to process the next element in the list
        current = current.next

    return head


print(printList(a))
print(printList(b))

new_head = mergeTwoLinkedLists(a, b)
print(printList(new_head))
