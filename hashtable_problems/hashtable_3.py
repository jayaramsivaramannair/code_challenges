'''

You are given an array and you need to find the number of triplets of indices(i, j, k) such that the elements
at those indices are in geometric progression for a given common ratio r and i < j < k

Example:

arr = [1,4,16,64]
r = 4

There are [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3). Return 2. 

Function Description:

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

- int arr[n]: an array of integers
- int r: the common ratio

Returns:
- int: the number of triplets

Example 1:

arr = [1,3,9,9,27,81]
r = 3

There are 6 triplets. 
The triplets satisfying are index(0,1,2), (0,1,3), (1,2,4), (1,3,4), (2,4,5) and (3,4,5)


Source: Interview Preparation on Hackerrank.com (Dictionaries and Hashmaps)
'''

arr1 = [1,4,16,64]
arr2 = [1,3,9,9,27,81]

def countTriplets(arr, r):
    # Initializing an empty dictionary to keep track of after elements in GP
    after = {}
    before = {}
    # Create a dictionary with frequency of each element in the array
    for i in range(len(arr)):
        if arr[i] in after:
            after[arr[i]] += 1
        else:
            after[arr[i]] = 1
            
    count = 0
    for i in arr:
        #get the before element
        j = i // r
        #get the after element
        k = i * r
        #reduce the count of current element in after dictionary
        after[i] -= 1
        
        # check if the before element appears in the before dictionary
        # check if the after element appears in the after dictionary
        # check if the current element is perfectly divisible
        if (j in before) and (k in after) and i % r == 0:
            count += before[j] * after[k]
        
        # Popule the before dictionary with count of the current element
        # We are simply using before dictionary to see if a particular element
        # exists inside the before dictionary or not
        if i not in before:
            before[i] = 1
        else:
            before[i] += 1
        
    return count

print(countTriplets(arr1, 4))
print(countTriplets(arr2, 3))
        