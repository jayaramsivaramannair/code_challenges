/*
Directions
- Implement a 'peek' method in the queue class. 
- Peek should return the last element (next one to be returned) from queue without actually removing it. 



Additionally:
Implement a weave function:
- weave receives two queues as arguments and combines the contents of each into a new, third queue
- The third queue should contain the alternating content of the two queues
- The function should handle queues of different lengths without inserting 'undefined' into the new one
- Do not access the array inside of any queue, only use the add, remove and peek functions

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Queue {
  constructor() {
    this.data = []
  }

  add(record) {
    this.data.unshift(record)
  }

  remove(record) {
    return this.data.pop()
  }

  peek() {
    return this.data[this.data.length - 1]
  }
}



const q = new Queue()
q.add(1)
q.add(2)
q.add(3)

const q2 = new Queue()
q2.add('Hi')
q2.add('There')

function weave(sourceOne, sourceTwo) {
  const new_q = new Queue()

  while(true) {
    if(sourceOne.peek()) {
      new_q.add(sourceOne.remove())
    }
    
    if (sourceTwo.peek()) {
      new_q.add(sourceTwo.remove())
    } 

    if(!sourceOne.peek() && !sourceTwo.peek()) {
      break;
    }
  }

  return new_q
}

const q3 = weave(q, q2)
console.log(q3.remove())
console.log(q3.remove())
console.log(q3.remove())
console.log(q3.remove())
console.log(q3.remove())