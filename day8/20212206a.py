'''
Given an array of strings strs, 
write a function that can group the anagrams. 
The groups should be ordered such that the larger groups come first, 
with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input:
strs = ["apt","pat","ear","tap","are","arm"]

Output:
[["apt","pat","tap"],["ear","are"],["arm"]]


Example 2:

Input:
strs = [""]

Output:
[[""]]


Example 3:

Input:
strs = ["a"]

Output:
[["a"]]

source: codesignal.com (Lambda Challenge)

'''


def csGroupAnagrams(strs):
    anagram_dict = {}

    for i in range(len(strs)):
        # sorted will separate the string into separate characters so we use join method to convert them back into a string
        sorted_word = "".join(sorted(strs[i]))
        # Checks for a key by the sorted_word
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(strs[i])
        else:
            anagram_dict[sorted_word] = [strs[i]]

    return sorted(anagram_dict.values(), key=len, reverse=True)


print(csGroupAnagrams(["apt", "pat", "ear", "tap", "are", "arm"]))
print(csGroupAnagrams([""]))
print(csGroupAnagrams(["a"]))
