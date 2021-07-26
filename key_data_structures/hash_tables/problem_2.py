'''

Write a function that accepts an array of strings and returns the first duplicate value it finds.
For example, if the array is ['a', 'b', 'c', 'd', 'e', 'f'], the function should return 'c',
since its duplicated within the array. You can assume that there's one pair of duplicates within the array. 
Make sure that the function has an efficiency of O(N)


'''

def first_duplicate_value(arr):
    hash_table = {}
    for i in range(len(arr)):
        # Checks if the key already exists or not
        # If the key already exists, then simply return the key
        # else add the key to the hash_table
        if arr[i] in hash_table:
            return arr[i]
        else:
            hash_table[arr[i]] = True

    

print(first_duplicate_value(['a', 'b', 'c', 'd', 'c', 'e', 'f']))