'''
The rgb function is incomplete. 
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

Examples: 

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

source: codewars.com
'''


def rgb(r, g, b):
    # Approach 1 Uses Conditional Statements to check if greater than 255 or less than zero.
    # Check if any of the numbers are greater than 255
    '''
    if (r > 255):
        r = 255
    elif (g > 255):
        g = 255
    elif (b > 255):
        b = 255

    # Check if the numbers are less than 0
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0

    # Pad the resultant string with 0 to ensure that they are atleast of length 2
    r = hex(r)[2:].zfill(2)
    g = hex(g)[2:].zfill(2)
    b = hex(b)[2:].zfill(2)

    return (r + g + b).upper()  # convert to upper case the entire string

    '''

    # Approach : 2 using the max max function to check if they are within a certain range
    r = min(255, max(r, 0))
    g = min(255, max(g, 0))
    b = min(255, max(b, 0))

    # Pad the resultant string with 0 to ensure that they are atleast of length 2
    r = hex(r)[2:].zfill(2)
    g = hex(g)[2:].zfill(2)
    b = hex(b)[2:].zfill(2)

    return (r + g + b).upper()  # convert to upper case the entire string


print(rgb(255, 255, 255))
print(rgb(255, 255, 300))
print(rgb(0, 0, 0))
print(rgb(148, 0, 211))
print(rgb(1, 2, 3))
print(rgb(-42, -28, 229))
print(rgb(218, 13, 274))
