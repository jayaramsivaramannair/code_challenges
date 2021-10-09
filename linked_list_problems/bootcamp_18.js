/*

Directions:
Implementation of a Linked List Node

Create a class instance to represent a node. The node should have two properties - 'data' and 'next'
Accept both of these as arguments to the 'Node' constructor, then assign them to the instance as properties 'data'
and 'next'. If 'next' is not provided to the constructor, then default its value to be 'null'

Examples:

const n = New Node('There')
n.data // returns 'There'
n.next // returns null
const n2 = new Node('Hi', n)
n.next // returns n

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Node {
  constructor(record, nextNode = null) {
    this.data = record
    this.next = nextNode
  }
}

const node_2 = new Node('Hi')
const node_1 = new Node('There', node_2)

console.log(node_1.data)
console.log(node_1.next)


console.log(node_2.data)
console.log(node_2.next)

