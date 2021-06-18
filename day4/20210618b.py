'''
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

source: codewars.com
'''


def is_pangram(s):
    # Approach : 1 Using a for loop to check each character and add them to the dictionary as a key if unique
    # Before returning check if the count == 26
    my_alpha_dict = {}

    for i in range(len(s)):
        if s[i].isalpha():
            search_key = s[i].lower()
            if search_key not in my_alpha_dict:
                my_alpha_dict[search_key] = 1

    return len(my_alpha_dict.keys()) == 26

    # Approach: 2 Uses the inbuilt set method to create a list of unique characters in the string
    '''
    return set(string.lowercase) <= set(s.lower()) 

    The above makes a set of all letters in the english alphabet and checks if it is a subset of the set comprising characters in the provided string
    
    '''


print(is_pangram('The quick brown fox  over the lazy dog'))
