'''
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. 
Your task is to determine whether or not the sequence is a valid bracket sequence.


The Valid bracket sequence is defined in the following way:

- An empty bracket sequence is a valid bracket sequence.
- If S is a valid bracket sequence then (S), [S] and {S} are also valid.
- If A and B are valid bracket sequences then AB is also valid.

Examples:

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.

source: codesignal.com (Lambda Challenge)

'''


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        popped_item = self.data.pop()


def validBracketSequence(sequence):
    brackets = Stack()
    for i in range(len(sequence)):
        # Check the opening bracket, add to the stack
        if(sequence[i] == '(' or sequence[i] == '{' or sequence[i] == '['):
            brackets.data.append(sequence[i])

        # Check for the closing parenthesis only if the array's length is greater than 1 or else skip the current iteration
        if (len(brackets.data) == 0):
            continue

        if(sequence[i] == ')' and brackets.data[-1] == '('):
            brackets.data.pop()
        elif(sequence[i] == '}' and brackets.data[-1] == '{'):
            brackets.data.pop()
        elif(sequence[i] == ']' and brackets.data[-1] == '['):
            brackets.data.pop()

    return len(brackets.data) == 0


print(validBracketSequence("()"))
print(validBracketSequence("(]"))
print(validBracketSequence("([)]"))
print(validBracketSequence("()[]{}"))
