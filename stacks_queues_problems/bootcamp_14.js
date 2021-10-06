/*
Description
- Create a queue data structure. The queue should be a class with methods 'add' and 'remove'.
Adding to the queue should store an element until it is removed

Examples
- const q = new Queue();
- q.add(1)
- q.remove() -> returns 1;

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Queue {
  constructor() {
    this.data = []
  }

  add(record) {
    this.data.unshift(record)
  }

  remove() {
    return this.data.pop();
  }

  peek() {
    return this.data
  }
}

const q = new Queue()
q.add(1)
q.add(5)
q.add(7)
q.add(10)
q.remove()

console.log(q.peek())