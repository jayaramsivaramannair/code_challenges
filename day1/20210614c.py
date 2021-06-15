'''
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. 
The string can contain any char.

Example Input / Output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

Source: codewars.com


'''


def xo(s):

    # Approach: 1 Using for loop and incrementing the variables based on 'x' or 'o'
    '''
    count_x = 0
    count_o = 0

    for ch in s:
        if(ch.lower() == 'x'):
            count_x += 1
        elif (ch.lower() == 'o'):
            count_o += 1

    return count_x == count_o
    '''

    # Approach: 2 Using the in-built count function
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
