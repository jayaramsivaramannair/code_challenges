/*
Given pointers to the head nodes of 2 Linked Lists that merge together at some point, 
find the node where the two lists merge. 

The merge point is where both lists point to the same node, i.e. they reference
the same memory location. It is guaranteed that the two head nodes will be different
and neither will be NULL. If the lists share a common node, return that node's data value


source: Hackerrank Interview Preparation Questions
*/

class Node {
  constructor(record, nextNode = null) {
    this.data = record
    this.next = nextNode
  }
}

function print_nodes(head) {
  while(head) {
    console.log(head.data)
    head = head.next
  }

  return null
}

let headA = new Node('a')
let b = new Node('b')
let x = new Node('x')
let y = new Node('y')
let z = new Node('z')


let headB = new Node('p')
let q = new Node('q')
headB.next = q
q.next = x

headA.next = x
x.next = y
y.next = z


function findMergeNode(headA, headB) {
  let current_node_A = headA
  let current_node_B = headB

  while (current_node_A !== current_node_B) {
    if(current_node_A.next === null) {
      //Start iterating through list2 once list1 is complete
      current_node_A = headB
    } else {
      current_node_A = current_node_A.next;
    }

    if(current_node_B.next === null) {
      //Start iterating through list1 once list2 is complete
      current_node_B = headA
    } else {
      current_node_B = current_node_B.next;
    }
  }

  return current_node_A.data
}

console.log('List A ------>')
print_nodes(headA)
console.log('List B ------>')
print_nodes(headB)

console.log('Merge Node')
console.log(findMergeNode(headA, headB))
