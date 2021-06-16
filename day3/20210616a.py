'''
Write a function that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

Examples:

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Along with opening (() and closing ()) parenthesis, 
input may contain any valid ASCII characters. 
Furthermore, the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

source: codewars.com
'''


def valid_parentheses(string):
    # Approach # 1 Using Loop - Increments the count for every "(" and decrements it for every ")"
    total = 0
    for i in range(len(string)):
        if total == 0 and string[i] == ")":
            return False

        if (string[i] == "("):
            total = total + 1
        elif (string[i] == ")") and total >= 1:
            total = total - 1

    return total == 0

    # Approach 2 Checks that the count does not become a negative number

    '''
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

    '''


print(valid_parentheses(")(()))"))
print(valid_parentheses("()"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses(")test"))
