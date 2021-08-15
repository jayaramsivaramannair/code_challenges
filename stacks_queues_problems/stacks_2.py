'''

A queue is an abstract data type that maintains the order in which elements were added to it, 
allowing the oldest elements to be removed from the front and new elements to be added to the rear. 
This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue 
(i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

- Enqueue: add a new element to the end of the queue.
- Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. 
Then process q queries, where each query is one of the following 3 types:

- 1x: Enqueue element x into end of the queue. 
- 2: Dequeue the element at the front of the queue.
- 3: Print the element at the front of the queue. 

Function Description:

Complete the put, pop, and peek methods in the editor below. They must perform the actions as described above.

Output:

For each query of type 3, return the value of the element at the front of the fifo queue on a new line. 

source: hackerrank.com (Interview Preparation on Stacks and Queues)
'''

class MyQueue(object):
    def __init__(self):
        #used for appending items
        self.stack_1 = []
        #used for popping items
        self.stack_2 = []
        
    def peek(self):
        if self.stack_2:
            return self.stack_2[-1]
        return self.stack_1[0]   
    
    def pop(self):
        #check if stack_2 is empty
        # If stack_2 is empty then copy over all the items from stack_1 to stack_2
        # while copying items over to stack_2, simulataenously empty stack_1 as well
        if (len(self.stack_2) == 0):
            while(len(self.stack_1) > 0):
                self.stack_2.append(self.stack_1.pop())
                
        return self.stack_2.pop()
                
          
    def put(self, value):
        self.stack_1.append(value)

queue = MyQueue()
queue.put(42)
queue.pop()
queue.put(14)
print(queue.peek())
queue.put(28)
print(queue.peek())
queue.put(60)
queue.put(78)
queue.pop()
queue.pop()
        