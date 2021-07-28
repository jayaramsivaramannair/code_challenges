'''
Add a method to the DoublyLinkedList class that prints all the elements of the list in reverse order. 


'''

class ListNode:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # Perfect for adding to the end of a queue
    def insert_at_tail(self, value):
        new_node = ListNode(value)

        # If there are no elements yet in the linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the linked list already has one node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Perfect for removing from the front of queue
    def remove_from_head(self):
        if self.head is None:
            return
        removed_node = self.head
        self.head = self.head.next
        return removed_node.data

    def normal_print(self):
        print_string = "Elements of the list are : "
        if self.head is None:
            return "There are no items in the list!"
        
        current_node = self.head
        while current_node:
            print_string += " -> " + str(current_node.data)
            current_node = current_node.next

        return print_string

    def reverse_print(self):
        print_string = "Items of the list in reverse order are: "

        if self.tail is None:
            return "There are no items to be printed in reverse!"
        
        current_node = self.tail

        while current_node:
            print_string += " -> " + str(current_node.data)
            current_node = current_node.previous
        return print_string


new_list = DoublyLinkedList()
print(new_list.normal_print())
print(new_list.reverse_print())

new_list.insert_at_tail(10)
new_list.insert_at_tail(11)
new_list.insert_at_tail(12)
print(new_list.normal_print())

new_list.insert_at_tail(13)
new_list.insert_at_tail(14)
new_list.insert_at_tail(15)
print(new_list.normal_print())
print(new_list.reverse_print())
