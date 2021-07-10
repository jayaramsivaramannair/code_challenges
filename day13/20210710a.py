'''
Implementation of a code using two stacks

You are given an array of requests, where requests[i] can be "push <x>" or "pop". 
Return an array composed of the results of each "pop" operation that is performed.

Example

For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1}; after the second it is {1, 2}. 
Then we do the third request, "pop", and add the first element of the queue 1 to the answer array. 
The queue becomes {2}. After the fourth request, the queue is {2, 3}. 
Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.

source: codesignal.com (Lambda Challenge)
'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    # left stack is used for all the items associated with 'push' in requests
    left = Stack()
    # right stack is used for all the items associated with 'pop' in requests
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        # Check if the right stack is empty or not
        if(right.isEmpty()):
            while(left.isEmpty() is not True):
                right.push(left.pop())
        return right.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


print(queueOnStacks(["push 1", "push 2", "pop", "push 3", "pop"]))
