/* 
Directions:
Implementation of a Linked List

Create a class to represent a Linked List. When created, a linked list should have 
"no" head node associated with it. The LinkedList instance will have one property, 
'head', which is a reference to the first node of the linked list. By default 'head'
should be 'null'

Example-

const list = new LinkedList()
list.head // Returns null

Linked List Methods:
- insertFirst(data)
Create a new Node from argument 'data' and assigns the resulting node to the 
'head' property. Make sure to handle the case in which the linked list already
has a node assigned to the 'head' property

Example - 
const list = new LinkedList()
list.insertFirst('Hi There'); // List has one node

- size
Returns the number of nodes in the linked list

Example  -

const list = new LinkedList()
list.insertFirst('a')
list.insertFirst('b')
list.insertFirst('c')
list.size() // Returns 3

- getFirst
Returns the first node of the linked list

const list = new LinkedList()
list.insertFirst('a');
list.insertFirst('b');
list.getFirst(); // Returns Node instance with data 'a'


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


//Creates a new instance of a linked list
const new_list = new LinkedList()


//Returns head of the list
console.log(new_list.head)


//Returns the number of nodes in the list
console.log(new_list.size())

//Insert a new node at the provided index
new_list.insertAt(60,2)
console.log(new_list.size())

//Returns first node in the list
console.log(new_list.getFirst())

//Returns last node in the list
console.log(new_list.getLast())




