'''

Write a function that takes an integer as input, 
and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: 

The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case

Source: codewars.com
'''


def count_bits(n):
    # Approach : 1 Uses In-built format function to convert integer to binary representation
    '''
    return format(n, 'b').count('1')
    '''

    # Approach: 2 Uses in-built bin() function which returns a string consisting of binary representation
    return bin(n).count('1')


print(count_bits(1234))
