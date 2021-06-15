'''
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:

add_binary(1, 1) == "10" (1 + 1 = 2 in decimal or 10 in binary)
add_binary(5, 9) == "1110" (5 + 9 = 14 in decimal or 1110 in binary)

source: codewars.com


'''


def add_binary(a, b):
    # Approach: 1 Using the in-built format function
    '''
    return format(a + b, 'b')
    '''

    # Approach: 2 Using the in-built bin function
    return bin(a + b)[2:]


print(add_binary(1, 1))
print(add_binary(5, 9))
