'''
A left rotation operation on an array shifts each of the array's elements  1  unit to the left. 
For example, if 2 left rotations are performed on array [1,2,3,4,5] , then the array would become [3,4,5,1,2] . 
Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.


Given an array a of n integers and a number, d , perform d left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.

Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

- int a[n]: the array to rotate
- int d: the number of rotations

Returns:

- int a'[n]: the rotated array



source: hackerrank (Interview Preparation Material on Arrays)
'''

def rotLeft(a, d):
    #Recursive Approach
    '''
    def RotateByOne(arr, n):
        # Take the first element and store it in a temp variable
        temp = arr[0]
        # Iterate through all the elements except the last one
        for i in range(n - 1):
            arr[i] = arr[i + 1]
            
        # Replace the last element in the array with one stored in temp
        arr[n- 1] = temp

        # Shifts the elements in the array one position to the left by calling 
        # RotateByOne recursively
        for i in range(d):
            RotateByOne(a, n)
        
        return a
    '''
    return a[d:] + a[:d]

print(rotLeft([1,2,3,4,5], 4))