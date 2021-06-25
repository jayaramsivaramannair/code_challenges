'''
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

For n = 1, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 60 = 5 + 55 = F5 + F10.

For n = 66, the output should be
fibonacciSimpleSum2(n) = false.


source: codesignal.com (Lambda Challenge)
'''


def generate_constituents(n):
    if(n == 0 or n == 1):
        return n

    prev, curr, next = 0, 1, 1

    while(next <= n):
        prev = curr
        curr = next
        next = prev + curr

    return curr


def fibonacciSimpleSum2(n):
    num1 = generate_constituents(n)
    num2 = generate_constituents(n - num1)
    return num1 + num2 == n


print(fibonacciSimpleSum2(1))
print(fibonacciSimpleSum2(11))
print(fibonacciSimpleSum2(60))
print(fibonacciSimpleSum2(61))
