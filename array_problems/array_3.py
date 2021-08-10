'''
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

arr = [7, 1, 3, 2, 4, 5, 6]

i   arr                     swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

it took 5 swaps to sort the array

Complete the function minimumSwaps in the editor below.

minimumSwaps has the following parameter(s):

- int arr[n]: an unordered array of integers

Returns:

- int: the minimum number of swaps to sort the array


source: hackerrank(interview preparation material on arrays)
'''

def minimumSwaps(arr):
    #Assigns an index starting at 1 to each value in the list
    #Creates a dictionary using index as key 
    a = dict(enumerate(arr, 1))
    
    # creates a new dictionary by using the value as key
    b = {v:k for k, v in a.items()}
    
    # Variable used to keep a track of number of swaps
    count = 0
    
    #iterates over each key in the dictionary 'a'
    for i in a:
        #Retrieves the value in dictionary 'a'
        x = a[i]
        if x != i:
            #Retrieves the index in dictionary 'b'
            y = b[i]
            # below ensures that key and value become the same in both dictionaries
            a[y] = x
            b[x] = y
            count += 1
            
    return count

print(minimumSwaps([2,3,4,1,5]))