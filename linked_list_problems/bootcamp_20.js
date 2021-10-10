/* 
Directions:
Return the 'middle' node of a linked list. 
If the list has an even number of elements, return the node at the end of the first half of the list. 
Note: Do not use a counter variable, also Do not retrieve size of the list and only iterate through the list one time. 


Example:
const l = new LinkedList()
l.insertLast('a')
l.insertLast('b')
l.insertLast('c')
midpoint(l) // Returns {data: 'b'}


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

class Node {
  constructor(record, nextNode = null) {
    this.data = record
    this.next = nextNode
  }
}

class LinkedList {
  constructor() {
    this.head = null
  }

  insertFirst(data) {
    //Get a reference to the current head node in the list
    let old_head = this.head

    //Create a new node
    let new_node = new Node(data, old_head)

    //Make the new node to become the new head
    this.head = new_node
  }

  size() {
    let nodes = 0

    let current_node = this.head
    while(current_node) {
      nodes += 1
      current_node = current_node.next
    }

    return nodes
  }

  getFirst() {
    return this.head
  }

  getLast() {
    let current_node = this.head

    if(!current_node) {
      return null
    }

    while(current_node.next) {
      current_node = current_node.next
    }

    return current_node
  }

  clear() {
    this.head = null
  }

  removeFirst() {

    //Check if a head node exists or not
    if(!this.head) {
      return
    }

    let old_head = this.head
    this.head = old_head.next

  }

  removeLast() {
    
    //Check if a head node exists or not
    if(!this.head) {
      return 
    }

    //If the list contains only one node
    if(this.size() === 1) {
      this.head = null
      return
    }

    let current_node = this.head
    let previous_node = null

    while(current_node.next) {
      previous_node = current_node
      current_node = current_node.next
    }

    previous_node.next = null
  }

  insertLast(data) {

    let last_node = this.getLast()
    //Check if the list is currently empty or not
    if (last_node) {
      last_node.next = new Node(data)
    } else {
      this.head = new Node(data)
    }
  }

  getAt(index) {
    let counter = 0
    let current_node = this.head


    while(current_node) {
        if(counter === index) {
          return current_node
        }
        counter += 1
        current_node = current_node.next
    }
    //This will be reached only if index is invalid
    return null
  }

  removeAt(index) {
    let target_node = this.getAt(index)
    let previous_node = this.getAt(index- 1)

    //If the list is empty
    if(!target_node && !previous_node) {
      return
    }

    //if the target_node is head node
    if(!previous_node) {
      this.head = this.head.next
      return 
    }

    if(target_node && previous_node) {
      previous_node.next = target_node.next
      return 
    }
  }

  insertAt(data, index) {
    //If the index is out of bounds or if the index points to the tail
    if(index < 0 || index > this.size() - 1) {
      this.insertLast(data)
      return
    }

    let previous_node = this.getAt(index - 1)
    let new_node = new Node(data)

    //Insert at head or when the list is empty
    if(!previous_node) {
      new_node.next = this.head
      this.head = new_node
      return
    }
    
    new_node.next = previous_node.next
    previous_node.next = new_node
    return 
  }
}

const ll = new LinkedList()
ll.insertLast('a')
ll.insertLast('b')
ll.insertLast('c')
ll.insertLast('d')
ll.insertLast('e')

console.log(ll.size())

function midpoint(list) {
  let slow = list.head
  let fast = list.head
  while(fast.next && fast.next.next) {
    //slow variable is iterating through the list at half the speed of fast variable
    slow = slow.next
    fast = fast.next.next
  }

  return slow
}

console.log(midpoint(ll))
