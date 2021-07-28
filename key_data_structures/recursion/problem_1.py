'''

Following is a function in which we pass in two numbers called low and high. 
The function returns the sum of all numbers from low to high. 
For example, if low is 1, and high is 10, the function will return the sum of all numbers from 
1 to 10, which is 55. However our code is missing the base case, and will run indefinitely!
Fix the code by adding the base case. 

Erroneous Code:

def sum(low, high):
    return high + sum (low, high - 1)

'''

def sum(low, high):
    if low == high:
        return low
    return high + sum(low, high - 1)

print(sum(1, 10))