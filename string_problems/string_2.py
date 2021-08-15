'''

You are given a string containing characters A and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string. 

Your task is to find the minimum number of required deletions. 

Example:

s = AABAAB

Remove an A at positions 0 and 3 to make s = ABAB in 2 deletions. 

Function Description:

Complete the alternatingCharacters function in the editor below.

alternatingCharacters has the following parameter(s):
- string s: a string

Returns:
- int: the minimum number of deletions required

source: hackerrank.com (interview preparation on string manipulation problems)
'''

def alternatingCharacters(s):
    # Write your code here
    my_dict = {}
    deletions = 0
    for i in range(len(s) - 1):
        # If the adjacent character has already been seen before, then increase the count
        if s[i] == s[i + 1]:
            deletions += 1
          
    return deletions

print(alternatingCharacters('AAAA'))
print(alternatingCharacters('BBBBB'))
print(alternatingCharacters('ABABABAB'))
print(alternatingCharacters('BABABA'))
print(alternatingCharacters('AAABBB'))
