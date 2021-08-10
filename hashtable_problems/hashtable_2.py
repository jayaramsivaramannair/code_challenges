'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example:

string1 = 'and'
string2 = 'art'

These share the common substring a.

Example 2:

string1 = 'be'
string2 = 'cat'

These do not share a substring

Function Description:

Complete the function twoStrings in the editor below:

twoStrings has the following parameters:

- String1: a string
- String2: another string

Returns:

string: either YES or NO


source: hackerrank (Interview Preparation on hashtables)
'''


def twoStrings(s1, s2):
    # Write your code here
    string_one_dict = {}
    
    for i in range(len(s1)):
        if s1[i] in string_one_dict:
            string_one_dict[s1[i]] += 1
        else:
            string_one_dict[s1[i]] = 1
            
    for i in range(len(s2)):
        # As soon as a common character is found, then return 'YES'
        if s2[i] in string_one_dict:
            return 'YES'
    
    return 'NO'