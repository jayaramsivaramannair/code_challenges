'''
Write a function that uses a stack to reverse a string. 
For example, "abcde" would bcome "edcba". 

'''

class Stack:
    def __init__(self):
        self.data = []

    #Removes the last item
    def remove(self):
        return self.data.pop()

    #Adds item to the end
    def add(self, value):
        self.data.append(value)

    #Reads the last item
    def read(self):
        return self.data[-1]

    def print_stack(self):
        return self.data[::-1]

    def length(self):
        return len(self.data)


def reverse_string_stack(str):
    reverse_stack = Stack()
    for i in range(len(str)):
        reverse_stack.add(str[i])
    
    reverse_string = ""
    # As long as we can read elements from a stack
    while reverse_stack.length() > 0:
        reverse_string += reverse_stack.remove()

    return reverse_string

print(reverse_string_stack('abcde'))
print(reverse_string_stack('jayaram'))
