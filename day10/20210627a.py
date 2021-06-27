'''
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

After changing the first letter 't' to 'a' in the word1, the words become anagrams.

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), 
we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, 
and here 't' is changed to 'p'.

For word1 = "aba" and word2 = "bab", the output should be
checkBlanagrams(word1, word2) = true.

You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", 
which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and 
obtain "aab", which is an anagram of word1 = "aba".

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made 
(the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.


source: codesignal.com (Lambda Sprint Challenge)
'''


def checkBlanagrams(word1, word2):
    char_count = {}
    count_odd = 0

    # Go through word1 and add the character count to the dictionary
    for i in range(len(word1)):  # 0(n)
        if word1[i] in char_count:
            char_count[word1[i]] += 1
        else:
            char_count[word1[i]] = 1

    # Go through word2 and add the character count to the dictionary
    for i in range(len(word2)):  # O(n)
        if word2[i] in char_count:
            char_count[word2[i]] += 1
        else:
            char_count[word2[i]] = 1

    # Track the value in count_odd variable to see if any character appears odd number of times in either word
    # count_odd variable will be 0 if words are perfect anagrams of each other.
    # If the count_odd variable is 2 it means that there are two characters which do not appear in either words and thus can be subsitutions for each other
    for value in char_count.values():  # O(n)
        if value % 2:
            count_odd += 1

    return count_odd == 2


print(checkBlanagrams('tangram', 'anagram'))
print(checkBlanagrams('tangram', 'pangram'))
print(checkBlanagrams('aba', 'bab'))
print(checkBlanagrams('silent', 'listen'))
