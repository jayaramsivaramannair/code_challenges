'''

Write a function that accepts a string that contains all the letters of the alphabet
except one and returns the missing letter. 
For example, the string "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter 'f'. The function should have a time complexity of O(N)

'''



def missing_letters(str):
    # Creates a hash_table with each letter of the string as key
    hash_table = {}
    for i in range(len(str)):
        hash_table[str[i]] = True

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(alphabet)):
        # If the key is not present in the hash_table then it is the missing character
        if alphabet[i] not in hash_table:
            return alphabet[i]

print(missing_letters('the quick brown fox jumps over a fazy dog'))
    