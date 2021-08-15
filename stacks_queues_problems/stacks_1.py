'''

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) 
of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. 
For example, {[(])} is not balanced because the contents in between { and } are not balanced. 
The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses 
encloses a single, unbalanced closing square bracket, ].


By this logic, we say a sequence of brackets is balanced if the following conditions are met:

- It contains no unmatched brackets.
- The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

Given n strings of brackers, determine whether each sequence of brackets is balanced. 
If a string is balanced, return YES. 

Otherwise, return NO. 

Function Description:

Complete the function isBalanced in the editor below.

isBalanced has the following parameters:
 - string s: a string of brackets

 Returns:
 - string: either YES or NO



source: hackerrank.com (interview preparation on stacks and queues)
'''

def isBalanced(s):
    # Write your code here
    stack = []
    
    for i in range(len(s)): 
        #If the stack is already empty, simply add the bracket to the stack
        # This will prevent any further checks
        if not stack:
            stack.append(s[i])  
        elif s[i] == "}" and stack[-1] == "{":
            stack.pop()
        elif s[i] == ")" and stack[-1] == "(":
            stack.pop()
        elif s[i] == "]" and stack[-1] == "[":
            stack.pop()
        else:
            stack.append(s[i])
        
        
    if (len(stack)):
        return 'NO'
            
    return 'YES'

print(isBalanced('{[()]}'))
print(isBalanced('{[(])}'))
print(isBalanced('{{[[(())]]}}'))