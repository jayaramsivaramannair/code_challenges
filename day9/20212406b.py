'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

source: codesignal.com (lambda challenge) # Binary Search Implementation using a while loop
'''


def csBinarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    mid = (high + low) // 2

    while low <= high:
        if(nums[mid]) == target:
            return mid

        # target lies in the right half of the split
        if(target > nums[mid]):
            low = mid + 1
        # target lies in the left half of the split
        elif (target < nums[mid]):
            high = mid - 1
        # reset the mid index
        mid = (high + low) // 2

    return -1


print(csBinarySearch([-1, 0, 3, 5, 9, 12], 9))
print(csBinarySearch([-1, 0, 3, 5, 9, 12], 2))
