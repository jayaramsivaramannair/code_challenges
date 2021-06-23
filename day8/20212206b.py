'''

Given a pattern and a string a,
find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence
between a letter in pattern and a non-empty word in a.




Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true


Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false

Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false


Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false

source: codesignal.com (Lambda Assignment)

'''


def csWordPattern(pattern, a):
    lst = a.split(' ')
    pattern_dict = {}
    string_dict = {}

    if(len(lst) != len(pattern)):
        return False
    for i in range(len(pattern)):
        # Check whether the key in pattern_dict has the same mapped value as value at corresponding index in string
        # Also check whether the key in string_dict has the same mapped value as value at corresponding index in pattern

        if (pattern[i] in pattern_dict and pattern_dict[pattern[i]] != lst[i]) or lst[i] in string_dict and string_dict[lst[i]] != pattern[i]:
            return False
        else:
            # Setting up each character in the pattern as a key and setting the string at the same index as corresponding value
            pattern_dict[pattern[i]] = lst[i]
            # Setting up each word in the lst as a key and setting the character in pattern at the same index as corresponding value
            string_dict[lst[i]] = pattern[i]
    return True


print(csWordPattern("abba", "lambda school school lambda"))
print(csWordPattern("abba", "lambda school school coding"))
print(csWordPattern("aaaa", "lambda school school lambda"))
print(csWordPattern("abba", "lambda lambda lambda lambda"))
