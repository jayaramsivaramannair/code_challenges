'''
Add a method to the classic LinkedList class that reverses the list. 
That is, if the original list is A -> B -> C, all of the list's links should change so that 
C -> B -> A. 

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

    def list_reversal(self):
        if self.head is None:
            return 'There are no items in the list!'

        #Once we finish iterating through the list, the next node after the last node will be empty
        previous_node = None
        current_node = self.head

        while current_node:
            # This variable will help us move through the list
            next_node = current_node.next

            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        #Once we break out of the loop, current_node will be None and previous_node will become the last_node in the list
        self.head = previous_node



new_list = LinkedList()
new_list.append(4)
new_list.append(5)
new_list.append(6)
new_list.append(7)
new_list.append(8)
new_list.append(9)
print(new_list.print_node_data())
new_list.list_reversal()
print(new_list.print_node_data())