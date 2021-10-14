/*

Implementation of a binary search tree:

a) Implement the Node class to create a binary search tree.
The constructor should initialize values 'data', 'left', and 'right'.

b) Implement the 'insert' method for the Node class. Insert should accept an argument
'data', then insert a new node at the appropriate location in the tree. 

c) Implement the 'contains' method for the Node class. Contains should accept a 'data'
argument and return the Node in the tree with the same value. 


Note:
Binary Tree has atleast two nodes on either side - right and left
Binary Search Tree requires that a value less than current node value goes on the left side
whereas a value greater than the current node goes on the right side. 


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/


class Node {
  constructor(data) {
    this.data = data
    this.left = null
    this.right = null
  }

  insert(data) {
    if(data < this.data) {
        if(this.left) {
            this.left.insert(data)
        } else {
            this.left = new Node(data)
            return
        }
    } else if (data > this.data) {
        if(this.right) {
            this.right.insert(data)
        } else {
            this.right = new Node(data)
            return
        }
    }
  }

  //The recursive call must use the return keyword
  contains(data) {
    if(this.data === data) {
      return this
    }

    if(data < this.data && this.left) {
        return this.left.contains(data)
    } else if (data > this.data && this.right) {
        return this.right.contains(data)
    }
    
    return null
  }
}

let a = new Node(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)


console.log(a.contains(5))