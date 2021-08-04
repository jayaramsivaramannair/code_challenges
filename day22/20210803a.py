'''
There is a string S of lowercase English letters that is repeated infinitely many times. 
Given an integer N, find and print the number of letter a's in the first N letters of the infinite string. 


Example:

s = 'abcac'
n = 10

The substring we consider is abcacabcac, the first 10 characters of the infinite string. 
There are 4 occurences of a in the substring. 

Complete the repeatedString function in the editor below. 
repeatedString has the following parameters:
- s: a string to repeat
- n: the number of characters to consider

Return:

- int: the frequency of a in the substring

Source: hackerrank( Warm up challenges from Interview Preparation Kit)

'''

stringA = 'aba'
n = 10

def repeatedString(s, n):
    # In the solution below, the part after else clause takes care of the case where the n is not evenly divisible by length of the provided string
    count_a = 0
    count_a += (s.count('a') * (n // len(s)))

    if len(s) > n:
        count_a += s[:n].count('a')
    else:
        count_a += s[:n% len(s)].count('a')

    return count_a

print(repeatedString(stringA, n))
print(repeatedString('abcac', 10))

