/*
Direction:

Implement a depth-first traversal for a tree

Hint: Depth-First Traversal visits each node starting at the root  until all of a node's children have been visited (no matter how deep)


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

  traverseDF(fn) {
    //Create an empty array and add the root node to it
    const arr = [this.root]

    //As long as the array is not empty
    while(arr.length) {
      //Remove the first element from the array
      const node = arr.shift()

      //Push the first element's children to the array
      arr.unshift(...node.children)

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

tree.traverseDF(print_children)
