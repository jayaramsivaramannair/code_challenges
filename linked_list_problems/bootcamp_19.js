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
}

const new_list = new LinkedList()
console.log(new_list.head)

new_list.insertFirst(10)

new_list.insertFirst(12)

new_list.insertFirst(14)

const list_b = new LinkedList()
console.log(new_list.size())
console.log(new_list.getFirst())