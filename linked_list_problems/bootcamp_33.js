/*
Reversal of a doubly-linked list:

Given the pointer to the head node of a doubly linked list, 
reverse the order of the nodes in place.
That is, change the next and prev pointers of the nodes 
so that the direction of the list is reversed. 
Return a reference to the head node of the reversed list. 

Note: The head node might be NULL to indicate that the list is empty


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
b.next = c

c.prev = b
c.next = d

d.prev = c
d.next = e

e.prev = d
e.next = null

//parameter is head of the linked-list
function reverse(llist) {
  //Check whether the head is null or not
  if (llist === null) {
    return llist
  }

  //Create a reference for head of the list
  let current_node = llist
  let new_head = llist

  //As long as the current node is not null
  while(current_node) {
    let prev = current_node.prev
    current_node.prev = current_node.next
    current_node.next = prev
    new_head = current_node
    current_node = current_node.prev
  }

  return new_head
}


let head = a
console.log('Old List:')
print_nodes(head)

let new_head = reverse(a)
console.log('New List:')
print_nodes(new_head)



