/*
- Directions:
Given a linked list, return true if the list is circular, false if it is not. 

- Examples:

const l = new List();
const a = new Node('a');
const b = new Node('b')
const c = new Node('c')

l.head = a;
a.next = b;
b.next = c;
c.next = b;

circular(l) // true

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Node {
  constructor(record, nextNode = null) {
    this.data = record
    this.next = nextNode
  }
}

class LinkedList {
  constructor() {
    this.head = null
  }

  insertFirst(data) {
    //Get a reference to the current head node in the list
    let old_head = this.head

    //Create a new node
    let new_node = new Node(data, old_head)

    //Make the new node to become the new head
    this.head = new_node
  }

  size() {
    let nodes = 0

    let current_node = this.head
    while(current_node) {
      nodes += 1
      current_node = current_node.next
    }

    return nodes
  }

  getFirst() {
    return this.head
  }

  getLast() {
    let current_node = this.head

    if(!current_node) {
      return null
    }

    while(current_node.next) {
      current_node = current_node.next
    }

    return current_node
  }

  clear() {
    this.head = null
  }

  removeFirst() {

    //Check if a head node exists or not
    if(!this.head) {
      return
    }

    let old_head = this.head
    this.head = old_head.next

  }

  removeLast() {
    
    //Check if a head node exists or not
    if(!this.head) {
      return 
    }

    //If the list contains only one node
    if(this.size() === 1) {
      this.head = null
      return
    }

    let current_node = this.head
    let previous_node = null

    while(current_node.next) {
      previous_node = current_node
      current_node = current_node.next
    }

    previous_node.next = null
  }

  insertLast(data) {

    let last_node = this.getLast()
    //Check if the list is currently empty or not
    if (last_node) {
      last_node.next = new Node(data)
    } else {
      this.head = new Node(data)
    }
  }

  getAt(index) {
    let counter = 0
    let current_node = this.head


    while(current_node) {
        if(counter === index) {
          return current_node
        }
        counter += 1
        current_node = current_node.next
    }
    //This will be reached only if index is invalid
    return null
  }

  removeAt(index) {
    let target_node = this.getAt(index)
    let previous_node = this.getAt(index- 1)

    //If the list is empty
    if(!target_node && !previous_node) {
      return
    }

    //if the target_node is head node
    if(!previous_node) {
      this.head = this.head.next
      return 
    }

    if(target_node && previous_node) {
      previous_node.next = target_node.next
      return 
    }
  }

  insertAt(data, index) {
    //If the index is out of bounds or if the index points to the tail
    if(index < 0 || index > this.size() - 1) {
      this.insertLast(data)
      return
    }

    let previous_node = this.getAt(index - 1)
    let new_node = new Node(data)

    //Insert at head or when the list is empty
    if(!previous_node) {
      new_node.next = this.head
      this.head = new_node
      return
    }
    
    new_node.next = previous_node.next
    previous_node.next = new_node
    return 
  }
}


const l1 = new LinkedList();
const a = new Node('a')
const b = new Node('b')
const c = new Node('c')

l1.head = a;
a.next = b;
b.next = c;
c.next = b;

const l2 = new LinkedList()
const z = new Node('z')
const y = new Node('y')
const x = new Node('x')
const v = new Node('v')
const u = new Node('u')

l2.head = u
u.next = v;
v.next = x;
x.next = y;
y.next = z;
z.next = null;


function circular(list) {


  let slow = list.head
  let fast = list.head

  while(fast.next && fast.next.next) {

    slow = slow.next
    fast = fast.next.next


    //If both end up pointing at the same node
    if(slow === fast) {
      return true
    }
  }

  return false
}

console.log(circular(l1))
console.log(circular(l2))
