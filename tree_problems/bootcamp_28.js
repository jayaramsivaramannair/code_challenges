/*

Directions:
Given a node, validate the binary search tree, ensuring that every node's lef hand 
child is less than the parent node's value, and every node's right hand child is greater than 
the parent


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

function validate(node, min = null, max = null) {
  if(max !== null && node.data > max) {
    return false;
  }

  if(min !== null && node.data < min) {
    return false;
  }

  if(node.left && !validate(node.left, min, node.data)) {
    return false;
  }

  if(node.right && !validate(node.right, node.data, max)) {
    return false;
  }

  return true;

}

let node = new Node(10)
node.insert(0)
node.insert(12)



console.log(validate(node))

