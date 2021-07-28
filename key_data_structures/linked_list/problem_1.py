'''
Add a method to the classic LinkedList aka Singly Linked List class that prints all the elements of the list.

'''

class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

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
            print_string += " -> " + str(current_node.data)
            current_node = current_node.next

        return print_string


new_list = LinkedList()
print(new_list.print_node_data())
new_list.append(4)
new_list.append(5)
print(new_list.print_node_data())
new_list.append(6)
new_list.append(7)
new_list.append(8)
new_list.append(9)
print(new_list.print_node_data())


    