'''
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1: 

Input: text = "mbxcdatlas"
Output: 1

Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2


Example 3:

Input: text = "sctlamb"
Output: 0


source: codesignal.com (Lambda Challenge)

'''


def csMaxNumberOfLambdas(text):
    count_lambda = 0
    for ch in text:
        if ch in "lambda":
            count_lambda += 1

    return count_lambda // 6


print(csMaxNumberOfLambdas('mbxcdatlas'))
print(csMaxNumberOfLambdas("lalaaxcmbdtsumbdav"))
print(csMaxNumberOfLambdas('"sctlamb"'))
