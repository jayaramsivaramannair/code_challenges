'''
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [1,2,3,4,5,6,7] might become [4,5,6,7,1,2,3]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,1,2,3,4,5], target = 1
Output: 2

Example 2:
Input: nums = [6,7,1,2,3,4,5], target = 3
Output: 4

Example 3:
Input: nums = [1], target = 2
Output: -1

Your solution should have better than O(n) time complexity over the number of items in the list. There is an O(log n) solution. There is also an O(1) solution.


source: codesignal.com (Lambda Challenge) # Using a modified binary search to first determine if the left half or the right half is sorted

'''


def csSearchRotatedSortedArray(nums, target):
    low = 0
    high = len(nums) - 1

    while (low < high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            return mid

        # if the left half is sorted
        if(nums[low] <= nums[mid]):
            if target >= nums[low] and target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        # else if the right half is sorted
        else:
            if target <= nums[high] and target > nums[mid]:
                low = mid + 1
            else:
                high = mid

    return -1


print(csSearchRotatedSortedArray([6, 7, 1, 2, 3, 4, 5], 1))
print(csSearchRotatedSortedArray([6, 7, 1, 2, 3, 4, 5], 3))
print(csSearchRotatedSortedArray([1], 2))
