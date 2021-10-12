/*
Direction:

Implement a breadth-first traversal for a tree

Hint: Breadth-First traversal visits each node at every level from left to right


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

function print_children(node) {
  for (let child of node.children) {
    console.log(child.data)
  }
}

class Tree {
  constructor() {
    this.root = null
  }

  traverseBF(fn) {
    //Create an empty array and add the root node to it
    const arr = [this.root]

    //As long as the array is not empty
    while(arr.length) {
      //Remove the first element from the array
      const node = arr.shift()

      //Push the first element's children to the array
      arr.push(...node.children)

      //Apply the function to the first element
      fn(node)
    }
  }
}


const a = new Node('a')
a.add('b')
a.add('c')
a.add('d')

console.log(a)

const tree = new Tree()
tree.root = a

tree.traverseBF(print_children)
