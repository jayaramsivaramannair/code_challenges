/* 

Directions - 

1) Create a node calss. The constructor should accept an argument that gets assigned to the data property
and initialize an empty array for storing children. The node should have methods 'add' and 'remove'.

2) Create a tree class. The tree constructor should initialize a 'root' property to null. 


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

class Tree {
  constructor() {
    this.root = null
  }
}

const a = new Node('a')
a.add('b')
a.add('c')
a.add('d')

console.log(a.children)

a.remove('d')

console.log(a.children)
const tree = new Tree()
Tree.root = a;

console.log(Tree)