'''
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: 
a = "odd"
b = "egg"

Output:
true

Example 2:

Input:
a = "foo"
b = "bar"

Output:
false


Example 3:

Input:
a = "abca"
b = "zbxz"

Output:
true

Example 4:

Input:
a = "abc"
b = ""

Output:
false


source: codesignal.com (Lambda Challenge)

This checks for the character count of each string
'''


def csIsomorphicStrings(a, b):
    dict_1 = {}
    dict_2 = {}

    for i in range(len(a)):
        if a[i] in dict_1:
            dict_1[a[i]] += 1
        else:
            dict_1[a[i]] = 1

    for i in range(len(b)):
        if b[i] in dict_2:
            dict_2[b[i]] += 1
        else:
            dict_2[b[i]] = 1

    return sorted(dict_1.values()) == sorted(dict_2.values())


print(csIsomorphicStrings("odd", "egg"))
print(csIsomorphicStrings("foo", "bar"))
print(csIsomorphicStrings("abca", "zbxz"))
print(csIsomorphicStrings("abc", ""))
