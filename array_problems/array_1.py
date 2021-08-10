'''

Given a 6 x 6 Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are  16 hourglasses in this array. An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in this array, then print the maximum hourglass sum. The array will always be 6 x 6.

arr = 

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0


 The 16 hourglass sums are as below:

 -63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

  The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2

  Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

 - int arr[6][6]: an array of integers

Returns

 - int: the maximum hourglass sum

source: hackerrank - Interview Preparation on Arrays
'''

def hourglassSum(arr):
    # Write your code here
    sum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            #Take the sum of only cells which make the hourglass pattern
            sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
            + arr[i+2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
            
    return max(sum)