'''
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2

Example 2:

Note: You should be able to develop a solution that has O(n) time complexity.

source: codesignal.com - Lambda Challenge


Another approach to reduce space complexity is to use XOR operator as suggested by this solution:
https://www.educative.io/edpresso/find-the-integer-that-appears-once-in-an-array

'''


def csFindTheSingleNumber(nums):
    count_dict = {}

    # A Simple For Loop
    # Total Time Complexity will be O(n) + O(n)
    for i in range(len(nums)):  # 0(n)
        if nums[i] in count_dict:
            count_dict[nums[i]] += 1
        else:
            count_dict[nums[i]] = 1

    for key in count_dict.keys():  # 0(n)
        if(count_dict[key] == 1):
            return key


print(csFindTheSingleNumber([1, 1, 2, 1]))
print(csFindTheSingleNumber([1, 2, 1, 2, 1, 2, 80]))
