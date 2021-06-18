'''
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').



Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

source: codewars.com
'''


def solution(s):

    # Approach-1: Uses list comprehension to generate the string and step in range function
    lst_string = [s[i: i+2] for i in range(0, len(s), 2)]
    if(len(s) % 2):  # If the length of string is odd
        lst_string[-1] = lst_string[-1] + '_'

    return lst_string

    # Approach-2 Uses a similar list comprehension approach but it would check the length first
    # Instead of adding 'underscore' to the resultant list, 'underscore' would be added to the initial string itself


print(solution('abc'))
print(solution('abcdef'))
