/*

A Linked List is said to contain a cycle if any node is visited more than nce while
traversing the list. For example, in the following graph 
there is a cycle when node 5 points back to node 3


source: Hackerrank Interview Preparation Questions
*/

class Node {
  constructor(record, nextNode = null) {
    this.data = record
    this.next = nextNode
  }
}

let head = new Node('a')
let b = new Node('b')
let c = new Node('c')
let d = new Node('d')
let e = new Node('e')

head.next = b
b.next = c
c.next = d
d.next = e

function print_nodes(head) {
  while(head) {
    console.log(head.data)
    head = head.next
  }

  return null
}



function has_cycle(head) {
  let current_node = head
  let visited = []
  while(current_node) {
    if(visited.includes(current_node)) {
      return true
    }
    
    visited.push(current_node)
    current_node = current_node.next
  }

  return false
}

console.log(has_cycle(head))



