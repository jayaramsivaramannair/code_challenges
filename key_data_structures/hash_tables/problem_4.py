'''
Write a function which returns the first non-duplicated character in a string. 
For example the string 'minimum' has two characters that only exist once the 'n' and the 'u' so 
your function should return the 'n' since it occurs first. The function should have an 
efficiency of O(N)

'''

def non_dupicated_character(string):
    hash_table = {}
    for i in range(len(string)):
        if string[i] in hash_table:
            hash_table[string[i]] += 1
        else:
            hash_table[string[i]] = 1

    for i in range(len(string)):
        if hash_table[string[i]] == 1:
            return string[i]

print(non_dupicated_character('minimum'))

