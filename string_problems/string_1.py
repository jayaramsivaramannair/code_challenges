'''

A student is taking a cryptography class and has found anagrams to be very useful. 
Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency. 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. 
The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
Determine this number.

Given two strings, a and b that may or may not be of the same length, determine the minimum number of character deletions
required to make a and b anagrams. Any characters can be deleted from either of the strings. 

Example:

a = 'cde'
b = 'dcf'

Delete e from a and f from b so that the remaining strings are cd and dc which are anagrams. 
This takes 2 character deletions. 

Function Description:

Complete the makeAnagram function in the editor below.

makeAnagram has the following parameters:
 - string a: a string
 - string b: another string

 Returns:

 - int: the minimum total characters that must be deleted. 

source: hackerrank (Interview Preparation on String Manipulation Problems)
'''

a = 'cde'
b = 'abc'

def makeAnagram(a, b):
    # Write your code here
    dict_chars = {}
    
    for char in a:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
            
    for char in b:
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            dict_chars[char] = -1
            
    diff = 0
    
    for key in dict_chars.keys():
        diff += abs(dict_chars[key])
        
    return diff

print(makeAnagram(a,b))