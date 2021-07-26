'''
Write a function which returns the intersection of two arrays. 
The intersection is a third array that contains all values contained within the first two arrays. 
For example, the intersection of [1,2,3,4,5] and [0,2,4,6,8] is [2,4]
Your function should have a complexity of O(N). 


'''

def find_intersecting_array(arr1, arr2):
    hash_table = {}
    intersection = []
    # Time Complexity of 0(N) for creating the hash table
    for i in range(len(arr1)):
        hash_table[arr1[i]] = True


    # Time Complexity of O(N) for performing lookups
    # Since both the loops are independent, the overall time complexity is O(N)
    for i in range(len(arr2)):
        if arr2[i] in hash_table:
            intersection.append(arr2[i])


    return intersection
    

print(find_intersecting_array([1,2,3,4,5], [0,2,4,6,8]))
print(find_intersecting_array([1,3,4,5], [3,4,5]))

    