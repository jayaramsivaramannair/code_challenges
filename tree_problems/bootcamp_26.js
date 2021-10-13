/*
Given the root node of a tree, return an array where
each element is the width of the tree at each level. 

- Directions:

        0
    /   |    \
    1    2    3
    |         | 
    4         5

    
Answer: [1, 3, 2]
Hint: Whenever the question concerns width of a tree, customize the breadth-first traversal algo and use it
source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Node {
  constructor(record) {
    this.data = record
    this.children = []
  }

  add(data) {
    const new_node = new Node(data)
    this.children.push(new_node)
  }

  remove(data) {
    //Returns a new array with nodes not to be removed
    const new_children = this.children.filter(node => node.data !== data)

    this.children = new_children
  }
}

function levelWidth(root) {
  const arr = [root, 's']

  const counters = [0]

  while(arr.length > 1) {
    const node = arr.shift()

    //This signifies that a new row has begun
    if(node === 's') {
      //Create a new count in the counters array
      counters.push(0)
      arr.push('s');

    } else {

      arr.push(...node.children);
      counters[counters.length - 1] += 1
    }

  }

  return counters
}

const node = new Node(0)
const node1 = new Node(1)
const node2 = new Node(2)
const node3 = new Node(3)

const node4 = new Node(4)
const node5 = new Node(5)

node.children.push(node1)
node.children.push(node2)
node.children.push(node3)

node1.children.push(node4)
node3.children.push(node5)

console.log(levelWidth(node))