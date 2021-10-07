/*
-Directions:

Implement a Queue datastructure using two stacks. 
*Do not* create an array inside of the 'Queue' class. 
Queue should implement the methods 'add', 'remove', and 'peek'. 

-Examples:

const q = new Queue();
q.add(1)
q.add(2)
q.peek() // returns 1
q.remove() // returns 1
q.remove() // returns 2


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Stack {
  constructor() {
    this.data = []
  }

  push(record) {
    this.data.push(record)
  }

  pop() {
    return this.data.pop()
  }

  peek() {
    return this.data[this.data.length - 1]
  }
}


//Implementation of a Queue using Stack
class Queue {
  constructor() {
      this.dataOne = new Stack();
      this.dataTwo = new Stack();
  }
  
  add(record) {
     this.dataOne.push(record) 
  }
  
  remove() {
    if(!this.dataTwo.peek()) {
        while(this.dataOne.peek()) {
            this.dataTwo.push(this.dataOne.pop())
        }
    }
      
    return this.dataTwo.pop()
  }
  
  peek() {
    if(!this.dataTwo.peek()) {
      while(this.dataOne.peek()) {
          this.dataTwo.push(this.dataOne.pop())
      }
    }
    return this.dataTwo.peek()
  } 
}

const q = new Queue();
q.add(1)
q.add(2)
console.log(q.peek());
console.log(q.remove());
console.log(q.remove());
