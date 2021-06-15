"""

Your goal in this kata is to implement a difference function, which subtracts one list from the another and returns
the result. 

It should remove all values from list a, which are present in list b keeping their order. 

Example # 1
array_diff([1,2], [1]) == [2]

If a value is present in b, all of its occurences must be removed from the other:

Example # 2
array_diff([1,2,2,2,3], [2]) == [1,3]

Challenge Source: codewars.com
"""


def array_diff(lst1, lst2):
    # list comprehension can be used in this case
    # The usual approach would be to make a loop through each element and then make the comparison
    # However list comprehension would be more concise
    return [x for x in lst1 if x not in lst2]


print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2, 2, 3], [2]))
