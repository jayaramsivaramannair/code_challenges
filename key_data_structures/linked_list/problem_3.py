'''
Add a method to the classic LinkedList class that returns the last element from the list. 
Assume you don't know how many elements are in the list

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

    def return_last_element(self):
        if self.head is None:
            return "There are no items in the list"
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node.data


new_list = LinkedList()
print(new_list.return_last_element())
new_list.append(4)
new_list.append(5)
new_list.append(6)
print(new_list.return_last_element())
new_list.append(7)
new_list.append(8)
new_list.append(9)
print(new_list.print_node_data())
print(new_list.return_last_element())

