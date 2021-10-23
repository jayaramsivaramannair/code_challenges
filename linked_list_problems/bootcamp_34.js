/*
Inserting a Node Into a Sorted Doubly Linked List:

Given a reference to the head of a doubly-linked list and an integer, data, 
create a new DoublyLinkedList Node object having data value and insert it at the proper
location to maintain the sort.

source: Hackerrank Interview Preparation Questions
*/

class Node {
  constructor(data) {
    this.data = data
    this.next = null
    this.prev = null
  } 
}

function print_nodes(head) {
  while(head) {
    console.log(head.data)
    head = head.next
  }

  return null
}

let a = new Node('a')
let b = new Node('b')
let c = new Node('c')
let d = new Node('d')
let e = new Node('e')


a.next = b
a.prev = null

b.prev = a
b.next = d

d.prev = b
d.next = e

e.prev = d
e.next = null


function sortedInsert(llist, data) {
  let new_node = new Node(data);

  if(llist === null) {
    return new_node;
  }

  let current = llist;
  let previous = null;

  //If the new node is to be inserted at the end
  if(data < current.data) {
    new_node.next = current
    new_node.prev = null
    current.prev = new_node;
    return new_node;
  }

  //Iterate until the data is being passed greater than the current node
  while (current !== null && data > current.data) {
    previous = current;
    current = current.next
  }

  //This signifies that we have reached end of the list
  if(current === null) {
    new_node.prev = previous
    new_node.next = null
    previous.next = new_node;
  } else {
    //The below code will be reached only if the insertion takes place in the middle of the list
    new_node.prev = previous;
    new_node.next = previous.next;
    previous.next = new_node;
    new_node.next.prev = new_node;
  }

  return llist;
}

console.log("Before Insertion:")
print_nodes(a)
let new_head = sortedInsert(a, 'f')
console.log("After Insertion")
print_nodes(new_head)